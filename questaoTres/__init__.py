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

    cabecalho('Vez do time ladrão')
    chave = []
    for pessoa in ladrao:
        print(f'{pessoa} ESCOLHA UM LUGAR')
        locais = menu(['Sala', 'Quarto', 'Garagem', 'Cozinha', 'Sotão', 'Porão', 'Quintal', 'Banheiro'])
        chave.append(locais)
    while chave:
        key = 0
        cabecalho('Vez do time policia')
        for pessoa in policia:
            if not chave:
                break
            print(f'{pessoa} ESCOLHA UM LUGAR')
            proucura = menu(['Sala', 'Quarto', 'Garagem', 'Cozinha', 'Sotão', 'Porão', 'Quintal', 'Banheiro'])
            for valor in chave:
                key = int(valor)
                if key == proucura:
                    print('Ladrão encontrado')
                    chave.remove(proucura)
            if key != proucura:
                print('Desculpe, Não há ninguem nesse local')
    print('JOGO ENCERRADO')
