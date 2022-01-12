"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave':'valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados
    - Podemos usar qualquer tipo de dados como chaves de dicionário, inclusive outros dicionários

# Criação de dicionários

# Forma 1 (Mais comun)
paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 2 (Menos comun)
paises = dict(br='Brasil',eua='Estados Unidos', py='Paraguay')

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))

# OBS: caso o método get não encontre o objeto com a chave informada, ele retornará o valor None

Exemplo:

pais = paises.get('ru')
if pais:
    print('Encontrei o país')
else:
    print('Não encontrei o país')

Exemplo 2: Podemos definir um valor padrão para caso não encontramos o objeto para a chave informada
pais = pais.get('ru', 'Não encontrado')

Exemplo 3: Ele busca pelas chaves e não pelo valor
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

saída:
True
True
False

Exemplo 4: tupla como chave de dicionário
localidades = {
    (35, 6895, 39.5917): 'Escritório em Tókio',
    (40, 7126, 74.0060): 'Escritório em Nova York',
    (37, 7749, 122.4194): 'Escritório em São Paulo'
}

# Adicionando elementos em um dicionário

receita = {'jan':100, 'fev':120,'mar':300}

#Forma 1
receita['abr']= 350

#Forma 2
novo_dado = {'mai':500}
receita.update(novo_dado) 
#é o mesmo que: 
receita.update({'mai':500})

# Atualizando dados em um dicionário

#Forma 1
receita['mai']=500

#Forma 2
receita.update({'mai':500})

# CONCLUSÃO 1: A forma de adicionar novos elementos e atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2:  Em dicionários, Não podemos ter chaves repetidas.

# Remover dados de um dicionário
receita = {'jan':100, 'fev':120,'mar':300}

# Forma 1
receite.pop('mar')

OBS 1: É necessário sempre passar a chave
OBS 2: Ao remover um objeto, o valor deste objeto é sempre retornado

# Forma 2
del receita['fev']
print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado

Exemplo de uso dos dicionários:
carrinho = []

produto1 = {'nome':'Playstation 4', 'qtd':1,'preço':2300.00}
produto2 = {'nome':'God of war 4', 'qtd':1,'preço':150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

# Limpar o dicionário (zerar dados)
d.clear()

# Copiando um dicionário para outro

# Forma 1: Deep copy
novo = d.copy()

# Forma 2: Shallow copy
novo = d

novo['d']=4
print(d)
print(novo)

# Forma não usual de criação de dicionários, usando o método fromkeys

O método fromkeys recebe dois parâmetros: um interável e um valor.
Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

# Exemplo 1:
# A chave 'a' possui o valor 'b'

outro = {}.fromkeys('a', 'b')
print(outro)

# Exemplo 2:
# As chaves serão os dados da lista, o valor será repassado para todas as chaves

usuario = {}.fromkey(['nome','pontos','profile'],'desconhecido')
print(usuario)

# Exemplo 3:
veja = {}.fromkeys('teste','valor')
print(veja)

saida:
{'t': 'valor', 'e': 'valor', 's': 'valor'}

# O Range também funciona perfeitamente com os dicionários
# Exemplo:
veja = {}.fromkeys(range(1,11),'novo')
print(veja)

# Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

receita = {'jan':100, 'fev':250,'mar':400}

# Interar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves
# Forma Pythonica
for chave in receita.key():
    print(receita[chave])

# Acessando os valores
# Forma Pythonica
for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""