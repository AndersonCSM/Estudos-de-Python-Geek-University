"""
- Em Python, módulos são outros arquivos Python no programa.

### Módulo Random -> possui várias funções para geração de números pseudo-aleatórios(pode ter repetição).

# OBS: Existem duas formas de se utilizar um módulo ou função do módulo

# Forma 1 - Importando todo o módulo (não recomendado).

import random

# todo o módulo, todas as funções, atributos, classes e propriedades serão importadas.

# EX01:
import random

print(random.random())

# Forma 2 - Importando funções específicas do módulo.

from random import randint

# Forma 3 - Podemos importar apenas todas as funções de um módulo utilizando o *

# EX:
from random import *
print(random()) # Assim não precisamos usar a sintaxe random.random()

### Funções do módulo Random:

## random() -> Gera um número pseudo-aleatório entre 0 e 1.
# EX:
from random import random

for i in range(10):
    print(random())

## uniform() -> Gera um número pseudo-aleatório entre os valores estabelecidos
# EX:
from random import uniform
for i in range(10):
    print(uniform(3,7)) # gera valores no intervalo (3 < x < 7)

## randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
# EX:
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # Começa em 1 e vai até 60

## choice() -> Mostra um valor aleatório entre um iterável.
# EX01:
jogadas = ['pedra','papel','tesoura']

print(choice(jogadas))

# EX02:
print(choice('Geek University')) # Escolhe uma letra dentro da String(iterável)

## shuffle() -> Tem a função de embaralhar dados

cartas = ['K','Q','J','A','2','3','4','5','6','7']

print(cartas)

shuffle(cartas)

print(cartas[0])

print(carta.pop()) # Remove a última carta

### Módulos integrados(built-in)

________________________
Python(Módulos built-in)
------------------------
# Dentro do Site Python.org podemos encontrar todos os módulos built-in usáveis.

### Utilizando alias (apelidos) para módulos/funções

# EX:
from random import randint as rdi

print(rdi(5,89))

# EX:
from random import randint as rdi, random as rdm

print(rdi(5,89))
print(rdm())

# Costumamos utilizar tuple para colocar múltiplos imports de um mesmo módulo
# EX:
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3,7))

lista = ['geek','university','python']
shuffle(lista)
print(lista)

print(choice('university'))

### Módulos customizados

Como módulos Python nada mais são do que arquivos Python, então Todos os arquivos que criamos no curso são
módulos Python que podem ser utilizados.

import nome_do_arquivo

from nome_do_arquivo import função

from nome_do_arquivo import *

### Instalando e utilizando módulos externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em https://pypi.org

# Caso queira buscar por uma necessidade pesquise: python package for 'necessidade'
"""
