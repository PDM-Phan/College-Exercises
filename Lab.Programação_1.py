while True:
    try:
        N = float(input())
        if N == int(N):  # Verificação de que o número digitado é realmente inteiro
            n = int(N)  # Após verificar o programa converte para inteiro e printa a saida
            print(n + 1)
        else:
            continue

    except ValueError:
        continue

    else:
        break