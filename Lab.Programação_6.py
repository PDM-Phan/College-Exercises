senha1 = input().strip()
senha2 = input().strip()

if senha1 == senha2:
    if 4 <= len(senha1) <= 8 and 4 <= len(senha2) <= 8:
        print("Senha válida")

    else:
        print("Senha inválida")

else:
    print("Senha inválida")
