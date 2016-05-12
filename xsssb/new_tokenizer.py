import re
import pyparsing as pp
import utils

pp.ParserElement.setDefaultWhitespaceChars(" \t\f\v")

def number_parser():
    point = pp.Literal(".")
    e = pp.CaselessLiteral("e")
    plusorminus = pp.Literal("+") ^ pp.Literal("-")
    num = pp.Word(pp.nums)
    dec = pp.Combine(num + pp.Optional(point + pp.Optional(num)) + pp.Optional(e + pp.Optional(plusorminus) + num)) ^\
           pp.Combine(point + pp.Optional(num) + pp.Optional(e + pp.Optional(plusorminus) + num))
    bin = pp.Combine(pp.Literal("0") + pp.CaselessLiteral("b") + pp.Word("01"))
    hex = pp.Combine(pp.Literal("0") + pp.CaselessLiteral("x") + pp.Word(pp.hexnums))
    oct = pp.Combine(pp.Literal("0") + pp.Optional(pp.CaselessLiteral("o")) + pp.Word("01234567"))
    return dec ^ bin ^ hex ^ oct

token_lst = [
    ["endl", pp.Word("\r\n")],
    ["add_ass", pp.Literal("+=")],
    ["inc", pp.Literal("++")],
    ["add", pp.Combine(pp.Literal("+") + pp.NotAny(pp.Regex("\+=")))],
    ["ask", pp.Literal("?")],
    ["se", pp.Literal("===")],
    ["eq", pp.Combine(pp.Literal("==") + pp.NotAny(pp.Regex("=")))],
    ["ass", pp.Combine(pp.Literal("=") + pp.NotAny(pp.Regex("=")))],
    ["colon", pp.Literal(":")],
    ["comma", pp.Literal(",")],
    ["b_and_ass", pp.Literal("&=")],
    ["l_and", pp.Literal("&&")],
    ["b_and", pp.Combine(pp.Literal("&") + pp.NotAny(pp.Regex("&=")))],
    ["b_or_ass", pp.Literal("|=")],
    ["l_or", pp.Literal("||")],
    ["b_or", pp.Combine(pp.Literal("|") + pp.NotAny(pp.Regex("\|=")))],
    ["b_not_ass", pp.Literal("~=")],
    ["b_not", pp.Combine(pp.Literal("~") + pp.NotAny(pp.Regex("=")))],
    ["b_xor_ass", pp.Literal("^=")],
    ["b_xor", pp.Combine(pp.Literal("^") + pp.NotAny(pp.Regex("=")))],
    ["dot", pp.Literal(".")],
    ["exp_ass", pp.Literal("**=")],
    ["exp", pp.Combine(pp.Literal("**") + pp.NotAny(pp.Regex("=")))],
    ["mul_ass", pp.Literal("*=")],
    ["mul", pp.Combine(pp.Literal("*") + pp.NotAny(pp.Regex("=")))],
    ["k_await", pp.Keyword("await")],
    ["k_abstract", pp.Keyword("abstract")],
    ["k_break", pp.Keyword("break")],
    ["k_boolean", pp.Keyword("boolean")],
    ["k_byte", pp.Keyword("byte")],
    ["k_case", pp.Keyword("case")],
    ["k_catch", pp.Keyword("catch")],
    ["k_char", pp.Keyword("char")],
    ["k_class", pp.Keyword("class")],
    ["k_const", pp.Keyword("const")],
    ["k_continue", pp.Keyword("continue")],
    ["k_debugger", pp.Keyword("debugger")],
    ["k_default", pp.Keyword("default")],
    ["k_delete", pp.Keyword("delete")],
    ["k_do", pp.Keyword("do")],
    ["k_double", pp.Keyword("double")],
    ["k_else", pp.Keyword("else")],
    ["k_enum", pp.Keyword("enum")],
    ["k_export", pp.Keyword("export")],
    ["k_extends", pp.Keyword("extends")],
    ["k_final", pp.Keyword("final")],
    ["k_finally", pp.Keyword("finally")],
    ["k_float", pp.Keyword("float")],
    ["k_for", pp.Keyword("for")],
    ["k_function", pp.Keyword("function")],
    ["k_goto", pp.Keyword("goto")],
    ["k_if", pp.Keyword("if")],
    ["k_import", pp.Keyword("import")],
    ["k_implements", pp.Keyword("implements")],
    ["k_in", pp.Keyword("in")],
    ["k_instanceof", pp.Keyword("instanceof")],
    ["k_int", pp.Keyword("int")],
    ["k_interface", pp.Keyword("interface")],
    ["k_let", pp.Keyword("let")],
    ["k_long", pp.Keyword("long")],
    ["k_native", pp.Keyword("native")],
    ["k_new", pp.Keyword("new")],
    ["k_null", pp.Keyword("null")],
    ["k_of", pp.Keyword("of")],
    ["k_package", pp.Keyword("package")],
    ["k_private", pp.Keyword("private")],
    ["k_protected", pp.Keyword("protected")],
    ["k_public", pp.Keyword("public")],
    ["k_return", pp.Keyword("return")],
    ["k_short", pp.Keyword("short")],
    ["k_static", pp.Keyword("static")],
    ["k_super", pp.Keyword("super")],
    ["k_switch", pp.Keyword("switch")],
    ["k_synchronized", pp.Keyword("synchronized")],
    ["k_this", pp.Keyword("this")],
    ["k_throw", pp.Keyword("throw")],
    ["k_throws", pp.Keyword("throws")],
    ["k_transient", pp.Keyword("transient")],
    ["k_try", pp.Keyword("try")],
    ["k_typeof", pp.Keyword("typeof")],
    ["k_var", pp.Keyword("var")],
    ["k_void", pp.Keyword("void")],
    ["k_volatile", pp.Keyword("volatile")],
    ["k_while", pp.Keyword("while")],
    ["k_with", pp.Keyword("with")],
    ["k_yield", pp.Keyword("yield")],
    ["l_brace", pp.Literal("{")],
    ["l_bracket", pp.Literal("[")],
    ["l_par", pp.Literal("(")],
    ["l_sft_ass", pp.Literal("<<=")],
    ["l_sft", pp.Combine(pp.Literal("<<") + pp.NotAny(pp.Regex("=")))],
    ["lte", pp.Literal("<=")],
    ["lte", pp.Combine(pp.Literal("<") + pp.NotAny(pp.Regex("=")))],
    ["sne", pp.Literal("!==")],
    ["ne", pp.Combine(pp.Literal("!=") + pp.NotAny(pp.Regex("=")))],
    ["l_not", pp.Combine(pp.Literal("!") + pp.NotAny(pp.Regex("\!=")))],
    ["number", number_parser()],
    ["rmd_ass", pp.Literal("%=")],
    ["rmd", pp.Combine(pp.Literal("%") + pp.NotAny(pp.Regex("=")))],
    ["r_brace", pp.Literal("}")],
    ["r_brkt", pp.Literal("]")],
    ["r_par", pp.Literal(")")],
    ["semi", pp.Literal(";")],
    ["ml_cmt", pp.cStyleComment],
    ["sl_cmt", pp.dblSlashComment],
    ["div_ass", pp.Literal("/=")],
    ["reg", pp.Combine(pp.QuotedString("/", escChar="\\", unquoteResults=False) + pp.Optional(pp.Regex("[gimy]")))],
    ["div", pp.Combine(pp.Literal("/") + pp.NotAny(pp.Regex("/\*=")))],
    ["string", pp.quotedString],
    ["dec", pp.Literal("--")],
    ["sub_ass", pp.Literal("-=")],
    ["sub", pp.Combine(pp.Literal("-") + pp.NotAny(pp.Regex("-=")))],
    ["ur_sft_ass", pp.Literal(">>>=")],
    ["ur_sft", pp.Combine(pp.Literal(">>>") + pp.NotAny(pp.Regex("=")))],
    ["r_sft", pp.Combine(pp.Literal(">>") + pp.NotAny(pp.Regex(">=")))],
    ["r_sft_ass", pp.Literal(">>=")],
    ["gte", pp.Literal(">=")],
    ["gt", pp.Combine(pp.Literal(">") + pp.NotAny(pp.Regex(">=")))],
    ["id", pp.Regex("[$_a-zA-Z][$_a-zA-Z0-9]*")],
]

for i in token_lst:
    if isinstance(i[1], pp.ParserElement):
        i[1] = i[1].setResultsName(i[0])

class token:
    pass
map(lambda x:setattr(token, x[0], x[1]), token_lst)

token_before_regex = ("endl", "ask", "sem", "colon", "comma", "l_brace", "l_brkt", "l_par", "ass", "add", "add_ass", "l_sft", "l_sft_ass", "r_sft", "r_sft_ass", "ur_sft", "ur_sft_ass", "eq", "ne", "se", "sne", "gt", "gte", "lt", "lte", "inc", "dec", "l_and", "l_or", "l_not", "b_and", "b_and_ass", "b_or", "b_or_ass", "b_not", "b_not_ass", "b_xor", "b_xor_ass", "exp", "exp_ass", "mul", "mul_ass", "div", "div_ass", "rmd", "rmd_ass")


def tokenize_str_one(buf):
    r = reduce(lambda a, b: a ^ b, map(lambda x:x[1], token_lst))
    return r.parseString(buf).asDict().items()[0]

def tokenize_str(buf):
    r = reduce(lambda a, b: a ^ b, map(lambda x:x[1], token_lst))
    i = 0
    last_token = None
    while i < len(buf):
        buf = buf[i:]
        try:
            tbuf = buf.lstrip()
            if len(tbuf) > 2 and tbuf[0] == "/" and tbuf[1] == "/" and tbuf[1] == "*" and last_token in token_before_regex:
                t = token.regex.parseString(buf)
            else:
                t = r.parseString(buf)
            t = t.asDict().items()[0]
            if t[0] not in ("single_line_comment", "multi_line_comment"):
                last_token = t[0]
            yield t
            i = buf.find(t[1]) + len(t[1])
        except pp.ParseException as e:
            print e
            return

def tokenize_file(fname):
    buf = utils.readFile(fname)
    return tokenize_str(buf)

if __name__ == "__main__":
    import sys
    tks = tokenize_file(sys.argv[1])
    for i in tks:
        print "[{0:10s}] => {1}".format(i[0], repr(i[1]))
