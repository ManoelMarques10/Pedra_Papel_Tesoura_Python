#Pograma Básico Para Jogar Pedra, Papel E Tesoura Contra A Máquina.

import random
from time import sleep

try:
    escolha = int(input('\33[34mEscolha Entre: \n[1]Pedra \n[2]Papel \n[3]Tesoura\n '))
    if escolha == 1:
        escolhal = 'Pedra'
    elif escolha == 2:
        escolhal = 'Papel'
    elif escolha == 3:
        escolhal = 'Tesoura'
    else:
        print('\33[31mEscolha inválida!')
        exit()
    if escolhal == 'Pedra':
        print('\33[33mSua Escolha Foi Pedra.')
    elif escolhal == 'Papel':
        print('\33[33mSua Escolha Foi Papel.')
    elif escolhal == 'Tesoura':
        print('\33[33mSua Escolha Foi Tesoura.')

    lista = 'Pedra', 'Papel', 'Tesoura'
    maquina = random.choice(lista)
    print(f'\33[35mJo...')
    sleep(1)
    print(f'\33[35mKen...')
    sleep(1)
    print(f'\33[35mPo!')
    sleep(1)
    print(f'\33[36mVocê Escolheu {escolhal} E A Máquina {maquina}.')
    if escolhal == 'Papel' and maquina == 'Papel':
        print('\33[31mEmpate')
    elif escolhal == 'Pedra' and maquina == 'Pedra':
        print('\33[31mEmpate')
    elif escolhal == 'Tesoura' and maquina == 'Tesoura':
        print('\33[31mEmpate')
    elif escolhal == 'Papel' and maquina == 'Pedra':
        print('\33[32mVocê Ganhou!!')
    elif escolhal == 'Pedra' and maquina == 'Tesoura':
        print('\33[32mVocê Ganhou!!')
    elif escolhal == 'Tesoura' and maquina == 'Papel':
        print('\33[32mVocê Ganhou!!')
    elif escolhal == 'Pedra' and maquina == 'Papel':
        print('\33[31mVocê Perdeu...')
    elif escolhal == 'Papel' and maquina == 'Tesoura':
        print('\33[31mVocê Perdeu...')
    elif escolhal == 'Tesoura' and maquina == 'Pedra':
        print('\33[31mVocê Perdeu...')
except ValueError:
    print('\33[31m Ops Algo Deu Errado...')

