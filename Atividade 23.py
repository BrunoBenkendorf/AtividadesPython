#Def cria a função converter_quilometros_para_metros
def converter_quilometros_para_metros(quilometros):
#metros adquiri quilometros * 1000
    metros = quilometros*1000
#Retorna metros
    return metros
#O bloco try é utilizado para envolver código que pode gerar exceções. 
#Quando uma exceção entra no bloco do try, o controle é transferido para o bloco except,
#permitindo que de para tratar a excessão de maneira adequada.
try:
#quilometros do tipo real
    quilometros = float(input("Digite a distância em quiômetros:"))
#metros adquiri função converter_quilometros_para_metros
    metros = converter_quilometros_para_metros(quilometros)
#imprimir
    print("Metros:", metros)
#ValueError = Um ValueError em Python ocorre quando uma função recebe um argumento do tipo correto, mas com um valor inadequado.
#Isso pode acontecer em várias situações, como tentar converter uma string para um inteiro quando a string não representa um inteiro válido.
except ValueError:
#imprimir
    print("Entrada inválida!")
