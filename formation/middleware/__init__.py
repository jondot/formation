from .breaker import create_circuit_breaker
from .context import create_context
from .logger import create_request_logger
from .request_duration import create_request_duration
from .request_id import create_request_id
from .retry import retry


def default_stack(logger):
    return [
        create_request_id(),
        create_context(),
        create_request_duration(),
        create_request_logger(logger),
    ]
