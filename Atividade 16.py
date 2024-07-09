#Calcular o maior de três numeros
#Def = defini nova função
def maior3(a,b,c):
# se a maior igual b e a maior igual c retorna a
    if a >= b and a >= c:
        return a
#senão se b maior igual c retorna b
    elif b >= c:
        return b
#senão retorna c
    else: return c

#Entrada dos dados 
#n1, n2, n3 = inteiro
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))

#Processamento dos dados
#resultado adquiri função maior3
resultado = maior3(n1,n2,n3)
#imprimir
print(resultado)