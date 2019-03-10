# -----------------------------------------------------------------------------
# eva_lex
#
# Adrian Gerardo Peña Barrera A00816456
# -----------------------------------------------------------------------------

tokens = [
    'ID',
    'RBRA', 'LBRA','RSBRA', 'LSBRA', 'COLON', 'SEMICOLON',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'RELOP', "CHARACTER", "INTEGER", "NUMERIC", "LOGICAL", "COMMA", "AND", "OR", "NOT", "RETURN"
    ]

reserved = {
   'if'       :  'IF',
   'else'     :  'ELSE',
   'var'      :  'VAR',
   'program'  :  'PROGRAM',
   'main'     :  'MAIN',
   'int'      :  'INT',
   'num'      :  'NUM',
   'write'    :  'WRITE',
   'read'     :  'READ',
   'for'      :  'FOR',
   'char'     :  'CHAR',
   'bool'     :  'BOOL',
   'return'   :  'RETURN'
}
tokens += reserved.values()

# Tokens
t_LBRA    = r'\{'
t_RBRA    = r'\}'
t_LSBRA    = r'\['
t_RSBRA    = r'\]'
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
t_AND  = r'\&'
t_OR  = r'\|'
t_NOT  = r'\!'
t_RELOP   = r'<|>|==|<=|>=|!='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_CHARACTER(t):
    r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERIC(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_LOGICAL(t):
	r'true|false'
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

# PROGRAM
def p_programa_start(p):
    'programa : PROGRAM ID SEMICOLON programa2 programa3 main'

def p_program2(p):
    '''programa2 : vars programa2
                | empty'''

def p_programa3(p):
    '''programa3 : func programa3
                | empty'''

# MAIN
def p_main(p):
    '''main :  LBRA vars main2 RBRA'''

def p_main2(p):
    '''main2 : estatuto main2
                | empty'''



# Valeria, checa el apartado de VARS por favor.
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


# BLOQUE
def p_bloque(p):
    'bloque : LBRA bloque2 RBRA'

def p_bloque2(p):
    '''bloque2 : empty
               | estatuto bloque2'''

# TIPO
def p_type(p):
    '''type : BOOL
            | CHAR
            | INT
            | NUM'''


# EXPRESIONLOGICA
def p_exlog(p):
    'exlog: exlog2 expresion exlog3'

def p_exlog2(p):
    '''exlog2 : NOT
              | empty'''

def p_exlog3(p):
    '''exlog3 : AND exlog
              | OR exlog
              | empty'''


# EXP
def p_expresion(p):
    'expresion : exp expresion2'
def p_expresion2(p):
    '''expresion2 : empty
                  | RELOP exp'''

# ESTATUTO
def p_estatuto(p):
    '''estatuto : estatuto2 SEMICOLON'''

def p_estatuto2(p):
    '''estatuto2 : condicion
                | ciclo
                | funccall
                | asignacion
                | read
                | write
                | return
                | specfunc'''

# ASIGNACION
def p_asignacion(p):
    'asignacion : idmv EQUALS exlog SEMICOLON'

# DATA
def p_data(p):
    '''data : NUMERIC
            | CHARACTER
            | LOGICAL
            | idmvf'''

# RETURN
def p_return(p):
    '''return : RETURN return2'''

def p_return2(p):
    '''return2 : exlog
               | data
               | empty '''

# IDMVF
def p_idmvf(p):
    'idmvf : ID idmvf2'

def p_idmvf2(p):
    '''idmvf2 : LSBRA exp RSBRA LSBRA exp RSBRA
              | LPAREN exp RPAREN
              | empty'''

# IDMV
def p_idmv(p):
    'idmv : ID idmv2'

def p_idmv2(p):
    '''idmv2 : LSBRA exp RSBRA LSBRA exp RSBRA
              | empty'''

# ARGS
def p_args(p):
    'args : tipo ID args2'

def p_args2(p):
    '''args2 : COMMA args
              | empty'''

# FUNCCALL
def p_funccall(p):
    'funccall : ID LPAREN funccall2 RPAREN'

def p_funccall2(p):
    '''funccall2 : exp funccall3
              | empty'''

def p_funccall3(p):
    '''funccall3 : COMMA exp funccall3
              | empty'''


# CONDICION
def p_condicion(p):
    'condicion : IF LPAREN exlog RPAREN bloque condi2'

def p_condicion2(p):
    '''condicion2 : ELSE bloque
              | empty'''

# EXP
def p_exp(p):
    'exp : term exp2'
    
def p_exp2(p):
    '''exp2 : empty
            | PLUS exp
            | MINUS exp'''

# TERM
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
# VARCTE (Factor solo puede hacer uso de ids, numeric y integers, no de characters ni logicals, por eso se hizo este bloque.)
def p_varcte(p):
    '''varcte : ID
              | NUMERIC
              | INTEGER'''

            
# WRITE Favor de checarlo
def p_escritura(p):
    'escritura : PRINT LPAREN interior RPAREN SEMICOLON'

def p_interior(p):
    '''interior : expresion escritura2
                | CTESTRING escritura2'''

def p_escritura2(p):
    '''escritura2 : COMMA interior
                  | empty'''


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

