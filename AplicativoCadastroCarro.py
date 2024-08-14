#Autor:Bruno Henrique Benkendorf
#Data: 14/08/2024
import os

i_marca =""
i_nome = ""
i_modelo = ""
i_capacidade = ""
i_desempenho = ""
menu = 0
carros = []
class Carro:
    def __init__(self,marca,nome,modelo,capacidade,desempenho):
        self.marca = marca
        self.nome = nome
        self.modelo = modelo
        self.capacidade = float(capacidade)
        self.desempenho = float(desempenho)
        print("Carro Cadastrado com sucesso!")
def autonomia(combustivel_dis,desempenho):
    autonomia = combustivel_dis * desempenho
    return autonomia
def combustivel_necessario(distancia, autonomia_veiculo, capacidade_tanque):
    combustivel_necessario = distancia / autonomia_veiculo
    paradas_abastecer = int(combustivel_necessario / capacidade_tanque)
    return combustivel_necessario, paradas_abastecer
def limpa():
    input("Pressione Enter para continuar...")
    os.system("cls")
def mostrar_carros(carro):
    print("Marca do Veiculo: ", carro.marca)
    print("Nome do Veiculo: ", carro.nome)
    print("Modelo do Veiculo: ", carro.modelo)
    print("Capacidade do Tanque: ", carro.capacidade)
    print("Desempenho: ", carro.desempenho)

def pesquisar_carro_marca(marca, carros):
    for carro in carros:
        if carro.marca == marca:
            return carro
    return None

def pesquisar_carro_nome(nome, carros):
    for carro in carros:
        if carro.nome == nome:
            return carro
    return None
while menu != 6:
    limpa()
    print("""           
                         APLICATIVO CARROS
                       ____________________                              
                     //|           |        \                            
                   //  |           |          \                          
      ___________//____|___________|__________()\__________________      
    /__________________|_=_________|_=___________|_________________{}    
    [           ______ |           | .           | ==  ______      { }   
  __[__        /##  ##\|           |             |    /##  ##\    _{# }_ 
 {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
             /  ##__##                              /  ##__##        \   """)
    print("""
          Selecione a operação desejada:
          1- Cadastro de Veiculo 
          2- Visualizar Tudo
          3- Pesquisar Veiculo
          4- Calculo Autonomia
          5- Calculo Distancia percorrida
          6- Encerrar
          """) 
    menu = int(input("-> "))
    match menu:
        case 1:
            i_marca = input("Qual a marca do Veiculo: ")
            i_nome = input("Qual o nome do Veiculo: ")
            i_modelo = input("Qual o modelo do Veiculo(Compacto, Sedan, SUV…): ")
            i_capacidade = input("Qual a capacidade de Combustivel do Veiculo: ")
            i_desempenho = input("Qual o desempenho do Veiculo(Km/l):")
            carros.append(Carro(i_marca,i_nome,i_modelo,i_capacidade,i_desempenho))
        case 2:
            for x in range(len(carros)):
                mostrar_carros(carros[x])
        case 3:
            pesquisa = input("Pesquisar Por Marca ou Nome (M/N): ")
            if pesquisa.upper() == "M":
                marca = input("Digite a marca: ")
                carro_encontrado = pesquisar_carro_marca(marca, carros)
                if carro_encontrado:
                    print("Carro encontrado: ")
                    mostrar_carros(carro_encontrado)
                else:
                    print("Marca não encontrada")
            elif pesquisa.upper() == "N":
                nome = input("Digite o nome: ")
                carro_encontrado = pesquisar_carro_nome(nome, carros)
                if carro_encontrado:
                    print("Carro encontrado: ")
                    mostrar_carros(carro_encontrado)
                else:
                    print("Nome não encontrado")
        case 4:
            nome = input("Digite o nome do Veiculo para calcular a autonomia: ")
            carro_encontrado = pesquisar_carro_nome(nome, carros)
            if carro_encontrado:
                combustivel_disponivel = float(input("Digite o combustível disponível (em litros): "))
                autonomia_veiculo = autonomia(combustivel_disponivel, carro_encontrado.desempenho)
                print("A autonomia do veículo é de:", autonomia_veiculo, "KM")
            else:
                print("Veículo não encontrado")
        case 5:
            nome = input("Digite o nome do Veiculo para calcular a distância percorrida: ")
            carro_encontrado = pesquisar_carro_nome(nome, carros)
            if carro_encontrado:
                distancia = float(input("Digite a distância que deseja percorrer (em KM): "))
                combustivel_disponivel = float(input("Digite a quantidade de combustível disponível no tanque (em litros): "))
                
                autonomia_veiculo = autonomia(combustivel_disponivel, carro_encontrado.desempenho)
                combustivel_necessario, paradas_abastecer = combustivel_necessario(distancia, autonomia_veiculo, carro_encontrado.capacidade)
                
                print("Combustível necessário: ", combustivel_necessario, "litros")
                print("Paradas para abastecer: ", paradas_abastecer, "vezes")
            else:
                print("Veículo não encontrado")
        case 6:
            print("Programa Encerrado!!!")
            break