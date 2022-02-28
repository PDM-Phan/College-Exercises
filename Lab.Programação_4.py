qp = float(input())
vp = float(input())
qq = float(input())
vq = float(input())

valp = qp * vq
valq = qq * vq
total = valp + valq

print(f'Pao: R${valp:.1f}')
print(f'Queijo: R${valq:.1f}')
print(f'Total: R${total:.1f}')
