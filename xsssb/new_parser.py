import pyparsing as pp
from new_tokenizer import token

# https://tomcopeland.blogs.com/EcmaScript.html#prod62
class Grammar(dict):
    grm = {}

    def __getattr__(self, k):
        if k in Grammar.grm:
            return Grammar.grm[k]
        else:
            print k
            return pp.NoMatch()

    def __setattr__(self, k, v):
        if isinstance(v, pp.ParserElement):
            Grammar.grm[k] = pp.Group(v).setResultsName(k)

    __getitem__ = __getattr__
    __setitem__ = __setattr__


grammar = Grammar()

grammar.PrimaryExpression = token.k_this ^ grammar.ObjectLiteral ^ pp.Group(token.l_par ^ grammar.Expression ^ token.r_par) ^ token.id ^ grammar.ArrayLiteral ^ token.Literal


if __name__ == "__main__":
    pass
