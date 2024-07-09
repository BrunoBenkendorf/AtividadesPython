# Entrada dos dados lista 1
# Cria uma lista chamada lista1
lista1 = list()  
# Inicializa a variável i com o valor 1
i = 1  
# parar enquanto i for menor ou igual a 10
while i <= 10:  
# Solicita ao usuário um número inteiro e o armazena na variável elem
    elem = int(input("Digite um elemento da lista:"))  
 # Adiciona o elemento digitado à lista1
    lista1.append(elem) 
# Incrementa a variável i em 1
    i += 1  
 # Imprime a lista1 atualizada
    print(lista1) 
# Ordena a lista1 e armazena o resultado em lista1ordenada
    lista1ordenada = sorted(lista1) 
# Imprime a lista1ordenada
    print(lista1ordenada)  

# Entrada dos dados da lista 2
# Cria uma lista chamada lista2
lista2 = list()  
 # Inicializa a variável i com o valor 1
i = 1 
# parar enquanto i for menor ou igual a 10
while i <= 10:  
# Solicita ao usuário um número inteiro e o armazena na variável elem
    elem = int(input("Digite um elemento da lista")) 
# Adiciona o elemento digitado à lista2 
    lista2.append(elem) 
 # Incrementa a variável i em 1
    i += 1 
# Imprime a lista2 atualizada
    print(lista2) 
# Ordena a lista2 e armazena o resultado em lista2ordenada
    lista2ordenada = sorted(lista2) 

# Processamento dos dados
# Cria uma lista vazia chamada intercalada para armazenar o resultado da intercalação
intercalada = [] 
# Inicializa as variáveis i e j com o valor 0
i = j = 0  
# para que se repete enquanto i e j forem menores que o tamanho de lista1ordenada e lista2ordenada
while i < len(lista1ordenada) and j < len(lista2ordenada):  
# Compara o elemento atual de lista1ordenada com o elemento atual de lista2ordenada
    if lista1ordenada[i] < lista2ordenada[i]: 
# Adiciona o elemento de lista1ordenada à lista intercalada
        intercalada.append(lista1ordenada[i])
# Incrementa a variável i em 1  
        i += 1 
#Senão 
    else:
# Adiciona o elemento de lista2ordenada à lista intercalada
        intercalada.append(lista2ordenada[j])
# Incrementa a variável j em 1 
        j += 1  
# Adiciona os elementos restantes de lista1ordenada à lista intercalada
intercalada += lista1ordenada[i:] 
# Adiciona os elementos restantes de lista2ordenada à lista intercalada
intercalada += lista2ordenada[j:]  
# Imprime a lista intercalada
print(intercalada) 
