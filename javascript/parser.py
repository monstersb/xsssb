import sys
import os
import pprint
import time

from .tokenizer import Tokenizer
from .token import TokenType
from .ast import Ast



class Parser(object):
    def __init__(self, input):
        self.input = input
        self.read_grammar()
        self.first = {}

    def read_grammar(self):
        fname = os.path.join(os.path.dirname(__file__), './javascript.grm')
        self.grammars = {}
        with open(fname, 'r') as f:
            current_nonterminal_symbolic = None
            for line in f:
                line = line.strip()
                if line.endswith(':'):
                    current_nonterminal_symbolic = line[:-1].strip()
                    self.grammars[current_nonterminal_symbolic] = []
                elif len(line) > 0:
                    self.grammars[current_nonterminal_symbolic].append(line.split())
                else:
                    pass
        for s in self.grammars:
            print '{0} => \n\t   {1}\n'.format(s, '\n\t|  '.join([' '.join(i) for i in self.grammars[s]]))

    def tokenize(self):
        print '-' * 50
        t = Tokenizer(self.input)
        self.tokens = list(t.tokenize())

    def get_first(self, x):
        if x in self.first:
            return self.first[x]
        if x.startswith('_') or x == 'Empty':
            first = set([x])
        else:
            first = set()
            for i in self.grammars[x]:
                t = i[0]
                #if t == TokenType.empty:
                #    first.add(t)
                #elif t == x:
                if t == x:
                    pass
                #elif TokenType.is_terminal_symbolic(t):
                #    first.add(t)
                else:
                    for j in i:
                        tf = self.get_first(j)
                        if TokenType.empty not in tf:
                            first = first.union(tf)
                            break
                        tf.remove(TokenType.empty)
                        first = first.union(tf)
                    else:
                        first.add(TokenType.empty)
            self.first[x] = first
        return first.copy()


    def follow(self):
        pass

    def build_table(self):
        self.table = {}
        for n_sym in self.grammars:
            for ca in self.grammars[n_sym]:
                for fst in self.get_first(ca[0]):
                    self.table[(n_sym, fst)] = ca
        print '-' * 50
        pprint.pprint(self.table)



    def parse(self):
        self.tokenize()
        map(self.get_first, iter(self.grammars))
        self.build_table()
        print '-' * 50
        self.stack = ['Program']
        i = 0
        while True:
            print '{1}, {2}  ---------->   {0}'.format(self.stack, self.stack[-1], self.tokens[i].type)
            ti = self.tokens[i]
            si = self.stack.pop()
            if si.startswith('_'):
                if ti.type == si:
                    i += 1
                    continue
                else:
                    raise
            else:
                if TokenType.empty in self.get_first(si) and (si, ti.type) not in self.table:
                    continue
                for x in self.table[(si, ti.type)][::-1]:
                    self.stack.append(x)
            time.sleep(0.2)


def main(argv):
    grammars = read_grammar()
    pprint.pprint(grammars)

if __name__ == '__main__':
    main(sys.argv)

