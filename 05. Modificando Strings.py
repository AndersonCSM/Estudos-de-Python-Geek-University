''''
# Modificando Strings
tr = 'texto'
1- Nome em caixa alta: tr.upper()
2- Nome em caixa baixa: tr.lower()
3- Divide as palavras da String dentro de uma lista: tr.split()
nome= 'Geek University'
4- Substituir elementos de uma String (e) por outra (x): tr.replace('e','x')

# Fatiamento de Strings: Podemos tratar Strings como uma lista de caracteres e como isso realizar cortes.
Podemos resgatar os caracteres do índice 0 até o índice 3:
nome= 'Geek University'
print(nome[0:4]) = Geek

# Ao transformar em lista, a palavra Geek passa a ocupar a posição [0], podendo chama-la
print(nome.split()[0]) 

#Imprimindo uma String em ordem inversa:
nome= 'Geek University'
print(nome[::-1]) = ytisrevinU keeG
'''