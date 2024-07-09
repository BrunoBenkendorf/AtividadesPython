cod = int(input("Digite código: "))
ano_Nasc = int(input("Digite o Ano de nascimento: "))
ano_Ingresso = int(input("Digite o Ano de ingresso:"))
idade = 2024 - ano_Nasc
ano_Empresa = 2024 - ano_Ingresso

print("Idade: ", idade," Anos")
print("Tempo de empresa: ",ano_Empresa," Anos")
if idade >= 65 and ano_Empresa >= 30 or idade >= 60 and ano_Empresa >= 25:
    print("Requerer aposentadoria")
else:
    print("Não requerer")