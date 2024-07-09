#Somar os dígitos de um número menor que 100
#Comando para definir variavel numero do tipo inteiro e em seguida pedir para o usuário
numero = int(input("Digite um número menor que 100:"))
#Comando condição Se numero for maior ou igual a 100
if numero >= 100:
    #Comando para imprimir a mensagem 
    print("O número deve ser menor que 100.")
#Comando condição senão
else:
    #Comando para dezena adquirir numero dividido por 10
    dezena = numero // 10
    #Comando para unidade adquirir o resto de numero divido por 10
    unidade = numero % 10
    #Comando para soma adquirir dezena + unidade
    soma = dezena + unidade
    #Comando para imprimir a soma
    print("Soma:", soma)