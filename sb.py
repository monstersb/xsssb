#! /usr/bin/env python

import sys
import time
from xsssb.parser import Parser

def main(argv):
    t = Parser(sys.stdin)
    #return
    #print t.get_first(argv[1])
    t.parse()

if __name__ == '__main__':
    main(sys.argv)

