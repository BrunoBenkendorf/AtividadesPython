carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
valor_por_carro = float(input("Digite o valor que o vendedor recebe por cada carro vendido: "))

comissao_por_carro = carros_vendidos * valor_por_carro

comissao_por_vendas = valor_total_vendas * 0.05

salario_final = salario_fixo + comissao_por_carro + comissao_por_vendas

print("O salário final do vendedor é: R$",salario_final)
