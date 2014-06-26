#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Just demonstrate how to print a hello world
#   using asyncio's eventloop.
#
# NOTE:
#   This example is a little bit silly because say_hello
#   is a normal function and **not** a real coroutine. It's
#   just to show a hello-world as simple as possible using
#   asyncio event loop

import asyncio


# The decorator will convert the func to a coroutine (see NOTE above)
@asyncio.coroutine
def say_hello():
    print('Hello world!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(say_hello())
