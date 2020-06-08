from random import randint

#makes and prints board
board = []

for i in range(5):
  board.append(['O']*5)

def print_board(board_in):
  for row in board_in:
    print (" ".join(row))

print_board(board)

#chooses random location for ship
def random_row(board_in):
  return randint(0, len(board_in))
def random_col(board_in):
  return randint(0, len(board_in))

guess_count = 0
def total_guesses(x):
  x += 1
  if x == 10:
    print ("HAHAHA! You have no more guesses left! I winnn!!!!")

def row_guess():
  input("Ship Row: ")

def col_guess():
  input("Ship Column: ")  

def check():
  if row_guess == ship_row and col_guess == ship_col:
    print ("Oh no! You sank my ship!")
  elif int(row_guess) == int(ship_row) or int(col_guess) == int(ship_col):
    print ("Oh no! you hit me!")
    row_guess()
    col_guess()
    total_guesses(guess_count)
  else:
    print ("HA! I'm safe!")
    row_guess()
    col_guess()
    total_guesses(guess_count)

def repeat():
	while int(row_guess) != int(ship_row) or int(col_guess) != int(ship_col):
		row_guess()
		col_guess()
		total_guesses(guess_count)
		check()


random_row(board)
random_col(board)
row_guess()
col_guess()
total_guesses(guess_count)
check()
repeat()
