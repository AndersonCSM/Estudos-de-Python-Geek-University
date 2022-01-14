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

# questão 11
from random import randrange
vetor = []
sm, sn = 0, 0
for v in range(0,10):
    vetor.append(randrange(-10,10))

for k, v in enumerate(vetor):
    if v < 0:
        sn += v
    if v > 0:
        sm += v

print(vetor)
print(f'A soma dos valores negativos são {sn}')
print(f'A soma dos valores negativos são {sm}')

# questão 12
lista = list()

for c in range(0,5):
    try:
        lista.append(int(input(f'Insira o {c+1}º valor númerico \n')))
    except:
        print('Insira apenas valores inteiros')

for k, v in enumerate(lista):
    print(f' O {k+1} foi {v} ')

print(f'''
O maior valor foi {max(lista)}
O menor valor foi {min(lista)}
a média é {sum(lista)/len(lista)}
''')

# questão 13
lista = []
for c in range(0,5):
    try:
        lista.append(int(input(f'Insira o {c+1}º valor númerico \n')))
    except:
        print('Insira valores númericos inteiros')

print(f'O maior valor é {max(lista)}, na posição {lista.index(max(lista))}')
print(f'O menor valor é {min(lista)}, na posição {lista.index(min(lista))}')

# questão 14 não sei

# questão 15
lista = []
for c in range(0,10):
    try:
        lista.append(int(input(f'Insira o {c+1}º valor númerico \n')))
    except:
        print('Insira valores númericos inteiros')

print(set(lista))

# questão 16
import iteration_utilities
listNums = [1,1,2,3,3,4,5,5,5,5,6,8,8]

def listDupsUnique(listNums):
	return print(list(iteration_utilities.unique_everseen(iteration_utilities.duplicates(listNums))))

listDupsUnique(listNums)

# questão 17
from random import randrange
vetor = []

for c in range(0,10):
    vetor.append(randrange(-100,100))

for k, v in enumerate(vetor):
    if v < 0:
        vetor[k] = 0

print(vetor)

# questão 18
from random import randrange

vetor = []
vetorM = []
try:
    x = int(input('Insira um valor para acharmos múltiplos \n'))
except:
    print('valor inválido')
for c in range(0,10):
    vetor.append(randrange(-100,100))
for j in range(0,10):
    if (vetor[j] % x) == 0:
        vetorM.append(vetor[j])

print(vetor)
print(vetorM)

# questão 19
from random import randint
lista = list()

for i in range(0,50):
    lista.append(((i+5*i)%(i+1)))

print(lista)

# questão 20
from random import randint
vetor = []
vetorI = []

c, i = 0, 0

while i < 10:
    try:
        c = int(input(f'Insira o {i+1}º valor numérico\n'))
        if c in range(0,50):
            vetor.append(c)
            i +=1
    except:
        print('Insira apenas valores inteiros e dentro do intervalo de [0,50]')

for j in range(0,10):
    if (vetor[j] % 2) == 0:
        vetorI.append(vetor[j])

print(vetor)
print(vetorI)

# questão 21
A, B, C = [], [], []
for j in range(0,10):
    A.append(int(input(f'Informe o {j+1}º para o Vetor A \n')))
    B.append(int(input(f'Informe o {j+1}º para o Vetor B \n')))

for i in range(0,10):
    C.append(B[i] * A[i])

print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')

# questão 22
A, B, C = [], [], []
imp, par = 0, 0
for j in range(0,10):
    A.append(int(input(f'Informe o {j+1}º para o Vetor A \n')))
    B.append(int(input(f'Informe o {j+1}º para o Vetor B \n')))

for i in range(0,20):
    if (i % 2) == 0:
        C.append(A[imp])
        imp += 1
    else:
        C.append(B[par])
        par += 1

print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')

# questão 23
a = {1, 3, 5, 6, 7}
b = {2, 4, 10, 15, 5}
soma = 0

for v in a:
    for v2 in b:
        soma += v*v2
        break

print(f'{a} \n {b}')
print(soma)

# questão 24 Não consegui

# questão 25
lista = []
i, c, j = 1, 0, 0
while c < 100:
    if i % 7 == 0:
        lista.append(i)
        i += 1
        c += 1
    else:
        i +=1

print(lista)
print(len(lista))

# questão 26
import statistics
import random

vetor = []

for c in range(0,10):
    vetor.append(random.randint(0,100))

print(f'O desvio padrão do vetor é {statistics.pstdev(vetor)} com 10 graus de liberdade')

# questão 27
from random import randint
lista = list()


def is_prime(a):
    return all(a % i for i in range(2, a))

for c in range(0,10):
    lista.append(randint(0,100))

for i in range(0,10):
    if is_prime(lista[i]) == True:
        print(f'O elemento {lista[i]} é ímpar e sua posição é {lista.index(lista[i])}')

# questão 28
from random import randint
lista, v1, v2 = [], [], []

def isprimo(num):
    div = 0
    for c in range(1,num+1):
        if (c != 1) and (num % c == 0):
            div += 1
    if div == 1:
        return True
    else:
        return False

for c in range(0,10):
    lista.append(randint(0,100))
for k,v in enumerate(lista):
    if isprimo(lista[k]) == True:
        v1.append(v)
    else:
        v2.append(v)

print(lista)
print(f'Os números primos são: {v1}')
print(f'Os números não primos são: {v2}')

# questão 29
par, impar = [], []
for c in range(0,6):
    try:
        n = int(input('Insira valores númericos\n'))
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    except:
        print('Valor informado inválido')

print(f'''
Os números pares foram {par}
A soma dos números pares foi de {sum(par)}
Os números ímpares digitados foram {impar}
A quantidade de números ímpares digitados {len(impar)}
''')

# questão 30
l1 = [1,1,2,3,4,5,6,7]
l2 = [1,6,8,0,9,8,5]

v1 = set(l1)
v2 = set(l2)
print(v1 & v2)
"""

# questão 31