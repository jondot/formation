import pytest
from .utils import DummyLogger
from formation.middleware import (
    circuit_breaker,
    trigger_breaker_if,
    BreakerTriggerException,
)


def malfunction(ctx):
    raise Exception()


def force_run(cb):
    try:
        cb({}, malfunction)
    except:  # noqa
        pass


def test_trigger():
    t = trigger_breaker_if(lambda res: True)
    try:
        t({}, lambda _: {})
        pytest.fail("should throw")
    except BreakerTriggerException as ex:
        pass


def test_circuit_breaker_middleware(snapshot):
    logger = DummyLogger()
    cb = circuit_breaker(logger, "test-cb")
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)

    snapshot.assert_match(logger.messages)

