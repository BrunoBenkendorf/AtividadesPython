nome_Prod = input("Digite a descrição do produto: ")
qtd_adquirida = int(input("Digite a quantidade adquirida: "))
preco_uni = float(input("Digite o preço unitário:"))

total = qtd_adquirida * preco_uni

if qtd_adquirida <= 5:
    desconto = total*0.02
elif qtd_adquirida > 10:
    desconto = total*0.05
elif qtd_adquirida> 5 and qtd_adquirida <=10:
    desconto = total * 0.03
total_pagar = total - desconto

print("Total: R$", total,"\nDesconto: R$",desconto,"\nTotal a pagar: R$",total_pagar)