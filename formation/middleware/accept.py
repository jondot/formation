from ..formation import _REQ_HTTP


def accept(mime_type):
    def accept_middleware(ctx, call):
        req = ctx.get(_REQ_HTTP)
        req.headers["Content-Type"] = mime_type
        return call(ctx)

    return accept_middleware
