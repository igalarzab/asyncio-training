#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#   Implement a basic echo client using asyncio
#   StreamReaderProtocol
#

import asyncio
import sys


def send_data():
    reader, writer = yield from asyncio.open_connection('127.0.0.1', sys.argv[1])
    message = ' '.join(sys.argv[2:]) + '\n'

    writer.write(message.encode())
    yield from writer.drain()
    print('Message sent: %s' % message, end='')

    data = yield from reader.readline()
    print('Message received: %s' % data.decode(), end='')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Use: %s port message...' % sys.argv[0])
        sys.exit(0)

    loop = asyncio.get_event_loop()
    task = asyncio.async(send_data())

    loop.run_until_complete(task)
    loop.close()
