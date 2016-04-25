import sys
import pprint


def read_file():
    fname = sys.path[0] + '/javascript.grm'
    grammars = {}
    with open(fname, 'r') as f:
        current_nonterminal_symbolic = None
        for line in f:
            line = line.strip()
            if line.endswith(':'):
                current_nonterminal_symbolic = line[:-1].strip()
                grammars[current_nonterminal_symbolic] = []
            elif len(line) > 0:
                grammars[current_nonterminal_symbolic].append(line.split())
            else:
                pass
    return grammars

def main(argv):
    grammars = read_file()
    pprint.pprint(grammars)

if __name__ == '__main__':
    main(sys.argv)

