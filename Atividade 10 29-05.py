#Comando para criar um array 
numeros = []
#Comando para i ate 10
for i in range(10):
#Comando para definir variavel num do tipo inteiro e em seguida pedir para o usuario
    num = int(input("Digite um número:"))
#Comando para adicinor num no array numeros
    numeros.append(num)
#Comando soma adquiri sum(Soma) numeros
soma = sum(numeros)
#Comando maior = max(Maxímo) busca o maior dos numeros
maior = max(numeros)
#Comando menor = min(Minímo) busca o menor dos numeros
menor = min(numeros)
#Comando imprimir mensagem
print("Soma:", soma)
print("Maior:", maior)
print("Menor:", menor)