#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Show how to connect to different servers at
#   the same time, demonstrating how to use typical
#   third-party asyncio libraries
#

import asyncio
import websockets
import aioredis


@asyncio.coroutine
def get_number_clients(redis):
    value = yield from redis.get('websocket_clients')
    return value


@asyncio.coroutine
def inc_number_clients(redis):
    ok = yield from redis.incr('websocket_clients')
    return b'OK' == ok


@asyncio.coroutine
def handle_client(websocket, path):
    print("Client connected")
    redis = yield from aioredis.create_redis(('127.0.0.1', 6379))

    yield from inc_number_clients(redis)
    number_clients = yield from get_number_clients(redis)

    yield from websocket.send(
        'Hi, you are the client %s of this chat' % number_clients.decode()
    )

    while True:
        data = yield from websocket.recv()

        if not data or data == 'quit':
            yield from websocket.send('Bye!')
            websocket.close()
            print('Client disconnected')
            return

        yield from websocket.send(data)


if __name__ == '__main__':
    start_server = websockets.serve(handle_client, '127.0.0.1', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    print('WebSocket connected')
    asyncio.get_event_loop().run_forever()
