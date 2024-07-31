# Aluno: Bruno Henrique Benkendorf
# Data: 26/07/2024
# Turma: T DESI 2024/1 V1
import os

def fatorial(n, resultado=1):
    if n == 0 or n == 1:
        return resultado
    else:
        return fatorial(n - 1, n * resultado)
def raiz(n):
    return n**0.5
resultados = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
      
      
 _________        .------------------.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |    INTEIROS    | |             
|:______B:|      | |                | |             
|:______B:|      | |     IMPAR      | |             
|         |      | |      PAR       | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:   
                        by Bruno           
      ''')
    num1 = float(input("Digite o primeiro numero inteiro:")) 
    num2 = float(input("Digite o segundo numero inteiro:"))
    par = 0
    par1 = 0
    impar = 0
    impar1 = 0
    if num1 % 2 == 0:
        par = num1
    else:
        impar = num1
    if num2 % 2 == 0:
        par1 = num2
    else: 
        impar1 = num2
    
    
    if num1 == par and num2 == par1 :
        res = num1 ** num2
        print("Resultado: ",num1," ^ ",num2," = ",res)
    elif num1 == impar and num2 == impar1:
        res= fatorial(num1) + fatorial(num2)
        print("Resultado: ",fatorial(num1)," + ",fatorial(num2)," = ", res)
    elif num1 == impar and num2 == par1 or num1 == par and num2 == impar1:
        res = fatorial(num1)/raiz(num2)
        print("Resultado:", fatorial(num1), " / ", raiz(num2)," = ",res)
    else:
        print("Os numeros não atendem aos requisitos")

    resultados.append({'res' : res})
    for res in resultados:
        if res == 0:
            print("Nenhum dado disponível")
        else:
            print(f"Resultados: {res['res']}")

    continuar = input("\nDeseja continuar? (s/n): ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if continuar != 's':
        print("""
             _..--""---.
            /           ".
            `            l
            |'._  ,._ l/"\\
            |  _J<__/.v._/
             \( ,~._,,,,-)
              `-\' \`,,j|
                 \_,____J
            .--.__)--(__.--.
           /  `-----..--'. j
           '.- '`--` `--' \\
          //  '`---'`  `-' \\
         //   '`----'`.-.-' \\
       _//     `--- -'   \' | \________
      |  |         ) (      `.__.---- -'\\
       \7          \`-(               74\\
       ||       _  /`-(               l|//7__
       |l    ('  `-)-/_.--.          f''` -.-"|
       |\     l\_  `-'    .'         |     |  |
       llJ   _ _)J--._.-('           |     |  l
       |||( ( '_)_  .l   ". _    ..__I     |  L
       ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
            \ |           ) /.              ``'`-.._``-.
            l l          / / |                      |''|
             " \        / /   "-..__                |  |
             | |       / /          1       ,- t-...J_.'
             | |      / /           |       |  |
             J  \  /"  (            l       |  |
             | ().'`-()/            |       |  |
            _.-"_.____/             l       l.-l
        _.-"_.+"|                  /        \.  \\
    /"\\.-"_.-"  | |              /          \   \\
    \_   "      | |              1            | `'|
      |ll       | |              |            i   |
      \\\\       |-\            \j ..          L,,'. `/
     __\\\     ( .-\         .--'    ``--../..'      '-.
       `'''`----`\\\\ ...--'''
                  \\\\                    ---------FIM                  """)
        break