
import datetime


def create_request_duration(now=datetime.datetime.now):
    def request_duration(ctx, next):
        start = now()
        ctx = next(ctx)
        end = now() - start
        ctx["req.duration_us"] = end.microseconds
        return ctx

    return request_duration
