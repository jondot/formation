from toolz import reduce

_REQ_HTTP = "fmtn.req.http"
_RES_HTTP = "fmtn.res.http"
_CONTEXT = "fmtn.context"
_SESSION = "fmtn.session"
_RETRY = "fmtn.retry"
_REQ_ID = "req.id"
_UID = "uid"
_REQ_PARENT_ID = "req.parent.id"
_REQ_DURATION = "req.duration_us"


def wrap(call, middleware=[]):
    return reduce(
        lambda acc, m: lambda ctx: m(ctx, acc),
        reversed(middleware),
        lambda ctx: call(ctx),
    )
