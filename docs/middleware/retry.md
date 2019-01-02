---
id: retry
sidebar_label: Retry
hide_title: true
---
# Retry

A generic retry policy middleware (not specific to network requests). Will retry upon exception until meeting a `max_retries` threshold.

## API

```py
# all params have default values
retry(
    max_retries=3
)
```

## Usage

```py
from formation.middleware import retry

@client
class Google(object):
    base_uri = "https://google.com"
    middleware=[
        retry()
    ]
    ...
```
