from Funcoes_UTEIS import verificacao

cont = 0
numeros_totais = []
numeros_pares = []
numeros_impares = []

while cont < 20:
    num = verificacao('Digite qualquer número interio positivo > ')
    if num < 0:
        print('Por favor digite um número inteiro positivo.')
        print('Tente novamente.')
        continue
    else:
        numeros_totais.append(num)
        if num % 2 == 0:
            numeros_pares.append(num)
        else:
            numeros_impares.append(num)
        cont += 1

print('Todos os números digitados: ', *numeros_totais)
print('Todos os números pares digitados: ', *numeros_pares)
print('Todos os números impares digitados: ', *numeros_impares)
