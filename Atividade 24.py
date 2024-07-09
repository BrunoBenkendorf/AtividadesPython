# Define a função fatorial que calcula o fatorial de n usando recursão
def fatorial(n, resultado=1):
#se n é 0 ou 1, o que é o caso base da recursão
    if n == 0 or n == 1:  
#retorna o resultado
        return resultado   
    else:  # Senão 
        return fatorial(n - 1, n * resultado)  # Chama recursivamente fatorial com n-1 e atualiza resultado

# Define a função principal que será executada quando o script for executado diretamente
def main():
    n = int(input("Digite um número inteiro: "))  # Solicita ao usuário que digite um número inteiro e converte para int
    resultado = fatorial(n)  # Calcula o fatorial do número fornecido chamando a função fatorial
    print(20 * "#")  # Imprime uma linha de 20 caracteres '#' para formatação
    print("Fatorial:", resultado)  # Imprime o resultado do cálculo fatorial
    print(20 * "#")  # Imprime outra linha de 20 caracteres '#' para formatação

# Verifica se este arquivo está sendo executado diretamente (não importado como um módulo)
if __name__ == "__main__":
    main()  # Chama a função principal 'main' para executar o programa
