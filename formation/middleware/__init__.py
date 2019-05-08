from .breaker import (
    circuit_breaker,
    trigger_breaker_if,
    BreakerTriggerException,
)  # noqa
from .context import context
from .context_logger import context_logger  # noqa
from .logger import request_logger
from .request_duration import request_duration
from .request_id import request_id
from .retry import retry  # noqa
from .ua import ua  # noqa
from .accept import accept  # noqa
from .timeout import timeout  # noqa


def default_stack(logger):
    return [request_id(), context(), request_duration(), request_logger(logger)]
