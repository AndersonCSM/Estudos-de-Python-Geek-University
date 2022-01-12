"""
# Módulo Collections
Collections -> High-performance Container Datetypes


# Counter (Contador)
Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada, e o valor sendo a quantidade de ocorrências desse elemento.

# Utilizando o Counter

Exemplo 1:
from collections import Counter

# Podemos utilizar o counter com qualquer interável, aqui foi usado uma lista
lista =[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9, 9, 10]

res = Counter(lista)
print(type(res))
print(res)

# Saída:
# <class 'collections.Counter'>
# Counter({4: 4, 1: 3, 2: 3, 3: 3, 5: 2, 9: 2, 6: 1, 7: 1, 8: 1, 10: 1})
# Cada elemento único da lista foi definida como chave e contou a quantidade de ocorrência daquele elemento

# Exemplo 2:
from collections import Counter

print(Counter('Geek University'))
# Saída: Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3:
from collections import Counter

texto = ''''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised
in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum.
'''

palavras = texto.split()
res = Counter(palavras)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

# Defaultdict

# Recapitulando dicionários
dicionario = {'Curso':'Programação em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) #KeyError

Defaultdict -> Ao criar um dicionário utilizando-o, nós passamos um valor default.
podemos utilizar um lambda para isso. Esse valor será usado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, a chave será criada e o valor default será atribuido.

# OBS: Lambdas são funcões sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python é essencial'

print(dicionario)
print(dicionario['outro'])
print(dicionario)

# Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5}
for chave, valor in dicionario,items():
    print(f'chave={chave}:valor={valor}')

# Exemplo:
from collections import OrderedDict
dicionario = OrderedDict({'a':1,'b':2,'c':3,'d':4,'e':5})
 
for chaves, valor in dicionario.items():
    print(f'chaves={chaves}, valor={valor}')

# Entedendo a diferença entre Dict e Ordered Dict

# Dicionários comuns
dic1 = {'a'=1,'b'=2}
dic2 = {'b'=2,'a'=1}
print(dict1 == dict2) # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict
odict1= OrderedDict({'a'=1,'b'=2})
odict2 = OrderedDict({'b'=2,'a'=1})
print(odict1 == odict2) # False -> A ordem dos elementos é diferente

# Named Tuple

# Recap tupla
tupla = (1,2,3)
print(tupla{[1])

Named Tuple -> São tuplas, diferenciadas, onde especificamos um nome para a mesma e também parâmetros.

from collections import namedtuple
# Precisamos definir o nome e parâmetros.
# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração Named Tuple (Forma preferível por ser mais fácil de entender)
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando
ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados
# Forma 1
print(ray[0]) #idade
print(ray[1]) #raça
print(ray[2]) #nome

# Forma 2
print(ray.idade) #idade
print(ray.raça) #raça
print(ray.nome) #nome

# Deque
O Deque é uma lista de alta performance, logo seu funcionamento é idêntico

from collections import deque
deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona o elemento normalmente
deq.appendleft('k') # Adiciona o elemento a esquerda

# Removendo elementos
deq.pop()
deq.popleft()

"""
