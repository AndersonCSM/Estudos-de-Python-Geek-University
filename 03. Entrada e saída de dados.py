"""
# Entrada de dados

# Modelo antigo
print('Qual é seu nome ?')
nome = input()
# modelo atualizado
nome = input('Qual é seu nome? ')
idade = input('Qual sua idade? ')

# Entrada com Cast
idade = int(input('Qual sua idade? '))

# Input -> Entrada
# Todo dado recebido via input é do tipo String
Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Asplas simples triplas;
- Asplas duplas triplas;

# Saída de dados

#Exemplo de print Atual, Python 3.7
print(f'Seja bem-vindo(a) {nome}')
print(f'A {nome} nasceu em {2021 - int(idade)}}') 
# int(idade) -> está realizando um cast
# Cast é a 'conversão' de um tipo de dado para outro. 

#Exemplo de print 'Moderno' do print, Python 3.0
print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print antigo da versão Python 2.0
print('Seja bem-vindo(a) %s' % nome)
print('A %s tem %s anos' % (nome, idade))

# O ponto e vírgula no Python é usado para executar dois comandos ao mesmo tempo no python
import pdb; pdb.set_trace()
"""