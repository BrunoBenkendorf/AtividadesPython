# Aluno: Bruno Henrique Benkendorf
# Data: 26/07/2024
# Turma: T DESI 2024/1 V1
i_nome = ""
i_matricula = ""
i_nota1 = ""
i_nota2 = ""
i_nota3 = ""
i_situacao = ""
menu=0
aluno = []
class cadastro: 
    def __init__(self,nome,matricula,nota1,nota2,nota3,situacao):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.situacao = situacao
        print("Cadastrado com sucesso")
        
while menu != 6:
    print("Escolha a operação: 1(Cadastro), 2(Exibir), 3(Exibir Aprovados), 4(Exibir Reprovados), 5(Exibir Cursandos), 6(Encerrar)")
    menu = int(input("-> "))
    match menu:
        case 1:
            i_nome = input("Insira o nome do aluno que deseja cadastrar: ")
            i_matricula = input("Insira a matricula do aluno que deseja cadastrar: ")
            i_nota1 = input("Insira a primeira Nota: ")
            i_nota2 = input("Insira a segunda Nota: ")
            i_nota3 = input("Insira a terceira Nota:")
            i_situacao = input("Insira a situação (Aprovado,Reprovado,Cursando): ")
            aluno.append(cadastro(i_nome,i_matricula,i_nota1,i_nota2,i_nota3,i_situacao))
        case 2:
            for x in range(len (aluno)):
                print("Nome: ",aluno[x].nome)
                print("Matricula: ",aluno[x].matricula)
                print("Nota 1: ",aluno[x].nota1)
                print("Nota 2: ",aluno[x].nota2)
                print("Nota 3: ",aluno[x].nota3)
                print("Situação: ",aluno[x].situacao)
        case 3:
            for x in range(len (aluno) ):
                if(aluno[x].situacao == "Aprovado"):
                    print("Alunos Aprovados:")
                    print("Nome: ",aluno[x].nome)
                    print("Matricula: ",aluno[x].matricula)
                    print("Nota 1: ",aluno[x].nota1)
                    print("Nota 2: ",aluno[x].nota2)
                    print("Nota 3: ",aluno[x].nota3)
                    print("Situação: ",aluno[x].situacao)
        case 4: 
            for x in range(len (aluno)):
                if(aluno[x].situacao == "Reprovado"):
                    print("Alunos Reprovados:")
                    print("Nome: ",aluno[x].nome)
                    print("Matricula: ",aluno[x].matricula)
                    print("Nota 1: ",aluno[x].nota1)
                    print("Nota 2: ",aluno[x].nota2)
                    print("Nota 3: ",aluno[x].nota3)
                    print("Situação: ",aluno[x].situacao)
        case 5:
            for x in range(len (aluno)):
                if(aluno[x].situacao == "Cursando"):
                    print("Alunos Cursando:")
                    print("Nome: ",aluno[x].nome)
                    print("Matricula: ",aluno[x].matricula)
                    print("Nota 1: ",aluno[x].nota1)
                    print("Nota 2: ",aluno[x].nota2)
                    print("Nota 3: ",aluno[x].nota3)
                    print("Situação: ",aluno[x].situacao)
        case 6:
            break