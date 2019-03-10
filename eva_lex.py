# -----------------------------------------------------------------------------
# eva_lex
#
# Adrian Gerardo Peña Barrera A00816456
# -----------------------------------------------------------------------------

tokens = [
    'ID',
    'RBRA', 'LBRA', 'COLON', 'SEMICOLON',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'RELOP', "CTESTRING", "CTEI", "CTEF", "COMMA"
    ]

reserved = {
   'if'       :  'IF',
   'else'     :  'ELSE',
   'var'      :  'VAR',
   'program'  :  'PROGRAM',
   'int'      :  'INT',
   'float'    :  'FLOAT',
   'print'    :  'PRINT',
}
tokens += reserved.values()

# Tokens
t_LBRA    = r'\{'
t_RBRA    = r'\}'
t_COLON    = r':'
t_COMMA    = r','
t_SEMICOLON = r';'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RELOP   = r'<|>|<>'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_CTESTRING(t):
    r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEF(t):
    r'\d+'
    t.value = float(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()
'''
lexer = lex.lex()
lexer.input("program hola ;")
while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
'''

# dictionary of names (for storing variables)
names = { }

def p_programa_start(p):
    'programa : PROGRAM ID SEMICOLON programa2 bloque'

def p_program2(p):
    '''programa2 : vars
                | empty'''
def p_vars(p):
    'vars : VAR vars2 vars4'

def p_vars2(p):
    'vars2 : ID vars3 COLON type SEMICOLON'

def p_vars3(p):
    '''vars3 : empty
             | COMMA ID vars3'''
def p_vars4(p):
    '''vars4 : empty
             | vars2'''
def p_type(p):
    '''type : INT
            | FLOAT'''

def p_bloque(p):
    'bloque : LBRA bloque2 RBRA'

def p_bloque2(p):
    '''bloque2 : empty
               | estatuto bloque2'''

def p_estatuto(p):
    '''estatuto : asignacion
                | condi
                | escritura'''

def p_asignacion(p):
    'asignacion : ID EQUALS expresion SEMICOLON'

def p_expresion(p):
    'expresion : exp expresion2'
def p_expresion2(p):
    '''expresion2 : empty
                  | RELOP exp'''

def p_escritura(p):
    'escritura : PRINT LPAREN interior RPAREN SEMICOLON'

def p_interior(p):
    '''interior : expresion escritura2
                | CTESTRING escritura2'''

def p_escritura2(p):
    '''escritura2 : COMMA interior
                  | empty'''

def p_condi(p):
    'condi : IF LPAREN expresion RPAREN bloque condi2'

def p_condi2(p):
    '''condi2 : ELSE bloque
              | empty'''

def p_exp(p):
    'exp : term exp2'
def p_exp2(p):
    '''exp2 : empty
            | PLUS exp
            | MINUS exp'''

def p_term(p):
    'term : factor term2'
def p_term2(p):
    '''term2 : empty
             | TIMES term
             | DIVIDE term'''

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | PLUS varcte
              | MINUS varcte
              | varcte'''

def p_varcte(p):
    '''varcte : ID
              | CTEI
              | CTEF'''

def p_empty(p):
 'empty :'
 pass

def p_error(p):
    print("Syntax error at '%s'" % p.value)


import ply.yacc as yacc
yacc.yacc()
def loadFile():
    fn = input('Source Code File > ')
    file = open(fn+'.txt', 'r', encoding="utf8")
    s = file.read()
    yacc.parse(s)
loadFile()


'''while True:
    try:
        s = input('patito > ')   # use input() on Python 3
    except EOFError:
        break
'''

