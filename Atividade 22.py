# Define a classe Contato, que representará um contato na agenda
class Contato:
    # Método que inicializa os atributos nome, endereco e email
    def __init__(self, nome, endereco, email):
        self.nome = nome         # Atributo que guarda o nome do contato
        self.endereco = endereco # Atributo que guarda o endereço do contato
        self.email = email       # Atributo que guarda o e-mail do contato

# Define a classe Agenda, que gerenciará uma lista de contatos
class Agenda:
    # Método que inicializa a lista de contatos
    def __init__(self):
        self.contatos = []       # Atributo que guarda a lista de contatos, inicialmente vazia

    # Método para adicionar um contato à lista de contatos
    def adicionar_contato(self, contato):
        self.contatos.append(contato) # Adiciona o objeto contato à lista de contatos

    # Método para remover um contato da lista de contatos
    def remover_contato(self, contato):
        self.contatos.remove(contato) # Remove o objeto contato da lista de contatos

    # Método para listar todos os contatos na lista de contatos
    def listar_contatos(self):
        # Itera sobre a lista de contatos e imprime os detalhes de cada contato
        for contato in self.contatos:
            print("Nome:", contato.nome)         # Imprime o nome do contato
            print("Endereço:", contato.endereco) # Imprime o endereço do contato
            print("E-mail:", contato.email)      # Imprime o e-mail do contato

# Cria uma instância da classe Agenda
agenda = Agenda()

# Cria dois contatos, João e Maria
contato1 = Contato("João", "Rua A, 123", "joa@example.com")
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com")

# Adiciona os contatos João e Maria à agenda
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)

# Lista todos os contatos na agenda 
agenda.listar_contatos()

# Remove o contato 1
agenda.remover_contato(contato1)

# Lista todos os contatos na agenda novamente 
agenda.listar_contatos()
