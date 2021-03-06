def verificacao(string):
    """
    Cria uma variavel VERIFICA que receberá um int input.
    :param string: será uma pergunta que necessite de um tratamento de um número.
    :return: retorna a varival VERIFICA
    """
    while True:
        try:
            verifica = int(input(string))

        except ValueError:
            print('Digite um número válido.')
            print('Tente novamente.')
            continue

        else:
            return verifica


def encontra_primos(numero):
    """
    Função que recebe um param número e verifica se é primo ou não.
    :param numero:
    :return: True(booleano) se for primo e False(booleano) se não for.
    """
    if numero == 1:
        return True
    else:
        divisao_possivel = 0
        for num in range(1, numero + 1):
            if divisao_possivel <= 2:  # número primo só é divisivel por 1 e ele mesmo, logo, so há duas divisoes possiveis.
                if numero % num == 0:
                    divisao_possivel += 1
                else:
                    continue
            else:  # houve mais de duas divisoes, sendo assim um número não primo.
                break
        return True if divisao_possivel == 2 else False
