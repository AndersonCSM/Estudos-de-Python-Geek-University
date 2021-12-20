'''
# As aulas anteriores foram para a preparação de ambiente, bem como as aulas que faltam que se tratam de recaptulação.
# Aula 10: PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python
The Zen of Python

import this

A idéia de PEP8 é que possamos escrever códigos Python
de forma Pythônica (agradável).
[1] - Utilizar Camel Case para nome de Classes;
class Calculadora:

    pass


class calculadora_cinetifica: ERRADO 
    pass


class CalculadoraCientifica:  Correto
    pass


[2] - Utilizar nomes em minúsculo, sperados por underline para funções ou variáveis;
numero = 4

numero_impar = 5

def soma():
    pass

def soma_dois():
    pass


[3] - Utilize 4 espaços para identação! equivale a um Tab, CUIDADO AO USAR Tab, pois pode ser configurado, assim, no seu pc pode ser 4 espaços, mas para outro usuário não.
if 'a' in 'banana':
    print('tem')    

[4] - Linhas em branco,
- Separar funções e def com duas linhas em branco;
- Método dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

# Import Errado
import sys, os

# Import Certo
import sys
import os

# Não há problemas em importar módulos de uma biblioteca, usando o from:
from types import StringType, ListType

# Caso tenha muito imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções
# Não faça:
funcão( algo[ 1 ], { outro: 2} )

# FaçaL
funcao(algo[1], {outro: 2})

# Não faça:
algo (1)

# Faça:
algo(1)

# Não faça:
dict ['chave'] = lista [indice]

# Faça:
dict['chave'] - lista[indice]

# Não faça:
x        = 1
y        = 2

# Faça:
x = 1
y = 3

[7] - Termine sempre uma instrução com uma nova linha em branco
print('linha em branco após esse comando')

# Aula 11: dir e help
Utilitários Python para te auxiliar na programação
Funciona perfeitamente quando usados no terminal do SO.
podemos utiliza-los no código chamando dentro do print

# dir -> Apresenta todos os atributo, funções/métodos disponíveis para determinado tipo de dado ou variável.
dir(tipo de dado/variável)
dir(variavel) -> visualizar as opções da variável
num = ''
print(dir(num))

# help -> Apresenta a documentação/como utilizar os atributos/propriedade e funções/métodos disponíveis para
determinado tipo de dado ou variável.
help(print)

Nota: Para deixar um texto bem formatado, podemos usar primeiro um lower e depois um title.
print('TEXTO'.lower().title())

# Aula 12: Entrada e saída de dados
# Entrada de dados

# Modelo antigo
print('Qual é seu nome ?')
nome = input()

#modelo atualizado
nome = input('Qual é seu nome? ')
idade = input('Qual sua idade? ')

#Entrada com Cast
idade = int(input('Qual sua idade? '))

# Input -> Entrada
# Todo dado recebido via input é do tipo String
Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Asplas simples triplas;
- Asplas duplas triplas;


# Saída de dados

#Exemplo de print Atual, Python 3.7
print(f'Seja bem-vindo(a) {nome}')
print(f'A {nome} nasceu em {2021 - int(idade)}}') 
# int(idade) -> está realizando um cast
# Cast é a 'conversão' de um tipo de dado para outro. 

#Exemplo de print 'Moderno' do print, Python 3.0
print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print antigo da versão Python 2.0
print('Seja bem-vindo(a) %s' % nome)
print('A %s tem %s anos' % (nome, idade))


'''


