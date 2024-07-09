salario = float(input("Digite o salario: "))
valor_vendas = float(input("Digite o valor de vendas"))
comissao3 = float 
comissao5 = float
comissao3=0
comissao5=0

if valor_vendas <= 1500:
    comissao3 = valor_vendas*0.03
    comissao5 = 0
else :
    comissao3 = 1500*0.03
    comissao5 = (valor_vendas-1500)*0.05

    salario_total = salario + comissao3 + comissao5

    print("Salario final: R$", salario_total)
