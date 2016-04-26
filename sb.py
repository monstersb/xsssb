#! /usr/bin/env python

import sys
import time
from javascript.parser import Parser

def main(argv):
    t = Parser(sys.stdin)
    #return
    print t.get_first(argv[1])

if __name__ == '__main__':
    main(sys.argv)

