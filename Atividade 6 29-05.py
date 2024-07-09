#Calcular as raízes de uma equação do segundo grau
#Comando para importa a biblioteca math
import math
#Comando para importa a biblioteca cmath
import cmath
#Comando para definir a variavel a do tipo real e em seguida pedir para o usuario
a = float(input("a:"))
#Comando para definir a variavel b do tipo real e em seguida pedir para o usuario
b = float(input("b:"))
#Comando para definir a variavel c do tipo real e em seguida pedir para o usuario
c = float(input("c:"))
#Comando condição Se a for igual a 0
if a == 0:
#Comando imprimir mensagem
    print("Não é uma equação do segundo grau!!!")
#Comando condição senão
else:
#Comando para delta adquirir b**2-4*a*c
    delta = b**2-4*a*c
#Comando condição Se delta for < 0
if delta < 0: #Raízes complexas
#Comando para x1 adquirir (-b + cmath.sqrt(delta))/(2*a)
    x1 = (-b + cmath.sqrt(delta))/(2*a)#cmath.sqrt = raiz quadrada
#Comando para x2 adquirir (-b - cmath.sqrt(delta))/(2*a)
    x2 = (-b - cmath.sqrt(delta))/(2*a)
#Comando imprimir mensagem
    print("Raizes complexas:",x1,"e",x2)
#Comando condição senão se delta for igual a 0
elif delta == 0: #Apenas uma raiz
#Comando para x adquiri -b/(2*a)
    x = -b/(2*a)
#Comando imprimir mensagem
    print("Uma raiz real:",x)
#Comando condição senão
else:
#Comando para x1 adquirir  x1 = (-b + math.sqrt(delta))/(2*a)
    x1 = (-b + math.sqrt(delta))/(2*a)#math.sqrt = raiz quadrada
#Comando para x2 adquirir x2 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
#Comando imprimir mensagem
    print("Duas raízes reais:", x1,"e",x2)
