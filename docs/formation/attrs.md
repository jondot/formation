---
id: attrs
sidebar_label: Structured Queries with Attrs
hide_title: true
---
# Structured Queries with Attrs

[Attrs](https://attrs.org) is a popular and lightweight data class implementation for Python.

With Formation and its sister-project [attrs-serde](https://github.com/jondot/attrs-serde) you can build an HTTP client that treats all queries as structured, strongly typed, queries. Here's an example:


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

Formation client will detect `Query` being an `attrs-serde` friendly class instance and will serialize it into a query string automatically.

To see how you can build even more sophisticated clients, learn more about [attrs-serde](https://github.com/jondot/attrs-serde).