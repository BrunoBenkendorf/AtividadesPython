num_Conta = int(input("Digite o numero da conta: "))
saldo = float(input("Digite o saldo da conta: "))
credito = float(input("Digite o gasto em crédito: "))
debito = float(input("Digite o gasto em débito: "))

saldo_atual = saldo - (debito + credito)
print("A conta de Numero: ",num_Conta,"Tem saldo: ")
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
