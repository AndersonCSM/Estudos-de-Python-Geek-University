'''
Listas em Python funcionam como vetores/matriz (arrays) em outras linguagens, 
com a diferença de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguahgens C/Java: Arrays:
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se vocÊ criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteior e poderá ter sempre no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representados por colchetes: []

Nas listas, acessos os elementos de forma indexada

podemos criar uma lusta usando o método list()

lista = [1, 2, 4, 6, 7, 0, 59, 30]

lista2 = ['a', 'b', ' ', 't', 'v']

lista3 = []

lista4 = list(range(11)) # gera uma lista de 0 à 10 usando a ferramenta list

lista5 = list('Geek University')

# Podemos facilmente checar se um determinado valor está contido em uma lista
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(F'Não encotrei o número {num}')

# Podemos facilmente ordenar uma lista usando o método .sort():
lista.sort()
print(lista)    

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista.count(1))
print(lista5.count('e'))

# Adicionar elementos em uma lista
OBS: Para adicionar elementos em listas, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar 1 elementos por vez
lista.append(42)
print(lista)

# Podemos adicionar listas dentro de outras listas.
lista.append([4, 5, 10]) # Coloca a lista como um único elemento (sublista)

# Adicionando diversos valores de uma lista à outra lista
lista.extend([123, 44, 67]) # Coloca cada elemento da lista como um valor adicional a lista

# Podemos inserir um novo elemento na lista infomrando a posição do índice
OBS: isso não substitui o valor ocupado pelo índice, o mesmo será deslocado para direita
lista.insert(2, 'novo valor')
print(lista)

# Podemos facilmente juntar duas listas
lista6 = lista + lista2
lista = lista + lista2
# é a mesma coisa do que usando o extend:
lista.extend(lista2)
print(lista)

# Podemos inverter uma lista
lista.reverse()
print(lista)
# Também podemos usar o fatiamento para inverter
print(lista[::-1])

# Copiar uma lista
lista7 = lista2.copy()
print(listaa7)

# Contar a quantidade de elementos de uma lista, usando o len()
print(len(lista))

# Podemos remover o último elemento de uma lista
# Além de remover o último elemento, mas também retorna-o
print(lista)
lista.pop() 
print(lista)

# Podemos remover um elemento pelo índice
# Os elementos a direita do índice serão deslocados a esquerda
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos da lista (zerar a lista)
print(lista5)
lista3.clear()
print(lista5)

# Podemos repetir elementos de uma lista
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista
# Exemplo 1:
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2: O separador é uma vírgula
curso = 'Programação, em, Python:, Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma String
lista6 = ['Programação','em','Python:','Essencial']
curso = ' '.join(lista6) # adicionando espaços entre cada elemento da lista
print(curso)

# Iterando sobre listas
# Exemplo 1: Utilizando for
soma = ''
for elementos in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2: Utilizando While
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair')
    produto = input()
    if produto != 'sair': # Era para ter um laço com break, mas por alguma bruxaria não precisa
        carrrinho.append(produto)

for produto in carrinho:
    print(produto)

# Podemos acessar os índices de maneira inversa
cores = ['verde','amarelo','azul','branco']
print(core[-1]) # Branco
print(cores[-4]) # verde
print(cores[-5]) # Erro, não existe

# Gerar um índice em um for
for indice, cor in enumerate(cores): #enumerate gera variáveis para índice e para o dado
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(32)
lista.append(32)
print(lista)

# Outros métodos não tão importantes mas também úteis
# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 9, 5, 8, 9, 7, 10]

# Em qual indice está o valor 6?
print(numeros.index(6))

# OBS: Caso não tenha este elemento na lista, irá apresentar erro

# OBS: Retorna o índice do primeiro elemento encontrado
print(numero.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # buscando a partir do índice 1
print(numeros.index(5, 2)) # buscando a partir do índice 2

# Podemos buscar dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o índice do valor 8 entre os índices 3 e 6

# Revisando o slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro "inicio"
lista = [1, 2, 3, 4]
print(lista[1:])

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2]) # começa em 0, pega até o índice 2-1=1

# Trabalhando com slice de lista com o parâmetro "passo"

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2
print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Forma Pitônica
nomes.reverse()
print(nomes)

# Soma*, valor máximo*, valor mínimo*, tamanho
* - Se os valores forem todos inteiros ou reais.
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) # soma dos valores
print(max(lista)) # maior valor
print(min(lista)) # menor valor
print(len(lista)) # tamanho da lista

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
# OBS: se tivermos um número diferente de elementos da lista e variáveis para receber, teremos um erro.

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow copy e Deep copy)
# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Ao utilizar lista.copy() copiamos os dados de uma lista para outra, sem criar uma ligação, de maneira que
ambas as listas são totalmente independentes, ou seja, alterar uma não afeta a outra. Isso em Python é chamado de 
Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# Realizamos uma cópia utilizando atribuição, ou seja, copiamos os dados de uma lista para outra atribuindo, porém
nessa foram de modificação é criado uma ligação entre as listas, assim, quando se modifica qualquer uma das listas, irá impactar a outra.
No Python isso é chamado de Shallow Copy.

# Para contornar isso podemos usar o slice
lista = [1, 2, 3]
print(lista)

nova = lista[::]
print(nova)

nova.append(4)
print(lista)
print(nova)

'''
