#Criptografia utilizando cifra de César
#Deslocamento tipo inteiro
deslocamento = int(input("Digite o deslocamento: "))
#Texto tipo string
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado =""
#For = para
for letra in texto:
#if = se
#a função isupper() verifica se todos os caracteres na string estão em maiúsculas
    if letra.isupper():
#A função chr() em Python retorna uma string que representa um caractere cujo ponto de código Unicode é o inteiro especificado
#A função ord() em Python retorna o número que representa o código Unicode de um caractere específico.
#A função lower()transforma todos carcteres em minusculo
        letra_criptografada = chr((ord(letra.lower())+deslocamento - 97)%26+65)
#elif = senão se
#A função islower() em Python verifica se todos os caracteres de uma string estão em minúsculas. Ele retorna True se todos os caracteres forem minúsculo.
    elif letra.islower():
        letra_criptografada = chr((ord(letra)+deslocamento-97)%26+97)
#else = senão
    else: letra_criptografada = letra 
    texto_criptografado += letra_criptografada
#Imprimir
    print("Texto criptografado:", texto_criptografado)