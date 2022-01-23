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

# questão 31
l1 = [1,1,2,3,4,5,6,7]
l2 = [1,6,8,0,9,8,5]

v1 = set(l1)
v2 = set(l2)
print(v1 | v2)

# questão 32
l1 = [1,2,3,4,5]
l2 = [6,7,8,0,9]
soma, multi, dif = [], [], []
for i in range(0,5):
    soma.append(l1[i] + l2[i])
    multi.append(l1[i] * l2[i]) 
    dif.append(l1[i] - l2[i])

l1set = set(l1)
l2set = set(l2)

print(f'''
1º vetor: {l1}
2º vetor:{l2}

A soma dos vetores é: {soma}
O produto dos vetores é: {multi}
A diferença entre os vetores é {dif}
A intersecção entre os elementos dos vetores é {l1set & l2set}
A união entre os elementos dos vetores é {l1set | l2set}
''')
print('Não existe intersecção entre os vetores' if (l1set & l2set) == set() else f'A intersecção entre os elementos dos vetores é {l1set & l2set}')

# questão 33
from random import randint
l1, l2 = [], []

for c in range(0,15):
    l1.append(randint(0,5))

print(l1)

for k, v in enumerate(l1):
    if v != 0:
        l2.append(v)
    
print(l2)

# questão 34
l1 = []
c = 0
while c != 15:
    try:
        v = int(input('Insira um valor para adicionarmos \n'))
        if v not in l1:
            l1.append(v)
            c += 1
        else:
            print('Valor já existe, informe outro')
    except:
        print('valor inválido')

print(l1)

# questão 35: Falta de informação para concluir a questão

# questão 36:
lista = []
try:
    for c in range(0,10):
        lista.append(float(input(f'Insira o {c+1}º valor \n')))  
except:
    print('Erro, insira um valor válido novamente')

print(sorted(lista) )

# questão 37:
from random import randint

lista, listaAN, listaPO = [], [], []
for c in range(0,11):
    lista.append(randint(0,22))

for c in range(0,6):
    listaAN.append(lista[c])
for c in range(10,5,-1):
    listaPO.append(lista[c]) 

listaAN.sort()
listaPO.sort(reverse=True)

lista = listaAN+listaPO

c = 0
print(f'[ ', end='')
for c in range(0,11):
    if c < 5:
        print(f'{lista[c]} < ', end='' )
        c += 1
    elif c != 10:
        print(f'{lista[c]} > ', end='')
        c += 1
    else:
        print(f'{lista[-1]}', end ='')
print(' ]')

# questão 38:
lista = []
for c in range(0,10):
    lista.append(int(input('Insira valores númericos \n')))
    print(sorted(lista))

# questão 39:
from math import factorial 
n = 5
for i in range(n): 
    for j in range(n-i+1): 
        print(end=" ") 
  
    for j in range(i+1): 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ") 
  
    
    print()

# questão 40:
from random import randint
l, c, m = [], [], []
for i in range(0,4):
    for j in range(0,4):
        c.append(randint(0,12))
    l.append(c.copy())
    c.clear()

for i in range(0,4):
    for j in range(0,4):
        if l[i][j] >= 10:
            m.append(l[i][j])
        print(f'|{l[i][j]:>2}| ',end='')
    print('')

print(m)

# questão 41:
l, c = [], []
for i in range(0,5):
    for j in range(0,5):
        if i == j:
            c.append(1)
        else:
            c.append(0)
    l.append(c.copy())
    c.clear()

for i in range(0,5):
    for j in range(0,5):
        print(f'|{l[i][j]}| ', end='')
    print('')

# questão 42:
l, aux = [], []
for i in range(1,6):
    for j in range(1,6):
        aux.append(i*j)
    l.append(aux[:])
    aux.clear()

for i in range(0,5):
    for j in range(0,5):
        print(f'|{l[i][j]:>2}| ',end='')
    print('')

# questão 43(4):
from random import randint

l, aux, mai = [], [], []
for i in range(0,5):
    for j in range(0,5):
        aux.append(randint(0,10))
    l.append(aux.copy())
    aux.clear()

for i in range(0,5):
    for j in range(0,5):
        print(f'|{l[i][j]:>2}| ',end='')
    print('')

for i in range(0,5):
        mai.append(max(l[i]))
print('')
print(mai)
print(max(mai))

# questão (5):
from random import randint


l, aux = [], []
for i in range(0,5):
    for j in range(0,5):
        aux.append(randint(0,10))
    l.append(aux.copy())
    aux.clear()

for i in range(0,5):
    for j in range(0,5):
        print(f'|{l[i][j]:>2}| ', end='')
    print('')
while True:
    try:
        x = int(input('Insira um número para buscarmos na matriz \n'))
        for i in range(0,5):
            for j in range(0,5):
                if x == l[i][j]:
                    print(f'O valor {x} está na linha {i+1}, coluna {j+1}')
        break
    except:
        print('ERRO: o valor informado não é válido')

# questão (6):
from random import randint


m1, m2, m3, aux1, aux2, aux3 = [], [], [], [], [], []

for i in range(0,4):
    for j in range(0,4):
        aux1.append(randint(0,10))
        aux2.append(randint(0,10))
    m1.append(aux1.copy())
    m2.append(aux2.copy())
    aux1.clear()
    aux2.clear()

for i in range(0,4):
    for j in range(0,4):
        if m1[i][j] > m2[i][j]:
            aux3.append(m1[i][j])
        else:
            aux3.append(m2[i][j])
    m3.append(aux3.copy())
    aux3.clear()

for i in range(0,4):
    for j in range(0,4):
        print(f'|{m1[i][j]:>2}| ',end='')
    print('')
print('')

for i in range(0,4):
    for j in range(0,4):
        print(f'|{m2[i][j]:>2}| ',end='')
    print('')
print('')

for i in range(0,4):
    for j in range(0,4):
        print(f'|{m3[i][j]:>2}| ',end='')
    print('')

# questão (7):
matrix, aux = [], []
for i in range(1,11):
    for j in range(1,11):
        if i < j:
            aux.append(2*i + 7*j - 2)
        elif i == j:
            aux.append(3*(i**2)-1)
        else:
            aux.append(4*(i**3)-5*(j**2)+1)
    matrix.append(aux.copy())
    aux.clear()

for i in range(0,10):
    for j in range(0,10):
        print(f'|{matrix[i][j]:>4}| ',end='')
    print('')

# questão (8):
from random import randint


matrix, aux = [], []
soma = 0
for i in range(0,3):
    for j in range(0,3):
        aux.append(randint(0,10))
    matrix.append(aux.copy())
    aux.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'|{matrix[i][j]:>2}| ', end='')
    print('')

for i in range(0,3):
    for j in range(0,3):
        if j > i:
            soma += matrix[i][j]
            
print(soma)

# questão (9):
from random import randint


matrix, aux = [], []
soma = 0
for i in range(0,3):
    for j in range(0,3):
        aux.append(randint(0,10))
    matrix.append(aux.copy())
    aux.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'|{matrix[i][j]:>2}| ', end='')
    print('')

for i in range(0,3):
    for j in range(0,3):
        if j < i:
            soma += matrix[i][j]

print(soma)

# questão (10):
from random import randint


matrix, aux = [], []
soma = 0
for i in range(0,3):
    for j in range(0,3):
        aux.append(randint(0,10))
    matrix.append(aux.copy())
    aux.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'|{matrix[i][j]:>2}| ', end='')
    print('')

for i in range(0,3):
    for j in range(0,3):
        if j == i:
            soma += matrix[i][j]

print(soma)

# questão (11): Diagonal secundária
matriz, aux = [], []
soma = 0
for i in range(0,3):
    for j in range(0,3):
        aux.append(i+j)
    matriz.append(aux.copy())
    aux.clear()

for i in range(0,3):
    soma = soma + matriz[i][(3-i-1)] #(3: linhas, i: iteráavel, -1, decréscio de ajuste)
    for j in range(0,3):
        print(f'{matriz[i][j]} ',end='')
    print('')

print(soma)

# questão (12):
matriz, aux = [], []

for i in range(0,3):
    for j in range(0,3):
        aux.append(2*i+j-1)
    matriz.append(aux.copy())
    aux.clear()        

for i in range(0,3):
    for j in range(0,3):
        print(f'{matriz[i][j]} ',end='')
    print('')
print('')
for i in range(0,3):
    for j in range(0,3):
        print(f'{matriz[j][i]} ',end='')
    print('')

# questão (13):
from random import randint


matriz, aux = [], []
for i in range(0,4):
    for j in range(0,4):
        aux.append(randint(0,20))
    matriz.append(aux.copy())
    aux.clear()

for i in range(0,4):
    for j in range(0,4):
        print(f'[{matriz[i][j]:>2}] ',end='')
    print('')
print('')

for i in range(0,4):
    for j in range(0,4):
        if j > i:
            matriz[i][j]= 0

for i in range(0,4):
    for j in range(0,4):
        print(f'[{matriz[i][j]:>2}] ',end='')
    print('')
print('')

# questão (14):
from random import randint


x, c = 0, 0
matriz, aux = [], []
for i in range(0,4):
    while c != 4:
        x = randint(0,99)
        if (x not in aux) and (x not in matriz):
            aux.append(x)
            c += 1
    matriz.append(aux.copy())
    aux.clear()
    c = 0

for i in range(0,4):
    for j in range(0,4):
        print(f'{matriz[i][j]:>2} ',end='')
    print('')
print('')

# questão (15):
import random


aux, gabarito = [], ('a', 'b', 'c', 'd')

alunos = {
    'ana':[],
    'beto':[],
    'carlos':[],
    'Lando':[],
    'Isaias':[]
}

respostas = ('a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'a', 'd')

resultado = {
    'ana':0,
    'beto':0,
    'carlos':0,
    'Lando':0,
    'Isaias':0
}

for i in alunos:
    for j in range(0,10):
        aux.append(random.choice(gabarito))
    alunos.update({i: aux.copy()})
    aux.clear()

for i in alunos:
    print(f'{i}: ',end='')
    for j in range(0,10):
        print(f'|{alunos[i][j]}| ',end='')
    print('')
print('')

c = 0
for i in resultado:
    for j in range(0,10):
        if respostas[j] == alunos[i][j]:
            c += 1
    resultado.update({i:c})
    c = 0

for i in resultado:
    print(f'{i}: {resultado[i]} acertos')

# questão (16):

# questão (17):

# questão (18):

# questão (19):

# questão (20):

# questão (21):

# questão (22):
from random import randint

def printer(lista):
    for i in range(0,3):
        for j in range(0,3):
            print(f'|{lista[i][j]:>2}| ',end='')
        print('')
    print('')



A, B, C, aux, aux2, aux3 = [], [], [], [], [], []

for i in range(0,3):
    for j in range(0,3):
        aux.append(randint(0,10))
        aux2.append(randint(0,10))
    A.append(aux.copy())
    B.append(aux2.copy())
    aux.clear()
    aux2.clear()
 
for i in range(0,3):
    for j in range(0,3):
        aux3.append(A[i][j] * B[i][j])
    C.append(aux3.copy())
    aux3.clear()
    
printer(A)
printer(B)
printer(C)

# questão (23):
from random import randint


A, B, aux = [], [], []

def gerarM(matriz):
    aux = []
    for i in range(0,3):
        for j in range(0,3):
            aux.append(randint(0,10))
        matriz.append(aux.copy())
        aux.clear()



def printer(lista):
    for i in range(0,3):
        for j in range(0,3):
            print(f'|{lista[i][j]:>3}| ',end='')
        print('')
    print('')

gerarM(A)

for i in range(0,3):
    for j in range(0,3):
        aux.append(A[i][j] * A[j][i])
    B.append(aux.copy())
    aux.clear()


printer(A)
printer(B)

# questão (24):

# questão (25):
"""
