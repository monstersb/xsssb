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

token = {
    "addition" : pp.Literal("+"),
    "addition_assignment" : pp.Literal("+="),
    "ask" : pp.Literal("?"),
    "assignment" : pp.Literal("="),
    "colon" : pp.Literal(":"),
    "comma" : pp.Literal(","),
    "bitwise_and" : pp.Literal("&"),
    "bitwise_and_assignment" : pp.Literal("&="),
    "bitwise_or" : pp.Literal("|"),
    "bitwise_or_assignment" : pp.Literal("|="),
    "bitwise_not" : pp.Literal("~"),
    "bitwise_not_assignment" : pp.Literal("~="),
    "bitwise_xor" : pp.Literal("^"),
    "bitwise_xor_assignment" : pp.Literal("^="),
    "decrement" : pp.Literal("--"),
    "division" : pp.Literal("/"),
    "division_assignment" : pp.Literal("/="),
    "dot" : pp.Literal("."),
    "equal" : pp.Literal("=="),
    "exp" : pp.Literal("**"),
    "exp_assignment" : pp.Literal("**="),
    "greater_than" : pp.Literal(">"),
    "greater_than_or_equal" : pp.Literal(">="),
    "increment" : pp.Literal("++"),
    "identifier" : pp.Regex("[$_a-zA-Z][$_a-zA-Z0-9]*"),
    "keyword_await" : pp.Keyword("await"),
    "keyword_abstract" : pp.Keyword("abstract"),
    "keyword_break" : pp.Keyword("break"),
    "keyword_boolean" : pp.Keyword("boolean"),
    "keyword_byte" : pp.Keyword("byte"),
    "keyword_case" : pp.Keyword("case"),
    "keyword_catch" : pp.Keyword("catch"),
    "keyword_char" : pp.Keyword("char"),
    "keyword_class" : pp.Keyword("class"),
    "keyword_const" : pp.Keyword("const"),
    "keyword_continue" : pp.Keyword("continue"),
    "keyword_debugger" : pp.Keyword("debugger"),
    "keyword_default" : pp.Keyword("default"),
    "keyword_delete" : pp.Keyword("delete"),
    "keyword_do" : pp.Keyword("do"),
    "keyword_double" : pp.Keyword("double"),
    "keyword_else" : pp.Keyword("else"),
    "keyword_enum" : pp.Keyword("enum"),
    "keyword_export" : pp.Keyword("export"),
    "keyword_extends" : pp.Keyword("extends"),
    "keyword_final" : pp.Keyword("final"),
    "keyword_finally" : pp.Keyword("finally"),
    "keyword_float" : pp.Keyword("float"),
    "keyword_for" : pp.Keyword("for"),
    "keyword_function" : pp.Keyword("function"),
    "keyword_goto" : pp.Keyword("goto"),
    "keyword_if" : pp.Keyword("if"),
    "keyword_import" : pp.Keyword("import"),
    "keyword_implements" : pp.Keyword("implements"),
    "keyword_in" : pp.Keyword("in"),
    "keyword_instanceof" : pp.Keyword("instanceof"),
    "keyword_int" : pp.Keyword("int"),
    "keyword_interface" : pp.Keyword("interface"),
    "keyword_let" : pp.Keyword("let"),
    "keyword_long" : pp.Keyword("long"),
    "keyword_native" : pp.Keyword("native"),
    "keyword_new" : pp.Keyword("new"),
    "keyword_null" : pp.Keyword("null"),
    "keyword_of" : pp.Keyword("of"),
    "keyword_package" : pp.Keyword("package"),
    "keyword_private" : pp.Keyword("private"),
    "keyword_protected" : pp.Keyword("protected"),
    "keyword_public" : pp.Keyword("public"),
    "keyword_return" : pp.Keyword("return"),
    "keyword_short" : pp.Keyword("short"),
    "keyword_static" : pp.Keyword("static"),
    "keyword_super" : pp.Keyword("super"),
    "keyword_switch" : pp.Keyword("switch"),
    "keyword_synchronized" : pp.Keyword("synchronized"),
    "keyword_this" : pp.Keyword("this"),
    "keyword_throw" : pp.Keyword("throw"),
    "keyword_throws" : pp.Keyword("throws"),
    "keyword_transient" : pp.Keyword("transient"),
    "keyword_try" : pp.Keyword("try"),
    "keyword_typeof" : pp.Keyword("typeof"),
    "keyword_var" : pp.Keyword("var"),
    "keyword_void" : pp.Keyword("void"),
    "keyword_volatile" : pp.Keyword("volatile"),
    "keyword_while" : pp.Keyword("while"),
    "keyword_with" : pp.Keyword("with"),
    "keyword_yield" : pp.Keyword("yield"),
    "left_brace" : pp.Literal("{"),
    "left_bracket" : pp.Literal("["),
    "left_par" : pp.Literal("("),
    "left_shift" : pp.Literal("<<"),
    "left_shift_assignment" : pp.Literal("<<="),
    "less_than" : pp.Literal("<"),
    "less_than_or_equal" : pp.Literal("<="),
    "endl" : pp.Literal("\n"),
    "logical_and" : pp.Literal("&&"),
    "logical_or" : pp.Literal("||"),
    "logical_not" : pp.Literal("!"),
    "multi_line_comment" : pp.cppStyleComment,
    "multiplication" : pp.Literal("*"),
    "multiplication_assignment" : pp.Literal("*="),
    "not_equal" : pp.Literal("!="),
    "number" : number_parser(),
    "remainder" : pp.Literal("%"),
    "remainder_assignment" : pp.Literal("%="),
    "regex" : pp.Combine(pp.QuotedString("/", escChar="\\", unquoteResults=False) + pp.Optional(pp.Regex("[gimy]"))),
    "right_shift" : pp.Literal(">>"),
    "right_shift_assignment" : pp.Literal(">>="),
    "right_brace" : pp.Literal("}"),
    "right_bracket" : pp.Literal("]"),
    "right_par" : pp.Literal(")"),
    "semicolon" : pp.Literal(";"),
    "single_line_comment" : pp.dblSlashComment,
    "strict_equal" : pp.Literal("==="),
    "strict_not_equal" : pp.Literal("!=="),
    "string" : pp.quotedString,
    "subtraction" : pp.Literal("-"),
    "subtraction_assignment" : pp.Literal("-="),
    "unsigned_right_shift" : pp.Literal(">>>"),
    "unsigned_right_shift_assignment" : pp.Literal(">>>="),
}


def tokenize(inputStream):
    r = token["addition"] |\
        token["addition_assignment"] |\
        token["ask"] |\
        token["assignment"] |\
        token["bitwise_and"] |\
        token["bitwise_and_assignment"] |\
        token["bitwise_not"] |\
        token["bitwise_not_assignment"] |\
        token["bitwise_or"] |\
        token["bitwise_or_assignment"] |\
        token["bitwise_xor"] |\
        token["bitwise_xor_assignment"] |\
        token["colon"] |\
        token["comma"] |\
        token["decrement"] |\
        token["endl"] |\
        token["equal"] |\
        token["exp"] |\
        token["exp_assignment"] |\
        token["greater_than"] |\
        token["greater_than_or_equal"] |\
        token["identifier"] |\
        token["increment"] |\
        token["keyword_abstract"] |\
        token["keyword_await"] |\
        token["keyword_boolean"] |\
        token["keyword_break"] |\
        token["keyword_byte"] |\
        token["keyword_case"] |\
        token["keyword_catch"] |\
        token["keyword_char"] |\
        token["keyword_class"] |\
        token["keyword_const"] |\
        token["keyword_continue"] |\
        token["keyword_debugger"] |\
        token["keyword_default"] |\
        token["keyword_delete"] |\
        token["keyword_do"] |\
        token["keyword_double"] |\
        token["keyword_else"] |\
        token["keyword_enum"] |\
        token["keyword_export"] |\
        token["keyword_extends"] |\
        token["keyword_final"] |\
        token["keyword_finally"] |\
        token["keyword_float"] |\
        token["keyword_for"] |\
        token["keyword_function"] |\
        token["keyword_goto"] |\
        token["keyword_if"] |\
        token["keyword_implements"] |\
        token["keyword_import"] |\
        token["keyword_in"] |\
        token["keyword_instanceof"] |\
        token["keyword_int"] |\
        token["keyword_interface"] |\
        token["keyword_let"] |\
        token["keyword_long"] |\
        token["keyword_native"] |\
        token["keyword_new"] |\
        token["keyword_null"] |\
        token["keyword_of"] |\
        token["keyword_package"] |\
        token["keyword_private"] |\
        token["keyword_protected"] |\
        token["keyword_public"] |\
        token["keyword_return"] |\
        token["keyword_short"] |\
        token["keyword_static"] |\
        token["keyword_super"] |\
        token["keyword_switch"] |\
        token["keyword_synchronized"] |\
        token["keyword_this"] |\
        token["keyword_throw"] |\
        token["keyword_throws"] |\
        token["keyword_transient"] |\
        token["keyword_try"] |\
        token["keyword_typeof"] |\
        token["keyword_var"] |\
        token["keyword_void"] |\
        token["keyword_volatile"] |\
        token["keyword_while"] |\
        token["keyword_with"] |\
        token["keyword_yield"] |\
        token["left_brace"] |\
        token["left_bracket"] |\
        token["left_par"] |\
        token["left_shift"] |\
        token["left_shift_assignment"] |\
        token["less_than"] |\
        token["less_than_or_equal"] |\
        token["logical_and"] |\
        token["logical_not"] |\
        token["logical_or"] |\
        token["multiplication"] |\
        token["multiplication_assignment"] |\
        token["regex"] |\
        token["single_line_comment"] |\
        token["multi_line_comment"] |\
        token["division"] |\
        token["division_assignment"] |\
        token["not_equal"] |\
        token["number"] |\
        token["dot"] |\
        token["remainder"] |\
        token["remainder_assignment"] |\
        token["right_brace"] |\
        token["right_bracket"] |\
        token["right_par"] |\
        token["right_shift"] |\
        token["right_shift_assignment"] |\
        token["semicolon"] |\
        token["strict_equal"] |\
        token["strict_not_equal"] |\
        token["string"] |\
        token["subtraction"] |\
        token["subtraction_assignment"] |\
        token["unsigned_right_shift"] |\
        token["unsigned_right_shift_assignment"]
    #r = reduce(lambda a, b: a | b, Parser.token.values())
    #a = Parser.token.keys()
    #a.sort()
    #print ' | \n'.join(['Parser.token["{0}"]'.format(i) for i in a])
    return pp.OneOrMore(r).parseFile(inputStream)


if __name__ == "__main__":
    import sys
    print tokenize(sys.argv[1])
