atletas = []  # cria uma lista para receber os atletas

while True:
    atleta = {}
    atleta['nome'] = input('Qual o nome do atleta > ').strip().title()
    if not atleta['nome'].isnumeric() and atleta['nome'] != '':  # verificando que é mesmo um nome
        pulos = []
        for p in range(1, 6):
            pulo = float(input(f'Quantos metros o atleta {atleta["nome"]} pulou no {p}º pulo > '))
            pulos.append(pulo)
        atleta['pulos'] = pulos
        atleta['media'] = sum(pulos) / len(pulos)
        atletas.append(atleta)

    elif atleta['nome'] == '':
        print('Fechando programa...')
        break

    else:
        print('[ERRO] Por favor digite um nome válido.')
        print('Digite novamente.')
        continue

# criando um contador para localizar os atletas
cont = 0
while cont != len(atletas):
    print(f'Atleta: {atletas[cont]["nome"]}')
    po = 0  # posiçaão do pulo
    p = 1  # numero do pulo
    while po < 5:
        pul = atletas[cont]['pulos']  # "tira" os pulos do dicionario e coloca como uma varivael
        print(f'{p}º pulo: {pul[po]:.1f} m')
        p += 1
        po += 1
    print('\nResultado final:')
    print(f'Atleta: {atletas[cont]["nome"]}')
    print('Saltos:', end=' ')
    for p in range(0, len(pul)):
        if p < len(pul) - 1:
            print(pul[p], end=' - ')
        else:
            print(pul[p], end='')
    print(f'\nMédia de saltos: {atletas[cont]["media"]} m')
    cont += 1
