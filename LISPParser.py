from LISPLexer import tokens
from ply import yacc 


def p_start(p):
    '''start : lisp SEMI 
    '''
    p[0] = p[1]


def p_types(p):
    '''lisp : expression
            | bool
            | list
    '''
    p[0] = p[1]


def p_numbers(p):
    '''expression : NUMBER
    '''
    p[0] = ['number', p[1]]


def p_expression_aop(p):
    '''expression : LPRN PLUS expression expression RPRN
                | LPRN MINUS expression expression RPRN
                | LPRN MULTIPLY expression expression RPRN
                | LPRN DIVIDE expression expression RPRN
    '''
    p[0] = ['aop', p[2].lower(), p[3], p[4]]


def p_expression(p):
    '''expression : LPRN IF bool expression expression RPRN
    '''
    p[0] = ['if', p[3], p[4], p[5]]


def p_expression_car(p):
    '''expression : LPRN CAR list RPRN
    '''
    p[0] = ['car', p[3]]


def p_boolean(p):
    '''bool : BOOLEAN
    '''
    p[0] = ['boolean', p[1]]


def p_boolean_logic_and_or(p):
    '''bool : LPRN AND bool bool RPRN
            | LPRN OR bool bool RPRN
    '''
    p[0] = [p[2].lower(), p[3], p[4]]


def p_boolean_logic_not(p):
    '''bool : LPRN NOT bool RPRN
    '''
    p[0] = [p[2].lower(), p[3]] 


def p_boolean_comp_op(p):
    '''bool : LPRN GTE expression expression RPRN
            | LPRN LTE expression expression RPRN
            | LPRN GT expression expression RPRN
            | LPRN LT expression expression RPRN
            | LPRN EQ expression expression RPRN
            | LPRN NEQ expression expression RPRN
    '''
    p[0] = ['comparison', p[2], p[3], p[4]]


def p_list(p):
    '''list : LPRN array RPRN 
    '''
    p[0] = ['list', p[2]]


def p_list_empty_array(p):
    '''array : 
    '''
    p[0] = []


def p_list_array(p):
    '''array : array expression
    '''
    p[0] = p[1] + [p[2]]


def p_list_cdr(p):
    '''list : LPRN CDR list RPRN
    '''
    p[0] = ['cdr', p[3]]


def p_list_cons(p):
    '''list : LPRN CONS expression list RPRN
    '''
    p[0] = ['cons', p[3], p[4]]


def p_error(p):
    print(f"Syntax Error at position {p.lexpos}, line {p.lineno} for the input!\n")


parser = yacc.yacc()