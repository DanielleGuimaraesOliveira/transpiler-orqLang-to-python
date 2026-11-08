import ply.lex as lex

palavras_reservadas = {
    'INICIO': 'INICIO',
    'FIM': 'FIM',
    'VAR': 'VAR',
    'SERVICO': 'SERVICO',
    'IMPRIMIR': 'IMPRIMIR',
    'SE': 'SE',
    'ENTAO': 'ENTAO',
    'SENAO': 'SENAO',
    'REPITA': 'REPITA',
    'VEZES': 'VEZES',
    'VERDADEIRO': 'VERDADEIRO',
    'FALSO': 'FALSO'
}

identificadores_variaveis = [
    'ID','NUM','STR'
]

operadores = [
    'MAIS','MENOS','MULTIPLICACAO', 'DIVISAO','IGUAL_IGUAL','DIFERENTE',
    'MENOR','MENOR_IGUAL','MAIOR','MAIOR_IGUAL','ATRIBUICAO'
]

simbolos = [
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
    'VIRGULA',
    'SETA'
]

tokens = (list(palavras_reservadas.values()) + identificadores_variaveis + simbolos + operadores)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavras_reservadas.get(t.value, 'ID')
    return t

def t_STR(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    return t

def t_NUM(t):
    r'[0-9]+(\.[0-9]+)?'

    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)

    return t

t_IGUAL_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_MENOR = r'<'
t_MAIOR = r'>'
t_ATRIBUICAO = r'='

t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_VIRGULA = r','
t_SETA = r'->'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()