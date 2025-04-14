#Pograma Básico Para Jogar Pedra, Papel E Tesoura Contra A Máquina.

import random
from time import sleep
jogarnovamente = ' '
vitorias = 0

try:
    while jogarnovamente != 'n':
        escolha = int(input('\33[34mEscolha entre: [1]Pedra🗿 [2]Papel📜 [3]Tesoura✂️ [4]Sair ❌\n\33[35mEscolha:\33[m '))
        if escolha == 1:
            decisao = 'Pedra'
        elif escolha == 2:
            decisao = 'Papel'
        elif escolha == 3:
           decisao = 'Tesoura'
        elif escolha == 4:
            exit()
        else:
            while escolha != 1 and escolha != 2 and escolha != 3:
                print('\33[31mEscolha inválida, tente novamente! ')
                escolha = int(input('\33[34mEscolha entre: [1]Pedra🗿 [2]Papel📜 [3]Tesoura✂️ [4]Sair ❌\n\33[35mEscolha:\33[m '))
                if escolha == 1:
                    decisao = 'Pedra'
                elif escolha == 2:
                    decisao = 'Papel'
                elif escolha == 3:
                    decisao = 'Tesoura'

        if decisao == 'Pedra':
            print('\33[33mSua escolha foi pedra. 🗿')
        elif decisao == 'Papel':
            print('\33[33mSua escolha foi papel. 📜')
        elif decisao == 'Tesoura':
            print('\33[33mSua escolha foi tesoura. ✂️')

        lista = 'Pedra', 'Papel', 'Tesoura'
        maquina = random.choice(lista)
        print(f'\33[35mJo...')
        sleep(0.45)
        print(f'\33[35mKen...')
        sleep(0.45)
        print(f'\33[35mPo!')
        sleep(0.45)
        print(f'\33[36mVocê escolheu "{decisao}" e a máquina "{maquina}".')
        if decisao == 'Papel' and maquina == 'Papel':
            print('\33[1;31mEmpate.\33[m')
            vitorias = 0
        elif decisao == 'Pedra' and maquina == 'Pedra':
            print('\33[1;31mEmpate.\33[m')
            vitorias = 0
        elif decisao == 'Tesoura' and maquina == 'Tesoura':
            print('\33[1;31mEmpate.\33[m')
            vitorias = 0
        elif decisao == 'Papel' and maquina == 'Pedra':
            vitorias += 1
            print(f'\33[1;32mVocê venceu!!! \33[31mWinstreak: {vitorias}X 🔥.\33[m')
        elif decisao == 'Pedra' and maquina == 'Tesoura':
            vitorias += 1
            print(f'\33[1;32mVocê venceu!!! \33[31mWinstreak: {vitorias}X 🔥.\33[m')
        elif decisao == 'Tesoura' and maquina == 'Papel':
            vitorias += 1
            print(f'\33[1;32mVocê venceu!!! \33[31mWinstreak: {vitorias}X 🔥.\33[m')
        elif decisao == 'Pedra' and maquina == 'Papel':
            vitorias = 0
            print('\33[1;31mVocê perdeu.\33[m')
            jogarnovamente = input('\33[34mQuer jogar novamente? [S] ou [N]\nEscolha: ').lower()
            if jogarnovamente == 's':
                print('\33[32mTudo bem, vamos jogar de novo! 👌')
            elif jogarnovamente == 'n':
                break
            else:
                while jogarnovamente != "s" and jogarnovamente != "n":
                    print('\33[31mO programa só aceita "S" ou "N".')
                    jogarnovamente = input('\33[34mQuer jogar novamente? [S] ou [N]\nEscolha: ').lower()

        elif decisao == 'Papel' and maquina == 'Tesoura':
            vitorias = 0
            print('\33[1;31mVocê perdeu.\33[m')
            jogarnovamente = input('\33[34mQuer jogar novamente? [S] ou [N]\nEscolha: ').lower()
            if jogarnovamente == 's':
                print('\33[32mTudo bem, vamos jogar de novo! 👌')
            elif jogarnovamente == 'n':
                break
            else:
                while jogarnovamente != "s" and jogarnovamente != "n":
                    print('\33[31mO programa só aceita "S" ou "N"')
                    jogarnovamente = input('\33[34mQuer jogar novamente? [S] ou [N]\nEscolha: ').lower()

        elif decisao == 'Tesoura' and maquina == 'Pedra':
            vitorias = 0
            print('\33[1;31mVocê perdeu.\33[m')
            jogarnovamente = input('\33[34mQuer jogar novamente? [S] ou [N]\nEscolha: ').lower()
            if jogarnovamente == 's':
                print('\33[32mTudo bem, vamos jogar de novo! 👌')
            elif jogarnovamente == 'n':
                break
            else:
                while jogarnovamente != "s" and jogarnovamente != "n":
                    print('\33[31mO programa só aceita "S" ou "N"')
                    jogarnovamente = input('\33[34mQuer jogar novamente? [S] ou [N]\nEscolha: ').lower()

except ValueError:
    print('\33[31mOps! algo deu errado... 😣')
