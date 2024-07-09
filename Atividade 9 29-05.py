#Imprimir tabuada de um número
#Comando continua adquirir Verdadeiro
continua = True
#Comando enquanto continua for verdadeiro
while continua:
#Comando para definir variavel n do tipo inteiro e em seguida pedir para o usuario
    n = int(input("Digite um número: "))
#Comando para i de 1 ate 10
    for i in range(1,11):
#Comando imprimir mensagem
        print(n,"x",i,"=",n*i)
#Comando para resposta adquirir entrada com mensagem
    resposta = input("Deseja continuar(s/n)?")
#Comando condição Se resposta for "n"
    if resposta == "n":
#Comando para continua adquirir Falso
        continua = False