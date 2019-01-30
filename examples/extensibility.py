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

    def __init__(self, **kwargs):
        pass

    def search(self, text):
        return self.request.get("/", params=Query(text))


if __name__ == "__main__":
    google = Google(base_uri="https://www.google.co.il")
    (xml, _code, _headers) = google.search("larry page")
    print(google.base_uri)
    print(xml.xpath("//title/text()"))
