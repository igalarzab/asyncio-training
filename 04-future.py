#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Print a hello world using a future, showing how the
#   eventloop can be executed until the future is resolved.
#

import asyncio


@asyncio.coroutine
def say_hello(future):
    print('Hello ', end='')
    future.set_result('world!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fut = asyncio.Future()
    asyncio.async(say_hello(fut))
    loop.run_until_complete(fut)
    print(fut.result())
