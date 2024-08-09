#Autor:Bruno Henrique Benkendorf
#Data: 09/08/2024
import os

i_nomePec = ""
i_cod = ""
i_desc = ""
i_valor = ""
i_qtd = ""
menu = 0
peca = []
class pecas:
    def __init__(self, nomePec, cod,desc, valor, qtd = 0):
        self.nomePec = nomePec
        self.cod = cod
        self.desc = desc 
        self.valor = valor
        self.qtd = qtd
        print("Peça Cadastrada com sucesso")
def pesquisar_peca():
    nomePec = input("Pesquisar Peça: ").upper()
    for x in range(len(peca)):
        if peca[x].nomePec == nomePec:
            return peca[x] 
    print("Não encontrado")
    return None
def limpa():
    input("Pressione Enter para continuar...")
    os.system("cls")
def mostrar_peca(peca):
    print("Nome da Peça: ", peca.nomePec)
    print("Codigo da Peça: ", peca.cod)
    print("Descrição da Peça: ", peca.desc)
    print("Valor da Peça: ", peca.valor)
    print("Quantidade de Peças: ", peca.qtd)
while menu != 5:
    limpa()
    print("""                                                                                                                                                                                                                                                                                                                                                   
                                                ####              --##            ######                                                    
                                                  ####            ####            ####  --####                                              
                                          ##        ####          mm##            ######  ######                                            
                                          ##      ######          ######        ##############                                              
                                          ############            ######        ######    ####                                              
                                            ########              ######        ######  ######                                              
                                              ##########          ######            ####  ####                                              
                                                ########          ######            ####                                                    
                                                  ######          ######            ####                                                    
                                                  ########        ######          ####                                                      
                                                    ######      ########          ##mm                                                      
                                                    ######      ##########        @@##                                                      
                                                      ######          ####      ######                                                      
                                                  ++  ######  ############  ##  ######++++++                                                
                                                  ++++######    ############mm########    ++++                                              
                                            mm++mm++mm  ######            ####      ####  mmmmmm++++                                        
                                                --mmmm  ######      ##MM  ##          ##MMmmmm                                              
                                              mmmmmmmmmm..  ####MM######--##          mmmmmmmmmm                                            
                                            MMmmmmmmmmmmmmmmmmMM              ..MMmmmmmmmmmmmmmmmmMM                                        
                                            MM          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM          MM                                        
                                              MMMM    MM  MMmmMMMMMM@@    MMMMMMMMMMMM  MM    ::MMMM                                        
                                                          MMMMMM                MMMMMM++                                                    
                                                          @@@@  @@                @@@@@@                                                    
                                                          MM@@@@                ++@@@@@@                                                    
                                                                                                                                            
                                                                                                                                            
                                             _____          __        __________                __          
                                            /  _  \  __ ___/  |_  ____\______   \_____ ________/  |_  ______
                                           /  /_\  \|  |  \   __\/  _ \|     ___/\__  \\_  __ \   __\/  ___/
                                          /    |    \  |  /|  | (  <_> )    |     / __ \|  | \/|  |  \___ \ 
                                          \____|__  /____/ |__|  \____/|____|    (____  /__|   |__| /____  >
                                                  \/                                  \/                 \/                   """)
    print("Menu: 1(Cadastro), 2(Adicionar), 3(Mostrar), 4(Pesquisar), 5(Encerrar)")
    menu = int(input("-> "))
    match menu:
        case 1:
            i_nomePec = input("Nome da peça: ").upper()
            i_cod = input("Digite o Cod: ")
            i_desc = input("Descrição: ")
            i_valor = input("Valor: ")
            peca.append(pecas(i_nomePec,i_cod,i_desc,i_valor))
        case 2: 
            index_nome = pesquisar_peca()
            try:
                index_nome = int(index_nome)
                i_qtd = input("Digite a quantidade de peças:")
                peca[index_nome].qtd = i_qtd
            except:
                print("Erro ao adicionar")
        case 3: 
            for x in range(len (peca)):
                mostrar_peca(peca[x])
        case 4:
            peca_encontrada = pesquisar_peca()
            if peca_encontrada:
                print("Peça encontrada: ")
                mostrar_peca(peca_encontrada)
            else:
                print("Peça não encontrada")
        case 5:
            break