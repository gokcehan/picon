#!/usr/bin/env python
#
# picon.py
#
# https://github.com/gokcehan/lf
#
# Run your code in python interactive console from the command line
#

from __future__ import print_function

import argparse
import code
import collections
import fileinput
import sys


class OutputFilter(object):
    def __init__(self):
        self.buf = ''
        self.queue = collections.deque()

    def read(self):
        lines = []
        while True:
            try:
                line = self.queue.popleft()
                lines.append('#|' + line + '\n')
            except IndexError:
                break
        return ''.join(lines)

    def write(self, output):
        lines = output.splitlines()
        lines[0] = self.buf + lines[0]
        self.buf = ''
        for line in lines[:-1]:
            self.queue.append(line)
        if output.endswith('\n'):
            self.queue.append(lines[-1])
        else:
            self.buf = lines[-1]


def parse_args():
    parser = argparse.ArgumentParser(
        description='Run code in python interactive console')

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-l',
        '--live',
        help='show the code and the output as in a live session',
        action='store_true')

    group.add_argument(
        '-a',
        '--append',
        help='append the output as comments below the code',
        action='store_true')

    parser.add_argument(
        '-o',
        '--output',
        help='output file name (stdout/stderr if not given)')

    parser.add_argument(
        'file',
        nargs='*',
        help="file to be evaluated (stdin if '-' or not given)")

    return parser.parse_args()


def run():
    args = parse_args()

    if args.output:
        output_file = open(args.output, 'w')
        sys.stdout = output_file
        sys.stderr = output_file

    if args.append:
        output = OutputFilter()
        stdout = sys.stdout
        sys.stdout = output
        sys.stderr = output

    console = code.InteractiveConsole()

    more = False
    for line in fileinput.input(files=args.file):
        line = line.rstrip()

        if args.live:
            if more:
                print('...', line)
            else:
                print('>>>', line)

        elif args.append:
            if not line.startswith('#|'):
                stdout.write(line + '\n')

        more = console.push(line)

        if args.append and not more:
            stdout.write(output.read())

if __name__ == "__main__":
    run()
