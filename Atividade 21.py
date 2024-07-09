#Def cria função obter_ultimo_elemento
def obter_ultimo_elemento(lista):
#se lista retorne lista[-1]
    if lista:
        return lista[-1]
#senão retorne nada
    else: return None
#lista do tipo list()
lista = list()
#i adquiri 1
i = 1
#enquanto i for menor igual a 5
while i<=5:
#elem do tipo inteiro
    elem = int(input("Digite um elemento da lista:"))
#lista adiciona elem ao final da lista
    lista.append(elem)
#i++
    i+=1
#imprimir
    print(lista)
#ultimo_elemento adquiri função obter_ultimo_elemento
    ultimo_elemento = obter_ultimo_elemento(lista)
#imprimir
    print("Último elemento da lista:", ultimo_elemento)
