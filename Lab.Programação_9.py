Candidato1 = 'José Alfredo'
Candidato2 = 'Maria Junqueira'
Candidato3 = 'Marivaldo Silva'
Candidato4 = 'Juliana Antônia'

eleitores = int(input())
total_de_votos = 0  # todos os votos que posteriormente será usado no cauculo
cand1 = cand2 = cand3 = cand4 = nulo = 0  # voto que cada candidato recebeu

for e in range(0, eleitores):
    voto = input().strip().lower()
    if voto.isnumeric():
        votoint = int(voto)
        if 1 <= votoint <= 4:
            if votoint == 1:
                cand1 += 1
                total_de_votos += 1
            elif votoint == 2:
                cand2 += 1
                total_de_votos += 1
            elif votoint == 3:
                cand3 += 1
                total_de_votos += 1
            else:
                cand4 += 1
                total_de_votos += 1
        else:
            nulo += 1
            total_de_votos += 1
    elif voto.isalpha():
        if voto == 'sair':
            break
    elif voto == '':
        nulo += 1
        total_de_votos += 1

print(f'Nome--------------Votos--------------Porcentagem')
print(f'{Candidato1} ------ {cand1} ------------------- {(cand1*100)/total_de_votos:.2f}%')
print(f'{Candidato2} --- {cand2} ------------------- {(cand2*100)/total_de_votos:.2f}%')
print(f'{Candidato3} --- {cand3} ------------------- {(cand3*100)/total_de_votos:.2f}%')
print(f'{Candidato4} --- {cand4} ------------------- {(cand4*100)/total_de_votos:.2f}%')
print(f'Nulo -------------- {nulo} ------------------- {(nulo*100)/total_de_votos:.2f}%')
