#! /usr/bin/env python
#
# asyncio training (@igalarzab)
# =============================
#
# What:
#    Implement a redis client using coroutines
#

import asyncio
import sys


def build_command(command, *arguments):
    """
    Build a redis command using RESP
    """
    arguments = [arg for arg in arguments if arg is not None]
    command = '*%(num_params)d\r\n$%(len_command)d\r\n%(command)s\r\n' % {
        'num_params': len(arguments) + 1,
        'len_command': len(command),
        'command': command
    }

    for i in range(len(arguments)):
        command += '$%(len_param)d\r\n%(param)s\r\n' % {
            'len_param': len(arguments[i]),
            'param': arguments[i]
        }

    return command.encode()


@asyncio.coroutine
def get_response(reader):
    response = (yield from reader.readline()).decode()

    if response[0] in ('+', '-'):
        return response[1:]
    elif response[0] == '$':
        return (yield from reader.readline()).decode()
    else:
        return '?\n'


@asyncio.coroutine
def main(command, name, value=None):
    reader, writer = yield from asyncio.open_connection('127.0.0.1', 6379)

    raw_command = build_command(command, name, value)

    writer.write(raw_command)
    yield from writer.drain()

    response = yield from get_response(reader)
    print("Command %s sent, received %s" % (command, response), end='')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Use: %s [get|set] key_name [key_value]' % sys.argv[0])
        sys.exit(0)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1], *sys.argv[2:]))
