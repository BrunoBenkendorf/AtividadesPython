#Autor:Bruno Henrique Benkendorf
# Data: 21/08/2024
import os
from collections import defaultdict
x=10
lista = []

def limpa():
    input("Pressione Enter para continuar...")
    os.system("cls")
print("""                                                      
                MMmmmmmmmmMMmmmmmmmmmm  mmmmmmmmmmmm..      
              mmmmmmmmmmmmmmmmmmmmmm--  mmmmmmmmmmmmmmmm++  
              mmmmmmmmmmmmmmmmmmmm++  ++mmmmmmmmmmmmmmmmmm  
              mmmmmmmmmmmmmmmmmmmm    mmmmmmmmmmmmmmmmmmmmMM
            ++mmmmmmmmmmmmmmmmmm      mmmmmmmmmmmmmmmmmmmmMM
            mmmmmmmmmmmmmmmm++        mmmmmmmmmmmmmmmmmmmmmm
          mmmmmmmmmmmmmm++    mmmmmm  ++mmmmmmmmmmmmmmmmmm  
          mmmmmmmm++++      MMmmmmmmmm  ++MMmmmmmmmmmmmmmm  
                            mmmmmmmmmm                      
        mmmmmmMMmmmm++mm    mmmmmmmm++          ::++mmmm    
        MMmmmmmmmmmmmmmmmm  ++mmmmMM      mmmmmmmmmmmm++    
      MMmmmmmmmmmmmmmmmmmmmm          mmMMmmmmmmmmmmmm      
      mmmmmmmmmmmmmmmmmmmmmm      mmmmmmmmmmmmmmmmmmmm      
      mmmmmmmmmmmmmmmmmmmmmm    mmmmmmmmmmmmmmmmmmmmmm      
      MMmmmmmmmmmmmmmmmmmm++  mmmmmmmmmmmmmmmmmmmmMM        
        mmmmmmmmmmmmmmmmmm    mmmmmmmmmmmmmmmmmmmmmm        
            ++mmmmmmmmmm++  mmmmmmmmmmmmmmmmmmmmmm          
                                                            
                _____ ____   _____ ______ 
               |_   _|  _ \ / ____|  ____|
                 | | | |_) | |  __| |__   
                 | | |  _ <| | |_ |  __|  
                _| |_| |_) | |__| | |____ 
               |_____|____/ \_____|______|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
""")
limpa()
for i in range(x):
    pesquisa=input("DIGITE UM ASSUNTO: ")
    lista.append(pesquisa)

keys = defaultdict(list)

for key, value in enumerate(lista):

    keys[value].append(key)
print("Assuntos digitados: ",lista)
for value in keys:
    if len(keys[value]) > 1:
        print("Assuntos Repetidos:\n",value, keys[value])

    
