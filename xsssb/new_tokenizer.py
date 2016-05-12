import pyparsing as pp
import re

def number_parser():
    point = pp.Literal(".")
    e = pp.CaselessLiteral("E")
    plusorminus = pp.Literal("+") | pp.Literal("-")
    num = pp.Word(pp.nums)
    dec = pp.Combine(num + pp.Optional(point + pp.Optional(num)) + pp.Optional(e + pp.Optional(plusorminus) + num)) |\
           pp.Combine(point + pp.Optional(num) + pp.Optional(e + pp.Optional(plusorminus) + num))
    bin = pp.Regex("0[bB][01]+")
    hex = pp.Regex("0[xX][0-0a-fA-F]+")
    oct = pp.Regex("0[oO]?[0-7]+")
    return dec | bin | hex | oct

token_lst = [
    ("addition_assignment", pp.Literal("+=")),
    ("increment", pp.Literal("++")),
    ("addition", pp.Literal("+") + pp.NotAny(pp.Regex('\+='))),
    ("ask", pp.Literal("?")),
    ("strict_equal", pp.Literal("===")),
    ("equal", pp.Literal("==") + pp.NotAny(pp.Regex('='))),
    ("assignment", pp.Literal("=") + pp.NotAny(pp.Regex('='))),
    ("colon", pp.Literal(":")),
    ("comma", pp.Literal(",")),
    ("bitwise_and_assignment", pp.Literal("&=")),
    ("logical_and", pp.Literal("&&")),
    ("bitwise_and", pp.Literal("&") + pp.NotAny(pp.Regex('&='))),
    ("bitwise_or_assignment", pp.Literal("|=")),
    ("logical_or", pp.Literal("||")),
    ("bitwise_or", pp.Literal("|") + pp.NotAny(pp.Regex('\|='))),
    ("bitwise_not_assignment", pp.Literal("~=")),
    ("bitwise_not", pp.Literal("~") + pp.NotAny(pp.Regex('='))),
    ("bitwise_xor_assignment", pp.Literal("^=")),
    ("bitwise_xor", pp.Literal("^") + pp.NotAny(pp.Regex('='))),
    ("dot", pp.Literal(".")),
    ("exp_assignment", pp.Literal("**=")),
    ("exp", pp.Literal("**") + pp.NotAny(pp.Regex('='))),
    ("multiplication_assignment", pp.Literal("*=")),
    ("multiplication", pp.Literal("*") + pp.NotAny(pp.Regex('='))),
    ("keyword_await", pp.Keyword("await")),
    ("keyword_abstract", pp.Keyword("abstract")),
    ("keyword_break", pp.Keyword("break")),
    ("keyword_boolean", pp.Keyword("boolean")),
    ("keyword_byte", pp.Keyword("byte")),
    ("keyword_case", pp.Keyword("case")),
    ("keyword_catch", pp.Keyword("catch")),
    ("keyword_char", pp.Keyword("char")),
    ("keyword_class", pp.Keyword("class")),
    ("keyword_const", pp.Keyword("const")),
    ("keyword_continue", pp.Keyword("continue")),
    ("keyword_debugger", pp.Keyword("debugger")),
    ("keyword_default", pp.Keyword("default")),
    ("keyword_delete", pp.Keyword("delete")),
    ("keyword_do", pp.Keyword("do")),
    ("keyword_double", pp.Keyword("double")),
    ("keyword_else", pp.Keyword("else")),
    ("keyword_enum", pp.Keyword("enum")),
    ("keyword_export", pp.Keyword("export")),
    ("keyword_extends", pp.Keyword("extends")),
    ("keyword_final", pp.Keyword("final")),
    ("keyword_finally", pp.Keyword("finally")),
    ("keyword_float", pp.Keyword("float")),
    ("keyword_for", pp.Keyword("for")),
    ("keyword_function", pp.Keyword("function").setResultsName('function')),
    ("keyword_goto", pp.Keyword("goto")),
    ("keyword_if", pp.Keyword("if")),
    ("keyword_import", pp.Keyword("import")),
    ("keyword_implements", pp.Keyword("implements")),
    ("keyword_in", pp.Keyword("in")),
    ("keyword_instanceof", pp.Keyword("instanceof")),
    ("keyword_int", pp.Keyword("int")),
    ("keyword_interface", pp.Keyword("interface")),
    ("keyword_let", pp.Keyword("let")),
    ("keyword_long", pp.Keyword("long")),
    ("keyword_native", pp.Keyword("native")),
    ("keyword_new", pp.Keyword("new")),
    ("keyword_null", pp.Keyword("null")),
    ("keyword_of", pp.Keyword("of")),
    ("keyword_package", pp.Keyword("package")),
    ("keyword_private", pp.Keyword("private")),
    ("keyword_protected", pp.Keyword("protected")),
    ("keyword_public", pp.Keyword("public")),
    ("keyword_return", pp.Keyword("return")),
    ("keyword_short", pp.Keyword("short")),
    ("keyword_static", pp.Keyword("static")),
    ("keyword_super", pp.Keyword("super")),
    ("keyword_switch", pp.Keyword("switch")),
    ("keyword_synchronized", pp.Keyword("synchronized")),
    ("keyword_this", pp.Keyword("this")),
    ("keyword_throw", pp.Keyword("throw")),
    ("keyword_throws", pp.Keyword("throws")),
    ("keyword_transient", pp.Keyword("transient")),
    ("keyword_try", pp.Keyword("try")),
    ("keyword_typeof", pp.Keyword("typeof")),
    ("keyword_var", pp.Keyword("var")),
    ("keyword_void", pp.Keyword("void")),
    ("keyword_volatile", pp.Keyword("volatile")),
    ("keyword_while", pp.Keyword("while")),
    ("keyword_with", pp.Keyword("with")),
    ("keyword_yield", pp.Keyword("yield")),
    ("left_brace", pp.Literal("{")),
    ("left_bracket", pp.Literal("[")),
    ("left_par", pp.Literal("(")),
    ("left_shift_assignment", pp.Literal("<<=")),
    ("left_shift", pp.Literal("<<") + pp.NotAny(pp.Regex('='))),
    ("less_than_or_equal", pp.Literal("<=")),
    ("less_than", pp.Literal("<") + pp.NotAny(pp.Regex('='))),
    ("strict_not_equal", pp.Literal("!==")),
    ("not_equal", pp.Literal("!=") + pp.NotAny(pp.Regex('='))),
    ("logical_not", pp.Literal("!") + pp.NotAny(pp.Regex('\!='))),
    ("number", number_parser()),
    ("remainder_assignment", pp.Literal("%=")),
    ("remainder", pp.Literal("%") + pp.NotAny(pp.Regex('='))),
    ("right_brace", pp.Literal("}")),
    ("right_bracket", pp.Literal("]")),
    ("right_par", pp.Literal(")")),
    ("semicolon", pp.Literal(";")),
    ("multi_line_comment", pp.cppStyleComment),
    ("single_line_comment", pp.dblSlashComment),
    ("division_assignment", pp.Literal("/=")),
    ("regex", pp.Combine(pp.QuotedString("/", escChar="\\", unquoteResults=False) + pp.Optional(pp.Regex("[gimy]")))),
    ("division", pp.Literal("/") + pp.NotAny(pp.Regex('/\*='))),
    ("string", pp.quotedString),
    ("decrement", pp.Literal("--")),
    ("subtraction_assignment", pp.Literal("-=")),
    ("subtraction", pp.Literal("-") + pp.NotAny(pp.Regex('-='))),
    ("unsigned_right_shift_assignment", pp.Literal(">>>=")),
    ("unsigned_right_shift", pp.Literal(">>>") + pp.NotAny(pp.Regex('='))),
    ("right_shift", pp.Literal(">>") + pp.NotAny(pp.Regex('>='))),
    ("right_shift_assignment", pp.Literal(">>=")),
    ("greater_than_or_equal", pp.Literal(">=")),
    ("greater_than", pp.Literal(">") + pp.NotAny(pp.Regex('>='))),
    ("identifier", pp.Regex("[$_a-zA-Z][$_a-zA-Z0-9]*")),
]

token_dic = {i[0]:i[1] for i in token_lst}


def tokenize(inputStream):
    r = reduce(lambda a, b: a | b, map(lambda x:x[1], token_lst))
    t = pp.ZeroOrMore(r).parseFile(inputStream)
    return t


if __name__ == "__main__":
    import sys
    pp.ParserElement.setDefaultWhitespaceChars(' \t')
    print tokenize(sys.argv[1])
