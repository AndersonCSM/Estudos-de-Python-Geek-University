'''
### Utilizando Lambdas
- São conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções SEM NOME, ou seja,
Funções anônimas.
- São bastante usadas na ordenação / filtragem de informações

# Funcão em Python
def funcao(x):
    return 3*x +1
print(funcao(2))

# Expressão Lambda
lambda entrada: saida

lambda x: 3*x+1
# E como utilizar a expressão lambda?
calc = lambda x:3*x+1
print(calc(2))

# Podemos ter expressões lambdas com mútliplas entradas de dados

EX 01: 
nome = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome('angelina','Julie'))

EX 02:
amar = lambda:'Como não amar Python?'
uma = lambda x: 3*x+1
# n = lambda x1, x2, ... xn : <expressão>
print(amar())
print(uma(6))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

EX 03:
# Outro exemplo: ordenando autores pelo sobrenome
# Forma usual para expressões lambdas
autores = ['Isaac Asimov', 'Ray Bradbyry', 'Arthur C. Clarke']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
# EX 04: Função Quadrática
def funcao_quadratica(a,b=0,c=0):
    """
    Retonra uma função quadrática do tipo: f(x) = a * x**2 + b*x + c
    x = lambda
    a = obrigatório
    b = opcional
    c = opcional
    """
    return lambda x: a *x**2 + b*x+ c

print(funcao_quadratica(3,0,1)(2))

'''

