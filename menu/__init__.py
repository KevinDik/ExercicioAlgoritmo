def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('Tipo de valor inserido INVÁLIDO!')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu principal')
    controle = 1
    for item in lista:
        print(f'[{controle}] - {item}')
        controle += 1
    print(linha())
    opc = leiaInt('Escolha uma das opções: ')
    return opc
