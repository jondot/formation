import requests
from .formation import wrap, _REQ_HTTP, _RES_HTTP, _SESSION
from attr import attrib, attrs, fields, asdict

__all__ = ["build_sender", "build"]


@attrs
class FormationHttpRequest(object):
    url = attrib()
    method = attrib(default="get")
    headers = attrib(default={})
    params = attrib(default={})
    auth = attrib(default=None)
    data = attrib(default=None)


def build_sender(middleware=[]):
    wrapped = wrap(requests_adapter, middleware=middleware)

    def sender(method, url, session_context={}, **kwargs):
        ctx = {
            _REQ_HTTP: FormationHttpRequest(url=url, method=method, **kwargs),
            _SESSION: session_context,
        }
        ctx = wrapped(ctx)
        return ctx[_RES_HTTP]

    return sender


def build(middleware=[]):
    class Sender(object):
        def __init__(self):
            self.send = build_sender(middleware)

        def send(self, url, session_context={}, **kwargs):
            ctx = {
                _REQ_HTTP: FormationHttpRequest(url=url, method="get", **kwargs),
                _SESSION: session_context,
            }
            ctx = self.wrapped(ctx)
            return ctx[_RES_HTTP]

        def get(self, url, **kwargs):
            return self.send("get", url, **kwargs)

        def post(self, url, **kwargs):
            return self.send("post", url, **kwargs)

        def put(self, url, **kwargs):
            return self.send("put", url, **kwargs)

    return Sender


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
