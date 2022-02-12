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

### Map

Map difere dos conjuntos.
Com map, fazemos mapeamento de valores para função.

# Exemplo 01: programa para cálcular a área de uma circunferência
import math
def area(r):
    """
    Calcula a área de uma circunferência com raio 'r'.
    """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3)) 

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma 1: modo comum de trabalhar com a lista:
raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2: utilizando o Map
# Map é uma função que recebe dois parâmetros
# O primeiro uma função, o segundo um iterável

areas2 = map(area, raios)
print(areas2)
print(type(areas)) # Retorna um Map Object

print(list(areas2))

# Forma 3: Map com lambda
print(list(map(lambda r: math.pi * (r **2), raios)))

#OBS: após o primeiro uso da função map(), o resultado é zerado como forma de economizar memória.
#OBS: o retorno do tipo Map Object é um iterável

# Fixando - Map
# Dados iteráveis: a1,a2,...,an
# Função: f(x)

# Utilizando a função map, onde ocorrerá um 'mapeamento' de cada elemento dos dados, sendo aplicado a função:
# map(f,dados) -> f(a1), f(a2), f(...), f(an)

# EX 02:
cidades = [('Berlim',29),('Cairo',36),('Buenos Aires',19),('Nova York', 28)]

print(cidades)
# Repassando para farenheit

c_p_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_p_f, cidades)))

### Filter
filter() -> Serve para filtrar dados de uma determinada coleção
# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo:
# uma função e um iterável.
# Assim como a função map(), os dados são apagados da memória após a primeira utilização
# Também retorna o resutaldo como Filter Object
# A diferença entre map() e filter() é:
- map(): recebe dois parâmetros, uma função e um iterável e retorna um objeto, mapeando(executando) a função para cada elemento
- filter(): recebe dois parâmetros, uma função e m iterável e retorna um objeto, filtrando(Apenas elementos True, de acordo com a função) os elementos de acordo com a função. 
    O filter retorna valores booleanos, e apenas os verdadeiros serão repassados, diferente do map() que todas serão repassados

# EX 01: 
# Biblioteca para trabalhar com dados estatísticos
import statistics
dados = [1,3,2.7,0.8,4.1,4.3,-0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

res = filter(lambda x: x > media, dados)
print(list(res))

print(f'novamente: {list(res)}')

# EX 02:
paises = ['','Argentina','Brasil','','Chile','Equador','']
print(f'{list(filter(None, paises))}')

# Outro modelo de mesmo resultado
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# Outro modelo:
res = filter(lambda pais: pais != '',paises)
print(list(res))

# Exemplo mais complexo
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo gatos']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}
    ]

# OBJETIVO: filtrar os usuários que estão inativos no Twitter
print(usuarios)

# Forma 1
# Filtrando usuários que estão inativos no Twitter
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos2 = list(filter(lambda u: not u['tweets'] , usuarios))
print(inativos2)

# Ex 03:
# Combinando filter() e map()
# OBJETIVO: Criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

nomes = ['Vanessa','Ana','Maria']
                # 1: Função do map()                    , #2: Iterável que é a lista nomes filtradas pela função filter().
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

# O código equivale a:

# lista = list(map(lambda nome: f'Sua instrutora é {nome}', ['Ana']))
print(lista)

### Reduce
OBS: A partir do Python3 a função reduce() não é mais uma função integrada (built-in).
Para usa-lá é necessário importar do módulo 'functools'

Guildo van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso. 99% das vezes um loop for é mais legível.

# Entendendo a função reduce()
# Dado uma coleção:
dados = [a1,a2,a3,...,an]

# E uma função que recebe dois parâmetros
def fun(x,y):
    retunr x*y

# A função reduce() também recebe dois parâmetros:
# 1º-funcão com dois parâmetros, 2º-iterável
# A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1,a2) # Aplica a função nos dois primeiros elementos da coleção, armazenando resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado anterior e o próximo elemento, armazendo o novo resultado.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    passo 4: resn = f(resn, n)
# Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado anterior, e o segundo o próximo argumento.

Alternativamente, podemos ver a função reduce() como:
funcao(funcao(funcao(funcao(a1,a2),a3),...), an)

# EX 01:
# utilizando a função reduce() para multiplicar todos os números de uma lista
from functools import reduce
dados = [1,3,4,5,6,7,8,9,2,12]
f_multi = lambda x,y: x*y

print(reduce(f_multi,dados))

# Utilizando um loop normal - Preférivel ao invés do uso do reduce()
res = 1
for n in dados:
    res *= n

print(res)

### Any e ALL
##all() -> Retorna True se todos os lementos do iterável são verdadeiros ou ainda se o iterável estiver vazio.

EX 01:
print(all([0,1,2,3,4])) # Todos os números são verdadeiros? False

print(all([1,2,3,4])) # Todos os números são verdadeiros? True

print(all([])) # Todos os números são verdadeiros? True

print(all((1,2,3,4))) # Todos os números são verdadeiros? True

print(all({0,1,2,3,4})) # Todos os números são verdadeiros? True

print(all('Geek')) # Todos os números são verdadeiros? True

EX 02:
nomes = ['carlos','camila','cassiano','cristina']

print(all([n[0] == 'c' for n in nomes]))

OBS: Um iterável vazio convetido em boolean é False, mas o all() entende como True.
CUIDADO COM isso

EX 03:
print(all([num for num in [4,2,10,6,8] if num % 2 == 0])) # Retorna True pela lógica dos iteráveis

print(all([num for num in [4,2,10,6,8] if num % 2 == 1])) # Retorna True devido a peculiaridade do all, pois será gerado uma lista vazia, e ele entende isso como True

## any() => Retorna True se qualquer elemento do iterável for verdadeiro, se o iterável estiver vazio, retorna False
print(any([0, 1,3,4,5])) # True

print(any([0, False, {},[],())) # False

print(any([num for num in [4,2,10,8] if num % 2 == 0])) # True

### Generators Expression
Em aulas anteriores estudados:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

NÃO VIMOS:
-Tuple Comprehension - porque elas se chamam Generators
# O generator não retornar uma Tupla, mas sim um generator object 
# O resultado é apagado da memória após o primeiro código
# O diferencial do Generators é que ele possui uma melhor performance
# Também permite que ocorra iterações

EX 01:
nomes = ['carlos','camila','cassiano','cristina']

# List Comprehension
res = [nome[0] == 'c' for nome in nomes]
print(type(res))

# Generator
RES = (nomes[0] == 'c' for nome in nomes)
print(type(RES))

# EX 02:
# getsizeof() -> retorna a quantidade de bytes em memória do argumento repassado
from sys import getsizeof

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(9598418974))

print(getsizeof(True))

# EX 03: 
from sys import getsizeof

lists = getsizeof([x *10 for x in range(100)])
print(lists)

sets = getsizeof({x *10 for x in range(100)})
print(sets)

dics = getsizeof({x:x *10 for x in range(100)})
print(dics)

gen = getsizeof((x *10 for x in range(100)))
print(gen)

# EX 04: iterando com generators
gen = ((x *10 for x in range(100)))

for n in gen:
    print(n)
'''

