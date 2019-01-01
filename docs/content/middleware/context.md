# Context

General request context collection. Collects data points like thread ID, process ID, and so on, for common middleware usage.

_Api:_

```py
# all params come with defaults
context(
    namespace="service",
    scope="all",
    env="local",
    sha="dev",
    version="0.01",
    context_fn=get_context,
    getpid=os.getpid,
    gettid=thread.get_ident,
)
```

_Context:_

* `v` - Logical product version
* `sha` - Physical source tree version (e.g. Git SHA)
* `env` - Development environment
* `pid` - Process ID of current process running request
* `tid` - Thread ID of current thread running request
* `uid` - User ID for the current request
* `scope` - Scope, i.e. module name
* `ns` - Namespace, i.e. product name
* `rid` - Request ID for correlation
* `rid_p` - Parent request ID for correlation,


_Usage:_

```py
from formation.middleware import context

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        context(
            namespace="acme"
            scope="billing"
        )
    ]
    ...
```


_Accessing context from your middleware:_

```py
from formation import _CONTEXT
def my_mware(mime_type):
    def my_mware_middleware(ctx, call):
        c = ctx.get(_CONTEXT)
        print(c)
        return call(ctx)

    return my_mware_middleware
```
