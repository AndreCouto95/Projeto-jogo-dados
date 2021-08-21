from random import *

def deseja_jogar():
    jogar = input("Deseja jogar o jogo? (digite sim, caso queira jogar/ nao, caso não queira jogar)")
    while jogar != 'sim' and jogar !=  'nao':
        jogar = input("Deseja jogar o jogo? (digite sim, caso queira jogar/ nao, caso não queira jogar)")
    return jogar

def aleatorio():
    num = randrange(1,7)
    print(f'valor do dado: {num}\n')
    return num

def jogo():
    num_players = input("Número de jogadores: ")
    while num_players.isnumeric() == False or int(num_players) <= 1:
        num_players = input("Digite um número de jogadores(2 ou mais jogadores): ")

    num_players = int(num_players)
    numero = []
    maior = -1
    player = -1

    for x in range(0,(num_players)):
        print(f'Player {x+1}')
        numero.append(aleatorio())
        if numero[x] > maior:
            maior = numero[x]
            player = x+1
        elif numero[x] == maior:
            x = x + 1
            player = str(player) + " ," + str(x)
    print(f'Vencedor(es): Players {player}\nMaior número sorteado:{maior}.')


jogar = deseja_jogar()
while jogar == 'sim':
    jogo()
    jogar = deseja_jogar()
print("Quem sabe na próxima né!?\nAté mais.")    
