# Aluno: Bruno Henrique Benkendorf
# Data: 26/07/2024
# Turma: T DESI 2024/1 V1
from datetime import datetime, timedelta
import os 
def calcular_data_nascimento(data_atual_str, idade_anos, idade_meses, idade_dias):
    data_atual = datetime.strptime(data_atual_str, "%d%m%Y")

    ano_nascimento = data_atual.year - idade_anos
    mes_nascimento = data_atual.month - idade_meses
    dia_nascimento = data_atual.day - idade_dias

    if mes_nascimento <= 0:
        mes_nascimento += 12
        ano_nascimento -= 1
        
    if dia_nascimento <= 0:
        mes_nascimento -= 1
        if mes_nascimento <= 0:
            mes_nascimento += 12
            ano_nascimento -= 1
        ultimo_dia_mes = (datetime(ano_nascimento, mes_nascimento + 1, 1) - timedelta(days=1)).day
        dia_nascimento += ultimo_dia_mes
        
    try:
        data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
    except ValueError:
        if mes_nascimento == 2 and dia_nascimento == 29:
            data_nascimento = datetime(ano_nascimento, mes_nascimento, 28)
        else:
            raise

    return data_nascimento.strftime("%d%m%Y")
listanasc = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
________             __                .___          _______                           .__                            __           
\______ \  _____   _/  |_ _____      __| _/  ____    \      \  _____     ______  ____  |__|  _____    ____    ____  _/  |_   ____  
 |    |  \ \__  \  \   __\\__  \    / __ | _/ __ \   /   |   \ \__  \   /  ___/_/ ___\ |  | /     \ _/ __ \  /    \ \   __\ /  _ \ 
 |    `   \ / __ \_ |  |   / __ \_ / /_/ | \  ___/  /    |    \ / __ \_ \___ \ \  \___ |  ||  Y Y  \\  ___/ |   |  \ |  |  (  <_> )
/_______  /(____  / |__|  (____  / \____ |  \___  > \____|__  /(____  //____  > \___  >|__||__|_|  / \___  >|___|  / |__|   \____/ 
        \/      \/             \/       \/      \/          \/      \/      \/      \/           \/      \/      \/                                                                 
          """)
    data_atual = input("Digite a data atual (ddmmaaaa): ")
    idade_anos = int(input("Digite sua idade em anos: "))
    idade_meses = int(input("Digite sua idade em meses: "))
    idade_dias = int(input("Digite sua idade em dias: "))

    data_nascimento = calcular_data_nascimento(data_atual, idade_anos, idade_meses, idade_dias)
    listanasc.append({'nasc':data_nascimento})
    print(f"Sua data de nascimento é (ddmmaaaa): {data_nascimento}")
    continuar = input("\nDeseja continuar? (s/n): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if continuar != 's':
        for datas in listanasc:
            print("Tabela de Nascimentos:")
            print(f"Data de nascimento: {datas['nasc']} ")
        print("""                                                                                
                                        ##                                      
                                        ####                                    
                                      MM####                                    
                                      ##  MM##                                  
                                    ##      ##                                  
                                    ##..  MM##                                  
                                      ######                                    
                                    ::##  ##                                    
                                    ++##  ##                                    
                                    ++##  ##                                    
                                    ++##  ##                                    
                                    ++##  ##                                    
                  ##############################################                
                  ##                                          ##                
                  ##      ####            MM##@@            ####                
                  ##    ##    ####      ####  ####      ####  ##                
                  ######        ########@@      ..########    ##                
                  ##                                          ##                
                  ##                                          ##                
                  ##                                          ##                
                  ##                                          ##                
                  ##                                          ##                
                  ##                                          ##                
      ####################################################################@@    
      ##                                                                  ##    
      ##                                                                  ##    
      ##          ########..              ##########                ########    
      ##        ##        ####          ####      @@##          mm##      ##    
      ##    ####            ####      ##@@            ##      ####        ##    
      ########                ::######                  ######MM          ##    
      ##                                                                  ##    
      ##                                                                  ##    
      ##                  FIM!!!!!!!!!!!!!!!!!!!!!!!                      ##    
      ##                                                                  ##    
      ##                                                                  ##    
      ##                                                                  ##    
      ##                                                                  ##    
      ##                                                                  ##    
      @@##################################################################@@      """)
        break