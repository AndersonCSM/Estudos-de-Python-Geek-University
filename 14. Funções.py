"""
# Definindo Funções

- Funções são pequenos trechos de código que realizam uma tarefa especifica ou repetitiva.
- Pode ou não receber entradas de dados e retornar um saída de dado;
- Muito útil para executar uma ação que se repete.

OBS: Se você escrever uma função que realiza várias tarefas, é bom fazer uma revisão para que a função seja simplificada.


Algumas funções já utilizadas:
- print()
- len()
- max()
- min()
- count()

OBS: funções são facilmente identificadas devido ao uso dos parênteses

# Exemplo de utilização de funções:
cores = ['verde','azul', 'branco']

# Utilizando uma função integrada (Built-in) do Python print()
print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself - Não repita você mesmo / não repita seu código.

Em python, a forma geral de definir uma função é

def nome_da_função(parâmetros_de_entrada)"
    bloco_de_função

Onde:
nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece
Neste bloco, pode ter ou nào retorno da função.

OBS: Para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função.
Também abrimos o bloco de código com o já conhecido dois pontos : que é usado em Python para definir blocos.

# Definindo a primeira função
def diz_oi():
    print('oi')

# Chamada de execução
diz_oi()

OBS:
1 - Dentro das nossas funções podemos utilizar outras funções;
2 - Nossa função executa apenas 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - A função não recebe nenhum parâmetro de entrada;
4 - A função retornada nada.

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

oi = diz_oi
oi()

# Não recomendado, pois pode deixar o código confuso.

# Funções com retorno

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar valores com a palavra reserva return
OBS: Não é necessário criar uma variável para retorno de uma função

OBS: sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, sai do execução da função;
2 - Podemos ter, em uma função, diferentes returns, mas a função só retornará um;
3- Podemos, em uma função, retorna qualquer tipo de dado e até mesmo múltiplos valores.

# EX 1:
def quadrado_de_7():
    print(7**2)

ret = quadrado_de_7()
print(f'O retorno da função é {ret}')
# A função não retorna nada, ela usa a função print para imprimir

# Vamos refatorar(Re-escrever) esta função para que ela retorne um valor
def quadrado_de_7():
    return 7**2

ret = quadrado_de_7()
print(f'O retorno da função é {ret}')

# refatorando a primeira função
def diz_oi():
    return 'oi '

alguem = 'Pedro'
print(diz_oi()+ alguem)

# EX 2: diversos returns 
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# EX 3: retornando vários valores
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print(outra_funcao())

# EX 4: Função para jogar uma moeda

from random import random


def jogar_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(f'O resultado de jogar a moeda foi {jogar_moeda()}')

# Podemos importa a função jogar_moeda em outros arquivos.
# from 14.Funções import jogar_moeda

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.
# EX 5: errado
def eh_par():
    numero = 6
    if numero % 2 != 0:
        return True
    else: # else desnecessáro
        return False
    
print(eh_par())

# EX 5: certo
def eh_par():
    numero = 6
    if numero % 2 != 0:
        return True
    return False
    
print(eh_par())

# Funções com parâmetro

# Funções podem ter n parâmetos de entrada, ou seja, várias entradas.
# EM uma função com diversos parâmetros, estes são separados por vírgula
# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(6))
print(quadrado(7))

print(quadrado()) # TypeError, não foi passado um parâmetro

Ex 1:
def soma(a, b): (a, b) -> parâmetros da função soma
    return a+ b

def multiplicar(a, b):
    return a * b

def outra(a, b, msg):
    return (a+b) * msg

print(soma(2,3)) -> (2,3) argumento da função soma
print(multiplicar(10,5))
print(outra(1, 2, 'Geek '))

# OBS: Se a gente informar um número errado de parâmetro ou argumento, teremos TypeError

# A diferença entre parâmetros e Argumentos
- Parâmetros são variáveis declaradas na definição de um função;
- Argumentos são dados  passados durante a execução de um função;

# A ordem de precêdencia dos argumentos influência na função, pois os argumentos assumirão o valor dos parâmetros.
# Caso utilizemos nomes dos parâmetros nos argumentos, podemos utilizar qualquer ordem.
def nome_completo(nome, sobrenome):
    return f'{nome} {sobrenome}'

print(nome_completo(nome='Anderson', sobrenome='Carlos'))
print(nome_completo(sobrenome='Carlos', nome='Anderson'))

# Funções com Parâmetro Padrão (Default parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Por quê utlizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parêmtros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código.

# Quais tipos de dados podemos utilizar com valores default para parâmetros?
- Qualquer tipo de dado:


# EX 1: exemplo de uma função em que a passagem de parâmetro é opcional.
print('Geek University')
print()

# EX 2: exemplo de função em que a passagem de parâmetro é obrigatório.
def quadrado(numero):
    return numero ** 2

print(quadrado(2))

# EX 3:
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # Eleva a potência que o usuário informa
print(exponencial(3)) # Por padrão eleva ao quadrado

# OBS: se o usuário repassar apenas um argumento, este será atribuido ao parâmetro número.
# OBS: se o usuário passar 2 argumentos, o primeiro será o número e o segundo o parâmetro potência. Então será calculada a está potência.

# OBS: Os parâmetros default (padrão) devem sempre estar no final da declaração
# ERRO:
def teste(num=0, potencia):
    return num ** potencia

print(teste(3))

# EX 4:
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo Instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

# EX 5: função que retorna outra função
def soma(a, b):
    return a + b

def mat(a, b, fun=soma):
    return fun(a, b)

def subtracao(a, b):
    return a - b

print(mat(1, 2))
print(mat( 1, 2, subtracao))

# Escopo de variáveis: evitando problemas

# Se tivermos uma variável local com o mesmo nome de uma variável global. A local terá prefêrencia sobre a global
# A variável local só existe dentro do bloco que foi declarada

# ATENÇÃO: evite usar variáveis globais se puder.

EX 6:
instrutor = 'Geek' # variável global

def diz_oi():
    instrutor = 'Python' # variável local
    return f'OI {instrutor}'

print(diz_oi())

# EX 7:
total = 0
def incrementa():
    global total

    total += 1
    return total

incrementa()
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador # Uma variável que não é local e nem global, é da função anterior

        contador = contador +1
        return contador
    return dentro()


print(fora())
print(fora())
# print(dentro()) # erro, ela é desconhecida fora da função fora

# Docstrings
- Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial __doc__ ou a função help().

EX 01:
def diz_oi():
    '''
    Uma função simples que retorna a string 'Oi!'
    '''
    return 'Oi!'

print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)

EX 02:
def exponencial(numero, potencia=2):
    '''
    Função que retorna por padrão o quadrado do número, ou o produto da potencia informada
    :param numero: base do expoente
    :param potencia: expoente do número, por padrão é 2
    : retunr: retorna o exponecial do 'número' na 'potência'
    '''
    return numero ** potencia

# Entendendo o *args
- O *args é um parâmetro. Isso significa que você poderá chamar de qualquer coisa, desde que comece com asterisco.

EX:
*xis
Por convenção, utilizamos *args para defini-lo

Mas o que é o '*args?'
O parâmetro *args utilizando em uma função, coloca os argumentos extras que foram informados como entrada em uma tupla.

EX 01:
def soma(num1,num2,num3):
    return num1+num2+num3

Na função definida teriamos problema, caso fosse repassado mais de três valores ou menos de três.

# Entendendo *args
def soma(*args):
    return sum(args)

print(soma(1,2,3,4))
print(soma(1,2,3,4,5))
print(soma(1,2,3,4,5,6))

# Podemos mesclar o uso de parâmetros obrigatórios e o *args
def soma(nome, emai, *args):
    retunr sum(args)

# EX 02:
def verifica(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'

print(verifica())
print(verifica(True, 'University' ))
print(verifica('Geek','University'))

# ex 03:
def soma(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5]
print(soma(*numeros))

# OBS: O asterisco(*) serve para informar ao Python que estamos passando uma lista como argumento. 
# Desta forma, ele saberá que é necessário desempacotar os dados da lista.

# **kwargs

Poderiamos chamar este parâmetro de **xis, mas por conveção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que adiciona valores extras em uma tupla, o **kwargs exige que
utilizamos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

# EX 01:
def cores(**kwargs):
    for k, v in kwargs.items():
        print(f'A cor favorita de {k.title()} é {v}')

cores(marcos='verde', julia='preto', fernanda='azul', vanessa='branco')

# OBS: os parâmetros *args e **kwargs não são obrigatórios.
cores()
cores(geek='musgo')

# Nas nossas funções, podemos ter (NESTA ORDEM):
1- parâmetros obrigatórios;
2- * args
3- Parâmetros default (não obrigatório)
4- ** kwargs

# EX 02: ORDEM DE PRECEDÊNCIA DOS ARGUMENTOS
def funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    print()

funcao(8, 'julia')
funcao(18, 'felas', 4, 5, 3, solteiro=False)
funcao(34, 'Felipe', eu='não', você='vai')

# Desempacotando com **kwargs
def mostra(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {'nome':'felicity', 'sobrenome':'Jones'}

print(mostra(**nomes))

# OBS: OS nomes das chaves do dicionário devem ser os mesmos dos parâmetros da função

"""

