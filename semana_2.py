pi = 3.14  # valor de pi pra calculo

while True:
    try:
        raio = float(input('Qual o valor do raio desse circulo? '))

    except ValueError:
        print('[ERRO] Por favor digite um número valido.')
        print('Tente novamente.')
        continue

    else:
        break

area = pi * (raio ** 2)
perimetro = 2 * pi * raio

print(f'De acordo com esse raio de {raio}, essas são as informações disponiveis:\n'
      f'Área do circulo = {area};\n'
      f'Perimetro = {perimetro};\n'
      f'Diametro = {raio * 2}')
