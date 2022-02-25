"""
### Dunder Name e Dunder Main

Dunder -> doble Under = __

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos/ propriedades e etc. Utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na lingaugem C, temos um programa da seguinte forma:
int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main(String[] args) {

}

# Em Python, se executamos um módulo Python diretamente na linha de comando, internamente o
Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

# Resumo: quanto executamos códigos em um arquivo, o nome do arquivo passa-se a se chamar __main__, caso o código não esteja no arquivo de execução(importação) o __name__ do
arquivo será o nome do arquivo.

# Executando um código em um arquivo: __name__ == __main__

# EX01:
import primeiro, segundo

"""