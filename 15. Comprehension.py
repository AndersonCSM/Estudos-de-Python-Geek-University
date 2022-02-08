'''
### List Comprehension
- Utilizando List Comprehension podemos gerar uma lista com dados processados a partir de outro iterável

# Sintaxe da List Comprehension
[ dado for dado in iterável ]

# EX 01:
numeros = [1,2,3,4,5]

res = [numero * 10 for numero in numeros]
print(res)

# Entedendo melhor o que está acontecendo, dividindo em duas partes:
- Primeira parte: for numero in numeros
- Segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)

# EX 02:
numeros = [1,2,3,4,5]

def funcao(valor):
    return valor * valor

print(f'{[funcao(numero) / 2 for numero in numeros]}')

# List Comprehension x Loop
# Loop
numeros = [1,2,3,4,5]
numerosd = []

for numero in numeros:
    numerosd.append(numero * 2)
print(numerosd)

### List Comprehension
numeros = [1,2,3,4,5]
print([numero * 2 for numero in numeros])

# Outros exemplos de uso
# EX 03:
nome = 'Geek University'
print([letra.upper() for letra in nome])

# EX 04:
def caixa_alta(nome):
    return nome.replace(nome[0], nome[0].upper())


amigos = ['maria','julia','pedro','vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# EX 05:
print([numero * 3 for numero in range(1,10)])

# EX 04:
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# EX 05:
print([str(numero) for numero in [1, 2, 3, 4, 5]])

### List Comprehension parte II

-Podemos também adicionar estruturas condicionais lógicas às nossas List Comprehension

# EX 01:
numeros = [1,2,3,4,5]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# refatorando

# Qualquer número par, o resto da divisão por 2 é 0, no Python, 0 é False. Assim not False = True
# O uso do not é para negar, assim apenas os que são False(pares) se tornarão verdadeiros e serão impressos
pares = [numero for numero in numeros if not numero % 2]

# Qaulquer número ímpar, o resto da divisão por 2 é 1, em Python 1 é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# EX 03
numeros = [1,2,3,4,5]

res = [numeros * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

### Dictionary Comprehension
Pense no seguinte

Se quisermos criar uma lista fazemos:
lista = [1,2,3,4]

Se quisermos uma tupla:
tupla = (1,2,3,4)

Se quisermos um set:
conjunto={1,2,3,4}

Se quisermos um dicionário:
dicionario = {'a':1, 'b':2, 'e':3, 'd':4}

# Sintaxe para um dicionário
{chave:valor for valor in iterável}

# sintaxe das listas
[valor for valor in iterável]

# EX 01:
dicionario = {'a':1, 'b':2, 'e':3, 'd':4,'e':5}
quadrado = {chave:valor **2 for chave, valor in dicionario.items()}
print(quadrado)

# EX 02: Adicionando valores de uma lista como chave, e elevando o valor ao quadrado
numeros = [1,2,3,4]
quadrado = {valor: valor**2 for valor in numeros}
print(quadrado)

# EX 03: Adicionando chaves e valores a um dicionário
chaves='abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# EX 04: Usando lógica condicional
numeros=[1,2,3,4,5,6]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

### Set Comprehension

Lista = [1,2,3,4,5]
Set = {1,2,3,4,5}

# EX 01:
numeros = {num for num in range(1,7)}
print(numeros)

# EX 02:
numeros = {x**2 for x in range(10)}
print(numeros)

# Gerando um dicionário do código acima:
numeros = {x: x**2 for x in range(10)}
print(numeros)

# EX 03:
letras = {letra for letra in 'Geek University'}
print(letras)

'''
