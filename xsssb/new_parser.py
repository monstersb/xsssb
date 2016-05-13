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

grammar.AllocationExpression = token.k_new + grammar.MemberExpression + pp.ZeroOrMore(grammar.Arguments + pp.ZeroOrMore(grammar.MemberExpressionPart))
grammar.MemberExpressionForIn = (grammar.FunctionExpression ^ grammar.PrimaryExpression) + pp.ZeroOrMore(grammar.MemberExpressionPart)
grammar.MemberExpression = ((grammar.FunctionExpression ^ grammar.PrimaryExpression) + pp.ZeroOrMore(grammar.MemberExpressionPart)) + grammar.AllocationExpression
grammar.PropertyName = token.id ^ token.string ^ token.number
grammar.PropertyNameAndValue = grammar.PropertyName + token.colon + grammar.AssignmentExpression
grammar.PropertyNameAndValueList = grammar.PropertyNameAndValue + pp.ZeroOrMore(token.comma + pp.Optional(grammar.PropertyNameAndValue))
grammar.ObjectLiteral = token.l_brace + pp.Optional(grammar.PropertyNameAndValueList) + token.r_brace
grammar.Elision = pp.OneOrMore(token.comma)
grammar.ElementList = pp.Optional(grammar.Elision) + grammar.AssignmentExpression + pp.ZeroOrMore(grammar.Elision + grammar.AssignmentExpression)
grammar.ArrayLiteral = token.l_brkt + (pp.Optional(grammar.Elision) ^ (grammar.ElementList + grammar.Elision) ^ pp.Optional(grammar.ElementList)) + token.r_brkt
grammar.Literal = token.number ^ token.string ^ token.k_true ^ token.k_false ^ token.k_null ^ token.reg
grammar.PrimaryExpression = token.k_this ^ grammar.ObjectLiteral ^ pp.Group(token.l_par ^ grammar.Expression ^ token.r_par) ^ token.id ^ grammar.ArrayLiteral ^ grammar.Literal


if __name__ == "__main__":
    pass
