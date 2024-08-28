#Autor:Bruno Henrique Benkendorf
#Data: 28/08/2024
import os 

menu = 0
area = 0
perimetro = 0
volume = 0

def quadradoPer(perimetro):
    return perimetro/4

def quadradoAr (area):
    return area ** 0.5

def retanguloLado (lado,area):
    return area / lado

def circuloArea(raio):
    return (3.14 *(raio**2))

def circuloPerimetro(a):
    return (2*3.14*a)

def circuloDiametro(area):
    raio =(area / 3.14)**0.5
    return  2 * raio

def cilindroVolume(raio,altura):
    return(3.14*(raio**2)*altura)

def cilindroAltura(volume, diametro):
    raio = diametro / 2
    return volume / (3.14 * (raio**2))
def limpa():
    input("Pressione Enter para continuar...")
    os.system("cls")
    
while menu != 5:

    limpa()

    print("""
_________        .__               .__              .___                    
\_   ___ \_____  |  |   ____  __ __|  | _____     __| _/________________    
/    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \   / __ |/  _ \_  __ \__  \   
\     \____/ __ \|  |_\  \___|  |  /  |__/ __ \_/ /_/ (  <_> )  | \// __ \_ 
 \______  (____  /____/\___  >____/|____(____  /\____ |\____/|__|  (____  / 
        \/     \/          \/                \/      \/                 \/     
  ________                             __         .__               
 /  _____/  ____  ____   _____   _____/  |________|__| ____ _____   
/   \  ____/ __ \/  _ \ /     \_/ __ \   __\_  __ \  |/ ___\\__  \  
\    \_\  \  ___(  <_> )  Y Y  \  ___/|  |  |  | \/  \  \___ / __ \_
 \______  /\___  >____/|__|_|  /\___  >__|  |__|  |__|\___  >____  /
        \/     \/            \/     \/                    \/     \/    
          """)
    
    limpa()

    menu = int(input("Escolha uma opção |Quadrado - 1|Retangulo - 2|Circulo - 3|Cilindro - 4|Encerrar - 5| : "))
    limpa()
    match menu:
        case 1:

            print("Inicio calculos do Quadro!")

            menu = int(input("Escolha a operação do Quadrado |Area - 1|Perimetro - 2|Calculo Lados - 3| : "))
            limpa()
            match menu:
                case 1:
                    lado = float(input("Digite um dos lados do quadrado: "))
                    area = lado**2
                    print("Área do quadrado: ", area)
                case 2:
                    lado = float(input("Digite um dos lados do quadrado: "))
                    perimetro = lado*4
                    print("Perimetro do Quadrado: ", perimetro)
                case 3:
                    menu = int(input("Escolha se dejesa calcular pelo meio |Area - 1|Perimetro - 2| : "))
                    if(menu == 1):
                        area = float(input("Digite a area do quadrado : "))
                        lado = quadradoAr(area)
                        print("Tamanho do lado: ", lado)
                    elif(menu == 2):
                        perimetro = float(input("Digite o perimetro do quadrado: "))
                        lado = quadradoPer(perimetro)
                        print("Tamanho do lado: ", lado)

        case 2:
            print("Inicio calculos do Retangulo!")

            menu = int(input("Escolha a operação do Retangulo |Area - 1|Perimetro - 2|Calculo Lados - 3| : "))
            limpa()
            match menu:
                case 1:
                    ladomenor = float(input("Digite o lado menor do retangulo: "))
                    ladomaior = float(input("Digite o lado maior do retangulo: "))
                    area = ladomenor * ladomaior
                    print("Area do Retangulo: ", area)
                case 2: 
                    ladomenor = float(input("Digite o lado menor do retangulo: "))
                    ladomaior = float(input("Digite o lado maior do retangulo: "))
                    perimetro = 2*(ladomenor + ladomaior)
                    print("Perimetro do Retangulo: ", perimetro)
                case 3: 
                    lado = float(input("Digite um dos lados do retangulo: "))
                    area = float(input("Digite a area do retangulo: "))
                    lado = retanguloLado(area, lado)
                    print("Tamanho do lado descoberto: ", lado)
        case 3: 
            print("Inicio calculos do Circulo!")
            limpa()
            menu = int(input("Escolha a operação do Circulo |Area - 1|Perimetro - 2|Diâmetro - 3| : "))

            match menu:
                case 1:
                    raio = float(input("Digite o raio do circulo: "))
                    area = circuloArea(raio)
                    print("Area do Circulo: ", area)
                case 2: 
                    raio = float(input("Digite o raio do circulo: "))
                    perimetro = circuloPerimetro(raio)
                    print("Perimetro do Circulo: ", perimetro)
                case 3: 
                    area= int(input("Digite a area do circulo: "))
                    diametro = circuloDiametro(area)
                    print("Diametro do Circulo: ", diametro)
        case 4:
            print("Inicio calculos do Cilindro!")
            limpa()
            menu = int(input("Escolha a operação do Circulo |Volume - 1|Altura - 2| : "))

            match menu:
                case 1:
                    raio = float(input("Digite o raio da base do cilindro: "))
                    altura = float(input("Digite a altura do cilindro: "))
                    volume = cilindroVolume(raio,altura)
                    print("Volume do Cilindro: ", volume)
                case 2:  
                    volume = float(input("Digite o volume do cilindro: "))
                    diametro = float(input("Digite o diametro do cilindro: "))
                    altura = cilindroAltura(volume,diametro)
                    print("Altura do Cilindro: ", altura)
        case 5: 
            print("Fim!")
            break