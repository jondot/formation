---
id: scraping
sidebar_label: Scraping Web Sites
hide_title: true
---
# Scraping Web Sites

Formation client recognizes that one of the popular tasks in Python, having a rich data science ecosystem, is information retrieval, or in the more down-to-earth name: scraping.

When you use `html_response` you get an xpath/css selector ready result:

```py
from formation.for_requests import client, html_response
from formation.middleware import request_logger
from attr import attrib, attrs
from attrs_serde import serde
import structlog

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