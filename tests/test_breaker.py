from .utils import DummyLogger
from formation.middleware import circuit_breaker


def malfunction(ctx):
    raise Exception()


def force_run(cb):
    try:
        cb({}, malfunction)
    except:  # noqa
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

