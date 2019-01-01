# Request Logger

A general logger middleware for requests. Will log context created by the [context](context.md) middleware.

_Usage:_

```py
from formation.middleware import request_logger

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        request_logger(structlog.getLogger())
    ]
    ...
```
