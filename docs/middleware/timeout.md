---
id: timeout
sidebar_label: Timeout
hide_title: true
---
# Timeout

Set a timeout on a request (HTTP).


## API

```py
# all params have default values
timeout(
    timeout=None
)
```

## Usage

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
