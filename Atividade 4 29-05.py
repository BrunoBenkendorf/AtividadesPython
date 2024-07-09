#Calcular os divisores de um número
#Comando para definir a variavel n do tipo inteiro e em seguida pedir para o usuario
n = int(input("Digite um número"))
#Comando para imprimir a mensagem
print("Os divisores de",n,"são:")
#Comando para i 1, n+1
for i in range(1, n+1):
#Comando condição Se resto de n / i for = 0    
    if n % i == 0:
#Comando para imprimir i e em seguida terminar
        print(i, end=" ")