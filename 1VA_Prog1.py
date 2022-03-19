from random import randint
from time import sleep

# estoque previamente cadastrado no sistema
estoque = [{'produto': 'CDs', 'codigo': 0, 'quantidade': 0},
           {'produto': 'Capas para CDs', 'codigo': 0, 'quantidade': 0},
           {'produto': 'Playstation 2', 'codigo': 0, 'quantidade': 0},
           {'produto': 'Controle', 'codigo': 0, 'quantidade': 0},
           {'produto': 'Headsets', 'codigo': 0, 'quantidade': 0}]

# coloca um valor aleatorio de 0 a 100 na parte de codigo e quantidade dos produtos
codigos = []
for p in range(0, len(estoque)):
    while True:  # loop feito pra impedir codigos de se repetirem
        estoque[p]['codigo'] = randint(0, 100)
        if estoque[p]['codigo'] not in codigos:
            codigos.append(estoque[p]['codigo'])
            break
        else:
            continue
    estoque[p]['quantidade'] = randint(0, 50)

while True:
    try:
        escolha = int(input('Qual das ações abaixo você deseja realizar:\n'
                            '[1] Utilizar estoque cadastrado\n'
                            '[2] Alterar estoque\n'
                            '[3] Mostrar o estoque já cadastrado\n'
                            '>> '))
        if escolha < 1 or escolha > 3:
            print('[ERRO] Por favor digite uma opção válida.\n'
                  'Tente novamente.')
            continue
        else:
            if escolha == 1:  # realizar a venda de um produto do estoque
                while True:
                    try:
                        sleep(1)
                        op_venda_codigo = int(input('Digite o código do produto que se deseja vender >> '))
                        pro_encontrados = 0  # verificação de caso o produto exista
                        local_pro = 0  # local do produto na lista do estoque
                        for c in range(0, len(estoque)):
                            if estoque[c]['codigo'] == op_venda_codigo:
                                pro_encontrados += 1
                                local_pro += c
                                break

                        if pro_encontrados == 0:
                            print('Código de produto não encontrado.\n'
                                  'Digite um código válido.')
                            continue

                        elif pro_encontrados == 1:
                            while True:
                                try:
                                    sleep(1)
                                    quant_venda = int(input('Quantas unidades você deseja comprar desse produto >> '))
                                    # caso a quantidade de venda seja maior que a quantidade disponivel
                                    if quant_venda > estoque[local_pro]['quantidade']:
                                        print('Não é possivel realizar essa operação pois o valor de venda excede o'
                                              ' estoque disponível.')
                                        break

                                    else:
                                        print('Venda aprovada.\nAtualizando o estoque...')
                                        sleep(1)
                                        estoque[local_pro]['quantidade'] -= quant_venda  # atualizando a quantidade
                                        print('Atualização finalizada.')
                                        break

                                except ValueError:
                                    print('[ERRO] Por favor digite uma quantidade válida.\n'
                                          'Tente novamente.')
                                    continue

                                else:
                                    break

                    except ValueError:
                        print('[ERRO] Por favor digite uma opção válida.\n'
                              'Tente novamente.')
                        continue

                    else:
                        break

            elif escolha == 2:  # realizar alguma alteraçao no estoque registrado
                while True:
                    try:
                        sleep(1)
                        add_remove = int(input('Qual açõa deseja realiar:\n'
                                               '[1] Adcionar um produto no estoque\n'
                                               '[2] Remover um produto do estoque\n'
                                               '[3] Refazer o estoque\n'
                                               '>> '))
                        if add_remove < 1 or add_remove > 3:
                            print('[ERRO] Por favor digite uma opção válida.\n'
                                  'Tente novamente.')
                            continue

                        else:
                            # adicionar um produto ao estoque
                            if add_remove == 1:
                                produto = {}  # produto que será cadastrado
                                produto['produto'] = input('Nome do produto a ser cadastrado: ').title().strip()
                                while True:
                                    try:
                                        produto['codigo'] = int(input('Código do produto a ser cadastrado: '))
                                        if produto['codigo'] not in codigos and produto['codigo'] >= 0:
                                            codigos.append(produto['codigo'])
                                            break
                                        else:
                                            print('[ERRO] Esse código já é usado em outro produto.')
                                            print('Digite outro código para esse produto.')
                                            continue

                                    except ValueError:
                                        print('[ERRO] Por favor digite um código válido.\n'
                                              'Tente novamente.')
                                        continue
                                while True:
                                    try:
                                        produto['quantidade'] = int(input('Qual a quantidade disponivel para estoque: '))
                                        if produto['quantidade'] < 0:
                                            print('[ERRO] Por favor digite uma quantidade válida.\n'
                                                  'Tente novamente.')
                                            continue

                                    except ValueError:
                                        print('[ERRO] Por favor digite uma quantidade válida.\n'
                                              'Tente novamente.')
                                        continue

                                    else:
                                        break
                                print('Cadastrando produto...')
                                sleep(1)
                                estoque.append(produto)
                                print('Produto cadastrado com sucesso.')

                            # remover um produto do estoque
                            elif add_remove == 2:
                                while True:
                                    try:
                                        sleep(1)
                                        cod_prod_remove = int(input('Qual o código do produto que deseja remover: '))
                                        cod_found = 0
                                        for cod in range(0, len(estoque)):
                                            if estoque[cod]['codigo'] == cod_prod_remove:
                                                cod_found += 1
                                                print('Removendo produto do estoque...')
                                                sleep(1)
                                                estoque.pop(cod)
                                                print('Produto removido com sucesso.')
                                                break

                                        if cod_found == 0:
                                            print('Código de produto não encontrado.\n'
                                                  'Digite um código válido.')
                                            continue

                                    except ValueError:
                                        print('[ERRO] Por favor digite um codigo valido.')
                                        print('Tente novamente.')
                                        continue

                                    else:
                                        break

                            elif add_remove == 3:
                                print('Reiniciando o estoque...')
                                sleep(2)
                                estoque.clear()
                                print('Estoque reiniciado.')

                    except ValueError:
                        print('[ERRO] Por favor digite uma opção válida.\n'
                              'Tente novamente.')
                        continue

                    else:
                        break

            # limpar o estoque
            elif escolha == 3:
                print(f'\033[4m{">> ESTOQUE DO EPAMINOMBAS <<":^50}\033[m')
                # condição para caso nao haja produtos cadastrados
                if len(estoque) > 0:
                    print(f'|{"CÓDIGO":<6}| {"PRODUTO":<}')
                    for p in range(0, len(estoque)):
                        print(f'|{estoque[p]["codigo"]:^6}| {estoque[p]["produto"]:<}({estoque[p]["quantidade"]})')

                else:
                    print(f'{">> AINDA NÃO HÁ PRODUTOS CADASTRADOS <<":^50}')

            volta = ''
            while volta == '':
                volta = input('Deseja continuar?[S/N] ').strip().upper()
                if volta not in 'SN':  # caso o usuario digite uma palavra alem de s ou n
                    print('Por favor digite uma resposta válida.')
                    print('Tente novamente')
                    volta = ''
                    continue
                elif volta == '':  # caso ele digite nada
                    print('Por favor digite uma resposta válida.')
                    print('Tente novamente')
                    volta = ''
                    continue

            if volta == 'S':
                print('Atualizando sistema...')
                sleep(1)
                continue
            else:
                print('O estoque atualizado após as alterações será:')
                print(f'\033[4m{">> ESTOQUE DO EPAMINOMBAS <<":^50}\033[m')
                if len(estoque) > 0:
                    print(f'|{"CÓDIGO":<6}| {"PRODUTO":<}')
                    for p in range(0, len(estoque)):
                        print(f'|{estoque[p]["codigo"]:^6}| {estoque[p]["produto"]:<}({estoque[p]["quantidade"]})')

                else:
                    print(f'{">> AINDA NÃO HÁ PRODUTOS CADASTRADOS <<":^50}')
                print('Finalizando sistema...')
                sleep(1)
                print('Sistema finalizado.')
                break

    except ValueError:
        print('[ERRO] Por favor digite uma opção válida.\n'
              'Tente novamente.')
        continue

    else:
        break
