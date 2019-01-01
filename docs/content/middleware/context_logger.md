# Context Logger

A general logger middleware for anything with context. Will log context created by the [context](context.md) middleware.

_Usage:_

```py
from formation.middleware import context_logger

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        context_logger(structlog.getLogger())
    ]
    ...
```
