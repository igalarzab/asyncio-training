#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Print a hello world using a task, demonstrating how
#   tasks execute registering themselves in the eventloop,
#   unlike normal coroutines.
#

import asyncio


@asyncio.coroutine
def say_hello():
    print('Hello world')

    # Sleep one second (without blocking), then stop the loop
    yield from asyncio.sleep(1)
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # async() convert coroutines to Tasks, so both lines are equivalent
    # asyncio.async(say_hello())
    asyncio.Task(say_hello())

    # Task won't be executed until the loop runs
    loop.run_forever()
