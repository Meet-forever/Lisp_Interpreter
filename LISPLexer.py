import ply.lex as lex


reserved = {
    'and': 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'if' : 'IF',
    'cdr' : 'CDR',
    'car' : 'CAR',
    'cons' : 'CONS'
}


tokens = [
    'NUMBER',
    'BOOLEAN',
    'LPRN',
    'RPRN',
    'SEMI',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'EQ',
    'NEQ',
    'GTE',
    'LTE',
    'GT',
    'LT',
] + list(reserved.values())


t_LPRN = r'\('
t_RPRN = r'\)'
t_SEMI = r';'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQ = r'='
t_NEQ = r'<>'
t_GTE = r'>='
t_LTE = r'<='
t_GT = r'>'
t_LT = r'<'
t_IF = r'[iI][fF]'
t_AND = r'[aA][nN][dD]'
t_OR = r'[oO][rR]'
t_NOT = r'[nN][oO][tT]'
t_CDR = r'[cC][dD][rR]'
t_CAR = r'[cC][aA][rR]'
t_CONS = r'[cC][oO][nN][sS]'


def t_BOOLEAN(t):
    r'([tT][rR][uU][eE])|([fF][aA][lL][sS][eE])'
    t.value = t.value.capitalize() == 'True'
    t.type = 'BOOLEAN'
    return t


def t_NUMBER(t):
    r'[-]?\d+(\.\d+)?'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t


# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'


def t_error(t):
    raise Exception(f'Lexer Error!\nIllegal character: {t.value[0]}\n')


lexer  = lex.lex()

# lexer.input("1 -1")

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)