# Aula 26: Loop for (para)
'''
Loop -> Estrutura de repetição
Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Anderson'
- Lista
    lista = []
- Range
    numeros = range[1,10]

Sintaxe:
c = variável de controle
for c in interavel:
    Execução do Loop

EX: Iterando em uma String 
# como String é uma lista de caracteres
nome = 'Geek University'
for letra in nome:
    print(letra)

EX 2: Iterando sobre uma lista
lista = [1, 3, 5, 7, 9]
for numero in lista:
    print(numero)

EX 3: iterando sobre um range
# range(valor_inicial, valor_final) OBS: o valor final não é incluso.
for numero in range(1,10):
    print(numero)

EX 4:
nome = 'Geek University'
for i, v in enumerate(nome):
    print(f'indice: {i}, letra:{v}')

EX 5:
OBS: quando não precisamos de um valor, podemos descartá-lo usando um underline(_)
nome = 'Geek University'
for _, v in enumerate(nome):
    print(v)

EX 6: Resgatar uma informação específica.
o (i) será a informação específica.
    -se digitarmos 0, irá resgatar o índice da letra 
    -se digitarmos 1, será o valor, logo o caractere armazenado
nome = 'Geek University'
for v in enumerate(nome):
print(v[i], end='')    

DICA: É possível concatenar Strings no Python, bem como multiplicar Strings.
nome = 'Geek'
nome + ' University'
nome * 3

DICA: a contrabarra (\) é um caractere de escape, sendo usado no String para que algum elemento seja desconsiderado

# Aula 27: Entedendo e explorando ranges
Ranges

- Precisamos conhecer o loop para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas, definidas e específica.

# Forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusivo (inicio padrão 0, e passo de 1 em 1)
for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não incluso (inicio especificado pelo usuário, e passo de 1 em 1)
for num in range(4, 11):
    print(num)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não incluso (inicio especificado pelo usuário, e passo especificado pelo usuário)
for num in range(5, 50, 5):
    print(num)

# Forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não incluso (inicio especificado pelo usuário, e passo especificado pelo usuário)
for num in range(10, 0, -1):
    print(num)

# Aula 28: Loop While
Forma geral

While expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Boolana é toda expressão onde o resultado é True or False.

EX:
numero = 1

while numero < 10:
    print(numero)
    numero += 1

OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

# Aula 29: saindo de loops com break
Funciona da mesma forma que nas linguagens C ou Java
Utilizamos o break para sair de loops de maneira projetada.

EX 1:
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('fim')

EX 2:
while True:
    comando = input('Digite \'sair\' para sair').lower().strip()
    if comando == 'sair':
        break
print('fim')
'''