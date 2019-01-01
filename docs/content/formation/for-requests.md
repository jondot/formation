# For Requests

While Formation was created as a _generic_ middleware infrastructure, it has special support for [requests](https://github.com/requests/requests).

If you want to create an HTTP client that is production grade: operable, maintainable, and robust -- Formation's `for_requests` and `middleware` submodules contains the building blocks to do so.

Here's a canonical Google client, created with Formation:

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


Note that it uses a sister project, [attrs-serde](https://github.com/jondot/attrs-serde) to shape queries and data contracts, which helps build a client that feels strongly typed and is more maintainable and has a self-explaining API.


Here's how you would probably build a client in a production-like settings (imports omitted):

```py
@client
class ConversionDownloader(object):
    base_uri = "https://internal.acme.srv/ads"
    middleware = [
        request_id(),
        context(
            namespace="ads",
            scope="conversion-downloader",
            env=env.get('NODE_ENV', 'development'),
            sha=current_git_sha(),
            version=ads.__version__,
        ),
        request_logger(structlog.getLogger()),
        request_duration(),
        circuit_breaker(),
        timeout(0.3)
    ]
    response_as = json_response

    def download(self, text):
        return self.request.get("/ad-conversions", params=Query(text))
```

This client tells a story, here's the important bits.

## Avoids Cascading Errors 

Cascading errors are the silent killer of production environments. If you pay attention to post-mortems great companies like Amazon, Google publish, in many ways the root cause is a cascading error. 

The reason is that usual errors, and even complex errors, are caught by the intelligent people that are already working on these systems at these companies. Cascading errors and their effects notoriously don't. This only means that we can't count on intelligence alone, and program _defensively_, by dividing codebases and separating mechanisms with [bulk heads](https://en.wikipedia.org/wiki/Bulkhead_(partition)).

Here are two that operate here:

* This specific client requests are bound by a 300ms limit, enabling predictable workloads. Essentially a bulkhead in the form of timeout or in other words it doesn't allow for thundering herds effect to happen due to a build-up of slow clients.

* It sports a circuit breaker, effectively making error conditions more civilized and keeps bad behavior under a stop-gap mechanism. Based on `pybreaker`, this one has support for open/half-open/closed and central state management; and is arguably the closest thing in the Python ecosystem to [hysterix](https://github.com/Netflix/Hystrix) considered by many as industry standard circuitbreaker implementation.


## Great Operability By Default

Production systems should be _operable_. They should be as easy to do forensics on, in real time, under stress, as they are to maintain and develop.

This client supports operability because:

* It adds request duration and request context - various bits of data and insights that make sense when shit hits the fan and you need to answer operative questions. How long did it take? on what machine? in what environment? from which code base was this cut? and more.

* Correlation ID is added to every request. Generated if missing and carried forward if already given; this allows for traceability and the power to search for a storyline of every business process via one connecting ID in your central log management system.

* Finally, a standard structured logging systems makes sure that you get data in a user-friendly way as well as machine friendly way, using `structlog`.

## Learning as Code

A huge enabler of modularity in this client, is the formation middleware 
mechanism. It means that what ever learning happens from production or elsewhere, you can codify and build a middleware to solve for. 

You then stick it in the middleware stack and hopefully share it share with other services and teams. Before you know it, you have a _standard_ production stack, which is your best practices, living as code, telling _your_ production story and experience.


