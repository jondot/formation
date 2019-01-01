# User Agent

Sets `User-Agent` in request.

_Usage:_

```py
from formation.middleware import ua

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        ua('super-client/1.0')
    ]
    ...
```
