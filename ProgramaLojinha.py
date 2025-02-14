#Aluno: Bruno Henrique Benkendorf
#Data: 12'/02/2025
import os
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='lojinha',
    charset='utf8mb4',
    port=3307,
    cursorclass=pymysql.cursors.DictCursor
)

produtos = []
menu = 0

def limpa():
    os.system('cls')

class Produto:
    def __init__(self, cod, nome, descricao, valor_compra, valor_venda, qtd=0):
        self.cod = str(cod)
        self.nome = nome
        self.descricao = descricao
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.qtd = qtd
        print("Produto cadastrado com sucesso!")

def cadastrar_produto_banco(produto: Produto):
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO produtos (cod, nome, descricao, valor_compra, valor_venda, qtd) VALUES (%s, %s, %s, %s, %s, %s) """
            cursor.execute(sql, (produto.cod, produto.nome, produto.descricao, produto.valor_compra, produto.valor_venda, produto.qtd))
            conn.commit()
            print("Produto cadastrado com sucesso no banco de dados!")
    except Exception:
        print("Erro ao cadastrar produto no banco")

def exibir_produtos():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            
            if produtos:
                print(f"{'Cod':<10} {'Nome':<30} {'Descricao':<50} {'Valor Compra':<16}{'Valor de Venda':<16}{'Quantidade':<5}")
                for produto in produtos:
                    print(f"{produto['cod']:<10} {produto['nome']:<30} {produto['descricao']:<50} {produto['valor_compra']:<16} {produto['valor_venda']:<16}{produto['qtd']:<5}")
            else:
                print("Nenhum produto encontrado no banco de dados.")
    except Exception:
        print("Erro ao exibir produtos do banco")

def alterar_produto_banco(cod: str, campo: str, novo_campo):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM produtos WHERE cod = %s", (cod,))
            if cursor.fetchone() is None:
                print(f"Produto com código {cod} não existe!")
                return
            if campo == "nome":
                sql = "UPDATE produtos SET nome = %s WHERE cod = %s"
            elif campo == "descricao":
                sql = "UPDATE produtos SET descricao = %s WHERE cod = %s"
            elif campo == "valor_compra":
                sql = "UPDATE produtos SET valor_compra = %s WHERE cod = %s"
            elif campo == "valor_venda":
                sql = "UPDATE produtos SET valor_venda = %s WHERE cod = %s"
            elif campo == "qtd":
                sql = "UPDATE produtos SET qtd = %s WHERE cod = %s"
            elif campo == "cod":
                sql = "UPDATE produtos SET cod = %s WHERE cod = %s"
            else:
                print("Campo inválido!")
                return
            
            cursor.execute(sql, (novo_campo, cod))
            conn.commit()
            print(f"Produto {cod} atualizado no banco de dados com sucesso!")
    except Exception:
        print("Erro ao alterar produto no banco")

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
            while True:
                try:
                    qtd_recebida = input("Digite a quantidade recebida: ")
                    if not qtd_recebida:  
                        print("Erro: A quantidade não pode ser vazia!")
                        continue
                    qtd_recebida = int(qtd_recebida) 
                    if qtd_recebida <= 0:
                        print("Erro: A quantidade deve ser maior que zero!")
                        continue
                    break
                except ValueError:
                    print("Erro: Insira um número válido para a quantidade!")
                
            produto.qtd += qtd_recebida
            print(f"Estoque Atualizado! Existem {produto.qtd} unidades de {produto.nome} agora.")
            alterar_produto_banco(produto.cod, 'qtd', produto.qtd)
        else:
            print("Produto não encontrado!")
    
    elif opcao == 2:
        cod = input("Digite o código do produto vendido: ")
        produto = next((produto for produto in produtos if produto.cod == cod), None)
    
        if produto:
            while True:
                try:
                    qtd_venda = input("Digite a quantidade vendida: ")
                    if not qtd_venda:  
                        print("Erro: A quantidade não pode ser vazia!")
                        continue
                    qtd_venda = int(qtd_venda)  
                    if qtd_venda <= 0:
                        print("Erro: A quantidade deve ser maior que zero!")
                        continue
                    if qtd_venda > produto.qtd:
                        print("Erro: Estoque insuficiente!")
                        continue
                    break
                except ValueError:
                    print("Erro: Insira um número válido para a quantidade!")
                
            produto.qtd -= qtd_venda
            print(f"Venda confirmada! Restam {produto.qtd} unidades de {produto.nome}.")
            alterar_produto_banco(produto.cod, 'qtd', produto.qtd)
        else:
            print("Produto não encontrado!")
    else:
        print("Opção inválida!")


def cadastrar_produto():
    cod = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")

    while True:
        try:
            valor_compra = input("Digite o valor da compra: ")
            valor_compra = valor_compra.replace(",",".")
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

    novo_produto = Produto(cod, nome, descricao, valor_compra, valor_venda, qtd)
    cadastrar_produto_banco(novo_produto)
def remover_produto_banco(cod: str):
    confirmacao = input(f"Tem certeza de que deseja remover o produto com o código {cod}? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("Ação cancelada. O produto não foi removido.")
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM produtos WHERE cod = %s"
            cursor.execute(sql, (cod,))
            conn.commit()
            print(f"Produto {cod} removido do banco de dados com sucesso!")
    except Exception as e:
        print(f"Erro ao remover produto do banco: {e}")
def carregar_produtos_banco():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM produtos")
            produtos_banco = cursor.fetchall()
            global produtos
            produtos = [Produto(produto['cod'], produto['nome'], produto['descricao'], produto['valor_compra'], produto['valor_venda'], produto['qtd']) for produto in produtos_banco]
    except Exception:
        print("Erro ao carregar produtos do banco")

limpa()
print("         Bem-vindo ao Sistema da Loja")
input("     Pressione qualquer tecla para continuar...")
limpa()
carregar_produtos_banco()
limpa()
while menu != 8:
        print("""
          -------------------------------------------
          |1- Adicionar                             |
          |2- Visualizar                            |
          |3- Alterar                               |
          |4- Remover                               |
          |5- Registrar Entrada ou Saída            |
          |6- Encerrar                              |
          -------------------------------------------
          """)                   
        try:
            menu = int(input("-> "))
            if menu < 1 or menu > 6:
                raise ValueError
        except ValueError:
            limpa()
            print("Erro: Opção inválida! Digite um número entre 1 e 8.")
            continue
        match menu:
            case 1:
                limpa()
                cadastrar_produto()
                input("Pressione qualquer tecla para continuar...")
                limpa()
            case 2:
                limpa()
                exibir_produtos()
                input("Pressione qualquer tecla para continuar...")
                limpa()
            case 3:
                limpa()
                cod = input("Digite o código do produto a ser alterado: ")
                campo = input("Digite o campo que deseja alterar (cod,nome, descricao, valor_compra, valor_venda, qtd): ").lower()
                novo_campo = input("Digite o novo campo: ")
                alterar_produto_banco(cod, campo, novo_campo)
                input("Pressione qualquer tecla para continuar...")
                limpa()
            case 4:
                limpa()
                cod = input("Digite o código do produto a ser alterado: ")
                remover_produto_banco(cod)
                input("Pressione qualquer tecla para continuar...")
                limpa()
            case 5:
                limpa()
                registrar_entrada_saida()
                input("Pressione qualquer tecla para continuar...")
                limpa()
            case 6:
                print("Operações Encerradas...")
                break