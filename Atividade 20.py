#Def cria função isertion_sort(ordenação por inserção)
def insertion_sort(lista):
#len()= Retorna o comprimento de um objeto
#para i de 1 ate len(lista)
    for i in range(1, len(lista)):
#chave adquiri lista[i]
        chave = lista[i]
#j adquiri i-1
        j = i-1
#enquanto j maior igual a 0 e chave for menor que lista[j]
        while j >=0 and chave< lista[j]:
#lista[j+1] adquiri lista[j]
            lista[j+1] = lista[j]
#j--
            j -= 1 
#lista[j+1] adquiri chave
            lista[j+1] = chave
#lista do tipo list()
lista = list()
# i adquiri 1
i = 1
#enquanto i for menor igual a 10
while i<=10:
#elem do tipo inteiro
    elem = int(input("Digite um elemento da lista:"))
#lista adiciona elem ao final da lista
    lista.append(elem)
#i++
    i+=1
#imprimir
    print(lista)
#função insetion_sort ordena a lista
    insertion_sort(lista)
#imprimir
    print(lista)