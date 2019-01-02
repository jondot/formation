---
id: user-agent
sidebar_label: User Agent
hide_title: true
---
# User Agent

Sets `User-Agent` in request.

## Usage

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
