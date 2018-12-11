from .formation import (
    _REQ_HTTP,
    _CONTEXT,
    _SESSION,
    _RES_HTTP,
    _RETRY,
    _REQ_ID,
    _REQ_PARENT_ID,
    _REQ_DURATION,
    _UID,
)
from six.moves import _thread as thread
import datetime
from uuid import uuid4
from toolz.curried import valfilter, get_in
import pybreaker
import os


def default_stack(logger):
    return [
        create_request_id(),
        create_context(),
        create_request_duration(),
        create_request_logger(logger),
    ]


def create_request_id(key="x-request-id", idgen=uuid4):
    def requests_id(ctx, next):
        headers = ctx[_REQ_HTTP].headers
        headers[key] = headers.get(key, str(idgen()))
        ctx[_REQ_ID] = headers[key]
        ctx = next(ctx)
        return ctx

    return requests_id


def create_request_duration(now=datetime.datetime.now):
    def request_duration(ctx, next):
        start = now()
        ctx = next(ctx)
        end = now() - start
        ctx["req.duration_us"] = end.microseconds
        return ctx

    return request_duration


def get_context(
    request_id=None,
    request_parent_id=None,
    namespace="service",
    env="local",
    sha="dev",
    version="0.0.1",
    scope="service",
    uid=None,
    getpid=os.getpid,
    gettid=thread.get_ident,
):
    pid = getpid()
    tid = gettid()
    return {
        "v": version,
        "sha": sha,
        "env": env,
        "pid": pid,
        "tid": tid,
        "uid": uid,
        "scope": scope,
        "ns": namespace,
        "rid": request_id,
        "rid_p": request_parent_id,
    }


def create_context(
    context_fn=get_context,
    namespace="service",
    scope="all",
    env="local",
    sha="dev",
    version="0.01",
    getpid=os.getpid,
    gettid=thread.get_ident,
):
    def context(ctx, call):
        request_id = ctx[_REQ_ID]
        request_parent_id = ctx.get(_REQ_PARENT_ID, None)
        uid = get_in([_SESSION, _UID], None)

        ctx[_CONTEXT] = context_fn(
            env=env,
            sha=sha,
            version=version,
            request_id=request_id,
            request_parent_id=request_parent_id,
            scope=scope,
            uid=uid,
            getpid=getpid,
            gettid=gettid,
        )
        ctx = call(ctx)
        return ctx

    return context


def create_request_logger(logger):
    no_nones = valfilter(lambda x: x)

    def request_logger(ctx, next):
        req = ctx[_REQ_HTTP]
        context = ctx.get(_CONTEXT, {})
        msg = "request.http"

        log = logger.bind(**context)
        log.info(msg, url=req.url, method=req.method, params=no_nones(req.params))
        log.debug(msg, headers=req.headers)

        ctx = next(ctx)

        res = ctx[_RES_HTTP]

        msg = "response.http"
        log.info(
            msg,
            url=res.request.url,
            status=res.status_code,
            method=res.request.method,
            elapsed=res.elapsed,
            size=len(res.content),
            duration_us=ctx.get(_REQ_DURATION, None),
        )
        log.debug(msg, headers=res.headers)
        return ctx

    return request_logger


def breaker_logger(logger):
    class LogListener(pybreaker.CircuitBreakerListener):
        "Listener used to log circuit breaker events."

        def state_change(self, cb, old_state, new_state):
            logger.warn(
                "circuitbreaker.state.changed",
                name=cb.name,
                old_state=old_state.name,
                new_state=new_state.name,
            )

    return LogListener()


def create_circuit_breaker(logger, name):
    breaker = pybreaker.CircuitBreaker(name=name, listeners=[breaker_logger(logger)])

    def circuit_breaker(ctx, call):
        context = ctx.get(_CONTEXT, {})
        log = logger.bind(**context)

        if breaker.current_state == "open":
            log.info("circuitbreaker.middleware.open", name=breaker.name)

        call = breaker(call)

        try:
            ctx = call(ctx)
            return ctx
        except pybreaker.CircuitBreakerError:
            return ctx

    return circuit_breaker


def retry(max_retries=3):
    def retry_middleware(ctx, call):
        try:
            res = call(ctx)
            return res
        except Exception as ex:
            retries = ctx.get(_RETRY, 0)
            if retries > max_retries:
                raise ex
            ctx[_RETRY] = 1 + retries
            # TODO exponential backoff
            res = retry_middleware(ctx, call)
            return res

    return retry_middleware
