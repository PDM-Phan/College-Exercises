while True:
    a, b = input().split(' ')  # desse jeito é possivel conseguir 2 inputs na mesma linha, caso seja necessario
    a = float(a)
    b = float(b)
    if a == int(a) and b == int(b):
        area = int(a) * int(b)  # posteriormente é possivel coloca-los como numeros se necessario
        print(area)
        break
    else:
        continue
