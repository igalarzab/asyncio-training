#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Implement a basic echo client using asyncio's
#   protocol class
#

import asyncio
import sys


class EchoClient(asyncio.Protocol):

    def connection_made(self, transport):
        message = ' '.join(sys.argv[2:]) + '\n'
        transport.write(message.encode())
        print('Message sent: {}'.format(message), end='')

    def data_received(self, data):
        print('Message received: {}'.format(data.decode()), end='')
        asyncio.get_event_loop().stop()

    def connection_lost(self, exc):
        print('Server disconnected...')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Use: %s port message...' % sys.argv[0])
        sys.exit(0)

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(EchoClient, '127.0.0.1', sys.argv[1])
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
