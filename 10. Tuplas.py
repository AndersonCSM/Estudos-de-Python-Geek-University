""""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla 1 = (1, 2, 3, 4, 5, 6)
# Ambos vão criar tuplas
tupla2 = 1, 2, 3, 4, 5, 6

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
tupla4 =(4,) # Isso é uma tupla!

# Conclusão: Podemos concluir que tuplas são definidas pelo uso da vírgula e não pelo uso de parênteses

(4) -> não é tupla
(4,) -> é tupla
4, -> é tupla

# Podemos gerar uma tupla dinamicamente com range(inicio ,fim, passo)
tupla = tuple(range(11)) # Função tuple

# Desempacotamento de tuplas
tuplas = ('Geek Univeristy', 'Programação em Python')
escola, curso = tupla

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos e variáveis para desempacotamento.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.
# Soma*, Valor máximo, valor mínimo* e Tamanho
# * se os valores forem todos inteiros ou reais
tuplas = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1 + tupla2) # Tuplas são imutáveis

tupla3 = tupla1 + tupla2

tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores
# Ou então podemos fazer:
tupla1 += tupla2
print(tupla)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for i, v in enumerate(tupla):
    print(i, v)

# Contando elementos dentro de uma tupla
tupla = 'a', 'b', 'c', 'a'
print(tupla.count('c'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

# O acesso a elementos de uma tupla também é semelhante a de uma lista 
dias = 1, 2, 3, 4, 5, 6, 7
print(dias[0])

# Iterar com while
i = 0

while i < len(dias):
    print(dias[i])
    i += 1

# Verificamos em qual índice um elemento está na tupla
print(dias.index(6))

# OBS: caso o elemento não exista, será gerado ValueError

# Slicing
tupla[inicio:fim:passo]

# Por quê utilizar tuplas?

1 - Tuplas são mais rápidas do que listas.
2 - Tuplas deixam seu código mais seguro*.

* Isso porque trabalhar com elementos imutáveis trás segurança para o código.

# Copiando uma tupla para outra
tupla = (1 ,2, 3)
nova = tupla # Na tupla não temos problemas de Shallow Copy
"""