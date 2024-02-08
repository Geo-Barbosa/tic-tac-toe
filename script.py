from os import system


headquarter = [ # Headquarter 3x3
	[x for x in range(7, 10)],
	[y for y in range(4, 7)],
	[z for z in range(1, 4)],
]


def winner_horinzotal(): # Verify if has a winner in the headquarter at horizontal
	if headquarter[0][0] == headquarter[0][1] == headquarter[0][2] \
	or headquarter[1][0] == headquarter[1][1] == headquarter[1][2] \
	or headquarter[2][0] == headquarter[2][1] == headquarter[2][2]:
		return True
	return False


def winner_vertical(): # Verify if has a winner in the headquarter at vertical
	if headquarter[0][0] == headquarter[1][0] == headquarter[2][0] \
	or headquarter[0][1] == headquarter[1][1] == headquarter[2][1] \
	or headquarter[0][2] == headquarter[1][2] == headquarter[2][2]:
		return True
	return False


def winner_diagonal(): # Verify if has a winner in the headquarter at diagonal
	if headquarter[0][0] == headquarter[1][1] == headquarter[2][2] \
	or headquarter[0][2] == headquarter[1][1] == headquarter[2][0]:
		return True
	return False


def execute(function, *args): # Function to execute a lambda function
	return function(*args)


def show_or_modify_headquarter(player=None, play=None): # Show the headquarter or modify it if it was a played
	for x in range(0, 3):
		if player is None: # If the parameter was passed to the funcion,
			print('|', end='') #  the headquarter will not be shown
		for y in range(0, 3):
			if headquarter[x][y] == play and play is not None:
				headquarter[x][y] = player
			if player is None:
				print(headquarter[x][y], end='|')
		if player is None:
			print()


def is_int_valid(num): # Validation of a int number
	try:
		num  = int(num)
		return num
	except ValueError:
		return False


player = 'X' # In tic-tac-toe, the "X" always begins
plays = set()
win = False
while True:
	show_or_modify_headquarter() # Without parameters, the headquarter will be shown
	if player == 'X':
		option = input('Digite onde o X vai jogar: ')
	else:
		option = input('Digite onde o O vai jogar: ')
	option = is_int_valid(option)
	if not option or option > 9:
		system('cls')
		print('Valor ínválido!')
		continue
	if option not in plays: # Verify if the play is valid or not
		system('cls')
		plays.add(option)
		show_or_modify_headquarter(player, option) # If the play is valid, the position choosed by the player will be substituted by the player
	else:
		system('cls')
		print('Essa casa está ocupada, escolha outro número!') # If that place was occupied by an "X" or a "O", the player will have to play again
		continue
	while True: # In this While True, we go to check if we have a winner, in any position
		win = winner_diagonal()
		if win:
			break
		win = winner_horinzotal()
		if win:
			break
		win = winner_vertical()
		if win:
			break
		break
	if win:
		break
	if len(plays) == 9: # If all spaces are occupied and we don't have a winner, its a Draw and the game stops
		break
	player = execute(lambda player: 'X' if player == 'O' else 'O', player) # This lambda funcion swich the players
show_or_modify_headquarter()
if win: # If "X" or "O" winned
	print(f'O "{player}" ganhou após {len(plays)} rodadas!')
else: # If it's a Draw
	print('DEU VELHA')