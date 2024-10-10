#Autor:Bruno Henrique Benkendorf
#Data: 02/10/2024
import os
frutas = []
verduras = []
legumes = []
menu = 0
escolha = 0
def limpa():
    os.system('cls')
class Planta:
    def __init__(self,nome,ambiente,vegetacao,caracteristica,flor,fruto):
        self.nome = nome
        self.ambiente = ambiente
        self.vegetacao = vegetacao
        self.caracteristica = caracteristica
        self.flor = flor
        self.fruto = fruto
        self.molhado = 0
    def Regar(self, dias_regados, dias_maximos):
        self.molhado += dias_regados
        if self.molhado < dias_maximos:
            return print("Você deve regar",self.nome ,"por mais ",dias_maximos - self.molhado, "dias.")
        else:
            self.molhado = self.molhar_Max
            return print("A planta ja foi molhada o suficiente")
def Regar_Tipo():
    escolha = int(input("Escolha qual planta deseja Regar:(1-Frutas|2-Verduras|3-Legumes)"))
    nome = input("Digite o nome da planta: ")
    dias_regados = int(input("Digite os dias que foram regados usando(Numeros):"))
    dias_maximos = int(input("Digite os dias maximos que essa planta pode ser regada: "))
    planta = None
    if escolha == 1:
        planta = pesquisar_frutas(frutas, nome)
    elif escolha == 2:
        planta = pesquisar_verduras(verduras, nome)
    elif escolha == 3:
        planta = pesquisar_legumes(legumes, nome)
    if planta:
        planta.Regar(dias_regados,dias_maximos)
    else:
        print("Planta não encontrada")
class Fruta(Planta):
    def __init__(self,nome,ambiente,vegetacao,caracteristica,flor,fruto,sabor):
        super().__init__(nome,ambiente,vegetacao,caracteristica,flor,fruto)
        self.sabor = sabor
        print("Fruta: ", self.nome, " Cadastrado!")
def cadastrar_Fruta():
    nome = input("Digite o nome da Fruta: ")
    ambiente = input("Digite o ambiente da Fruta: ")
    vegetacao = input("Digite a vegetação da Fruta: ") 
    caracteristica = input("Digite a caracteristica da Fruta: ")
    flor = input("Digite as carcteristicas da Flor: ")
    fruto = input("Digite as caracteristicas da Fruta: ")   
    sabor = input("Qual o sabor da Fruta: ")  
    nova_Fruta = Fruta(nome, ambiente, vegetacao, caracteristica, flor, fruto, sabor) 
    frutas.append(nova_Fruta)
def exibir_frutas(frutas_lista):
        print(f"{'Nome':<20} {'Ambiente':<20} {'Vegetação':<20} {'Característica':<30} {'Flor':<20} {'Fruto':<20} {'Sabor':<8}")
        for fruta in frutas_lista:
            print(f"{fruta.nome:<20} {fruta.ambiente:<20} {fruta.vegetacao:<20} {fruta.caracteristica:<30} {fruta.flor:<20} {fruta.fruto:<20} {fruta.sabor:<8}")
def pesquisar_frutas(frutas,nome):
    for fruta in frutas:
        if fruta.nome == nome:
            return fruta
    return None
class Verdura(Planta):
    def __init__(self,nome,ambiente,vegetacao,caracteristica,flor,fruto,sabor):
        super().__init__(nome,ambiente,vegetacao,caracteristica,flor,fruto)
        self.sabor = sabor
        print("Verdura: ", self.nome, " Cadastrado!")
def cadastrar_Verdura():
    nome = input("Digite o nome da Verdura: ")
    ambiente = input("Digite o ambiente da Verdura: ")
    vegetacao = input("Digite a vegetação da Verdura: ") 
    caracteristica = input("Digite a caracteristica da Verdura: ")
    flor = input("Digite as carcteristicas da Flor: ")
    fruto = input("Digite as caracteristicas da Fruta: ") 
    sabor = input("Qual o sabor da Verdura: ")    
    nova_Verdura = Verdura(nome, ambiente, vegetacao, caracteristica, flor, fruto, sabor) 
    verduras.append(nova_Verdura)
def exibir_verduras(verduras_lista):
        print(f"{'Nome':<20} {'Ambiente':<20} {'Vegetação':<20} {'Característica':<30} {'Flor':<20} {'Fruto':<20} {'Sabor':<8}")
        for verdura in verduras_lista:
            print(f"{verdura.nome:<20} {verdura.ambiente:<20} {verdura.vegetacao:<20} {verdura.caracteristica:<30} {verdura.flor:<20} {verdura.fruto:<20} {verdura.sabor:<8}") 
def pesquisar_verduras(verduras,nome):
    for verdura in verduras:
        if verdura.nome == nome:
            return verdura
    return None
class Legume(Planta):
    def __init__(self,nome,ambiente,vegetacao,caracteristica,flor,fruto,sabor):
        super().__init__(nome,ambiente,vegetacao,caracteristica,flor,fruto)
        self.sabor = sabor
        print("Legume: ", self.nome, " Cadastrado!")
def cadastrar_Legume():
    nome = input("Digite o nome do Legume: ")
    ambiente = input("Digite o ambiente do Legume: ")
    vegetacao = input("Digite a vegetação do Legume: ") 
    caracteristica = input("Digite a caracteristica do Legume: ")
    flor = input("Digite as carcteristicas da Flor: ")
    fruto = input("Digite as caracteristicas do Fruto: ") 
    sabor = input("Qual o sabor do Legume: ")    
    novo_Legume = Legume(nome, ambiente, vegetacao, caracteristica, flor, fruto, sabor) 
    legumes.append(novo_Legume)
def exibir_legumes(legumes_lista):
        print(f"{'Nome':<20} {'Ambiente':<20} {'Vegetação':<20} {'Característica':<30} {'Flor':<20} {'Fruto':<20} {'Sabor':<8}")
        for legume in legumes_lista:
            print(f"{legume.nome:<20} {legume.ambiente:<20} {legume.vegetacao:<20} {legume.caracteristica:<30} {legume.flor:<20} {legume.fruto:<20} {legume.sabor:<8}")
def pesquisar_legumes(legumes,nome):
    for legume in legumes:
        if legume.nome == nome:
            return legume
    return None
frutas.append(Fruta("Abacate","Tropical","Verde","Fruta tipica do Brasil","Flor Rosa","Fruta verde","Doce"))
verduras.append(Verdura("Alface","Temperado","Folhas agrupadas","podem variar em textura","Flores Amarelas","Seu fruto é verde","Suave"))
legumes.append(Legume("Pimentão","Tropical"," Erva perene","Cores Vibrantes","Flor branca","Baga com sementes","suave"))
limpa()
while menu != 5:
    print("""
          1- Exibir
          2- Cadastrar
          3- Pesquisar
          4- Regar
          5- Encerrar""")
    menu = int(input("-> "))
    match menu:
        case 1:
            limpa()
            escolha = int(input("Escolha qual deseja exibir:(1-Frutas|2-Verduras|3-Legumes) "))
            match escolha:
                case 1:
                    exibir_frutas(frutas)
                case 2:
                    exibir_verduras(verduras)
                case 3:
                    exibir_legumes(legumes)
        case 2:
            limpa()
            escolha = int(input("Escolha qual deseja cadastrar:(1-Frutas|2-Verduras|3-Legumes"))
            match escolha:
                case 1:
                    cadastrar_Fruta()
                case 2:
                    cadastrar_Verdura()
                case 3:
                    cadastrar_Legume()
        case 3:
            limpa()
            escolha = int(input("Escolha qual deseja pesquisar:(1-Frutas|2-Verduras|3-Legumes"))
            match escolha:
                case 1:
                    nome = input("Digite o nome da fruta: ")
                    resultado = pesquisar_frutas(frutas, nome)
                    if resultado:
                        print("Fruta encontrada")
                        exibir_frutas([resultado])
                    else: 
                        print("Fruta não encontrada")
                case 2:
                    nome = input("Digite o nome da verdura: ")
                    resultado = pesquisar_verduras(verduras, nome)
                    if resultado:
                        print("Verdura encontrada")
                        exibir_verduras([resultado])
                    else:
                        print("Verdura não encontrada")
                case 3:
                    nome = input("Digite o nome do legume: ")
                    resultado = pesquisar_legumes(legumes, nome)
                    if resultado:
                        print("Legume encontrado")
                        exibir_legumes([resultado])
                    else:
                        print("Legume não encontrado")
        case 4:
            limpa()
            Regar_Tipo()
        case 5:
            limpa()
            print("Obrigado por utilizar o sistema")
            break