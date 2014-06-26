#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Show how to chain coroutines using yield from
#

import asyncio


@asyncio.coroutine
def db_look(username, password):
    yield from asyncio.sleep(1)  # Huge computation
    return True


@asyncio.coroutine
def authenticate():
    result = yield from db_look('paco', 'pass')

    if result:
        print('Ouh yeah')
    else:
        print('Why?!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(authenticate())
