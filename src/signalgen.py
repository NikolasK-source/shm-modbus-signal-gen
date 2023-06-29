#!/usr/bin/python3

# MIT License
# 
# Copyright (c) 2023 Nikolas Koesling <nikolas@koesling.info>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__VERSION__ = "1.0.1"

import sys
import math
import time
import signal
import argparse
import os

#
#    function = ^toggle
#       f(x) = offset + scale * function((x + time-offset) * speed)
#    
#    function = toggle
#       f(x) = rect((x + time-offset) * speed)
#
#    x is generated from the current system time
#

def print_function(function:str):
    if function == 'sin':           
        print(' 1|            o  ^  o                                                         o')
        print('  |         o           o                                                   o')
        print('  |       o               o                                               o')
        print('  |     o                   o                                           o')
        print('  |    o                     o                                         o')
        print('  |  o                         o                                     o')
        print('  | o                           o                                   o')
        print('  |o                             o                                 o')
        print('--o-------------------------------o-------------------------------o------------>')
        print(' 0|              π/2             π o             3π/2            o 2π')
        print('  |                                 o                           o')
        print('  |                                  o                         o')
        print('  |                                    o                     o')
        print('  |                                     o                   o')
        print('  |                                       o               o')
        print('  |                                         o           o')
        print('-1|                                            o  _  o')
    elif function == 'cos':
        print('               o 1^  o                                                         o')
        print('            o     |     o                                                   o')
        print('          o       |       o                                               o')
        print('        o         |         o                                           o')
        print('       o          |          o                                         o')
        print('     o            |            o                                     o')
        print('    o             |             o                                   o')
        print('   o              |              o                                 o')
        print('--o---------------|---------------o-------------------------------o------------>')
        print('-π/2             0|            π/2 o              π              o 3π/2       2π')
        print('                  |                 o                           o')
        print('                  |                  o                         o')
        print('                  |                    o                     o')
        print('                  |                     o                   o')
        print('                  |                       o               o')
        print('                  |                         o           o')
        print('                -1|                            o  _  o')
    elif function == 'nsin':
        print(' 1|                                            o  ^  o')
        print('  |                                         o           o')
        print('  |                                       o               o')
        print('  |                                     o                   o')
        print('  |                                    o                     o')
        print('  |                                  o                         o')
        print('  |                                 o                           o')
        print('  |                                o                             o')
        print('--o-------------------------------o-------------------------------o------------>')
        print(' 0|o             π/2             o π            3π/2            2π o')
        print('  | o                           o                                   o')
        print('  |  o                         o                                     o')
        print('  |    o                     o                                         o')
        print('  |     o                   o                                           o')
        print('  |       o               o                                               o')
        print('  |         o           o                                                   o')
        print('-1|            o  _  o                                                         o')
    elif function == 'ncos':
        print('                 1|                            o  ^  o')
        print('                  |                         o           o')
        print('                  |                       o               o')
        print('                  |                     o                   o')
        print('                  |                    o                     o')
        print('                  |                  o                         o')
        print('                  |                 o                           o')
        print('-π/2              |                o                             o')
        print('--o---------------|---------------o-------------------------------o------------>')
        print('   o             0|              o π/2            π           3π/2 o          2π')
        print('    o             |             o                                   o')
        print('     o            |            o                                     o')
        print('       o          |          o                                         o')
        print('        o         |         o                                           o')
        print('          o       |       o                                               o')
        print('            o     |     o                                                   o')
        print('               o-1_  o                                                         o')
    elif function == 'rampdown':
        print('1  o           o           o')
        print('   |  o        :  o        :  o')
        print('   |     o     :     o     :     o')
        print('   |        o  :        o  :')
        print('0 -|-----------o-----------o----->')
        print('   0           1           2')
    elif function == 'rampup':
        print('1  |           o           o')
        print('   |        o  :        o  :')
        print('   |     o     :     o     :     o')
        print('   |  o        :  o        :')
        print('0 -o-----------o-----------o----->')
        print('   0           1           2')
    elif function == 'ramp':
        print('1  |           o')
        print('   |        o     o')
        print('   |     o           o           o')
        print('   |  o                 o     o')
        print('0 -o-----------------------o----->')
        print('   0           1           2')
    elif function == 'toggle':
        print('1  o o o o o o o           o o o o')
        print('   |           :           :')
        print('   |           :           :')
        print('   |           :           :')
        print('0 -|-----------o-o-o-o-o-o-o----->')
        print('   0           1           2')
    else:
        print(f'unknown function \"{function}\"', file=sys.stderr)
        exit(os.EX_USAGE)
# end def


def main():  
#### Argparse
    parser = argparse.ArgumentParser(prog="signal-gen",
                                     description="System time based signal generator for stdin-to-modbus-shm",
                                     epilog='f(x = time.time()) = offset + scale * function((x + time-offset) * speed)')
    
    parser.add_argument('-o', '--offset', type=float, default=0, help="function offset, ignored if function is toggle")
    parser.add_argument('-s', '--scale', type=float, default=1, help="function scale, ignored if function is toggle")
    parser.add_argument('-v', '--speed', type=float, default=1, help="function speed")
    parser.add_argument('-d', '--delay', type=float, help="delay between calculations", default=0.1)
    parser.add_argument('-e', '--endian', type=str, help="data type/endianess string (see stdin-to-modbus-shm)", default='')
    parser.add_argument('-t', '--time_offset', type=float, nargs=1, default=0, help="system time offset in seconds")
    parser.add_argument('-p', '--print', action='store_true', default=False, help="print function and exit")
    parser.add_argument('--version', action='version', version=__VERSION__)

    parser.add_argument('function', type=str, nargs=1, help="function that is calculated", 
                        choices=['sin', 'cos', 'nsin', 'ncos', 'rampup', 'rampdown', 'ramp', 'toggle'])
    parser.add_argument('register_type', type=str, nargs='?', help="register type (see stdin-to-modbus-shm)",
                        choices=['ai', 'ao', 'di', 'do'])
    parser.add_argument('register', type=str, nargs='*', help="modbus register to write value")

    args = parser.parse_args()

#### Setup
    function = f'{args.function[0]}'

    if args.print:
        print_function(function)
        exit(os.EX_OK)

    if args.register_type is None:
        print('no register type provided', file=sys.stderr)
        exit(os.EX_USAGE)

    if args.register is None:
        print('no registers provided', file=sys.stderr)
        exit(os.EX_USAGE)

    regtype = args.register_type
    offset = args.offset
    scale = args.scale
    speed = args.speed
    delay = args.delay
    if args.endian != '':
        endian = f':{args.endian}'
    else:
        endian = ''
    time_offset = args.time_offset
    
    try:
        regs = [int(x, 0) for x in args.register]
    except ValueError as e:
        print(f"failed to parse registers: {e}")
        exit(os.EX_USAGE)

    signal.signal(signal.SIGINT, lambda NUM, _: exit(0))
    signal.signal(signal.SIGTERM, lambda NUM, _: exit(0))

    if function == 'sin':
        fun = math.sin

    elif function == 'cos':
        fun = math.cos

    elif function == 'nsin':
        fun = lambda x: -math.sin(x)

    elif function == 'ncos':
        fun = lambda x: -math.cos(x)

    elif function == 'rampdown':
        fun = lambda x: 1.0 - (x - int(x))

    elif function == 'rampup':
        fun = lambda x: x - int(x)

    elif function == 'ramp':
        def ramp(x):
            if int(x) % 2 == 0:
                return x - int(x)
            else:
                return 1.0 - (x - int(x))
        fun = ramp

    elif function == 'toggle':
        fun = lambda x: int(x) % 2
        
    else:
        print(f'unknown function \"{function}\"', file=sys.stderr)
        exit(os.EX_USAGE)
    
#### main loop
    f_old = None
    while True:
        x = time.time() + time_offset
        f = offset + scale * fun(x * speed)

        # print value only if it differs
        if f != f_old:
            f_old = f
            for reg in regs:
                print(f'{regtype}:0x{reg:x}:{f}{endian}')

        time.sleep(delay)
    # end while
# end def

if __name__ == '__main__':
    main()
# end if
