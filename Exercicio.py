"""
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

#Algoritmo de apostas
from random import randint
numeros = [[], [], [], [], [], [], []]    
for c in range(0, 6):
    i = 0
    while i < 7: # adiciona um número a cada uma das sublistas
        n = randint(1,60)
        if n not in numeros[i]:
            numeros[i].append(n)
            i += 1

for k in range(0,7):
    numeros[k].sort()
    print(f'O {k+1}º jogo: {numeros[k]}')
    
# Exercícios Seção 7
# questão 1
A = [1,0,5,-2,-5,7]
soma = A[0] + A[1] + A[5]
print(soma)

A[4] = 100
print(A)

for v in A:
    print(v)

# questão 2
lista = list()
k = 0

while k != 5:
    try:
        v = int(input('Insira um valor numérico '))
        lista.append(v)
        k += 1
    except:
        print('Valor inválido, insira apenas valores inteiros')

print(lista)

# questão 3
Rconj = {1.5, 2.3, 3.0, 4.6, 5.9, 8.8, 9.5, 13.3, 12.2, 20.3}
lista = list(Rconj)



for k,v in enumerate(lista):
    lista[k] = lista[k] ** 2

for k,v in enumerate(lista):
    print(f'{v:.2f}', end=' ')

print(Rconj)

# questão 4
import random
vetor = list(range(0,10))
for c, v in enumerate(vetor):
    vetor[c] = random.randint(0,101)

while True:
    try:
        x = int(input('Insira o índice do primeiro número a ser somado \n'))
        y = int(input('Insira o índice do segundo número a ser somado \n'))
        print(f'A soma dos valores é {vetor[x] + vetor[y]}')
        break
    except:
        print('Apenas valores inteiros para os índices, entre 0 e 7')

print(vetor)

# questão 5
from random import randint
vetor = []
par = list()

for i in range(0,10):
    vetor.append(randint(0,100))


for v, c in enumerate(vetor):
    if (c % 2) == 0:
        par.append(c)

print(vetor)
print(f'A quantidade de número pares são {len(par)}, e os valores são: {par}')

# questão 6
from random import randint
vetor = []

for i in range(0,10):
    vetor.append(randint(0,100))

print(f'''
    Da lista 
    {vetor} 
    temos:
    O maior valor é: {max(vetor)}
    O menor valor é: {min(vetor)}
''')

# questão 7
vetor = list()
for c in range(0,8):
    vetor.append(input(f'Insira o {c+1}º valor da lista \n'))

maior = max(vetor)
print(f'''
A lista é formada por:
{vetor}
O maior valor é {maior}
Na posição {vetor.index(maior)}
''')

# questão 8
vetor = []
for c in range(0,6):
    vetor.append(input(f'Insira o {c+1}º Valor da lista \n'))

print(f'os valores na ordem inversa: {vetor.reverse()}')

# questão 9
vetor = []
c = 0
while c < 5:
    try:
        value = int(input(f'Insira o {c+1}º número inteiro \n'))
        if value % 2 == 0:
            vetor.append(value)
            c += 1
        else:
            print('É esperado um valor par')
    except:
        print('É esperado um número inteiro')
print(vetor.reverse())

# questão 10
from random import randrange
notas = []

for v in range(0,15):
    notas.append(randrange(0,10))

print(f'''
{notas}
A média de notas da turma é: {sum(notas)/float(len(notas)):.1f}''')

"""


# questão 11