from formation.for_requests import client, html_response
import traceback
from formation.middleware import (
    request_logger,
    circuit_breaker,
    trigger_breaker_if,
    timeout,
)
from attr import attrib, attrs
from attrs_serde import serde
from time import sleep
import structlog


logger = structlog.getLogger()


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

    def go(self):
        return self.request.get("/")


#
# for this example, we're triggering an error on an HTTP OK (200) from
# example.com. With the timings set on the breaker, you'll see something
# along these lines:
#
# ok
# breaker open
# half open
# .. (timeout 10s for reseting breaker)
# breaker half-closed
# (request)
# breaker open
# half open
#
# and so on, which symbols correct operation.
#
if __name__ == "__main__":
    breaker = Breaker()
    while True:
        print("requesting...")
        try:
            (xml, _code, _headers) = breaker.go()
        except Exception as ex:
            # traceback.print_exc()
            print(ex.__class__)
            print("error.")
        print("ok.")
        sleep(1)
