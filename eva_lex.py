# -----------------------------------------------------------------------------
# eva_lex
#
# Adrian Gerardo Peña Barrera A00816456
# Valeria Rocha Sepúlveda A01193039
#
# -----------------------------------------------------------------------------

'''
PENDIENTES:
- Checar el apartado de vars
- Checar el apartado de Write
- Checar si en asignación podemos sostener una funccall y verificar el uso correcto del ; en ese caso.
- Probar con prueba.txt una vez terminado.
'''

tokens = [
    'ID',
    'RBRA', 'LBRA','RSBRA', 'LSBRA', 'COLON', 'SEMICOLON',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'RELOP', "CHARACTER", "INTEGER", "NUMERIC", "LOGICAL", "COMMA", "AND", "OR", "NOT"
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
   'return'   :  'RETURN',
   'function' : 'FUNCTION',
   'void'     : 'VOID'
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
# def p_main(p):
#     '''main :  LBRA vars main2 RBRA'''
#
# def p_main2(p):
#     '''main2 : estatuto main2
#                 | empty'''

def p_main(p):
    '''main :  MAIN LBRA mainvars main2 RBRA'''

def p_main2(p):
    '''main2 : estatuto main2
                | empty'''

def p_mainvars(p):
    '''mainvars : vars mainvars
                | empty'''

#################

# Valeria, checa el apartado de VARS por favor.
# def p_vars(p):
#     'vars : VAR vars2 vars4'
#
# def p_vars2(p):
#     'vars2 : ID vars3 COLON type SEMICOLON'
#
# def p_vars3(p):
#     '''vars3 : empty
#              | COMMA ID vars3'''
# def p_vars4(p):
#     '''vars4 : empty
#              | vars2'''

#MANERA como esta en los diagramas de sintaxis
def p_vars(p):
    'vars : type idmv vars2 SEMICOLON'

def p_vars2(p):
    '''vars2 : empty
             | COMMA idmv vars2'''


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
    'exlog : exlog2 expresion exlog3'

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
                | escritura
                | return'''

# ASIGNACION
def p_asignacion(p):
    'asignacion : idmv EQUALS exlog'

# DATA
def p_data(p):
    '''data : NUMERIC
            | CHARACTER
            | LOGICAL
            | INTEGER
            | idmv
            | funccall
            | read'''

# RETURN
def p_return(p):
    '''return : RETURN return2'''

def p_return2(p):
    '''return2 : exlog
               | empty '''

# IDMVF
def p_idmvf(p):
    'idmvf : ID idmvf2'


def p_idmvf2(p):
    '''idmvf2 : LSBRA exp RSBRA idmvf3
              | LPAREN exp RPAREN
              | empty'''

def p_idmvf3(p):
    '''idmvf3 : LSBRA exp RSBRA
              | empty'''

# IDMV
def p_idmv(p):
    'idmv : ID idmv2'


def p_idmv2(p):
    '''idmv2 : LSBRA exp RSBRA idmvf3
              | empty'''

# ARGS
def p_args(p):
    'args : type ID args2'

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
# def p_condicion(p):
#     'condicion : IF LPAREN exlog RPAREN bloque condi2'
def p_condicion(p):
    'condicion : IF LPAREN exlog RPAREN bloque condicion2'

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
    '''factor : LPAREN exlog RPAREN
              | PLUS data
              | MINUS data
              | data'''
# VARCTE (Factor solo puede hacer uso de ids, numeric y integers, no de characters ni logicals, por eso se hizo este bloque.)
#AGREGAR
# def p_varcte(p):
#     '''varcte : ID
#               | NUMERIC
#               | INTEGER'''


# WRITE Favor de checarlo
def p_escritura(p):
    'escritura : WRITE LPAREN interior RPAREN'

def p_interior(p):
    '''interior : expresion escritura2
                | CHARACTER escritura2'''

def p_escritura2(p):
    '''escritura2 : COMMA interior
                  | empty'''

def p_read(p):
    'read : READ LPAREN read2 RPAREN'

def p_read2(p):
    '''read2 : CHARACTER
                | empty'''

def p_func(p):
    'func : FUNCTION functipo ID LPAREN funcargs RPAREN LBRA funcvars funcest RBRA'

def p_functipo(p):
    '''functipo : type
                | VOID'''

def p_funcargs(p):
    '''funcargs : args
                | empty'''

def p_funcEst(p):
    '''funcest : estatuto funcest
                | empty'''

def p_funcvars(p):
    '''funcvars : vars funcvars
                | empty'''

def p_ciclo(p):
    'ciclo : FOR LPAREN ciclo1 SEMICOLON exlog SEMICOLON asignacion RPAREN bloque'

def p_ciclo1(p):
    '''ciclo1 : asignacion
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
    file = open(fn+'.eva', 'r', encoding="utf8")
    s = file.read()
    yacc.parse(s)
loadFile()


'''while True:
    try:
        s = input('patito > ')   # use input() on Python 3
    except EOFError:
        break
'''
