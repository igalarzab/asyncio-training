#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Implement a basic echo server using asyncio's
#   protocol class
#

import asyncio
import sys


class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print('Message received: {}'.format(data.decode()), end='')
        self.transport.write(data + b'\n')

    def connection_lost(self, exc):
        print('Client disconnected...')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Use: %s port' % sys.argv[0])
        sys.exit(0)

    loop = asyncio.get_event_loop()
    coro = loop.create_server(EchoServer, '127.0.0.1', sys.argv[1])
    server = loop.run_until_complete(coro)
    print('Listening on {}'.format(server.sockets[0].getsockname()))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
