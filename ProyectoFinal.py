# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "../..")

tokens = (
    'NAME', 'INUMBER', 'FNUMBER', 'BOOLEAN'
)

literals = ['=', '+', '-', 'i', 'f', 'b', 'p', '{', '}', '(', ')']
reserved =  {
    'if' : 'IF',
    'then': 'THEN',
    'else': 'ELSE'
}
# Tokens

t_NAME = r'[ac-eg-hj-oq-z]'



def t_FNUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'True|False'
    t.value = bool(t.value)  

def t_lbrace(t):
     r'\{'
     t.type = '{'      
     return t
 
 def t_rbrace(t):
     r'\}'
     t.type = '}'
     return t


t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Test
data = '''
10.4 
11
False
 '''
lexer.input(data)

while True:
    tok = lexer.token()
    print(tok)
    if not tok:
        break;
    print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos) # lexpos es posición en tabla de símbolos.

# Parsing rules
class Node:
    def __init__(self,type,children=None,leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = [ ]
        self.leaf = leaf
# dictionary of names
names = {}
abstractTree = {}

def p_prog(p):
    'prog : dcls stmts'
    None

def p_dcls(p):
    '''dcls : dcl dcls
            | dcl'''
    None

def p_dcl_declare_int(p):
    'dcl : "i" NAME'
    names[p[2]] = { "type": "INT", "value":0}

def p_statement_declare_float(p):
    'dcl : "f" NAME'
    names[p[2]] = { "type": "FLOAT", "value":0}


def p_statements_recursion(p):
    '''stmts : statement stmts
             | statement'''
    None

def p_statement_print(p):
    'statement : "p" expression'
    print(p[2])

def p_statement_assign(p):
    'statement : NAME "=" expression'
    if p[1] not in names:
        print ( "You must declare a variable before using it")
    if isinstance(p[3], float) and names[p[1]]["type"] != "FLOAT":
        print ( "You should not assign a float value to a int variable")
    names[p[1]]["value"] = p[3]


# def p_statement_expr(p):
#     'statement : expression'
#     # print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_inumber(p):
    "expression : INUMBER"
    p[0] = p[1]


def p_expression_fnumber(p):
    "expression : FNUMBER"
    p[0] = p[1]

def p_expression_fnumber(p):
    "expression : BOOLEAN"
    p[0] = p[1]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]["value"]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

""" 
f = open("code.txt")
content = f.read()
yacc.parse(content) """

# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     yacc.parse(s)