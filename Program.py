from menu import menu, cabecalho
from time import sleep
from questaoUm import grauvertice
sleep(1)
while True:
    sleep(1)
    cabecalho('Exercicio de Algoritmo')
    sleep(0.70)
    resposta = menu(['Primeira questão', 'Segunda questão', 'Terceira Questão', 'SAIR'])
    if resposta == 1:
        while True:
            print('1 ) Dada a figura anexada, faça um algoritmo para calcular o grau de cara vértice,'
                  ' os vizinhos de cada vértice e a (Menor e a maior ligação entre dois vértices do gráfico).')
            opc = menu(['Ver o grau de cada vertice', 'Ver os vizinhos de cada vertice',
                        'Maior / Menor ligação de dois vertices', 'Retornar ao MENU principal'])
            if opc == 1:
                grauvertice()
                sleep(0.70)
            elif opc == 4:
                print('RETORNANDO AO MENU PRINCIPAL')
                break
            else:
                print('Opção inválida, escolha somente os intens no menu')
    elif resposta == 2:
        print('2 ) De acordo com o grafo orientado da figura anexada, '
              'faça um algoritmo que diga quais os graus entradas e saídas de cada vértice. \n'
              'Ainda diga quais os vértices que tem ligação de entrada para cada nó.')

    elif resposta == 3:
        print('3) Mario adora convidar seus amigos para brincar em sua casa. '
              'Então decidiu convidar seus amigos para brincarem de polícia e ladrão. \n'
              'O jogo consiste em dois grupos, um grupo é a polícia e o outro grupo dos ladrões. '
              'Os ladrões devem se esconder e a polícia deve capturá-los. \n'
              'Caso a polícia consiga capturá-los e prendê-los os ladrões perdem o jogo e '
              'caso a polícia não consiga capturá-los os ladrões vencem o jogo.')

    elif resposta == 4:
        print('SAINDO do programa', end='')
        for final in range(1, 4):
            print('.', end='')
            sleep(0.75)
        sleep(1)
        break
    else:
        print('Opção inválida, escolha somente os intens no menu')
print()
