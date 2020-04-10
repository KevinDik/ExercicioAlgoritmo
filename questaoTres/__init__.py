from menu import cabecalho, leiaInt


def policiaeladrao():
    from random import shuffle
    jogadores = []
    cabecalho('JOGO Policia e Ladrão')
    partida = leiaInt('Quantos jogadores irão participar? ')
    for part in range(1, partida+1):
        jogadores.append(str(input('Digite seu nome: ')))
    shuffle(jogadores)
    print(jogadores)
