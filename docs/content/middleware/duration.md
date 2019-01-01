# Request Duration

Sets request duration in context for other middleware to use down the pipeline. See [logger](logger.md) for how it's being used.


_Usage:_

```py
from formation.middleware import request_duration

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        request_duration()
    ]
    ...
```
