# Autor: Bruno Henrique Benkendorf
# Data: 30/10/2024
# Créditos: https://medium.com/vacatronics/cifra-de-c%C3%A9sar-em-python-8d02d3bc7d42
import os
MODE_ENCRYPT = 1
MODE_DECRYPT = 0
menu = 0
lista_palavras = []
lista_palavras_criptografadas = []

def cripto(data, chave, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ0123456789'
    new_data = ''
    for c in data:
        index = alfabeto.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + chave if mode == MODE_ENCRYPT else index - chave
            new_index = new_index % len(alfabeto)
            new_data += alfabeto[new_index:new_index+1]
    return new_data
def limpa():
    os.system('cls')
limpa()
while menu != 5:
    print("""
          1- Cadastrar
          2- Criptografar
          3- Descriptografar
          4- Mostrar palavras Criptografadas
          5- Encerrar""")
    menu = int(input("-> "))
    limpa()
    match menu:
        case 1:
            original = input("Digite a palavra: ")
            lista_palavras.append(original)
            print("Palavra cadastrada com sucesso!")

        case 2:
            if lista_palavras:
                print("Palavras cadastradas:")
                for i, palavra in enumerate(lista_palavras):
                    print(f"{i + 1} - {palavra}")
                
                escolha = int(input("Escolha o número da palavra para criptografar: ")) - 1
                if 0 <= escolha < len(lista_palavras):
                    original = lista_palavras[escolha]
                chave = int(input("Digite a cod chave: "))
                criptografado = cripto(original, chave, MODE_ENCRYPT)
                lista_palavras_criptografadas.append(criptografado)
                print('Palavra encriptada:', criptografado)
            else:
                print("Nenhuma palavra cadastrada para criptografar.")

        case 3:
            if lista_palavras:
                print("Palavras cadastradas:")
                for i, palavra in enumerate(lista_palavras_criptografadas):
                    print(f"{i + 1} - {palavra}")
            if lista_palavras:
                criptografado = input("Digite a palavra criptografada: ")
                descriptador = int(input("Digite o cod chave para descriptografar: "))
                descriptado = cripto(criptografado, descriptador, MODE_DECRYPT)
                print('Palavra descriptografada:', descriptado)
            else:
                print("Nenhuma palavra criptografada para descriptografar.")
        case 4:
            if lista_palavras_criptografadas:
                print("Palavras cadastradas:", lista_palavras_criptografadas)
            else:
                print("Nenhuma palavra cadastrada ainda.")
        case 5:
            print("Encerrando o programa...")
            break

    

