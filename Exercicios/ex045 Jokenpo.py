import emoji
import random
from time import sleep

Boasvindas = input('Bem vindo ao \033[1;97mJokenpô!\033[m')
sleep(0.5)
#Tutorial de como jogar!
print('''\033[1;97mComo jogar\033[m: 
- Cada jogador joga 1 vez por rodada
- Na rodada você terá que escolher entre \033[4mPEDRA\033[m, \033[4mPAPEL\033[m ou \033[4mTESOURA\033[m
- Ganha quem conseguir "eliminar o adversário" 
- Caso a escolha for igual, resultará em empate''')

Pedra = emoji.emojize(':fist:', language='alias')
Tesoura = emoji.emojize(':v:', language='alias')
Papel = emoji.emojize(':raised_hand:', language='alias')

print('''\033[1;97mComo eliminar\033[m:
- Pedra{} quebra a Tesoura{}
- Tesoura{} corta o Papel{}
- Papel{} enrola a Pedra{}'''.format(Pedra, Tesoura, Tesoura, Papel, Papel, Pedra))
input(' ')

#Começo da rodada!
print('\033[1;97mComeço da rodada!!\033[m')
escolha = print('''Sua vez: 
1 - \033[4mPedra\033[m 
2 - \033[4mPapel\033[m
3 - \033[4mTesoura\033[m''')

#escolha do jogador
jogador = int(input('Qual é a sua jogada? '))
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura!!!')
sleep(1)
print('-' * 30)

if jogador == 1:
    print('Você jogou {}'.format(Pedra))
elif jogador == 2:
    print('Você jogou {}'.format(Papel))
elif jogador == 3:
    print('Você jogou {}'.format(Tesoura))

#escolha do computador
lista = (Pedra, Papel, Tesoura)
computador = random.choice(lista)
print('Computador jogou {}'.format(computador))
print('-' * 30)
if computador == Pedra and jogador == 3:
    print('Você \033[1;31mPERDEU! ')
elif computador == Tesoura and jogador == 2:
    print('Você \033[1;31mPERDEU! ')
elif computador == Papel and jogador == 1:
    print('Você \033[1;31mPERDEU! ')
elif computador == Tesoura and jogador == 3:
    print('\033[1;33mEMPATE! ')
elif computador == Pedra and jogador == 1:
    print('\033[1;33mEMPATE! ')
elif computador == Papel and jogador == 2:
    print('\033[1;33mEMPATE! ')
else:
    print('Você \033[1;32mVENCEU! ')
