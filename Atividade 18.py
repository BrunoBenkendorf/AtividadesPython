#Def defini nova variavel maior_menor
def maior_menor(lista):
#maior adquiri lista[0]
    maior = lista[0]
#menor adquiri lista[0]
    menor = lista[0]
#para elemento em lista faca
    for elemento in lista :
#se elemento for maior que maior
        if elemento > maior:
#maior adquiri elemento
           maior = elemento
#senão se elemento for menor que menor 
        elif elemento < menor:
#menor adquiri elemento
             menor = elemento
#retorna maior e menor
    return maior, menor
#lista do tipo list()
lista = list()
#i adquiri 1
i = 1
#enquanto i for menor igual 10
while i<=10:
#elem do tipo inteiro
    elem = int(input("Digite um elemento da lista:"))
#lista adiciona elem no final da lista
    lista.append(elem)
#i adquiri i + 1
    i+=1
#imprimi
    print(lista)
#maior e menor adquiri função maior_menor
    maior, menor=maior_menor(lista)
#imprimir
    print("Maior",maior)
    print("Menor",menor)