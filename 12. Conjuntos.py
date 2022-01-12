""""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática

- No Python, os conjuntos são chamados de Sets

Como na matemática:
- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados

Os conjuntos são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor

# Definindo um conjunto:
# Forma 1: usando o método set, pode modificar outros tipos de variáveis
s = set({1, 2, 3, 4, 5, 5, 6, 8, 2, 3}) # Repare que temos valores repetidos
print(s)

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro.

# Forma 2: Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)

# Assim como as outras coleções, os Sets permitem tipos de dados diferentes

# Iterando um set normalmente
s = {1, 'b', True, 34.22, 44}

for valor in s:
    print(valor)

Exemplo de uso: contar o número de cidade e as cidades únicas

cidades = ['São Paulo','Campo Grande','Belo Horizonte','Cuiaba','São Paulo','Cuiaba']
print(len(cidades)) # quantidade de cidades por visitantes
print(len(set(cidades))) # Cidades únicas

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4) #Duplicidade não gera erro, só é ignorado
print(s)

# Remover elementos em um conjunto
# Forma 1
s = {1, 2, 3}
s.remove(3) # Não é índice, mas sim o valor a ser removido
print(s)

# OBS: caso o valor não exista, irá apresentar erro.

# Forma 2
s = {1, 2, 3}
s.discard(2)
print(s)

# Obs: Se o valor não existir, não é gerado erro.

# Copiando um conjunto para outro
s = {1, 2, 3}

# Forma 1 - Deep copy
novo = s.copy()
novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy
novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine dois conjuntos de estudantes de programação
python = {'Ana','Pedro','Guilherme','Gustavo','João'}
java = {'Fernanda','Gustavo','Ana','Henrique'}

#União de dois conjuntos 
# Gerando um conjunto com nomes únicos dos estudantes, 

# Forma 1 - Union(U) (Mais recomendado)
unicos1 = python.union(java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe (|)
unicos2 = python | java
print(unicos2)

# intersecção dos conjuntos
# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = python.intersection(java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = python & java
print(ambos2)

# Elementos únicos de um conjunto
# Gerar um conjunto de estudantes que não estão no outro curso
so_python = python.difference(java)
print(so_python)

so_java = java.difference(python)
print(so_java)

# Soma*, Valor máximo*, Valor mínimo*, tamanho
# * Se os valores forem todos inteiros ou reais
s = {1 ,2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""
