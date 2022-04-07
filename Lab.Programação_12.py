def retrona_dicionario(str):
    import re
    str_lower = str.lower()  # transforma a string em minuscula, facilitando a verificação
    # cria uma lista formada após separar a string com determinados separators
    lista_re = list(re.split('[,;. ]', str_lower))
    dicionario = {}
    for l in lista_re:
        # se o não for 'vazio' e não já estando no dicionario, a palavra será colocada no dicionario.
        if l != '' and l not in dicionario:
            dicionario[l] = lista_re.count(l)
        else:
            pass
    return dicionario


# Main program
if __name__ == '__main__':
    dic = retrona_dicionario(input())
    # printa os itens do dicionario.
    for k, v in dic.items():
        print(f'{k} - {v}')
