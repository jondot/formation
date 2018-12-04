
from formation.for_requests import build_sender
import pytest


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
