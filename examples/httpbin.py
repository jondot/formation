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


if __name__ == "__main__":
    data = {"key1": ["value1", "value2"]}
    httpbin = HttpBin()
    try:
        (resp, _, _) = httpbin.publish(data)
        print(resp)
        print("if you see this, you have a very fast internet")
    except:
        print("call timed out, which is OK because timeout is 100ms")
