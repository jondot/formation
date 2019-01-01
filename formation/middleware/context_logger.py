from ..formation import _REQ_HTTP, _RES_HTTP, _CONTEXT, _REQ_DURATION


def context_logger(logger):
    def context_logger_middleware(ctx, next):
        context = ctx.get(_CONTEXT, {})
        logger.bind(**context).info("context")
        ctx = next(ctx)
        return ctx

    return context_logger_middleware
