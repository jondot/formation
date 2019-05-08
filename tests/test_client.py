import pytest
import formation.for_requests
from formation.for_requests import (
    client,
    html_response,
    raw_response,
    json_response,
    xmltodict_response,
    text_response,
)
from formation.middleware import request_logger, ua, accept, timeout, request_id
from attr import attrib, attrs
from attrs_serde import serde
import structlog


@client
class HttpBin(object):
    base_uri = "https://httpbin.org"
    middleware = [
        request_id(key="x-flabber-id"),
        timeout(1.0),
        accept("application/json"),
        ua("the-fabricator/1.0.0"),
        request_logger(structlog.getLogger()),
    ]
    response_as = json_response

    def get(self):
        return self.request.get("get")

    def post(self, data):
        return self.request.post("post", data=data)

    def put(self, data):
        return self.request.put("put", data=data)

    def delete(self):
        return self.request.delete("delete")

    def get_4xx(self):
        return self.request.get("status/404")

    def post_4xx(self, data):
        return self.request.post("status/404", data=data)

    def put_4xx(self, data):
        return self.request.put("status/404", data=data)

    def delete_4xx(self):
        return self.request.delete("status/404")

    def get_5xx(self):
        return self.request.get("status/501")

    def post_5xx(self, data):
        return self.request.post("status/501", data=data)

    def put_5xx(self, data):
        return self.request.put("status/501", data=data)

    def delete_5xx(self):
        return self.request.delete("status/501")

    def get_3xx(self):
        return self.request.get("status/301")

    def post_3xx(self, data):
        return self.request.post("status/301", data=data)

    def put_3xx(self, data):
        return self.request.put("status/301", data=data)

    def delete_3xx(self):
        return self.request.delete("status/301")


@serde
@attrs
class Query(object):
    owner = attrib(metadata={"to": [":owner"]})
    repo = attrib(metadata={"to": [":repo"]})


@client
class Github(object):
    base_uri = "https://api.github.com/"
    middleware = []
    response_as = json_response

    def stargazers(self, owner, repo):
        return self.request.get(
            "repos/:owner/:repo/stargazers", params=Query(owner, repo)
        )


@client
class Google(object):
    base_uri = "https://www.google.com/"
    response_as = html_response

    def go(self, path="/"):
        return self.request.get(path)


@client
class GoogleRaw(object):
    base_uri = "https://www.google.com/"
    response_as = raw_response

    def go(self, path="/"):
        return self.request.get(path)


@client
class XmlToDict(object):
    base_uri = "https://httpbin.org"
    response_as = xmltodict_response

    def go(self, path="/xml"):
        return self.request.get(path)


@client
class GoogleText(object):
    base_uri = "https://www.google.com/"
    response_as = text_response

    def go(self, path="/"):
        return self.request.get(path)


def snap(resp_tuple):
    return (resp_tuple[0], resp_tuple[1], sorted(resp_tuple[2].items()))


@pytest.mark.vcr()
def test_json_all(snapshot):
    h = HttpBin()
    snapshot.assert_match(snap(h.get()))
    snapshot.assert_match(snap(h.post({"testing": 123})))
    snapshot.assert_match(snap(h.put({"testing": 123})))
    snapshot.assert_match(snap(h.delete()))

    snapshot.assert_match(snap(h.get_3xx()))
    snapshot.assert_match(snap(h.post_3xx({"testing": 123})))
    try:
        h.put_3xx({"testing": 123})
        pytest.fail("this method should not be allowed")
    except Exception as ex:
        pass

    try:
        h.delete_3xx()
        pytest.fail("this method should not be allowed")
    except Exception as ex:
        pass

    try:
        h.get_4xx()
        pytest.fail("404 empty response is not json")
    except Exception as ex:
        pass

    try:
        h.post_4xx({"testing": 123})
        pytest.fail("404 empty response is not json")
    except Exception as ex:
        pass

    try:
        h.put_4xx({"testing": 123})
        pytest.fail("404 empty response is not json")
    except Exception as ex:
        pass

    try:
        h.delete_4xx({"testing": 123})
        pytest.fail("404 empty response is not json")
    except Exception as ex:
        pass

    try:
        h.get_5xx()
        pytest.fail("5xx empty response is not json")
    except Exception as ex:
        pass

    try:
        h.post_5xx({"testing": 123})
        pytest.fail("5xx empty response is not json")
    except Exception as ex:
        pass

    try:
        h.put_5xx({"testing": 123})
        pytest.fail("5xx empty response is not json")
    except Exception as ex:
        pass

    try:
        h.delete_5xx({"testing": 123})
        pytest.fail("5xx empty response is not json")
    except Exception as ex:
        pass


@pytest.mark.vcr()
def test_html_response(snapshot):
    google = Google()
    snapshot.assert_match(snap(google.go("/?q=formation")))

    # force error
    snapshot.assert_match(snap(google.go("/aint-no-body-here")))


@pytest.mark.vcr()
def test_raw_response(snapshot):
    google = GoogleRaw()
    snapshot.assert_match(snap(google.go("/?q=formation")))

    # force error
    snapshot.assert_match(snap(google.go("/aint-no-body-here")))


@pytest.mark.vcr()
def test_xmldict_response(snapshot):
    cl = XmlToDict()
    snapshot.assert_match(snap(cl.go()))


@pytest.mark.vcr()
def test_text_response(snapshot):
    google = GoogleText()
    snapshot.assert_match(snap(google.go("/?q=formation")))


@pytest.mark.vcr()
def test_json_response(snapshot):
    github = Github()
    snapshot.assert_match(snap(github.stargazers("jondot", "formation")))

    # force error
    snapshot.assert_match(snap(github.stargazers("no-body", "formation")))


def test_responses_sad(snapshot):
    class Rig:
        xmltodict = xmltodict_response
        json = json_response
        text = text_response
        html = html_response
        raw = raw_response

    snapshot.assert_match(Rig.xmltodict({}))
    snapshot.assert_match(Rig.json({}))
    snapshot.assert_match(Rig.html({}))
    snapshot.assert_match(Rig.raw({}))
    snapshot.assert_match(Rig.text({}))
