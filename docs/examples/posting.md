---
id: posting
sidebar_label: Posting Data
hide_title: true
---
# Posting Data

In this example we'll post data to _httpbin_, a popular development tool to use when testing out HTTP clients.

First, let's import:

```py
from formation.for_requests import client, json_response
from formation.middleware import request_logger, ua, accept, timeout
import structlog
```

We use `client` to make our client, multiple middleware from `formation.middleware` and `structlog` to facilitate structured logging.


This is all it takes to make a class into a full blown HTTP client powered by formation:

```py
@client
class HttpBin(object):
    pass
```

Next, we'll set up how we want it to behave:

1. Required middleware from `formation.middleware`
2. Response type that we should always expect
3. A base URI to follow for the calls


In turn, we get a `self.request` to play with.

```py
@client
class HttpBin(object):
    base_uri = "https://httpbin.org"
    middleware = [
        timeout(0.1),
        accept("application/json"),
        ua("the-fabricator/1.0.0"),
        request_logger(structlog.getLogger()),
    ]
    response_as = json_response
```

Now, let's actually post data:

```py
    def publish(self, data):
        return self.request.post("post", data=data)
```

This will post to `post`, and actually, to `https://httpbin.org/post`. When you build the client, you don't need to worry about the base URI.

When a call makes its way out, it goes through _all of the middleware_ that we set up, and when it comes back, it goes through them again, and finally through our response _terminator_, specifically -- `json_response`.

This all means you eventually get a JSON response. All formation client responses are in a tuple form:

```
(body, code, headers)
```

And you can pick and choose. Here how we use our new client:

```py
httpbin = HttpBin()
(resp, _, _) = httpbin.publish(data)
```

And for the full listing:

```py
from formation.for_requests import client, json_response
from formation.middleware import request_logger, ua, accept, timeout
import structlog


@client
class HttpBin(object):
    base_uri = "https://httpbin.org"
    middleware = [
        timeout(0.1),
        accept("application/json"),
        ua("the-fabricator/1.0.0"),
        request_logger(structlog.getLogger()),
    ]
    response_as = json_response

    def publish(self, data):
        return self.request.post("post", data=data)
```
