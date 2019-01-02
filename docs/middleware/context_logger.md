---
id: context-logger
sidebar_label: Context Logger
hide_title: true
---
# Context Logger

A general logger middleware for anything with context. Will log context created by the [context](context.md) middleware.

## Usage

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
