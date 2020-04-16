from menu import cabecalho


def entradaesaida():
    vertice = {'1': {'Entrada': 0, 'Saída': (10, 100, 30, 50)}, '2': {'Entrada': (50, 5, 20), 'Saída': 0},
               '3': {'Entrada': 30, 'Saída': (50, 5)}, '4': {'Entrada': (50, 20, 100, 10), 'Saída': 0}, '5': {'Entrada': 10, 'Saída': 10}}
    cabecalho('Ligação dos vertices')
    for item in vertice.items():
        print(item)
