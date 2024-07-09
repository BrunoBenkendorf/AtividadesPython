#vetor de numeros
numeros = []
#para i ate 10
for i in range(10):
#O bloco try é utilizado para envolver código que pode gerar exceções. 
#Quando uma exceção entra no bloco do try, o controle é transferido para o bloco except,
#permitindo que de para tratar a excessão de maneira adequada.
    try:
#numero do tipo inteiro pede para o usuário
        numero = int(input("Digite um número inteiro:"))
#vetor numeros adiciona numero no final do vetor
        numeros.append(numero)
#ValueError = Um ValueError em Python ocorre quando uma função recebe um argumento do tipo correto, mas com um valor inadequado.
#Isso pode acontecer em várias situações, como tentar converter uma string para um inteiro quando a string não representa um inteiro válido.
    except ValueError:
#imprimir
        print("Entrada inválida!!!")
#soma adquiri função sum (numeros)
    soma = sum(numeros)
#media adquiri soma dividido pela função len(numeros)
#len = é uma função embutida que retorna o número de elementos em um objeto
    media = soma / len(numeros)
#imprimir
    print("Soma: ",soma)
    print("Media:",media)