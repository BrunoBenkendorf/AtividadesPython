# Aluno: Bruno Henrique Benkendorf
# Data: 26/07/2024
# Turma: T DESI 2024/1 V1
import os
   
resultados = [0, 0, 0, 0, 0]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

                  _____      _                                   ______    _                          
                 / ____|    | |                                 |  ____|  | |                       
                | |     ___ | |__  _ __ __ _ _ __   ___ __ _    | |__ __ _| |_ _   _ _ __ __ _ 
                | |    / _ \| '_ \| '__/ _` | '_ \ / __/ _` |   |  __/ _` | __| | | | '__/ _` |
                | |___| (_) | |_) | | | (_| | | | | (_| (_| |   | | | (_| | |_| |_| | | | (_| |
                 \_____\___/|_.__/|_|  \__,_|_| |_|\___\__,_|   |_|  \__,_|\__|\__,_|_|  \__,_|         
""")
    print("\nTabela de Preços das Chamadas"
          "\n----------------------------"
          "\n DDD | 47 | 48 | 49 |"
          "\n--------------------"
          "\n  47 | 0.15| 0.25| 0.32|" 
          "\n  48 | 0.28| 0.12| 0.28|"
          "\n  49 | 0.40| 0.25| 0.09|")

    origem = int(input("\nDigite o DDD de origem: "))
    destino = int(input("Digite o DDD de destino: "))
    tempo = int(input("Digite o tempo de ligação em minutos por mês: "))

    if origem == 47 and destino == 47:
        calculo = tempo * 0.15
    elif origem == 47 and destino == 48:
        calculo = tempo * 0.25
    elif origem == 47 and destino == 49:
        calculo = tempo * 0.32
    elif origem == 48 and destino == 47:
        calculo = tempo * 0.28
    elif origem == 48 and destino == 48:
        calculo = tempo * 0.12
    elif origem == 48 and destino == 49:
        calculo = tempo * 0.28
    elif origem == 49 and destino == 47:
        calculo = tempo * 0.40
    elif origem == 49 and destino == 48:
        calculo = tempo * 0.25
    elif origem == 49 and destino == 49:
        calculo = tempo * 0.09
    else:
        print("Combinação de DDDs inválida!")
        continue

    resultados.pop(0)
    resultados.append({
        'origem': origem,
        'destino': destino,
        'tempo': tempo,
        'valor': calculo
    })

    print("""
          __________________________________________  
         |                                          |
         |      Fatura mensal de: R$ {:.2f}        |
         |__________________________________________|   
        """.format(calculo))

    print("\nÚltimos 5 resultados:")
    for res in resultados:
        if res == 0:
            print("Nenhum dado disponível")
        else:
            print(f"Origem: {res['origem']}, Destino: {res['destino']}, Tempo: {res['tempo']} min, Valor: R$ {res['valor']:.2f}")
    
    input("\nPressione Enter para continuar...")