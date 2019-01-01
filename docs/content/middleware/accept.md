# Accept

Sets `Content-Type` in request.

_Usage:_

```py
from formation.middleware import accept

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        accept('application/json')
    ]
    ...
```
