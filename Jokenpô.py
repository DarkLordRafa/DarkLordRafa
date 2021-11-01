from time import sleep
from random import randint, choice
print('''Olá, eu sou o computador 😎
Vamos ver se você consegue ganhar de mim no famoso jogo Jokenpô. Ou pedra, papel, tesoura, se preferir.
Mas primeiro, vamos escolher seu avatar!
''')
while True:
	avatar = input('(1)🙂 (2)😷 (3)👻 (4)💀 (5)👨 (6)👩 (7)🦖\n\n(8)🎃\n\n---> ')
	if avatar.isdecimal():
		avatar = int(avatar)
	else:
		print('\nOpção inválida!\nTente de novo\n')
		continue
	if not 0 < int(avatar) < 9:
		print('\nOpção inválida!\nTente de novo\n')
		continue
	break
player = '🙂' '😷' '👻' '💀' '👨' '👩' '🦖' '🎃'[avatar - 1]
cpu = '😎'
print(f'\nSeu avatar: {player}')
print(f'\nAgora sim, vamos começar nosso joguinho. Prepare-se para perder 😎\nE quando você perder... SUA \033[1;31mALMA\033[m SERÁ MINHA\n{"😈":^40}\n\nQuer dizer... sua *\033[1;34mADMIRAÇÃO\033[m* será minha\n\n{"😎":^40}')
print('Vamos começar!')

while True:
	cpu_choose = randint(1, 3)
	player_choose = input('\nEscolha uma das opções abaixo:\n\n(1) 🤜 (Pedra)\n(2) 🤚 (Papel)\n(3) ✌️ (Tesoura)\n\n---> ')
	if player_choose.isdecimal():
		player_choose = int(player_choose)
	elif player_choose == 'MATRIX':
		while True:
			print('\033[0;33m', choice('A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'X' 'W' 'Y' 'Z' '1' '2' '3' '4' '5' '6' '7' '8' '9'), end = '')
	else:
		print('\nPor favor escolha uma das opções!')
		continue
	if not  0< int(player_choose) < 4:
			print('\nPor favor escolha uma das opções!')
			continue
	else:
		print('\n\033[1;33mCARREGANDO...\033[m\n')
		sleep(2)
		player_emoji = '🤜' '🤚' '✌️'[player_choose - 1]
		cpu_emoji = '🤜' '🤚' '✌️'[cpu_choose - 1]
	if player_choose == 1 and cpu_choose == 2:
		vencedor = cpu
	elif player_choose == 1 and cpu_choose == 3:
		vencedor = player
	elif player_choose == 2 and cpu_choose == 1:
		vencedor = player
	elif player_choose == 2 and cpu_choose == 3:
		vencedor = cpu
	elif player_choose == 3 and cpu_choose == 1:
		vencedor = cpu
	elif player_choose == 3 and cpu_choose == 2:
		vencedor = player
	else:
		print('Você   Computador')
		print(f'\n{player_emoji}    \033[1;31mVS\033[m   {cpu_emoji}\n\nEMPATOU 😎\nVamos de novo! 😎')
		while True:
			continuar = input('\n(1) Pode apostar!\n(2) Não\n\n---> ')
			if continuar.isdecimal():
				continuar = int(continuar)
			else:
				print('\nEscolha uma opção!')
				continue
			if 0 < int(continuar) < 3:
				break
			else:
				print('\nOpção inválida!\nTente de novo')
				continue
		if continuar == 1:
			continue
		else:
			print('\n\nCOVARDE! 👿')
			exit()
	break
print('Você   Computador')
print(f'\n{player_emoji}    \033[1;31mVS\033[m   {cpu_emoji}')
input(('\nPróximo --->'))
#vencedor = cpu
if vencedor == cpu:
	print(f'\nEU VENCI {cpu}')
	sleep(2)
	print(f'\nAgora sua \033[1;31mALMA\033[m é MINHA!\n\n              😈 HAHAHAHA!')
	sleep(4)
	print(f'''
             🏛️🏛️🏛️🏛️🏛️🏛️🏛️
             🏛️ ☆      ♂ 🏛️
             🏛️    😈    🏛️
             🏛️          🏛️
             🏛️    {player}    🏛️
             🏛 ♀      † 🏛️
             🏛️🏛️🏛️🏛️🏛️🏛️🏛️''')

elif vencedor == player:
	print(f'\nEU VENCI {player}')
	sleep(2)
	print(f'\nO que? Eu PERDI? 🤨')
	input('\nPróximo --->')
	print('\nIsso não é possível 👿')
	input('\nPróximo --->')
	print('\nNão posso perder para um HUMANO! 👿')
	input('\nPróximo --->')
	print('...')
	sleep(3)
	print('''               NÃÃÃÃÃÃÃÃO!!!
	     🔥🔥🔥🔥🔥🔥🔥
             🔥💥💥💥💥💥🔥
             🔥💥💥💥💥💥🔥
             🔥💥💥👿💥💥🔥
             🔥💥💥💥💥💥🔥
             🔥💥💥💥💥💥🔥
             🔥🔥🔥🔥🔥🔥🔥

Você venceu o computador e salvou sua alma
...''')
if vencedor == player:
	sleep(4)
	input('\nPróximo --->')
	print('\nParece que o computador deixou cair algo\n...')
	sleep(4)
	print('\nÉ um pedaço de papel velho\n...')
	sleep(4)
	input('\nPróximo --->')
	print('\n"MATRIX"')
	sleep(4)
