'''
# Aula 22: if (Se), else, elif (else if)
# sintaxe do if.
if idade < 10:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')

# Aula 23: Estruturas lógicas: and (e), or(ou), not(não), is(é)

Operadores unários:
    - not
Operadores binários:
    - and, or", IS

#Regras de funcionamento:
Para o 'and', ambos os vlaores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido

EX:
ativo, logado = True, True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precis ativar sua conta, por favor, cheque seu e-mail')

# O jeito pythônico é a forma mais otimizada, logo dificilmente usamos o is.
EX correto:
if ativo:
    print('Bem-vindo')

EX errado:
# Ativo é True?
if ativo is True:
    print('Bem-vindo')

EX:
1 == 1 é o mesmo que 1 is 1, retornando True
'''