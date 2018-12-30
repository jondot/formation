import datetime


def request_duration(now=datetime.datetime.now):
    def request_duration_middleware(ctx, next):
        start = now()
        ctx = next(ctx)
        end = now() - start
        ctx["req.duration_us"] = end.microseconds
        return ctx

    return request_duration_middleware
