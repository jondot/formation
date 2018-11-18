from toolz import reduce


def wrap(call, middleware=[]):
    return reduce(
        lambda acc, m: lambda ctx: m(ctx, acc),
        reversed(middleware),
        lambda ctx: call(ctx),
    )
