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
    
"""