#!/usr/bin/python3

def print_board(board):
	"""Affiche le plateau de jeu."""
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board):
	"""Vérifie s'il y a un gagnant (3 symboles identiques alignés)."""
	# Lignes
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	# Colonnes
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	# Diagonales
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def is_board_full(board):
	"""Vérifie si le plateau est complètement rempli (égalité)."""
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"
	while True:
		print_board(board)
		try:
			row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
			col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

			# Vérifie que les coordonnées sont valides
			if not (0 <= row < 3 and 0 <= col < 3):
				print("Invalid coordinates. Please enter numbers between 0 and 2.")
				continue

			if board[row][col] == " ":
				board[row][col] = player
				if check_winner(board):
					print_board(board)
					print(f"Player {player} wins!")
					break
				elif is_board_full(board):
					print_board(board)
					print("It's a tie!")
					break
				else:
					# Changer de joueur
					player = "O" if player == "X" else "X"
			else:
				print("That spot is already taken! Try again.")

		except ValueError:
			print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
	tic_tac_toe()
