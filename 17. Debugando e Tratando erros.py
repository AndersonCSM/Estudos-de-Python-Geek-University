"""
### Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros gerdas pela execução

OBS: Exceptions e Erros são sinônimos na programaçãO.

# Os erros mais comuns:

1- SyntaxError -> Erro na sintaxe. Ou seja, foi escrito algo que o Python não reconhece como parte da linguagem
EX A: 
def funcão: # falta de parênteses na definição da função
    print('Olá')

EX B:
None = 1 # None é uma palavra reservada da linguagem

EX C:
return # return é usando dentro de uma def

2- NameError -> Quando uma variável ou função não foi definida.
EX A:
print(geek) # geek não foi definido

EX B:
geek() # a função geek() não existe

3- TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
EX A:
print(len(5)) # A função len recebe um tipo iterável, não inteiro

EX B:
print('Geek'+[]) # Não podemos concatenar parâmetros de tipos diferentes

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado usando um índice inválido.
EX A:
lista=['Geek']
print(lista[1]) # não existe elemento no índice 1

5- ValueError -> Ooorre qunaod uma função/operação built-in (integrada) recebe um argumento com tipo correto, mas com valor inapropriado.
EX A:
print(int('Geek')) # O cast int() espera receber um valor conversível em int.

6- KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave inexistente.
EX A:
dic = {}
print(dic['geek']) # A chave geek não existe

7- AttributeError -> Ocorre quando uma variável não tem um atributo/função.
EX A:
tupla = (1,11,3,4)
print(tupla.sort()) # a função .sort() é aplicável somente em listas

8- IndentationError -> Ocorre quando não é respeitado a indentação do Python (4 espaços)
EX A:
def nova():
print('Geek') # Falta de indentação 

### Levantando os próprios erros com raise

raise -> lança exceções

OBS: O raise não é uma função, é uma palavra reservada.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:
raise TipoDoErro('Mensagem de erro')

#EX01:
raise ValueError('Valor incorreto')

#EX02:
def colore(texto, cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek','azul')
colore('Geek',5)

### Debugando código com Python Debugger(PDB)
PDB -> Python Debugger

# OBS: A utilização do print() para debugar código é uma prática ruim.

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# A partir do Python 3.7, não é preciso importar a biblioteca, pois o PDB foi incorporado como uma função built-in chamada
breakpoint()

#OBS: cuidado com conflitos entre nomes de variáveis e os comandos do PDB, evite criar variáveis com os mesmos comandos do PDB.

# Comandos básicos do PDB/breakpoint()
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

# EX01:
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + '' + sobrenome
curso = 'Programação em Python'
print(nome_completo + ' faz o curso de ' +curso )

# EX02:
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + '' + sobrenome
curso = 'Programação em Python'
print(nome_completo + ' faz o curso de ' +curso )

# O motivo para usar essa nomenclatura para usar o PDB é por se trata de uma ferramenta de desenvolvimento, após seu uso não é mais necessária e por
isso pode ser excluida, para facilitar a exclusão deixamos o import agrupado ao uso do PDB.

"""