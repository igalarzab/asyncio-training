#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Show common errors when programming coroutines
#   using asyncio
#
# Question:
#   1º) What's the supposed answer?
#   2º) How to fix it?
#

import asyncio


@asyncio.coroutine
def say_hi():
    yield from asyncio.sleep(1)
    print('Hello', end='')


def say_bye():
    yield from asyncio.sleep(3)
    print(' world', end='')


@asyncio.coroutine
def main():
    asyncio.async(say_hi())
    asyncio.Task(say_bye())
    yield from asyncio.sleep(2)
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('!')
