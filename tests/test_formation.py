from formation import wrap
import pytest
from requests import get


def log(ctx, call):
    print("started")
    ctx = call(ctx)
    print("ended")
    return ctx


def status_code(ctx, call):
    ctx = call(ctx)
    ctx["status_code"] = ctx["res"].status_code
    return ctx


# TODO: requests adapter (in and out)
def call_google(ctx={}):
    res = get("https://google.com")
    ctx.update({"res": res})
    return ctx


@pytest.mark.vcr()
def test_formation(snapshot):
    fancy_caller = wrap(call_google, middleware=[log, status_code])
    ctx = fancy_caller({})
    snapshot.assert_match(
        {
            "status_from_middleware": ctx["status_code"],
            "status_from_request": ctx["res"].status_code,
        }
    )
