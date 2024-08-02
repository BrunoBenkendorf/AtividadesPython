# Aluno: Bruno Henrique Benkendorf
# Data: 26/07/2024
# Turma: T DESI 2024/1 V1
import os
def Calculo(c, m):
    return c * (m / 100)

def ValorFinal(c, margem):
    return c + Calculo(c, margem)

def Lucro(c, margem):
    return Calculo(c, margem)

listaCompras = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
__________                   .___      __                 ________              .__    .___                        
\______   \_______  ____   __| _/_ ___/  |_  ____  ______ \______ \  __ _____  _|__| __| _/____  __________  ______
 |     ___/\_  __ \/  _ \ / __ |  |  \   __\/  _ \/  ___/  |    |  \|  |  \  \/ /  |/ __ |/  _ \/  ___/  _ \/  ___/
 |    |     |  | \(  <_> ) /_/ |  |  /|  | (  <_> )___ \   |    `   \  |  /\   /|  / /_/ (  <_> )___ (  <_> )___ \ 
 |____|     |__|   \____/\____ |____/ |__|  \____/____  > /_______  /____/  \_/ |__\____ |\____/____  >____/____  >
                              \/                      \/          \/                    \/          \/          \/ 
          """)

    nome = input("Digite o nome do produto: ")

    try:
        custo = float(input("Digite o custo do produto: "))
        margem = float(input("Digite a margem de lucro: "))
    except ValueError:
        print("Entrada Invalida")
        continue
    valor_final = ValorFinal(custo, margem)
    lucro = Lucro(custo, margem)
    print(f"Valor final do produto: R${valor_final:.2f}")

    listaCompras.append({'nome': nome, 'valor_final': valor_final, 'lucro': lucro})
    if not listaCompras:
        print("Nenhum dado")
    else:
        print("""                                                      
      ########                                              
      ##########                                            
            ####                                            
            ##########################################      
              ######################################        
              ####          ##        ##        ####        
                ##          ##        ##        ####        
                ####        ##        ##        ##          
                ####   CARRINHO DE COMPRAS:    ####          
                  ####      ##                ####          
                  ####      ##                ####          
                  ##############################            
                    ############################            
                    ####                                    
                    ############################            
                  ##############################            
                  ####    ##          ####    ####          
                  ##########            ########            
                    ########            ########          
              """)
    lucro_total = 0
    for produto in listaCompras:
        print(f"Produto: {produto['nome']} - Valor Produto: R${produto['valor_final']:.2f} - Lucro: R${produto['lucro']}")
        lucro_total += produto['lucro']
    
    print(f"Lucro do carrinho: R${lucro_total}")
    
    continuar = input("\nDeseja continuar? (s/n): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if continuar != 's':
        
        print('''            
             ________________________________________________              
            /                                                \             
           |    _________________________________________     |            
           |   |                                         |    |            
           |   |  C:\ > _ ---------FIM                   |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |_________________________________________|    |            
           |                                                  |            
            \_________________________________________________/            
                   \___________________________________/                   
                ___________________________________________                
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_             
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_          
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_       
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_    
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_ 
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                              -Bruno Benkendorf-                               
                             ''')
        input("Press ENTER...")
        break