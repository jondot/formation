# Request ID

Sets request ID in request. Useful for correlating many requests in a distributed system via centralized logging search system (e.g. Splunk, ELK, Graylog).

_API:_

```py
# all params have default values
request_id(
    key="x-request-id", 
    idgen=uuid4
)
```

* `key` will appear as an HTTP request header
* You can swap an ID generation function with `idgen`

_Usage:_

```py
from formation.middleware import request_id

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        request_id()
    ]
    ...
```
