from toolz import merge
from ..formation import _REQ_HTTP


def ua(user_agent="formation/1.0.0"):
    def ua_middleware(ctx, call):
        req = ctx.get(_REQ_HTTP)
        req.headers = merge(req.headers, {"User-Agent": user_agent})
        return call(ctx)

    return ua_middleware
