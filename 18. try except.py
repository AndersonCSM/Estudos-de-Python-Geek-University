"""
# O bloco try/except

Utilizamos o try/except para tratar erros que podem ocrrer no nosso código. Previnindo que o
programa para de funcionar e o usuário receba mensagens de erro inesperados.

A apresentação de erros aos usuários devem ser evitados: pois demonstram vulnerabilidade do sistema, além de
abalar a confiança do usuário no seu trabalho e sistema.

A forma geral mais simples é:
try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema

# EX01: Erro genérico
try:
    geek()
except:
    print('Deu algum problema')

# EX02: 
try:
    len(5)
except:
    print('Deu algum problema')

# OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O idela é SEMPRE tratar de forma específica.

# EX03: Tratando um erro específico
try:
    geek()
except NameError:
    print('Você está usando uma função inexistente')
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# EX04: 
try:
    geek()
except NameError as erra:
    print(f'Deu o seguinte erro: {erra}')
except TypeError as errb:
    print(f'Deu o seguinte erro: {errb}')
except: # Caso de erro geral
    print('Deu um erro diferente')

# EX05:
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome":"Geek"}

print(pega_valor(dic,'Geek'))

print(pega_valor(dic,8))

### Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

### Else -> É executado somente se não ocorrer o erro.

# EX01:
try: # Caso não de error, o código continuar linearmente.
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou: {num}')

### Finally

# OBS: O bloco finally é Sempre executado, independente se houve exceção ou não.

# o finally, geralmente, é utilizado para fechar ou desalocar recursos. Fechar arquivos ou encerrar conexão com banco de dados

# EX02:
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Fim da execução, com ou sem erro')

# EX03:
def dividir(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível fazer divisão por zero'

a = int(input())
b = int(input())

print(dividir(1,2))

# EX04:
def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

a = int(input())
b = int(input())

print(dividir(1,2))
"""
