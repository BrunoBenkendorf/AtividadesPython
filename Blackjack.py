import random
import os

# Função para limpar a tela
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para carregar o ranking
def carregar_ranking():
    try:
        with open('ranking.txt', 'r') as file:
            ranking = [linha.strip().split(",") for linha in file.readlines()]
            ranking = [(nome, int(pontuacao)) for nome, pontuacao in ranking]
            return ranking
    except FileNotFoundError:
        return []

# Função para salvar o ranking em um arquivo
def salvar_ranking(ranking):
    with open('ranking.txt', 'w') as file:
        for nome, pontuacao in ranking:
            file.write(f"{nome},{pontuacao}\n")

# Função para atualizar o ranking
def atualizar_ranking(novo_nome, pontuacao):
    ranking = carregar_ranking()
    ranking = [r for r in ranking if r[0] != novo_nome]  # Remove duplicados
    ranking.append((novo_nome, pontuacao))
    ranking.sort(key=lambda x: x[1], reverse=True)
    salvar_ranking(ranking)

# Função para exibir o ranking
def exibir_ranking():
    ranking = carregar_ranking()
    print("\nRanking Atual:")
    if ranking:
        for i, (nome, pontuacao) in enumerate(ranking, 1):
            print(f"{i}. {nome} - {pontuacao} pontos")
    else:
        print("Ainda não há jogadores no ranking.")
    print("\n")

# Função para buscar um jogador
def buscar_jogador(nome):
    ranking = carregar_ranking()
    for jogador, pontuacao in ranking:
        if jogador == nome:
            return pontuacao
    return None

# Função para criar e embaralhar o baralho
def criar_baralho():
    naipes = ['Copas', 'Espadas', 'Paus', 'Ouro']
    valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']
    return [(valor, naipe) for naipe in naipes for valor in valores]

# Função para determinar o valor da carta
def carta_valor(carta, pontuacao_atual=0):
    if carta[0] in ['Valete', 'Rainha', 'Rei']:
        return 10
    elif carta[0] == 'Ás':
        return 11 if pontuacao_atual + 11 <= 21 else 1
    else:
        return int(carta[0])

# Início do programa
limpa()
baralho = criar_baralho()
random.shuffle(baralho)
menu = 0

while menu != 2:
    print("""
          1- Jogar
          2- Sair
          3- Exibir Ranking
    """)
    menu = int(input("-> "))
    limpa()
    match menu:
        case 1:
            nome_jogador = input("Digite seu nome: ")
            saldo = buscar_jogador(nome_jogador)
            
            if saldo is not None:
                print(f"Bem-vindo de volta, {nome_jogador}! Seu saldo atual é: {saldo}")
            else:
                saldo = 200
                print(f"Bem-vindo, {nome_jogador}! Novo saldo inicial de: {saldo}")

            while True:
                if saldo <= 0:
                    print("Saldo zerado! Você não pode continuar jogando.")
                    reiniciar = input("Deseja reiniciar com 200 de saldo? [S/N]: ").lower()
                    limpa()
                    if reiniciar == 's':
                        saldo = 200
                        print(f"Saldo reiniciado. Seu novo saldo é: {saldo}")
                    else:
                        limpa()
                        input("Voltando ao menu principal...")
                        limpa()
                        atualizar_ranking(nome_jogador, saldo)
                        break

                if len(baralho) < 10:  # Reembaralha o baralho quando as cartas estão acabando
                    input("\nO baralho está acabando. Reembaralhando...\n")
                    limpa()
                    baralho = criar_baralho()
                    random.shuffle(baralho)

                continuar = input("Deseja continuar jogando? [S/N]: ").lower()
                limpa()
                if continuar == 'n':
                    print("Você decidiu parar. Seu saldo final é:", saldo)
                    atualizar_ranking(nome_jogador, saldo)
                    break

                # Distribuir cartas
                cartas_jogador = [baralho.pop(), baralho.pop()]
                cartas_bot = [baralho.pop(), baralho.pop()]

                while True:
                    try:
                        aposta = int(input(f"Seu saldo atual é {saldo}. Quanto deseja apostar? "))
                        if 0 < aposta <= saldo:
                            saldo -= aposta
                            break
                        else:
                            print("Aposta inválida! Insira um valor dentro do seu saldo.")
                    except ValueError:
                        print("Por favor, insira um valor numérico válido.")

                while True:
                    pontuacao_jogador = sum(carta_valor(carta, sum(carta_valor(c, 0) for c in cartas_jogador)) for carta in cartas_jogador)
                    print("Cartas do jogador:", cartas_jogador)
                    print("Pontuação do jogador:", pontuacao_jogador)

                    if pontuacao_jogador == 21:
                        print("JACKPOT! Você fez 21 pontos.")
                        saldo += aposta * 2
                        break  # O jogo termina aqui, e o bot não joga
                    elif pontuacao_jogador > 21:
                        print("Você excedeu 21 pontos. Bot venceu!")
                        break

                    escolha = input('O que você quer? ["J" para pedir outra carta, "P" para parar, "D" para dobrar]: ').lower()
                    if escolha == "j":
                        cartas_jogador.append(baralho.pop())
                    elif escolha == "p":
                        break
                    elif escolha == "d":
                        # Verifica se o jogador tem saldo suficiente para dobrar
                        if saldo >= aposta:  
                            saldo -= aposta  
                            aposta *= 2  
                            nova_carta = baralho.pop()  
                            cartas_jogador.append(nova_carta)
            
                            # Atualiza a pontuação do jogador após dobrar
                            pontuacao_jogador = sum(carta_valor(carta, pontuacao_jogador) for carta in cartas_jogador)
                            print(f"Você dobrou a aposta! Nova aposta total: {aposta}.")
                            print("Cartas do jogador:", cartas_jogador)
                            print("Pontuação do jogador:", pontuacao_jogador)
                            if pontuacao_jogador > 21:
                                print("Você excedeu 21 pontos. Bot venceu!")
                            elif pontuacao_jogador == 21:
                                print("JACKPOT! Você fez 21 pontos.")
                                saldo += aposta * 2
                            atualizar_ranking(nome_jogador, saldo)
                            # Após dobrar, o jogador para automaticamente
                            break
                        else:
                            print("Saldo insuficiente para dobrar a aposta.(O valor para dobrar tem que ser menor que o saldo pelo 50%)")
                    else:
                        print("Escolha inválida. TENTE NOVAMENTE!!!")

                # O bot só joga se o jogador não fez 21
                if pontuacao_jogador < 21:
                    pontuacao_bot = 0
                    while pontuacao_bot < 17:
                        pontuacao_bot = sum(carta_valor(carta, pontuacao_bot) for carta in cartas_bot)
                        if pontuacao_bot < 17:
                            cartas_bot.append(baralho.pop())

                    print("\nCartas do Bot:", cartas_bot)
                    print("Pontuação do Bot:", pontuacao_bot)

                    if pontuacao_bot > 21 or pontuacao_jogador > pontuacao_bot:
                        print("Jogador venceu!")
                        saldo += aposta * 2
                    elif pontuacao_jogador < pontuacao_bot:
                        print("Bot venceu!")
                    else:
                        print("Empate!")
                        saldo += aposta

                atualizar_ranking(nome_jogador, saldo)

        case 2:
            print("Jogo encerrado!")
            break

        case 3:
            exibir_ranking()
