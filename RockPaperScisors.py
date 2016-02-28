Player1 = input ('Player 1 choose: ')
Player2 = input ('Player 2 choose: ')

if Player1 == 'rock' and Player2 == 'rock':
    print ('Tie')
if Player1 == 'scissors' and Player2 == 'scissors':
	print('Tie')
if Player1 == 'paper' and Player2 == 'paper':
	print('Tie')
if Player1 == 'paper' and Player2 == 'rock':
	print('Player1 wins')
if Player1 == 'paper' and Player2 == 'scissors':
	print('Player2 wins')
if Player1 == 'rock' and Player2 == 'scissors':
	print('Player1 wins')
if Player1 == 'rock' and Player2 == 'paper':
	print('Player2 wins')
if Player1 == 'scissors' and Player2 == 'rock':
	print('Player2 wins')
if Player1 == 'scissors' and Player2 == 'paper':
	print('Player1 wins')

if Player1 != 'rock' and Player1 != 'paper' and Player1 != 'scissors':
	print('Enter correctly: paper, rock or scissors')
if Player2 != 'rock' and Player2 != 'paper' and Player2 != 'scissors':
	print('Enter correctly: paper, rock or scissors')
