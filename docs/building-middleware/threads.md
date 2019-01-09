---
id: threads
sidebar_label: Thread Safety and Concurrency
hide_title: true
---
# Thread Safety and Concurrency

Although not such a popular topic in the Python ecosystem to discuss (perhaps most infrastructure is still process based?) -- I believe a few words should be said about thread safety, just to be safe (pun intended).

The lifecycle of a Formation middleware is one per class. That means middleware instances are shared between all instances of your client.

This design decision is common in other middleware stacks as well, and the reasoning is to force the burden of maintaining implict state out of your infrastructure. What this means is simple:

> When you build your middleware, it should be thread safe.

To break it down, here are a few rules of thumb:

* Don't keep state in your middleware. Keeping state in your middleware will only call for trouble as it's an out-of-band, implicit state that someone needs to reason about. If you want to keep state, put it in the Formation context.
* Make sure all infrastructure pieces (for example your logger in a logger middleware) are _already_ thread safe.

Have fun!



