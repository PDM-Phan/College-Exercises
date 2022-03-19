idade = int(input())
analfabeto = input().lower().strip()

if 18 < idade <= 70:
    if analfabeto == 'n':
        print("Voto obrigatório")

    else:
        print("Voto não obrigatório")

elif 16 <= idade <= 18 or idade > 70:
    print("Voto não obrigatório")
