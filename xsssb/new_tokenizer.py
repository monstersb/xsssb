import re
import pyparsing as pp
import utils

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
    ("addition_assignment", pp.Literal("+=").setResultsName("addition_assignment")),
    ("increment", pp.Literal("++").setResultsName("increment")),
    ("addition", (pp.Literal("+") + pp.NotAny(pp.Regex('\+='))).setResultsName("addition")),
    ("ask", pp.Literal("?").setResultsName("ask")),
    ("strict_equal", pp.Literal("===").setResultsName("strict_equal")),
    ("equal", (pp.Literal("==") + pp.NotAny(pp.Regex('='))).setResultsName("equal")),
    ("assignment", (pp.Literal("=") + pp.NotAny(pp.Regex('='))).setResultsName("assignment")),
    ("colon", pp.Literal(":").setResultsName("colon")),
    ("comma", pp.Literal(",").setResultsName("comma")),
    ("bitwise_and_assignment", pp.Literal("&=").setResultsName("bitwise_and_assignment")),
    ("logical_and", pp.Literal("&&").setResultsName("logical_and")),
    ("bitwise_and", (pp.Literal("&") + pp.NotAny(pp.Regex('&='))).setResultsName("bitwise_and")),
    ("bitwise_or_assignment", pp.Literal("|=").setResultsName("bitwise_or_assignment")),
    ("logical_or", pp.Literal("||").setResultsName("logical_or")),
    ("bitwise_or", (pp.Literal("|") + pp.NotAny(pp.Regex('\|='))).setResultsName("bitwise_or")),
    ("bitwise_not_assignment", pp.Literal("~=").setResultsName("bitwise_not_assignment")),
    ("bitwise_not", (pp.Literal("~") + pp.NotAny(pp.Regex("="))).setResultsName("bitwise_not")),
    ("bitwise_xor_assignment", pp.Literal("^=").setResultsName("bitwise_xor_assignment")),
    ("bitwise_xor", (pp.Literal("^") + pp.NotAny(pp.Regex("="))).setResultsName("bitwise_xor")),
    ("dot", pp.Literal(".").setResultsName("dot")),
    ("exp_assignment", pp.Literal("**=").setResultsName("exp_assignment")),
    ("exp", (pp.Literal("**") + pp.NotAny(pp.Regex('='))).setResultsName("exp")),
    ("multiplication_assignment", pp.Literal("*=").setResultsName("multiplication_assignment")),
    ("multiplication", (pp.Literal("*") + pp.NotAny(pp.Regex('='))).setResultsName("multiplication")),
    ("keyword_await", pp.Keyword("await").setResultsName("await")),
    ("keyword_abstract", pp.Keyword("abstract").setResultsName("abstract")),
    ("keyword_break", pp.Keyword("break").setResultsName("break")),
    ("keyword_boolean", pp.Keyword("boolean").setResultsName("boolean")),
    ("keyword_byte", pp.Keyword("byte").setResultsName("byte")),
    ("keyword_case", pp.Keyword("case").setResultsName("case")),
    ("keyword_catch", pp.Keyword("catch").setResultsName("catch")),
    ("keyword_char", pp.Keyword("char").setResultsName("char")),
    ("keyword_class", pp.Keyword("class").setResultsName("class")),
    ("keyword_const", pp.Keyword("const").setResultsName("const")),
    ("keyword_continue", pp.Keyword("continue").setResultsName("continue")),
    ("keyword_debugger", pp.Keyword("debugger").setResultsName("debugger")),
    ("keyword_default", pp.Keyword("default").setResultsName("default")),
    ("keyword_delete", pp.Keyword("delete").setResultsName("delete")),
    ("keyword_do", pp.Keyword("do").setResultsName("do")),
    ("keyword_double", pp.Keyword("double").setResultsName("double")),
    ("keyword_else", pp.Keyword("else").setResultsName("else")),
    ("keyword_enum", pp.Keyword("enum").setResultsName("enum")),
    ("keyword_export", pp.Keyword("export").setResultsName("export")),
    ("keyword_extends", pp.Keyword("extends").setResultsName("extends")),
    ("keyword_final", pp.Keyword("final").setResultsName("final")),
    ("keyword_finally", pp.Keyword("finally").setResultsName("finally")),
    ("keyword_float", pp.Keyword("float").setResultsName("float")),
    ("keyword_for", pp.Keyword("for").setResultsName("for")),
    ("keyword_function", pp.Keyword("function").setResultsName('function')),
    ("keyword_goto", pp.Keyword("goto").setResultsName("goto")),
    ("keyword_if", pp.Keyword("if").setResultsName("if")),
    ("keyword_import", pp.Keyword("import").setResultsName("import")),
    ("keyword_implements", pp.Keyword("implements").setResultsName("implements")),
    ("keyword_in", pp.Keyword("in").setResultsName("in")),
    ("keyword_instanceof", pp.Keyword("instanceof").setResultsName("instanceof")),
    ("keyword_int", pp.Keyword("int").setResultsName("int")),
    ("keyword_interface", pp.Keyword("interface").setResultsName("interface")),
    ("keyword_let", pp.Keyword("let").setResultsName("let")),
    ("keyword_long", pp.Keyword("long").setResultsName("long")),
    ("keyword_native", pp.Keyword("native").setResultsName("native")),
    ("keyword_new", pp.Keyword("new").setResultsName("new")),
    ("keyword_null", pp.Keyword("null").setResultsName("null")),
    ("keyword_of", pp.Keyword("of").setResultsName("of")),
    ("keyword_package", pp.Keyword("package").setResultsName("package")),
    ("keyword_private", pp.Keyword("private").setResultsName("private")),
    ("keyword_protected", pp.Keyword("protected").setResultsName("protected")),
    ("keyword_public", pp.Keyword("public").setResultsName("public")),
    ("keyword_return", pp.Keyword("return").setResultsName("return")),
    ("keyword_short", pp.Keyword("short").setResultsName("short")),
    ("keyword_static", pp.Keyword("static").setResultsName("static")),
    ("keyword_super", pp.Keyword("super").setResultsName("super")),
    ("keyword_switch", pp.Keyword("switch").setResultsName("switch")),
    ("keyword_synchronized", pp.Keyword("synchronized").setResultsName("synchronized")),
    ("keyword_this", pp.Keyword("this").setResultsName("this")),
    ("keyword_throw", pp.Keyword("throw").setResultsName("throw")),
    ("keyword_throws", pp.Keyword("throws").setResultsName("throws")),
    ("keyword_transient", pp.Keyword("transient").setResultsName("transient")),
    ("keyword_try", pp.Keyword("try").setResultsName("try")),
    ("keyword_typeof", pp.Keyword("typeof").setResultsName("typeof")),
    ("keyword_var", pp.Keyword("var").setResultsName("var")),
    ("keyword_void", pp.Keyword("void").setResultsName("void")),
    ("keyword_volatile", pp.Keyword("volatile").setResultsName("volatile")),
    ("keyword_while", pp.Keyword("while").setResultsName("while")),
    ("keyword_with", pp.Keyword("with").setResultsName("with")),
    ("keyword_yield", pp.Keyword("yield").setResultsName("yield")),
    ("left_brace", pp.Literal("{").setResultsName("left_brace")),
    ("left_bracket", pp.Literal("[").setResultsName("left_bracket")),
    ("left_par", pp.Literal("(").setResultsName("left_par")),
    ("left_shift_assignment", pp.Literal("<<=").setResultsName("left_shift_assignment")),
    ("left_shift", (pp.Literal("<<") + pp.NotAny(pp.Regex('='))).setResultsName("left_shift")),
    ("less_than_or_equal", pp.Literal("<=").setResultsName("less_than_or_equal")),
    ("less_than", (pp.Literal("<") + pp.NotAny(pp.Regex('='))).setResultsName("less_than")),
    ("strict_not_equal", pp.Literal("!==").setResultsName("strict_not_equal")),
    ("not_equal", (pp.Literal("!=") + pp.NotAny(pp.Regex('='))).setResultsName("not_equal")),
    ("logical_not", (pp.Literal("!") + pp.NotAny(pp.Regex('\!='))).setResultsName("logical_not")),
    ("number", number_parser().setResultsName("number")),
    ("remainder_assignment", pp.Literal("%=").setResultsName("remainder_assignment")),
    ("remainder", (pp.Literal("%") + pp.NotAny(pp.Regex('='))).setResultsName("remainder")),
    ("right_brace", pp.Literal("}").setResultsName("right_brace")),
    ("right_bracket", pp.Literal("]").setResultsName("right_bracket")),
    ("right_par", pp.Literal(")").setResultsName("right_par")),
    ("semicolon", pp.Literal(";").setResultsName("semicolon")),
    ("multi_line_comment", pp.cppStyleComment.setResultsName("multi_line_comment")),
    ("single_line_comment", pp.dblSlashComment.setResultsName("single_line_comment")),
    ("division_assignment", pp.Literal("/=").setResultsName("division_assignment")),
    ("regex", pp.Combine(pp.QuotedString("/", escChar="\\", unquoteResults=False) + pp.Optional(pp.Regex("[gimy]"))).setResultsName("regex")),
    ("division", (pp.Literal("/") + pp.NotAny(pp.Regex('/\*='))).setResultsName("division")),
    ("string", pp.quotedString.setResultsName("string")),
    ("decrement", pp.Literal("--").setResultsName("decrement")),
    ("subtraction_assignment", pp.Literal("-=").setResultsName("subtraction_assignment")),
    ("subtraction", (pp.Literal("-") + pp.NotAny(pp.Regex('-='))).setResultsName("subtraction")),
    ("unsigned_right_shift_assignment", pp.Literal(">>>=").setResultsName("unsigned_right_shift_assignment")),
    ("unsigned_right_shift", (pp.Literal(">>>") + pp.NotAny(pp.Regex('='))).setResultsName("unsigned_right_shift")),
    ("right_shift", (pp.Literal(">>") + pp.NotAny(pp.Regex('>='))).setResultsName("right_shift")),
    ("right_shift_assignment", pp.Literal(">>=").setResultsName("right_shift_assignment")),
    ("greater_than_or_equal", pp.Literal(">=").setResultsName("greater_than_or_equal")),
    ("greater_than", (pp.Literal(">") + pp.NotAny(pp.Regex('>='))).setResultsName("greater_than")),
    ("identifier", pp.Regex("[$_a-zA-Z][$_a-zA-Z0-9]*").setResultsName('identifier')),
]

token_dic = {i[0]:i[1] for i in token_lst}


def tokenize(fname):
    buf = utils.readFile(fname)
    r = reduce(lambda a, b: a ^ b, map(lambda x:x[1], token_lst))
    i = 0
    while i < len(buf):
        buf = buf[i:]
        try:
            t = r.parseString(buf)
            yield t
            i = buf.find(t[0]) + len(t[0])
        except pp.ParseException:
            return


if __name__ == "__main__":
    import sys
    pp.ParserElement.setDefaultWhitespaceChars(' \t')
    for i in tokenize(sys.argv[1]):
        print '[{0:20s}] => {1}'.format(i.keys()[0], repr(i[0]))
