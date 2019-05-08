import pytest
from formation.for_requests import client, json_response
from formation.middleware import retry


def snap(resp_tuple):
    return (resp_tuple[0], resp_tuple[1], sorted(resp_tuple[2].items()))


def fail(times):
    def fail_middleware(ctx, call):
        t = ctx.get("fail", times)
        t = t - 1
        if t <= 0:
            return call(ctx)
        else:
            ctx["fail"] = t
            raise RuntimeError("something is wrong")

    return fail_middleware


@client
class HttpBinNice(object):
    base_uri = "https://httpbin.org"
    middleware = [retry(5), fail(3)]
    response_as = json_response

    def get(self):
        return self.request.get("get")


@client
class HttpBinBad(object):
    base_uri = "https://httpbin.org"
    middleware = [retry(5), fail(10)]
    response_as = json_response

    def get(self):
        return self.request.get("get")


@pytest.mark.vcr()
def test_retry(snapshot):
    c = HttpBinNice()
    snapshot.assert_match(snap(c.get()))


@pytest.mark.vcr()
def test_retry_fails(snapshot):
    c = HttpBinBad()

    try:
        c.get()
        pytest.fail("should actually fail")
    except RuntimeError as ex:
        pass
