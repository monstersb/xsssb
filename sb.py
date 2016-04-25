#! /usr/bin/env python

import sys
import time
from javascript.parser import Parser

def main(argv):
    t = Parser(sys.stdin)
    print t.first('Program')

if __name__ == '__main__':
    main(sys.argv)

