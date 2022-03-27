from Funcoes_UTEIS import verificacao


# Main program
valores = []
while True:
    valor = verificacao('Digite um valor para as notas dos alunos(-1 para finalizar o loop) > ')
    if valor == -1:
        print('Finalizando o programa...')
        break
    elif 0 < valor > 10:
        print('Digite uma nota possivel.')
        print('Tente novamente.')
        continue
    else:
        valores.append(valor)

print(f'Quantidade de notas lidas: {len(valores)}')
print('Valores na ordem de input informados: ', end='')
for v in range(0, len(valores)):
    if v < (len(valores) - 1):
        print(valores[v], end=' - ')
    else:
        print(valores[v], end='')

print('\nValores na ordem inversa de input informados: ', end='')
rev_valores = valores[::-1]  # uma copia inversa da lista valores
for va in range(0, len(rev_valores)):
    if va < (len(rev_valores) - 1):
        print(rev_valores[va], end=' - ')
    else:
        print(rev_valores[va], end='')

print('\nA soma de todas as notas será: ', end='')
quanti_notas_acima = 0
quanti_notas_abaixo_sete = 0
soma_total = 0
for v in range(0, len(valores)):
    soma_total += valores[v]

print(soma_total)
print(f'A média das notas será: {soma_total/len(valores):.2f}')
print('Quantidade de notas acima da média: ', end='')
for v in range(0, len(valores)):
    if valores[v] > soma_total / len(valores):
        quanti_notas_acima += 1
    if valores[v] < 7:
        quanti_notas_abaixo_sete += 1

print(quanti_notas_acima)
print(f'Quantidade de notas abaixo de sete: {quanti_notas_abaixo_sete}')
print('PROGRAMA FINALIZADO.')
