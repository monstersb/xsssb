import sys
import os
import pprint

from .tokenizer import Tokenizer


def read_grammar():
    fname = os.path.join(os.path.dirname(__file__), './javascript.grm')
    grammars = {}
    with open(fname, 'r') as f:
        current_nonterminal_symbolic = None
        for line in f:
            line = line.strip()
            if line.endswith(':'):
                if current_nonterminal_symbolic:
                    print '{0} => \n\t   {1}\n'.format(current_nonterminal_symbolic, '\n\t|  '.join([' '.join(i) for i in grammars[current_nonterminal_symbolic]]))
                current_nonterminal_symbolic = line[:-1].strip()
                grammars[current_nonterminal_symbolic] = []
            elif len(line) > 0:
                grammars[current_nonterminal_symbolic].append(line.split())
            else:
                pass
    return grammars

class Parser(object):
    def __init__(self, input):
        self.input = input
        self.grammars = read_grammar()
        self.tokenize()

    def tokenize(self):
        t = Tokenizer(self.input)
        self.tokens = list(t.tokenize())


def main(argv):
    grammars = read_grammar()
    pprint.pprint(grammars)

if __name__ == '__main__':
    main(sys.argv)

