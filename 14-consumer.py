#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#    Implement a serie of consumers and producers of data
#

import asyncio
from random import randrange

queue = asyncio.Queue(maxsize=15)


def consume_messages():
    while True:
        yield from queue.get()
        print('[] -> Messages in queue %d' % queue.qsize())
        yield from asyncio.sleep(randrange(10))


def gen_messages():
    while True:
        yield from queue.put('Message')
        print('[] <- Messages in queue %d' % queue.qsize())
        yield from asyncio.sleep(randrange(3))


if __name__ == '__main__':

    for _ in range(3):
        asyncio.async(gen_messages())

    for _ in range(10):
        asyncio.async(consume_messages())

    asyncio.get_event_loop().run_forever()
