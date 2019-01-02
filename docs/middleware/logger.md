---
id: request-logger
sidebar_label: Request Logger
hide_title: true
---
# Request Logger

A general logger middleware for requests. Will log context created by the [context](context.md) middleware.

## Usage

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
