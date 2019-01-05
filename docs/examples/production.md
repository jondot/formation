---
id: production
sidebar_label: Production Ready Clients
hide_title: true
---
# Production Ready Clients

Formation client has a few middleware to support production ready clients. Clients that are robust, fail fast and recover from failure in a timely manner.

The idea about formation is to be able to compose and execute a set of middleware on any kind of Python code. In this instance we use both the middleware infrastructure and the HTTP client (`for_requests`) to show how that can be powerful.

First, the necessary imports:

```py
from formation.for_requests import client, html_response
from formation.middleware import (
    request_logger,
    circuit_breaker,
    trigger_breaker_if,
    timeout,
)
import structlog

logger = structlog.getLogger()
```

Next, the client and middleware stack:


```py
@client
class Breaker(object):
    base_uri = "https://example.com"
    middleware = [
        timeout(1),
        circuit_breaker(logger, "breaker-1", reset_timeout=10),
        trigger_breaker_if(lambda res: res.status_code == 200),
        request_logger(logger),
    ]
    response_as = html_response
```
Here, we see that we allow for just one second timeout, for all requests -- `timeout(1)`, we set up a [circuit breaker](https://martinfowler.com/bliki/CircuitBreaker.html) with `circuit_breaker` in addition to defininf how it should trip with `trigger_breaker_if`.

Finally we're setting up a structured logger with `request_logger`.

