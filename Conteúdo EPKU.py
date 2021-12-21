'''
# As aulas anteriores foram para a preparação de ambiente, bem como as aulas que faltam que se tratam de recaptulação.
# Aula 10: PEP8 - Python Enhancement Proposal
#São propostas de melhorias para a linguagem Python
The Zen of Python

import this

# A idéia de PEP8 é que possamos escrever códigos Python
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

#Para deixar um texto bem formatado, podemos usar primeiro um lower e depois um title.
print('TEXTO'.lower().title())

# Aula 12: Entrada e saída de dados
# Entrada de dados

# Modelo antigo
print('Qual é seu nome ?')
nome = input()
# modelo atualizado
nome = input('Qual é seu nome? ')
idade = input('Qual sua idade? ')

# Entrada com Cast
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

# Aula 15: Tipo númerico
# No Python não existe limite para um valor númerico, ele armazenar o número até o quando de memória estiver disponível

# É possível definir um número com diversas casas de milhar usando underline
1_000_000 == 1000000

# Podendo ser usado qualquer operador aritmético(* / - +)
num += 1 == num = num + 1

# Operações aritméticas: no Python podemos realizar as operações tanto no terminal Python, como dentro do programa, como em áreas internas dos módulos.
1- soma: + print(1+1) = 2
2- subtração: - print(1-1) = 0
3- multiplicação: * num = 2*5 = 10
4- exponenciação: ** print(3**2) = 9
5- divisão: / print(5/2) = 2.5
6- divisão inteira: // print(5//2) = 2 outro modelo antigo de realizar a mesma operação: print(int(5/2))
7- Resto da divisão: % print(5%2) = 1

# É possível identificar o tipo da variável(classe) usando a função type()
num = 42
type(num) = <class 'int'>

# Aula 16: Tipo Float
# Tipo real, decimal

OBS: O separador de casas decimais é o ponto(.) e não vírgula.

# É possível declarar mais de uma variável em apenas uma linha
valor1, valor2 = 1, 44
print(valor1) = 1
print(valor2) = 44

# Todas as operações com os inteiros é possível com os flutuantes

# Podemos converter um float para um int.
OBS: Ao converter valores float para inteiros, perdemos precisão
valor = 1.44
print(int(valor)) = 1
print(type(valor)) = int

# É possível trabalhar com números complexos dentro do Python. Basta adicionarmos um j ao número
num = 5j
type(num) = complex

# Aula 17: Tipo Booleano
Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso
True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

# Operações básicas

# Negação (not):
print(not True): False

# Ou (or):
É uma operação binária, depende de dois valores. Ou um ou outro deve ser verdadeiro.
True or True = True
True or False = True
False or True = True
False or False = False 

# E (and):
Também é uma operação binária, depende de dois valores. Ambos os valores devem ser verdadeiros.
True and True = True
True and False = False
False and True = False
False and False = False 

# Aula 18: Tipo String
Em Python, um dado é considerado do tipo String sempre que:
- Estiver entre aspas simples, duplas, simples triplas, duplas triplas;
'uma String','43','True','a','42.3'

- Usar aspas simples dentro de um texto, alternandos o uso das aspas para usa-las adequadamente
nome = "Gina's Bar"

- Quebra de linha
nome = 'Angelina \n Julie' 
ou 
nome = """ Angelina
Julie"""

# Modificando Strings
tr = 'texto'
1- Nome em caixa alta: tr.upper()
2- Nome em caixa baixa: tr.lower()
3- Divide as palavras da String dentro de uma lista: tr.split()
nome= 'Geek University'
4- Substituir elementos de uma String (e) por outra (x): tr.replace('e','x')

# Fatiamento de Strings: Podemos tratar Strings como uma lista de caracteres e como isso realizar cortes.
Podemos resgatar os caracteres do índice 0 até o índice 3:
nome= 'Geek University'
print(nome[0:4]) = Geek

# Ao transformar em lista, a palavra Geek passa a ocupar a posição [0], podendo chama-la
print(nome.split()[0]) 

#Imprimindo uma String em ordem inversa:
nome= 'Geek University'
print(nome[::-1]) = ytisrevinU keeG

# Aula 19: Escopo de variáveis
Dois casos de escopo:
1 - Variáveis Globais;
    - Variáveis Globais são reconhecidas em todo o programa.

2- Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde fora declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python, fazemos:
variável = valor

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declarar uma variável,
nos não colocamos o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor na mesma.

# Exercícios - Seção 04
# Questão 1
num = int(input('Insira um número '))
print(num)

# Questão 2
num = float(input('Insira um número '))
print(num)

# Questão 3
num1, num2, num3 = int(input('Digite o primeiro número \n')), int(input('Digite o segundo número \n')), int(input('Digite o terceiro número \n'))
print(f'A soma dos três números é {num1+num2+num3}')

# Questão 4
num1 = float(input('Digite um número \n'))
print(f'O quadrado do número inserido é {num1**2}')

# Questão 5
num1 = float(input('Insira um número \n'))
print(f'A quinta parte do número inserido é {num1/5}')

# Questão 6
celsius = float(input('Insira uma temperatura em Celsius \n'))
print(f'A temperatura convertida em Fahrenheit é {celsius*(9/5)+32}ºF')

# Questão 35
from math import sqrt
a, b = float(input('Insirar um valor para o cateto a\n')), float(input('Insirar um valor para o cateto b\n'))
print(f' A hipotenusa é: {sqrt((a**2) + (b**2))}')

# Questão 46
num = int(input('Insira um número inteiro de três digitos \n'))
print(str(num)[::-1])
# Questão 51
from math import sqrt
x, y = float(input('insira as coordenadas para x \n')), float(input('insira as coordenadas para y \n'))
print(f'A distância do ponto formado pelas coordenadas ({x},{y}) é {sqrt((x**2)+(y**2))}')

'''
