#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Just demonstrate how to print a hello world
#   using asyncio's eventloop.
#

import asyncio


# The decorator will convert the func to a coroutine
@asyncio.coroutine
def say_hello():
    print('Hello world!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(say_hello())
