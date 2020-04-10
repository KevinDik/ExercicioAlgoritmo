from menu import cabecalho, linha


grau = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l')
vertice = {'ab': 16, 'ac': 10, 'aj': 12, 'bc': 7, 'bd': 13, 'be': 2, 'ce': 1,
           'cg': 21, 'dg': 15, 'ef': 9, 'ek': 4, 'fg': 3, 'fh': 20, 'fk': 8,
           'gh': 18, 'gi': 17, 'hj': 19, 'ij': 5, 'ik': 6, 'il': 14, 'kl': 11}


def grauvertice():
    print(f'Graus: {grau}')
    print(f'Vertices: {vertice}')
    graua = graub = grauc = graud = graue = grauf = graug = grauh = graui = grauj = grauk = graul = 0
    for item in vertice:
        for obj in item:
            if obj in 'a':
                graua += 1
    for item in vertice:
        for obj in item:
            if obj in 'b':
                graub += 1
    for item in vertice:
        for obj in item:
            if obj in 'c':
                grauc += 1
    for item in vertice:
        for obj in item:
            if obj in 'd':
                graud += 1
    for item in vertice:
        for obj in item:
            if obj in 'e':
                graue += 1
    for item in vertice:
        for obj in item:
            if obj in 'f':
                grauf += 1
    for item in vertice:
        for obj in item:
            if obj in 'g':
                graug += 1
    for item in vertice:
        for obj in item:
            if obj in 'h':
                grauh += 1
    for item in vertice:
        for obj in item:
            if obj in 'i':
                graui += 1
    for item in vertice:
        for obj in item:
            if obj in 'j':
                grauj += 1
    for item in vertice:
        for obj in item:
            if obj in 'k':
                grauk += 1
    for item in vertice:
        for obj in item:
            if obj in 'l':
                graul += 1
    cabecalho('Grau de cada vertice do grafo')
    print(f'''Grau de A ------------ Total: {graua}
Grau de B ------------ Total: {graub}
Grau de C ------------ Total: {grauc}
Grau de D ------------ Total: {graud}
Grau de E ------------ Total: {graue}
Grau de F ------------ Total: {grauf}
Grau de G ------------ Total: {graug}
Grau de H ------------ Total: {grauh}
Grau de I ------------ Total: {graui}
Grau de J ------------ Total: {grauj}
Grau de K ------------ Total: {grauk}
Grau de L ------------ Total: {graul}''')
    print(linha())


def vizinhovertice():
    print(f"""Vizinho do vertice A ------------ (B, C, J)
Vizinho do vertice B ------------ (A, C, D, E)
Vizinho do vertice C ------------ (A, B, E, G)
Vizinho do vertice D ------------ (B, G)
Vizinho do vertice E ------------ (B, C, F, K)
Vizinho do vertice F ------------ (E, G, H, K)
Vizinho do vertice G ------------ (D, F, H, I)
Vizinho do vertice H ------------ (F, G, J)
Vizinho do vertice I ------------ (G, J, K, L)
Vizinho do vertice J ------------ (A, H, I)
Vizinho do vertice K ------------ (E, F, I, L)
Vizinho do vertice L ------------ (I, K)""")


def maiormenorvertice():
    print(f'Maior ligação de vertice: {max(vertice.keys())} correspode ao valor: {max(vertice.values())}')
    print(f'Menor ligação de vertice: {min(vertice.keys())} correspode ao valor: {min(vertice.values())}')
