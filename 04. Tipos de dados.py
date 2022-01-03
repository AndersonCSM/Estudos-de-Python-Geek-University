'''
# No Python não existe limite para um valor númerico, ele armazenar o número até o quando de memória estiver disponível

# É possível definir um número com diversas casas de milhar usando underline
1_000_000 == 1000000

# Podendo ser usado qualquer operador aritmético(* / - +)
num += 1 == num = num + 1

# Operações aritméticas: no Python podemos realizar as operações tanto no terminal Python, como dentro do programa, como em áreas internas dos módulos.
1- soma: + print(1+1) = 2
2- subtração: - print(1-1) = 0
3- multiplicação: * num = 2*5 = 10
4- exponenciação: ** print(3**2) = 9
5- divisão: / print(5/2) = 2.5
6- divisão inteira: // print(5//2) = 2 outro modelo antigo de realizar a mesma operação: print(int(5/2))
7- Resto da divisão: % print(5%2) = 1

# É possível identificar o tipo da variável(classe) usando a função type()
num = 42
type(num) = <class 'int'>

# Aula 16: Tipo Float
# Tipo real, decimal

OBS: O separador de casas decimais é o ponto(.) e não vírgula.

# É possível declarar mais de uma variável em apenas uma linha
valor1, valor2 = 1, 44
print(valor1) = 1
print(valor2) = 44

# Todas as operações com os inteiros é possível com os flutuantes

# Podemos converter um float para um int.
OBS: Ao converter valores float para inteiros, perdemos precisão
valor = 1.44
print(int(valor)) = 1
print(type(valor)) = int

# É possível trabalhar com números complexos dentro do Python. Basta adicionarmos um j ao número
num = 5j
type(num) = complex

# Aula 17: Tipo Booleano
Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso
True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

# Operações básicas

# Negação (not):
print(not True): False

# Ou (or):
É uma operação binária, depende de dois valores. Ou um ou outro deve ser verdadeiro.
True or True = True
True or False = True
False or True = True
False or False = False 

# E (and):
Também é uma operação binária, depende de dois valores. Ambos os valores devem ser verdadeiros.
True and True = True
True and False = False
False and True = False
False and False = False 

# Aula 18: Tipo String
Em Python, um dado é considerado do tipo String sempre que:
- Estiver entre aspas simples, duplas, simples triplas, duplas triplas;
'uma String','43','True','a','42.3'

- Usar aspas simples dentro de um texto, alternandos o uso das aspas para usa-las adequadamente
nome = "Gina's Bar"

- Quebra de linha
nome = 'Angelina \n Julie' 
ou 
nome = """ Angelina
Julie"""

# Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia
ser conhecido também como tipo vazio, mas é recomendado falar que é um tipo sem tipo

OBS: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Certo: None
Errado: none

OBS: o tipo None é sempre considerado False no Python

Quando utilizamos?
- Utilizamos o None quando queremos iniciar um variável sem especificar um tipo de dado ou valor.

numeros = None
'''