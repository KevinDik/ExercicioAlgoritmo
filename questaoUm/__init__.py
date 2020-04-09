from menu import cabecalho, linha


def grauvertice():
    grau = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l')
    vertice = ('ab', 'ac', 'aj', 'bc', 'bd', 'be', 'ce', 'cg', 'dg', 'ef',
               'ek', 'fg', 'fh', 'fk', 'gh', 'gi', 'hj', 'ij', 'ik', 'il', 'kl')
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
