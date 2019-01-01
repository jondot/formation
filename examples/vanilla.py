from formation import wrap, _CONTEXT
from formation.middleware import retry, context_logger, context
import structlog


def bad_function(ctx):
    print(ctx)
    if ctx[_CONTEXT].get("env") == "development":
        raise Exception("boo hoo")


stack = wrap(
    lambda ctx: bad_function(ctx),
    middleware=[
        context(env="development"),
        context_logger(structlog.getLogger()),
        retry(max_retries=2),
    ],
)


# This should always fail, but you should see two retries, and a log
# to indicate the context that's been discovered.
if __name__ == "__main__":
    stack({"args": ["hello", "world"]})
