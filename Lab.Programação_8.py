inicio = int(input())
fim = int(input())

for n in range(inicio, fim + 1):
    if n % 2 == 0 or n % 3 == 0:
        print(n)
