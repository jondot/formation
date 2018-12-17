
import pybreaker
from ..formation import _CONTEXT


def breaker_logger(logger):
    class LogListener(pybreaker.CircuitBreakerListener):
        "Listener used to log circuit breaker events."

        def state_change(self, cb, old_state, new_state):
            logger.warn(
                "circuitbreaker.state.changed",
                name=cb.name,
                old_state=old_state.name,
                new_state=new_state.name,
            )

    return LogListener()


def create_circuit_breaker(logger, name):
    breaker = pybreaker.CircuitBreaker(name=name, listeners=[breaker_logger(logger)])

    def circuit_breaker(ctx, call):
        context = ctx.get(_CONTEXT, {})
        log = logger.bind(**context)

        if breaker.current_state == "open":
            log.info("circuitbreaker.middleware.open", name=breaker.name)

        call = breaker(call)

        try:
            ctx = call(ctx)
            return ctx
        except pybreaker.CircuitBreakerError:
            return ctx

    return circuit_breaker
