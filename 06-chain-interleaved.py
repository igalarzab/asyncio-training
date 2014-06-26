#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Show how to chain coroutines using yield from, having
#   more than one coroutine scheduled on the eventloop
#
# Question:
#   1º) It will print always the same? Why?
#   2º) Why is recommended to use the @coroutine decorator?
#

import asyncio


@asyncio.coroutine
def db_look(username, password):
    # Moar huge computation
    yield from asyncio.sleep(1)
    print('Thinking on your username')
    yield from asyncio.sleep(2)  # Moar huge computation
    print('Thinking on your password... uhmmm....')
    yield from asyncio.sleep(2)  # Moar huge computation
    print('Well, ok')
    return True


@asyncio.coroutine
def authenticate():
    result = yield from db_look('paco', 'pass')
    print('Ouh yeah' if result else 'Why?!')


# As you see, the @coroutine decorator isn't necessary (but recommended)
def noise():
    while True:
        print('BOOOM!')
        yield from asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.Task(noise())
    loop.run_until_complete(authenticate())
