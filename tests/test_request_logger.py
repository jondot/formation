from .utils import DummyLogger
from toolz.curried import update_in, keyfilter
from formation.for_requests import build_sender
from formation.middleware import (
    request_id,
    context,
    request_duration,
    request_logger,
    context_logger,
)
import pytest
import datetime


def get_test_stack(logger):
    now = lambda: datetime.datetime(2018, 12, 4, 16, 25, 28, 183004)
    return [
        request_id(idgen=lambda: "req-1"),
        context(getpid=lambda: "pid-1", gettid=lambda: "tid-1"),
        context_logger(logger),
        request_duration(now=now),
        request_logger(logger),
    ]


def sanitize(d):
    if d:
        filtered = keyfilter(lambda k: k not in ["etag", "elapsed"], d)
        return filtered
    return d


@pytest.mark.vcr()
def test_default_stack(snapshot):
    logger = DummyLogger()
    sender = build_sender(middleware=get_test_stack(logger))
    sender("get", "http://example.com")
    snapshot.assert_match(
        list(
            map(
                lambda arr: [
                    arr[0],
                    arr[1],
                    sanitize(update_in(arr[2], ["headers"], sanitize)),
                    sanitize(arr[3]),
                ],
                logger.messages,
            )
        )
    )
    snapshot.assert_match(sanitize(logger.context))
