def verificacao(string):
    """
    Cria uma variavel VERIFICA que receberá um int input
    :param string: será uma pergunta que necessite de um tratamento de um número
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