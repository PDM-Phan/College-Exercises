from time import sleep

print('Sobre o jogo Valheim, responda essas 3 perguntas abaixo.')
while True:
    print('-=' * 30)
    pergunta_1 = input('Quais animais são possiveis de se domesticar no jogo?\n'
                       'a) Cervos e Javalis\n'
                       'b) Cervos e Lobos\n'
                       'c) Lobos e Javalis\n'
                       'Qual a resposta certa? ').strip().lower()
    if pergunta_1.isnumeric() or pergunta_1 == '':
        print('[ERRO] Por favor escreva uma opção entre a,b e c.')
        print('Tente novamente.')
        sleep(1)
        continue
    else:
        if pergunta_1 in 'abc':
            while True:
                sleep(0.5)
                print('-=' * 30)
                pergunta_2 = input('Qual o unico alimento é vindo da terra que o javali não come?\n'
                                   'a) Cogumelos\n'
                                   'b) Mirtilos\n'
                                   'c) Cogumelos Amarelos\n'
                                   'Qual a resposta certa? ').strip().lower()
                if pergunta_2.isnumeric() or pergunta_2 == '':
                    print('[ERRO] Por favor escreva uma opção entre a,b e c.')
                    print('Tente novamente.')
                    sleep(1)
                    continue
                else:
                    if pergunta_2 in 'abc':
                        while True:
                            sleep(0.5)
                            print('-=' * 30)
                            pergunta_3 = input('No oceano, serpentes são mais perigosas do que o "Kraken".\n'
                                               'Essa afirmação é:\n'
                                               'a) Correta\n'
                                               'b) Impossivel\n'
                                               'c) Depende do barco\n'
                                               'Qual a resposta certa? ').strip().lower()
                            if pergunta_3.isnumeric() or pergunta_3 == '':
                                print('[ERRO] Por favor escreva uma opção entre a,b e c.')
                                print('Tente novamente.')
                                sleep(1)
                                continue
                            else:
                                if pergunta_3 in 'abc':
                                    print('Analizando respostas...')
                                    sleep(2)
                                    break
                                else:
                                    print('[ERRO] Por favor escreva uma opção entre a,b e c.')
                                    print('Tente novamente.')
                                    sleep(1)
                                    continue
                        break
                    else:
                        print('[ERRO] Por favor escreva uma opção entre a,b e c.')
                        print('Tente novamente.')
                        sleep(1)
                        continue
            break
        else:
            print('[ERRO] Por favor escreva uma opção entre a,b e c.')
            print('Tente novamente.')
            sleep(1)
            continue
print(f'Na primeira pergunta sua resposta foi  {pergunta_1}. '
      f'{"Que é a resposta correta! Parabens!" if pergunta_1 == "c" else "A resposta correta era a letra c."}')
sleep(1)
print('-' * 80)
print(f'Na segunda pergunta sua resposta foi {pergunta_2}. '
      f'{"Que é a resposta correta! Parabens!" if pergunta_2 == "c" else "A resposta correta era a letra c."}')
sleep(1)
print('-' * 80)
print(f'Na terceira pergunta sua resposta foi {pergunta_3}. '
      f'{"Que é a resposta correta! Parabens!" if pergunta_3 == "a" else "A resposta correta era a letra a."}')
