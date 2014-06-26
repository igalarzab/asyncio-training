#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Implement a basic echo server using asyncio
#   StreamReaderProtocol
#

import asyncio
import sys


def client_handle(reader, writer):
    while True:
        data = yield from reader.readline()

        if not data:
            return

        print('Message received: {}'.format(data.decode()), end='')
        writer.write(data)
        yield from writer.drain()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Use: %s port' % sys.argv[0])
        sys.exit(0)

    loop = asyncio.get_event_loop()
    fut = asyncio.start_server(client_handle, '127.0.0.1', sys.argv[1])
    server = loop.run_until_complete(fut)
    print('Listening on {}'.format(server.sockets[0].getsockname()))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
