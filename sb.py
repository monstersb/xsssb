#! /usr/bin/env python

import sys
import time
from javascript.tokenizer import Tokenizer


def main(argv):
    t = Tokenizer(sys.stdin)
    for i in t.tokenize():
        print i
        #time.sleep(0.1)

if __name__ == '__main__':
    main(sys.argv)

