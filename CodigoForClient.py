#Aluno: Bruno Henrique Benkendorf
#Data: 18/02/2025
import os
import pymysql
import requests

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='lojinha',
    charset='utf8mb4',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
clientes = []
fornecedores = []
menu = 0

def limpa():
    os.system('cls')

def buscar_endereco_cep(cep):
    try:
        
        cep = ''.join(filter(str.isdigit, cep))

        if len(cep) != 8:
            print("CEP inválido! Certifique-se de digitar 8 dígitos.")
            return

        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                print("Endereço encontrado:")
                print(f"Rua: {dados['logradouro']}")
                print(f"Bairro: {dados['bairro']}")
                print(f"Cidade: {dados['localidade']}")
                print(f"Estado: {dados['uf']}")
                return dados
            else:
                print("CEP não encontrado.")
        else:
            print("Erro na consulta do CEP.")
    except Exception as e:
        print(f"Erro ao buscar endereço: {e}")
        
class Cliente:
    def __init__(self, cpf, nome_cliente, email_cliente, telefone_cliente, cadastro, estado, cidade,bairro, rua, numero, cep):
        self.cpf = str(cpf)
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.telefone_cliente = telefone_cliente
        self.cadastro = cadastro
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero= numero
        self.cep = cep
        print("Cliente cadastrado com sucesso!")

def cadastrar_cliente_banco(cliente: Cliente):
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO clientes (cpf, nome_cliente, email_cliente, telefone_cliente, cadastro, estado, cidade,bairro, rua, numero, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(sql, (cliente.cpf, cliente.nome_cliente, cliente.email_cliente, cliente.telefone_cliente, cliente.cadastro,
                                 cliente.estado, cliente.cidade,cliente.bairro, cliente.rua,cliente.numero, cliente.cep))
            conn.commit()
            print("Cliente cadastrado com sucesso no banco de dados!")
    except Exception:
        print("Erro ao cadastrar cliente no banco")  

def cadastrar_cliente():
    cpf = input("Digite o CPF do cliente: (xxx.xxx.xxx-xx) ")
    nome_cliente = input("Digite o nome do cliente: ")
    email_cliente = input("Digite o email do cliente: ")
    telefone_cliente = input("Digite o telefone do cliente: ((xx)xxxxx-xxxx) ")
    cadastro = 'ATIVO'
    
    cep = input("Digite o CEP do cliente: ")
    endereco = buscar_endereco_cep(cep)
    
    if endereco:
        estado = endereco['uf']
        cidade = endereco['localidade']
        bairro = endereco['bairro']
        rua = endereco['logradouro']
    else:
        estado = input("Digite o estado do cliente: (UF) ")
        cidade = input("Digite o nome da cidade do cliente: ")
        bairro = input("Digite o bairro da cidade:")
        rua = input("Digite a rua do cliente: ")
    numero = input("Digite o numero do endereço:")
    novo_cliente = Cliente(cpf, nome_cliente, email_cliente, telefone_cliente, cadastro, estado, cidade,bairro, rua, numero, cep)
    cadastrar_cliente_banco(novo_cliente)


def exibir_clientes():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            
            if clientes:
                print(f"{'CPF':<14} {'Nome':<30} {'Email':<50} {'Telefone':<14}{'Cadastro':<14}{'Estado':<7}{'Cidade':<15}{'Bairro':<15}{'Rua':<30}{'Cep':<0}")
                for cliente in clientes:
                    print(f"{cliente['cpf']:<14} {cliente['nome_cliente']:<30} {cliente['email_cliente']:<50} {cliente['telefone_cliente']:<14} {cliente['cadastro']:<14}{cliente['estado']:<7}{cliente['cidade']:<15}{cliente['bairro']:<15}{cliente['rua']:<30}{cliente['cep']:<0}")
            else:
                print("Nenhum cliente encontrado no banco de dados.")
    except Exception:
        print("Erro ao exibir clientes do banco")

def alterar_cliente_banco(cpf: str, campo: str, novo_campo):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM clientes WHERE cpf = %s", (cpf,))
            if cursor.fetchone() is None:
                print(f"Cliente com o CPF {cpf} não existe!")
                return
            elif campo == "Email":
                sql = "UPDATE clientes SET email_cliente = %s WHERE cpf = %s"
            elif campo == "Telefone":
                sql = "UPDATE clientes SET telefone_cliente = %s WHERE cpf = %s"
            elif campo == "Cadastro":
                sql = "UPDATE clientes SET cadastro = %s WHERE cpf = %s"
            elif campo == "Estado":
                sql = "UPDATE clientes SET estado = %s WHERE cpf = %s"
            elif campo == "Cidade":
                sql = "UPDATE clientes SET cidade = %s WHERE cpf = %s"
            elif campo == "Bairro":
                sql = "UPDATE clientes SET bairro = %s WHERE cpf =%s"
            elif campo == "Rua":
                sql = "UPDATE clientes SET rua = %s WHERE cpf = %s"
            elif campo == "Numero":
                sql = "UPDATE clientes SET numero = %s WHERE cpf = %s"
            else:
                print("Campo inválido!")
                return
            
            cursor.execute(sql, (novo_campo, cpf))
            conn.commit()
            print(f"Cliente {cpf} atualizado no banco de dados com sucesso!")
    except Exception:
        print("Erro ao alterar cliente no banco")

def remover_cliente_banco(cpf: str):
    confirmacao = input(f"Tem certeza de que deseja remover o cliente com o CPF {cpf}? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("Ação cancelada. O cliente não foi removido.")
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE cpf = %s"
            cursor.execute(sql, (cpf,))
            conn.commit()
            print(f"Cliente {cpf} removido do banco de dados com sucesso!")
    except Exception as e:
        print(f"Erro ao remover cliente do banco: {e}")

def carregar_clientes_banco():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes")
            clientes_banco = cursor.fetchall()
            global clientes
            clientes = [Cliente(cliente['cpf'], cliente['nome_cliente'], cliente['email_cliente'], cliente['telefone_cliente'],
                                cliente['cadastro'], cliente['estado'], cliente['cidade'],cliente['bairro'], cliente['rua'],cliente['numero'],cliente['cep']) for cliente in clientes_banco]
    except Exception:
        print("Erro ao carregar clientes do banco")

def pesquisa_cliente():
    tipo_regiao = input("Digite a região do cliente que deseja pesquisar: (NORTE, NORDESTE, CENTRO-OESTE, SUL, SUDESTE): ").strip().upper()

    estados_por_regiao = {
        "NORTE": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
        "NORDESTE": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE", "BA"],
        "CENTRO-OESTE": ["DF", "GO", "MS", "MT"],
        "SUL": ["PR", "RS", "SC"],
        "SUDESTE": ["ES", "MG", "RJ", "SP"]
    }

    if tipo_regiao not in estados_por_regiao:
        print("Região inválida! Tente novamente.")
        return
    
    estados = estados_por_regiao[tipo_regiao]

    try:
        with conn.cursor() as cursor:
            estado_placeholder = ', '.join(["%s"] * len(estados))  
            sql = f"SELECT * FROM clientes WHERE estado IN ({estado_placeholder})"
            cursor.execute(sql, estados)
            clientes_encontrados = cursor.fetchall()
            
            if clientes_encontrados:
                print(f"{'CPF':<14} {'Nome':<30} {'Email':<50} {'Telefone':<14}{'Cadastro':<14}{'Estado':<7}{'Cidade':<15}{'Rua':<0}")
                for cliente in clientes_encontrados:
                    print(f"{cliente['cpf']:<14} {cliente['nome_cliente']:<30} {cliente['email_cliente']:<50} {cliente['telefone_cliente']:<14} {cliente['cadastro']:<14}{cliente['estado']:<7}{cliente['cidade']:<15}{cliente['rua']:<0}")
            else:
                print(f"Nenhum cliente encontrado na região '{tipo_regiao}'.")
    except Exception as e:
        print(f"Erro ao pesquisar clientes: {e}")

carregar_clientes_banco()

class Fornecedor:
    def __init__(self, cnpj, nome_fornecedor, tipo_fornecedor, email_fornecedor, telefone_fornecedor, prazo_pagamento, estado, cidade, bairro, rua, numero, cep):
        self.cnpj = str(cnpj)
        self.nome_fornecedor = nome_fornecedor
        self.tipo_fornecedor = tipo_fornecedor
        self.email_fornecedor = email_fornecedor
        self.telefone_fornecedor = telefone_fornecedor
        self.prazo_pagamento = prazo_pagamento
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.cep = cep
        print("Fornecedor cadastrado com sucesso!")



def cadastrar_fornecedor_banco(fornecedor: Fornecedor):
    try:
        with conn.cursor() as cursor:
            sql = """INSERT INTO fornecedores (cnpj, nome_fornecedor, tipo_fornecedor, email_fornecedor, telefone_fornecedor, prazo_pagamento, estado, cidade, bairro, rua, numero, cep) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (fornecedor.cnpj, fornecedor.nome_fornecedor, fornecedor.tipo_fornecedor, fornecedor.email_fornecedor, fornecedor.telefone_fornecedor,
                                 fornecedor.prazo_pagamento, fornecedor.estado, fornecedor.cidade, fornecedor.bairro, fornecedor.rua, fornecedor.numero, fornecedor.cep))
            conn.commit()
            print("Fornecedor cadastrado com sucesso no banco de dados!")
    except pymysql.MySQLError as e:
        print(f"Erro MySQL ao cadastrar fornecedor: {e}")
    except Exception as e:
        print(f"Erro inesperado ao cadastrar fornecedor: {e}")
  

def cadastrar_fornecedor():
    cnpj = input("Digite o CNPJ do fornecedor: (xx.xxx.xxx/xxxx-xx)")
    nome_fornecedor = input("Digite o nome do fornecedor: ")
    tipo_fornecedor = input("Digite o tipo do fornecedor:")
    email_fornecedor = input("Digite o email do fornecedor:")
    telefone_fornecedor = input("Digite o telefone do fornecedor: ((xx)xxxxx-xxxx)")
    prazo_pagamento = input("Digite o prazo de pagamento em dias:")
    cep = input("Digite o CEP do fornecedor: ")
    endereco = buscar_endereco_cep(cep)
    
    if endereco:
        estado = endereco['uf']
        cidade = endereco['localidade']
        bairro = endereco['bairro']
        rua = endereco['logradouro']
    else:
        estado = input("Digite o estado do fornecedor: (UF) ")
        cidade = input("Digite o nome da cidade do fornecedor: ")
        bairro = input("Digite o bairro da cidade")
        rua = input("Digite a rua do bairro: ")
    numero = input("Digite o numero do endereço:")

    novo_fornecedor = Fornecedor(cnpj, nome_fornecedor, tipo_fornecedor, email_fornecedor, telefone_fornecedor, prazo_pagamento, estado, cidade, bairro,rua, numero, cep)
    cadastrar_fornecedor_banco(novo_fornecedor)   

def exibir_fornecedor():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM fornecedores")
            fornecedores = cursor.fetchall()
            
            if fornecedores:
                print(f"{'CNPJ':<18} {'Nome':<30} {'Tipo':<14} {'Email':<35}{'Telefone':<21}{'Prazo de Pagamento':<15}")
                for fornecedor in fornecedores:
                    print(f"{fornecedor['cnpj']:<18} {fornecedor['nome_fornecedor']:<30} {fornecedor['tipo_fornecedor']:<14} {fornecedor['email_fornecedor']:<34} {fornecedor['telefone_fornecedor']:<21}{fornecedor['prazo_pagamento']:<30}")
            else:
                print("Nenhum fornecedor encontrado no banco de dados.")
    except Exception:
        print("Erro ao exibir clientes do banco")

def alterar_fornecedor_banco(cnpj: str, campo: str, novo_campo):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM fornecedores WHERE cnpj = %s", (cnpj,))
            if cursor.fetchone() is None:
                print(f"Fornecedor com o CNPJ {cnpj} não existe!")
                return
            elif campo == "Email":
                sql = "UPDATE fornecedores SET email_fornecedor = %s WHERE cnpj = %s"
            elif campo == "Telefone":
                sql = "UPDATE fornecedores SET telefone_fornecedor = %s WHERE cnpj = %s"
            elif campo == "Tipo":
                sql = "UPDATE fornecedores SET tipo_fornecedor = %s WHERE cnpj = %s"
            elif campo == "Prazo":
                sql = "UPDATE fornecedores SET prazo_pagamento = %s WHERE cnpj = %s"
            elif campo == "Estado":
                sql = "UPDATE fornecedores SET estado = %s WHERE cnpj = %s"
            elif campo == "Cidade":
                sql = "UPDATE fornecedores SET cidade = %s WHERE cnpj = %s"
            elif campo == "Bairro":
                sql = "UPDATE fornecedores SET bairro = %s WHERE cnpj =%s"
            elif campo == "Rua":
                sql = "UPDATE fornecedores SET rua = %s WHERE cnpj = %s"
            elif campo == "Numero":
                sql = "UPDATE fornecedores SET numero = %s WHERE cnpj = %s"
            else:
                print("Campo inválido!")
                return
            
            cursor.execute(sql, (novo_campo, cnpj))
            conn.commit()
            print(f"Fornecedor {cnpj} atualizado no banco de dados com sucesso!")
    except Exception:
        print("Erro ao alterar cliente no banco")

def remover_fornecedor_banco(cnpj: str):
    confirmacao = input(f"Tem certeza de que deseja remover o fornecedor com o CNPJ {cnpj}? (s/n): ").strip().lower()
    
    if confirmacao != 's':
        print("Ação cancelada. O cliente não foi removido.")
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM fornecedores WHERE cnpj = %s"
            cursor.execute(sql, (cnpj,))
            conn.commit()
            print(f"Fornecedor {cnpj} removido do banco de dados com sucesso!")
    except Exception as e:
        print(f"Erro ao remover cliente do banco: {e}")

def carregar_fornecedores_banco():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM fornecedores")
            fornecedores_banco = cursor.fetchall()
            global fornecedores
            fornecedores = [Fornecedor(fornecedor['cnpj'], fornecedor['nome_fornecedor'], fornecedor['tipo_fornecedor'], fornecedor['email_fornecedor'],
                                       fornecedor['telefone_fornecedor'], fornecedor['prazo_pagamento'],fornecedor['estado'],fornecedor['cidade'],fornecedor['bairro'],
                                       fornecedor['rua'],fornecedor['numero'],fornecedor['cep']) for fornecedor in fornecedores_banco]
    except Exception:
        print("Erro ao carregar fornecedores do banco")

def pesquisa_fornecedor():
    tipo_fornecedor = input("Digite o tipo de fornecedor que deseja pesquisar: ")
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM fornecedores WHERE tipo_fornecedor LIKE %s", ('%' + tipo_fornecedor + '%',))
            fornecedores_encontrados = cursor.fetchall()
            
            if fornecedores_encontrados:
                print(f"{'CNPJ':<18} {'Nome':<30} {'Tipo':<14} {'Email':<35}{'Telefone':<21}{'Prazo de Pagamento':<15}")
                for fornecedor in fornecedores_encontrados:
                    print(f"{fornecedor['cnpj']:<18} {fornecedor['nome_fornecedor']:<30} {fornecedor['tipo_fornecedor']:<14} {fornecedor['email_fornecedor']:<34} {fornecedor['telefone_fornecedor']:<21}{fornecedor['prazo_pagamento']:<30}")
            else:
                print(f"Nenhum fornecedor encontrado com o tipo '{tipo_fornecedor}'.")
    except Exception as e:
        print(f"Erro ao pesquisar fornecedor no banco: {e}")

carregar_fornecedores_banco()
limpa()
cadastrar_cliente()