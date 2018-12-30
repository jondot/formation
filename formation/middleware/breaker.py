import pybreaker
from ..formation import _CONTEXT, _RES_HTTP


class BreakerTriggerException(Exception):
    pass


def breaker_logger(logger):
    class LogListener(pybreaker.CircuitBreakerListener):
        "Listener used to log circuit breaker events."

        def state_change(self, cb, old_state, new_state):
            logger.warn(
                "circuitbreaker.state_changed",
                name=cb.name,
                old_state=old_state.name,
                new_state=new_state.name,
            )

    return LogListener()


def trigger_breaker_if(trigger):
    def trigger_breaker_middleware(ctx, call):
        ctx = call(ctx)
        if trigger(ctx.get(_RES_HTTP)):
            raise BreakerTriggerException

    return trigger_breaker_middleware


def circuit_breaker(
    logger, name, fail_max=5, reset_timeout=60, state_storage=None, exclude=[]
):
    breaker = pybreaker.CircuitBreaker(
        name=name,
        listeners=[breaker_logger(logger)],
        exclude=exclude,
        fail_max=fail_max,
        reset_timeout=reset_timeout,
        state_storage=state_storage,
    )

    def circuit_breaker_middleware(ctx, call):
        context = ctx.get(_CONTEXT, {})
        log = logger.bind(**context)

        if breaker.current_state == "open":
            log.info("circuitbreaker.open", name=breaker.name)

        call = breaker(call)

        try:
            ctx = call(ctx)
            return ctx
        except pybreaker.CircuitBreakerError:
            return ctx

    return circuit_breaker_middleware
