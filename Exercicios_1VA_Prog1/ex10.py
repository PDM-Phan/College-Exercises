from Funcoes_UTEIS import verificacao

# Main program
situacao_suspeito = 0  # inocente ate que se prove o contrario
pergunta = 1  # define qual pergunta será feita
while True:
    if pergunta == 1:
        perg = verificacao('1º)\033[4m Telefonou para a vítima (1-SIM / 2-NÃO)? \033[m')
        if 1 < perg > 2:
            print('Digite uma opção válida.')
            print('Tente nnovamente.')
            continue
        else:
            if perg == 1:
                situacao_suspeito += 1
                pergunta += 1
            else:
                pergunta += 1

    elif pergunta == 2:
        perg = verificacao('2º)\033[4m Esteve no local do crime (1-SIM / 2-NÃO)? \033[m')
        if 1 < perg > 2:
            print('Digite uma opção válida.')
            print('Tente nnovamente.')
            continue
        else:
            if perg == 1:
                situacao_suspeito += 1
                pergunta += 1
            else:
                pergunta += 1

    elif pergunta == 3:
        perg = verificacao('3º)\033[4m Mora perto da vítima (1-SIM / 2-NÃO)? \033[m')
        if 1 < perg > 2:
            print('Digite uma opção válida.')
            print('Tente nnovamente.')
            continue
        else:
            if perg == 1:
                situacao_suspeito += 1
                pergunta += 1
            else:
                pergunta += 1

    elif pergunta == 4:
        perg = verificacao('4º)\033[4m Devia para a vítima (1-SIM / 2-NÃO)? \033[m')
        if 1 < perg > 2:
            print('Digite uma opção válida.')
            print('Tente nnovamente.')
            continue
        else:
            if perg == 1:
                situacao_suspeito += 1
                pergunta += 1
            else:
                pergunta += 1

    elif pergunta == 5:
        perg = verificacao('5º)\033[4m Já trabalhou com a vítima (1-SIM / 2-NÃO)? \033[m')
        if 1 < perg > 2:
            print('Digite uma opção válida.')
            print('Tente nnovamente.')
            continue
        else:
            if perg == 1:
                situacao_suspeito += 1
                pergunta += 1
            else:
                pergunta += 1

    else:
        break

print('Analizando respostas... ')
print('Analise finalizada,', end=' ')

if situacao_suspeito > 1:
    if situacao_suspeito == 2:
        print('você é considerado \033[1mSUSPEITO\033[m')
    elif 2 < situacao_suspeito < 5:
        print('você é considerado \033[1mCÚMPLICE\033[m')
    else:
        print('VOCÊ É CONSIDERADO \033[1;31mASSASSINO\033[m!!')
        print('VOCÊ ESTÁ PRESO!!')
else:
    print('você é considerado \033[1mINOCENTE\033[m')
