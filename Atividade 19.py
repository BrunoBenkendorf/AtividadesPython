#Def cria função mdc("Minimo divisor comum")
def mdc(a,b):
#se b for igual a 0 retorne a
    if b == 0:
        return a
#senão retorne mdc(b e resto de a/b)
    else:
        return mdc(b,a % b)
#num1,num2 =  inteiro
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
#resultado adquiri função mdc
resultado = mdc(num1,num2)
#imprimir
print("MDC:", resultado)