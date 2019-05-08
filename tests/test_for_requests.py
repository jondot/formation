from formation.for_requests import build_sender, apply_params
from formation.middleware import ua, accept
import pytest


def test_apply_params(snapshot):
    snapshot.assert_match(
        apply_params(
            "http://github.com/:user/:repo?q=foobar",
            {":user": "jondot", ":repo": "formation", "foobar": "foobaz"},
        )
    )


@pytest.mark.vcr()
def test_for_requests():
    sender = build_sender(middleware=[])
    sender("get", "http://example.com")


@pytest.mark.vcr()
def test_for_requests_with_params():
    sender = build_sender(middleware=[])
    sender(
        "get",
        "http://example.com",
        headers={"x-custom": "hello"},
        params={"v": "1.0"},
        data="some-data",
    )


@pytest.mark.vcr()
def test_ua():
    sender = build_sender(middleware=[ua("foobar/1.0.0")])
    sender(
        "get", "http://example.com", headers={"x-custom": "hello"}, params={"v": "1.0"}
    )


@pytest.mark.vcr()
def test_accept():
    sender = build_sender(middleware=[accept("application/json")])
    sender(
        "get", "http://example.com", headers={"x-custom": "hello"}, params={"v": "1.0"}
    )

