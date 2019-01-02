---
id: docs
sidebar_label: About Formation
hide_title: true
---

# About Formation


Formation is a generic functional middleware infrastructure for Python. With it, you compose a stack of middleware, each of which has a tiny API, a shared context, and an ability to cancel or proceed to the next middleware.

In many ways, it is similar to Ruby's [Rack](https://rack.github.io/) middleware, and Node's [connect](https://github.com/senchalabs/connect). In the context of Python, it is a higher-level abstraction over WSGI.

Formation is not Pythonic, and it doesn't abide to the _Zen of Python_, where suitable it does away with these, and optimizes for developer happiness.

## As a Generic Middleware Infra

It can be used for any Python codebase and purpose:

```py
from datetime.datetime import now
from formation import wrap
from requests import get

def log(ctx, call):
    print("started")
    ctx = call(ctx)
    print("ended")
    return ctx

def timeit(ctx, call):
    started = now()
    ctx = call(ctx)
    ended = now() - started
    ctx['duration'] = ended
    return ctx

def to_requests(ctx):
    get(ctx['url'])

fancy_get = wrap(to_requests, middleware=[log, timeit])
fancy_get({'url':'https://google.com'})
```

## In Use with Requests

Or, using `formation.for_requests` for the requests HTTP lib:


```py
from formation.for_requests import client, html_response
from formation.middleware import request_logger
from attr import attrib, attrs
from attrs_serde import serde
import structlog

@serde
@attrs
class Query(object):
    query = attrib(metadata={"to": ["q"]})

@client
class Google(object):
    base_uri = "https://google.com"
    middleware = [request_logger(structlog.getLogger())]
    response_as = html_response

    def search(self, text):
        return self.request.get("/", params=Query(text))

if __name__ == "__main__":
    google = Google()
    (xml, _code, _headers) = google.search("larry page")
    print(xml.xpath("//title/text()"))
```
