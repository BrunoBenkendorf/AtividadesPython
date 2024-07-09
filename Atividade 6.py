import math

num = int(input('Digite um valor: '))
if num>=1 and num<=3:
    print (num**2)
elif num == 4 or num ==9:
    print(math.sqrt(num))
elif num == 6 or num == 7 or num == 8:
    print(num/9.0)