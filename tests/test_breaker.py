from .utils import DummyLogger
from formation.middleware import create_circuit_breaker


def malfunction(ctx):
    raise Exception()


def force_run(cb):
    try:
        cb({}, malfunction)
    except:
        pass


def test_circuit_breaker_middleware(snapshot):
    logger = DummyLogger()
    cb = create_circuit_breaker(logger, "test-cb")
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)
    force_run(cb)

    snapshot.assert_match(logger.messages)

