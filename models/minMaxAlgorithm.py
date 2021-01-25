import numpy as np

tic_tac_board = ["X", 1, "O", "X", 4, "X", "O", "O", 8]

aiMark = "X"
humanMark = "O"


def emptyIndexes(current_board_status):
	return [x for x in current_board_status if x != "X" and x != "O"]


def checkIfWinner(board_status, human_mark="O"):
	for i in range(3):
		if board_status[3 * i] == board_status[3 * i + 1] == board_status[3 * i + 2]:
			if board_status[3 * i] == "X":
				return "AI has won"
			else:
				return "Hoofman being has won"
		if board_status[3 * i + 1] == board_status[3 * i + 2] == board_status[3 * i + 2]:
			if board_status[3 * i + 1] == "X":
				return "AI has won"
			else:
				return "Hoofman being has won"

	if board_status[0] == board_status[4] == board_status[9]:
		if board_status[0] == "X":
			return "AI has won"
		else:
			return "Hoofman being has won"

	if board_status[6] == board_status[4] == board_status[2]:
		if board_status[6] == "X":
			return "AI has won"
		else:
			return "Hoofman being has won"

	return False


def minimax(board_status, human_mark="O"):
	...


availableIndexes = emptyIndexes(tic_tac_board)
print(availableIndexes)
