#Aluno: Bruno Henrique Benkendorf
#Data: 26/07/2024
#Turma: T DESI 2024/1 V1
resultados = []
while True:
    num1 = float(input("Digite um numero:"))
    num2 = float(input("Digite um numero:"))
    escolha = int(input("Escolha uma operação: (1(+), 2(-), 3(/), 4(*))"))
    if(escolha==1):
        print("Você escolheu adição")
        resultado = num1+num2
        print(num1, "+", num2, "=", resultado)
    elif(escolha==2):
        print("Você escolheu subtração")
        resultado = num1-num2
        print(num1, "-", num2, "=", resultado)
    elif(escolha==3):
        print("Você escolheu divisão")
        resultado = num1/num2
        print(num1, "/", num2, "=", resultado)
    elif(escolha==4):
        print("Você escolheu multiplicação")
        resultado = num1*num2
        print(num1, "*", num2, "=", resultado)
    else:
        print("Essa operação não existe!!!")
        resultado = None
    if resultado is not None:
        resultados.append(resultado)
    if len(resultados) > 3:
        resultados = resultados[-3:]

    print("\nÚltimos três resultados:")
    for i in resultados:
        print(i)
    finalizar = input("\nDeseja finalizar? (s/n): ")
    if finalizar == "s":
        break

