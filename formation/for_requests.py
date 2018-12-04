import requests
from .formation import wrap, _REQ_HTTP, _RES_HTTP, _SESSION
from attr import attrib, attrs, fields, asdict

__all__ = ["build_sender"]


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


def requests_adapter(ctx):
    req = ctx[_REQ_HTTP]
    meth = getattr(requests, req.method.lower())
    # TODO ship var as kwargs and not explicitly
    res = meth(
        req.url, headers=req.headers, params=req.params, auth=req.auth, data=req.data
    )
    ctx[_RES_HTTP] = res
    return ctx
