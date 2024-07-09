#Def denifini nova varivel dobrar_lista
def dobrar_lista(lista):
#nova_lista = lista
    nova_lista = []
#for = para elemento na lista
    for elemento in lista:
#novo_elemento adquiri elemento x 2
        novo_elemento = elemento*2
#nova_lista adiciona novo_elemento no fim da lista
        nova_lista.append(novo_elemento)
#Retorna nova_lista
    return nova_lista
#lista = tipo list
lista = list()
#i adquiri 1
i = 1
#Enquanto i for menor igual a 10
while i<=10:
#elem = inteiro
    elem = int(input("Digite um elemento da lista:"))
#lista adiciona elem ao final da lista
    lista.append(elem)
# i adquiri i + 1
    i+=1
#imprimir
    print(lista)
#nova_lista adquiri função dobrar_lista()
    nova_lista = dobrar_lista(lista)
#imprimir
    print(nova_lista)