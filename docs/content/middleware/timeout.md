# Timeout

Set a timeout on a request (HTTP).


_API:_

```py
# all params have default values
timeout(
    timeout=None
)
```

_Usage:_

```py
from formation.middleware import timeout

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        timeout(0.3) # 300ms
    ]
    ...
```
