import requests
from requests.compat import urljoin
from .formation import wrap, _REQ_HTTP, _RES_HTTP, _SESSION
from attr import attrib, attrs
import datetime

__all__ = ["build_sender", "build", "client"]


def client(cls=None):
    def client_decorator(cls):
        original_init = cls.__init__

        def now_iso(self):
            return datetime.datetime.utcnow().isoformat()

        def path(self, p):
            return requests.compat.urljoin(self.base_uri, p)

        def init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            base_uri = kwargs.get("base_uri", self.__class__.base_uri)
            self.request = build(
                middleware=kwargs.get("middleware", self.__class__.middleware),
                base_uri=base_uri,
            )
            self.base_uri = base_uri

        cls.path = path
        cls.now_iso = now_iso
        cls.__init__ = init
        return cls

    if cls:
        return client_decorator(cls)
    return client_decorator


@attrs
class FormationHttpRequest(object):
    url = attrib()
    method = attrib(default="get")
    headers = attrib(default={})
    params = attrib(default={})
    auth = attrib(default=None)
    data = attrib(default=None)


def build_sender(middleware=[], base_uri=None):
    wrapped = wrap(requests_adapter, middleware=middleware)

    def sender(method, url, session_context={}, **kwargs):
        ctx = {
            _REQ_HTTP: FormationHttpRequest(
                url=urljoin(base_uri, url), method=method, **kwargs
            ),
            _SESSION: session_context,
        }
        ctx = wrapped(ctx)
        return ctx[_RES_HTTP]

    return sender


class Sender(object):
    def __init__(self, send):
        self.send = send

    def get(self, path, **kwargs):
        return self.send("get", path, **kwargs)

    def post(self, path, **kwargs):
        return self.send("post", path, **kwargs)

    def put(self, path, **kwargs):
        return self.send("put", path, **kwargs)


def build(middleware=[], base_uri=None):
    return Sender(build_sender(middleware=middleware, base_uri=base_uri))


# TODO: pass more requests vars via req (e.g. timeout, retry)
def requests_adapter(ctx):
    req = ctx[_REQ_HTTP]
    meth = getattr(requests, req.method.lower())
    # TODO ship var as kwargs and not explicitly
    res = meth(
        req.url, headers=req.headers, params=req.params, auth=req.auth, data=req.data
    )
    ctx[_RES_HTTP] = res
    return ctx
