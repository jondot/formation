from ..formation import _RETRY


def retry(max_retries=3):
    def retry_middleware(ctx, call):
        try:
            res = call(ctx)
            return res
        except Exception as ex:
            retries = ctx.get(_RETRY, 0)
            if retries >= max_retries - 1:
                raise ex
            ctx[_RETRY] = 1 + retries
            # TODO exponential backoff
            res = retry_middleware(ctx, call)
            return res

    return retry_middleware
