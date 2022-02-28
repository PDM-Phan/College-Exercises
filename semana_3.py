from time import sleep

def menu():  # Uma função simples para poder facilitar a implementação do menu
    print('MINI-CAUCULADORA:\n'
          '[1] ADIÇÃO\n'
          '[2] SUBTRAÇÃO\n'
          '[3] MULTIPLICAÇÃO\n'
          '[4] DIVISÃO\n'
          '[5] RAIZ QUADRADA\n'
          '[6] MAIOR DE 3 NÚMEROS\n'
          '[7] MÉDIA ENTRE 4 NÚMEROS\n'
          '[8] SAIR')


def verificacao():  # verificar se o número é valido, caso o usuario seja um macaco
    while True:
        try:
            num = int(input('NÚMERO = '))
        except ValueError:
            print('[ERROR] ESCREVA UM NÚMERO INTEIRO VALIDO.')
            print('TENTE NOVAMENTE.')
            continue
        else:
            break
    return num


# Programa principal
while True:  # Um loop para repetir o menu se necessario
    menu()
    while True:
        # ‘loop’ para fazer a verificação da opçao impedindo assim do programa parar ou não funcionar caso o
        # usuario escreva algo não esperado, caso ele tente ser um macaco
        try:
            sleep(1)
            op = int(input('QUAL OPERAÇÃO VOCÊ DESSEJA REALIZAR >> '))
            if op <= 0 or op > 8:  # caso o usuario tente ser um macaco
                print('[ERROR] ESCREVA UMA OPÇÃO VALIDA.')
                print('TENTE NOVAMENTE.')
                continue
            else:
                if op == 1:
                    num1 = verificacao()
                    num2 = verificacao()
                    print(f'A SOMA ENTRE {num1} E {num2} SERÁ {num1 + num2}.')
                    print('-=' * 30)
                elif op == 2:
                    num1 = verificacao()
                    num2 = verificacao()
                    print(f'A SUBTRAÇÃO ENTRE {num1} E {num2} SERÁ {num1 - num2}.')
                    print('-=' * 30)
                elif op == 3:
                    num1 = verificacao()
                    num2 = verificacao()
                    print(f'A MULTIPLICAÇÃO ENTRE {num1} E {num2} SERÁ {num1 * num2}.')
                    print('-=' * 30)
                elif op == 4:
                    num1 = verificacao()
                    num2 = verificacao()
                    print(f'A DIVISÃO ENTRE {num1} E {num2} SERÁ {num1 / num2}.')
                    print('-=' * 30)
                elif op == 5:
                    while True:
                        num = verificacao()
                        if num <= 0:  # é necessário um número real para funcionar
                            print('POR FAVOR ESCREVA UM NÚMERO INTERIO POSITIVO.')
                            print('TENTE NOVAMENTE.')
                            continue
                        else:
                            print(f'A RAIZ QUADRADA DO NÚMERO {num} É {num ** (1 / 2):.2f}.')
                            print('-=' * 30)
                            break
                elif op == 6:
                    numeros = []  # lista para guardar os numeros
                    for n in range(1, 4):
                        num = verificacao()
                        numeros.append(num)
                    print(f'O MAIOR NÚMEROS DENTRE OS DIGITOS FOI {max(numeros)}.')
                    print('-=' * 30)
                    # função usada para ver o maior número de uma lista
                elif op == 7:
                    numeros = []  # lista para guardar os números que serão somados
                    for n in range(1, 5):
                        num = verificacao()
                        numeros.append(num)
                    print(f'A MÉDIA DOS QUATRO NÚMEROS DIGITADOS SERÁ {(sum(numeros))/4}')
                    print('-=' * 30)
                    # função usada para somar todos os valores de uma lista
        except ValueError:
            print('[ERROR] ESCREVA UMA OPÇÃO VALIDA.')
            print('TENTE NOVAMENTE.')
            continue
        else:
            break
    if op == 8:  # caso tenha sido escolhido a opçao 8 quebrando assim o ‘loop’
        print('DESLIGANDO...')
        break
    esc = ''
    while esc == '':
        esc = input(
            'DESEJA CONTINUAR[S/N]? ').strip().upper()  # verificação se o usuario deseja sair após realizar a operação
        if esc.isnumeric() or esc == '':  # caso o usuario escreva um número ou nada
            print('[ERROR] ESCREVA UMA OPÇÃO VALIDA.')
            print('TENTE NOVAMENTE.')
            esc = ''
            continue
        elif esc not in 'SN':  # caso o usuario escreva alguma palavra que não seja S ou N
            print('[ERROR] ESCREVA UMA OPÇÃO VALIDA.')
            print('TENTE NOVAMENTE.')
            esc = ''
            continue
    if esc == 'S':
        print('CARREGANDO...')
        sleep(1)
        continue
    else:
        print('DESLIGANDO...')
        break
