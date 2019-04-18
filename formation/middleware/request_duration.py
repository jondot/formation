import datetime
import math


def request_duration(now=datetime.datetime.now):
    def request_duration_middleware(ctx, next):
        start = now()
        ctx = next(ctx)
        end = now() - start
        ctx["req.duration_us"] = math.floor(end.total_seconds() * 1e6)
        return ctx

    return request_duration_middleware
