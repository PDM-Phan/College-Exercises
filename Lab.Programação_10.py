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


lista_primos = []
lista_par = []
lista_multiplos_n = []

inicio_intervalo = int(input())
fim_intervalo = int(input())
while True:
    n = int(input())  # variavel que precisa ser obrigatoriamente impar
    if n % 2 == 0:
        continue
    else:
        break

for num in range(inicio_intervalo, fim_intervalo):
    if encontra_primos(num):
        lista_primos.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    if num % n == 0:
        lista_multiplos_n.append(num)

print(lista_primos)
print(lista_par)
print(lista_multiplos_n)
