---
id: breaker
sidebar_label: Circuit Breaker
hide_title: true
---
# Circuit Breaker

A general logger middleware for requests. Will log context created by the [context](context.md) middleware.

## API

```py
def circuit_breaker(
    logger, 
    name, 
    fail_max=5, 
    reset_timeout=60, 
    state_storage=None, 
    exclude=[]
)
```

For detailed information about the above parameters, see [pybreaker](https://github.com/danielfm/pybreaker).


## Usage

```py
from formation.for_requests import client
from formation.middleware import circuit_breaker

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        circuit_breaker(structlog.getLogger(), 'breaker-1')
    ]
    ...
```
