#Aluno: Bruno Henrique Benkendorf
#Data: 04/02/2025
import os
produtos = []
menu = 0

def limpa():
    os.system('cls')
    
class Produto: 
    def __init__(self,cod,nome,descricao,valor_compra,valor_venda,qtd=0):
        self.cod = str(cod)
        self.nome = nome
        self.descricao = descricao
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.qtd = qtd
        print("Produto cadastrado com sucesso")
        
def cadastrar_produto():
    cod = input("Digite o código do produto: ")
    if any(produto.cod == cod for produto in produtos):
        print("Erro: Código já cadastrado! Escolha um código único.")
        return
    
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")

    while True:
        try:
            valor_compra = float(input("Digite o valor da compra: "))
            break  
        except ValueError:
            print("Erro: Insira um valor numérico válido para a compra!")

    while True:
        try:
            valor_venda = float(input("Digite o valor da venda: "))
            if valor_venda < valor_compra:
                print("Erro: O valor de venda não pode ser menor que o valor de compra!")
            else:
                break  
        except ValueError:
            print("Erro: Insira um valor numérico válido para a venda!")

    while True:
        try:
            qtd = int(input("Digite a quantidade em estoque: "))
            if qtd < 0:
                print("Erro: A quantidade não pode ser negativa!")
            else:
                break  
        except ValueError:
            print("Erro: Insira um número inteiro válido para a quantidade!")
    
    novo_produto = Produto(cod,nome,descricao,valor_compra,valor_venda,qtd)
    produtos.append(novo_produto)
    
def alterar_produto():
    cod = input("Digite o código do produto a ser alterado: ")
    produto_encontrado = None
    
    for produto in produtos:
        if produto.cod == cod:
            produto_encontrado = produto
            break

    if produto_encontrado:
        print(f"Produto encontrado: {produto_encontrado.nome} ({produto_encontrado.cod})")
        print(f"Descrição: {produto_encontrado.descricao}")
        print(f"Valor de Compra: {produto_encontrado.valor_compra}")
        print(f"Valor de Venda: {produto_encontrado.valor_venda}")
        print(f"Quantidade: {produto_encontrado.qtd}")
        
        opcao = input("Digite o campo que deseja alterar (nome, descricao, valor_compra, valor_venda, qtd) ou 'sair' para cancelar: ").lower()
        
        if opcao == "nome":
            novo_nome = input("Novo nome: ")
            if novo_nome.strip():  
                produto_encontrado.nome = novo_nome
                print(f"Produto {produto_encontrado.cod} atualizado com sucesso!")
            else:
                print("Nome não pode ser vazio!")

        elif opcao == "descricao":
            nova_descricao = input("Nova descrição: ")
            if nova_descricao.strip():  
                produto_encontrado.descricao = nova_descricao
                print(f"Produto {produto_encontrado.cod} atualizado com sucesso!")
            else:
                print("Descrição não pode ser vazia!")
        
        elif opcao == "valor_compra":
            try:
                novo_valor_compra = float(input("Novo valor de compra: "))
                produto_encontrado.valor_compra = novo_valor_compra
                print(f"Produto {produto_encontrado.cod} atualizado com sucesso!")
            except ValueError:
                print("Valor de compra inválido! Insira um número.")

        elif opcao == "valor_venda":
            try:
                novo_valor_venda = float(input("Novo valor de venda: "))
                produto_encontrado.valor_venda = novo_valor_venda
                print(f"Produto {produto_encontrado.cod} atualizado com sucesso!")
            except ValueError:
                print("Valor de venda inválido! Insira um número.")
        
        elif opcao == "qtd":
            try:
                nova_qtd = int(input("Nova quantidade: "))
                if nova_qtd >= 0:  
                    produto_encontrado.qtd = nova_qtd
                    print(f"Produto {produto_encontrado.cod} atualizado com sucesso!")
                else:
                    print("Quantidade não pode ser negativa!")
            except ValueError:
                print("Quantidade inválida! Insira um número inteiro.")
                
        elif opcao == "sair":
            print("Alteração cancelada.")
        else:
            print("Opção inválida!")
    else:
        print("Produto não encontrado!")

def exibir_produtos(produtos_lista):
    
    print(f"{'Cod':<3} {'Nome':<30} {'Descricao':<50} {'Valor Compra':<16}{'Valor de Venda':<16}{'Quantidade':<5}")
    
    for produto in produtos_lista:
        print(f"{produto.cod:<3} {produto.nome:<30} {produto.descricao:<50} {produto.valor_compra:<16} {produto.valor_venda:<16}{produto.qtd:<5}")

produtos.append(Produto(1, 'Chapeu', 'Feito a base de lã', 10.0, 15.0, 100))
produtos.append(Produto(2, 'Boné', 'Boné da mikes', 30.0, 50.0, 200))
produtos.append(Produto(3, 'Boina', 'Boina Italiana', 70.0, 100.0, 50))

def remover_produto():
    cod = input("Digite o código do produto que deseja remover: ")
    global produtos
    produto = next((p for p in produtos if p.cod == cod), None)
    
    if produto:
        confirmacao = input(f"Tem certeza que deseja remover {produto.nome}? (s/n): ").lower()
        if confirmacao == 's':
            produtos = [p for p in produtos if p.cod != cod]
            print("Produto removido com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Erro: Produto não encontrado!")

def buscar_produto():
    busca = input("Digite o código ou nome do produto: ").lower()
    encontrado = [produto for produto in produtos if busca in produto.cod.lower() or busca in produto.nome.lower()]
    
    if encontrado:
        exibir_produtos(encontrado)
    else:
        print("Nenhum produto encontrado!")

def ordenar_produtos():
    opcao = input("Ordenar por(Cod, Nome, Valor_Compra, Valor_Venda ou QTD):").lower()
    
    if opcao in ("cod", "nome", "valor_compra", "valor_venda", "qtd"):
        produtos.sort(key=lambda produto: getattr(produto, opcao))
        print(f"produtos ordenados por {opcao} com sucesso!")
    else:
        print("Opção inválida!")

def registrar_entrada_saida():
    opcao = int(input("""Digite:
                     1 - Entrada
                     2 - Saída 
                     """))
    limpa()
    if opcao == 1:
        cod = input("Digite o código do produto recebido: ")
        produto = next((produto for produto in produtos if produto.cod == cod), None)
        
        if produto:
            qtd_recebida = int(input("Digite a quantidade recebida: "))
            produto.qtd += qtd_recebida
            print(f"Estoque Atualizada! Existem {produto.qtd} unidade de {produto.nome} agora.")
        else:
            print("Produto não encontrado!")
    elif opcao == 2:
        cod = input("Digite o código do produto vendido: ")
        produto = next((produto for produto in produtos if produto.cod == cod), None)
    
        if produto:
            qtd_venda = int(input("Digite a quantidade vendida:"))
            if qtd_venda <= produto.qtd:
                produto.qtd -= qtd_venda
                print(f"Venda confirmada! Restam {produto.qtd} unidades de {produto.nome}.")
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não encontrado!")
    else:
        print("Opção inválida!")

limpa()
print("                                                 Bem vindo ao Sistema da Loja")
input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
limpa()
while menu != 8:
    print("""
          -------------------------------------------
          |1- Adicionar                             |
          |2- Visualizar                            |
          |3- Alterar                               |
          |4- Remover                               |
          |5- Buscar                                |
          |6- Ordenar                               |
          |7- Registrar Entrada ou Saída            |
          |8- Encerrar                              |
          -------------------------------------------
          """)                  
    try:
        menu = int(input("-> "))
        if menu < 1 or menu > 8:
            raise ValueError
    except ValueError:
        print("Erro: Opção inválida! Digite um número entre 1 e 8.")
        continue
    match menu:

        case 1:
            limpa()
            cadastrar_produto()
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa()
        case 2:
            limpa()
            exibir_produtos(produtos)
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa()
        case 3:
            limpa()
            alterar_produto()
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa()
        case 4:
            limpa()
            remover_produto()
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa()
        case 5:
            limpa()
            buscar_produto()
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa()
        case 6:
            limpa()
            ordenar_produtos()
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa()           
        case 7:
            limpa()
            registrar_entrada_saida()
            input("""
                  
                  
                                            Pressione qualquer tecla para continuar""")
            limpa() 
        case 8:
            print("Operações Encerradas...")
            break                      