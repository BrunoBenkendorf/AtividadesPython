#Calcular o fatorial de um número
#Comando para definir a variavel num do tipo inteiro em seguida pedir para o usuario
num = int(input("Digite um número: "))
#Comando condição se num for maior ou igual a 0
if num >= 0: 
#Comando para fatorial adquirir 1
    fatorial = 1
#Comando para i de (1,num+1)
    for i in range (1, num+1):
#Comando fatorial adquirir fatorial * i
        fatorial *= i
#Comando imprimir mensagem
        print("O fatorial de",num,"é",fatorial)
#Comando condição senão
else:
#Comando imprimir mensagem
    print("Entrada invalida!")