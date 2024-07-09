qtd_atual = int(input("Digite a quantidade atual em estoque:"))
qtd_min = int(input("Quantidade Mínima:"))
qtd_max = int(input("Quantida Máxima:"))

qtd_media = (qtd_max+qtd_min)/2

if qtd_atual >= qtd_media:
    print("Não efetuar compra")
else: 
    print("Efetuar compra")