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

grammar.emptyStatement = pp.Empty()
grammar.initialiser = token.eq + grammar.assignmentExpression
grammar.variableDeclaration = token.id + pp.Optional(grammar.initialiser)
grammar.variableDeclarationTail = token.comma + grammar.variableDeclaration
grammar.variableDeclarationList = grammar.variableDeclaration + pp.ZeroOrMore(grammar.variableDeclarationTail)
grammar.variableStatement = token.k_var + grammar.variableDeclarationList + token.semi
grammar.block = token.l_brace + grammar.statementList + token.r_brace
grammar.statement = grammar.block ^ grammar.variableStatement ^ grammar.emptyStatement ^ grammar.expressionStatement ^ grammar.ifStatement ^ grammar.iterationStatement ^ grammar.continueStatement ^ grammar.breakStatement ^ grammar.returnStatement ^ grammar.withStatement ^ grammar.labelledStatement ^ grammar.switchStatement ^ grammar.throwStatement ^ grammar.tryStatement
grammar.statementList = pp.OneOrMore(grammar.statement)
grammar.formalParameterListTail = pp.Group(token.comma + token.id)
grammar.formalParameterList = token.id + pp.ZeroOrMore(grammar.formalParameterListTail)
grammar.functionBody = grammar.sourceElements
grammar.functionDeclaration = token.k_function + token.id + token.l_par + pp.Optional(grammar.formalParameterList) + token.r_par + token.l_brace + grammar.functionBody + token.r_brace
grammar.sourceElement = grammar.statement ^ grammar.functionDeclaration
grammar.sourceElements = pp.OneOrMore(grammar.sourceElement)
grammar.program = grammar.sourceElements + pp.StringEnd()


if __name__ == "__main__":
    pass
