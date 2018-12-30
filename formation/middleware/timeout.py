from ..formation import _REQ_HTTP


def timeout(timeout=None):
    def timeout_middleware(ctx, call):
        req = ctx.get(_REQ_HTTP)
        if timeout:
            req.timeout = timeout
        return call(ctx)

    return timeout_middleware
