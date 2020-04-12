from menu import cabecalho, leiaInt, menu


def policiaeladrao():
    from random import randint
    policia = []
    ladrao = []
    cabecalho('JOGO Policia e Ladrão')
    partida = leiaInt('Quantos jogadores irão participar? ')
    controle = randint(1, 2)
    for part in range(1, partida + 1):
        jogadores = (str(input('Digite seu nome: ')))
        if controle == 1:
            policia.append(jogadores)
            controle += 1
        else:
            ladrao.append(jogadores)
            controle -= 1
    cabecalho('Lista de jogadores')
    for pos, pessoas in enumerate(policia):
        print(f'Policia {pos} -------------- {pessoas}')
    for pos, pessoas in enumerate(ladrao):
        print(f'Ladrão {pos} -------------- {pessoas}')

    cabecalho('O ladrão se esconde')
    esconderijo = []
    proucurar = []
    for pessoa in ladrao:
        print(f'{pessoa} ESCOLHA UM LUGAR')
        esconderijo = menu(['Sala', 'Quarto', 'Garagem', 'Cozinha', 'Sotão', 'Porão', 'Quintal', 'Banheiro'])
    while True:
        cabecalho('A Policia proucura')
        for pessoa in policia:
            print(f'{pessoa} ESCOLHA UM LUGAR')
            proucurar = menu(['Sala', 'Quarto', 'Garagem', 'Cozinha', 'Sotão', 'Porão', 'Quintal', 'Banheiro'])
        if proucurar == esconderijo:
            print('Ladrão encontrado')
            break
