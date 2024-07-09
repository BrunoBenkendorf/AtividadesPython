#Verifivar se uma string é uma palíndrome
#Comando para pedir palavra para o usuario
palavra = input("Digite uma palavra:")
#inversa adquiri para do contrário
inversa = palavra[::-1]
#Se palavra for igual a inversa
if palavra == inversa:
#Comando imprimi mensagem
    print("É uma palindrome")
#Senão
else:
#Comando imprimi mensagem
    print("Não é uma palindrome")