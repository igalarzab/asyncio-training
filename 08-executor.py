#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   How to run tasks in an executor
#
# Questions:
#   1º) Why do we need an executor here?
#

import asyncio
import signal
import time


def signal_handler():
    print("I received the signal")


def blocking_callback():
    time.sleep(3)


@asyncio.coroutine
def coroutine_blocking():
    for i in range(3):
        blocking_callback()
        print('Loop %d' % i)


@asyncio.coroutine
def coroutine_nonblocking():
    for i in range(3):
        yield from loop.run_in_executor(None, blocking_callback)
        print('Loop %d' % i)


@asyncio.coroutine
def main():
    loop.add_signal_handler(signal.SIGINT, signal_handler)
    # yield from coroutine_blocking()
    yield from coroutine_nonblocking()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
