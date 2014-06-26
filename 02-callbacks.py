#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Just demonstrate how to execute callbacks
#   using the eventloop
#

import asyncio


# What happens if we convert it to a coroutine?
# @asyncio.coroutine
def callback_now():
    print('Hello world!')


def callback_later(seconds):
    print('%d seconds later!' % seconds)


def callback_repeat(seconds):
    print('%s seconds later!' % seconds)
    loop.call_later(seconds, lambda: callback_repeat(seconds))


def stop_loop(seconds):
    print('stop loop %s seconds later' % seconds)
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(callback_now)
    loop.call_later(3, lambda: callback_later(3))
    loop.call_later(1, lambda: callback_repeat(1))
    loop.call_at(loop.time() + 5, lambda: stop_loop(5))
    loop.run_forever()
