#Autor:Bruno Henrique Benkendorf
#Data: 04/09/2024
import os
livros = []
biblioteca = []
menu = 0
def limpa():
    os.system('cls')
class Livro:
    def __init__(self,titulo,autor,editora,ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        print("Livro: ", self.titulo, " Cadastrado!")
class Biblioteca: 
    def __init__(self,titulo,autor,editora,ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        print("Livro: ", self.titulo, " Cadastrado!")

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    ano = input("Digite o ano do livro: ")
    novo_livro = Livro(titulo, autor, editora, ano)
    livros.append(novo_livro)
def exibir_livros(livros_lista):
    print(f"{'Título':<30} {'Autor':<30} {'Editora':<20} {'Ano':<4}")
    for livro in livros_lista:
        print(f"{livro.titulo:<30} {livro.autor:<30} {livro.editora:<20} {livro.ano:<4}")

livros.append(Livro("O Codificador Limpo", "Robert C. Martin", "Alta Books", "2012"))
livros.append(Livro("Effective Java", "Joshua Bloch", "Addison-Wesley", "2018"))
livros.append(Livro("Algorithms", "Robert Sedgewick, Kevin Wayne", "Addison-Wesley", "2011"))
livros.append(Livro("The Pragmatic Programmer", "Andrew Hunt, David Thomas", "Addison-Wesley", "1999"))
 
limpa()
print("""
                 _ _.-'`-._ _                 
                ;.'________'.;                
     _________n.[____________].n_________     
    |""_""_""_""||==||==||==||""_""_""_""]    
    |           ||BIBLIOTECA||           |    
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|    
    |.. .. .. ..||..||..||..||.. .. .. ..|    
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|    
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,, 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
""")
while menu != 5:
    print("""
          1-Livros
          2-Adicionar
          3-Livros da Biblioteca
          4-Alocar Livro
          6-Encerrar
          """)
    menu = int(input("-> "))
    
    match menu:
        case 1:
            limpa()
            exibir_livros(livros)

        case 2:
            limpa()
            cadastrar_livro()
            
        case 3:
            limpa()
            if biblioteca:
                exibir_livros(biblioteca)
            else:
                print("Nenhum livro na biblioteca.")
        case 4:
           # x = int(input())
           # bliblioteca.append(Biblioteca(livros[x].titulo, livros[x].autor, livros[x].editora, livros[x].ano))
            titulo = input("Digite o título do livro para alocar: ")
            for livro in livros:
                if livro.titulo == titulo:
                    livro_encontrado = livro
                    break
            if livro_encontrado:
                biblioteca.append(Biblioteca(livro_encontrado.titulo, livro_encontrado.autor, livro_encontrado.editora, livro_encontrado.ano))
            else:
                print("Livro não encontrado.")
        case 5:
            break