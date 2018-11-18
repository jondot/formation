![](media/cover.png)

# Formation

A generic functional middleware infrastructure for Python.

Take a look:

```py
from datetime.datetime import now
from formation import wrap
from requests import get

def log(ctx, call):
    print("started")
    ctx = call(ctx)
    print("ended")
    return ctx

def timeit(ctx, call):
    started = now()
    ctx = call(ctx)
    ended = now() - started
    ctx['duration'] = ended
    return ctx

def to_requests(ctx):
    get(ctx['url'])

fancy_get = wrap(to_requests, middleware=[log, timeit])
fancy_get({'url':'https://google.com'})
```

## Quick Start

Install using pip/pipenv/etc. (we recommend [poetry](https://github.com/sdispater/poetry) for sane dependency management):

```
$ poetry add formation
```

### Thanks:

To all [Contributors](https://github.com/jondot/formation/graphs/contributors) - you make this happen, thanks!

# Copyright

Copyright (c) 2018 [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE.txt) for further details.