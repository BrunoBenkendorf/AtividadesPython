#Gerar a sequência de Fibonacci
#Comando para definir variavel n do tipo inteiro em seguida pedir para o usuario
n = int(input("Digite o número: "))
#Comando imprimir mensagem
print("Sequência de Fibonacci")
#Comando para fib1 adquirir 0
fib1 = 0
#Comando para fib2 adquirir 1
fib2 = 1
#Comando imprimir mensagem
print(fib1, end=' ')
#Comando imprimir mensagem
print(fib2, end=' ')
#Comando para i de(2,n)
for i in range (2,n):
#Comando para fib adiquirir fib1 + fib2
    fib = fib1 + fib2
#Comando para fib1 adquirir fib2
    fib1 = fib2
#Comando para fib2 adquirir fib
    fib2 = fib
#Comando para imprimir mensagem
    print(fib,end=' ')
