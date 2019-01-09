---
id: simple
sidebar_label: A Simple Middleware
hide_title: true
---
# A Simple Middleware

One of the core design ideas for Formation was that a middleware is just a function. Not a class. Just a function.

```py
def print_middleware(ctx, call_next):
    return call_next(ctx)
```

## The Chain

The middleware chain, or stack, or pipeline, is a set of middleware, wrapped around eachother like an onion:

```py
# log_request
#   measure_duration
#      request_http <-- actuall work
#   measure_duration (after)
# log_request (after)
```

So figuratively speaking, without any kind of infrastructure, I would try to do something like this:

```py
log_request(measure_duration(request_http('...')))
```

While that looks fine, it's not composable, and there a lot of questions left out, such as - how do we generically handle state? or how do we cancel a middleware chain that started?

What we _would_ like to do is have to say, here's a bunch of middleware that's like a LEGO, and here's a `request_http` function that actually calls some service, and I want it to be logged, traced, measured, protected with try/catch, and maybe also parsed for its response, and here's how I'd like to do it:

```py
super_request = wrap(request_http, [log,  
                                     trace, 
                                     measure, 
                                     swallow_exception, 
                                     as_json])
# just like request_http, but wrapped w/middleware
super_request('...')
```

This is exactly what Formation does. In fact `wrap` is an actual function in the Formation package:

```py
from formation import wrap
```


## Middleware Lifecycle

Generally speaking, every middleware has things that happen _around_ the next middleware:


1. Before 
2. After
3. Around (Before + After)
4. Continue to the next one or break off
5. Somehow manage state of things, if one middleware want to inform a peer middleware up/down the chain

Here's a Formation middleware that would measure a duration of _something_:

```py
def print_middleware(ctx, call_next):
    started = get_current_time()
    next_ctx = call_next(ctx)
    next_ctx['duration'] = get_current_time() - started
    return next_ctx
```

What this does is to take a snapshot of the time before handing control to the next middleware, getting the result of the next middleware (`next_ctx`) -- which is just a bag of key/values -- sticking the duration on it, an returning it to whoever called that middleware.

The contract for any Formation middleware is simple:

```py
name(context: <dict>, call_next: <middleware>) -> context: <dict>
```


## Before

If you want to do stuff _before_ other middleware, for example a logging middleware, only write code before calling `call_next`:

```py
def print_middleware(ctx, call_next):
    log('hello, world')
    return call_next(ctx)
```

By the way, if you want to supply `log`, just build this as a closure:

```py
def create_print_middleware(log):
    def print_middleware(ctx, call_next):
        log('hello, world')
        return call_next(ctx)
    return print_middleware
```

## After

If you want to handle things that happen _after_ the middleware chain executed, write code after calling `call_next`:

```py
def print_middleware(ctx, call_next):
    ctx = call_next(ctx)
    log('hello, world')
    return ctx
```

Remember, you have to always return `ctx` so keep it aside while doing work, finally returning it.

## Around

And as we've seen with the duration example, if you have to do things which requires both before and around, make sure you write code surrounding `call_next`:

```py
def print_middleware(ctx, call_next):
    started = get_current_time()
    next_ctx = call_next(ctx)
    next_ctx['duration'] = get_current_time() - started
    return next_ctx
```

As an aside, another thing that often is _surrounding_ things, is the try/catch block. If you have to guard against other middleware, feel free to wrap with `try/catch` (you can also create a _middleware_ for generically wrapping and perhaps returning a different kind of exception that is more civilized).


## Passing it On

One poweful control _any_ middleware in the chain has, is the ability to decide if it wants the rest of the middleware down the chain to execute or not.

This is a sophisticated control mechanism. Instead of throwing exceptions, returning errors, or what-have-you, you need to make a simple decision: _call the next middleware or return early_. And you need to make this decision at the call site, localizing logic to where it needs to be (much like Go forces you to handle errors immediately).


```py
def print_middleware(ctx, call_next):
    result = compute_something()

    # I'm a smart middleware and I say: stop the chain!
    if not result: 
        return ctx

    # all good. continue on.
    return call_next(ctx)
```


You stop the chain by simply _not continuing it_, returning `ctx` immediately. In other words, to continue the chain you have to do actual work -- call `call_next`.
