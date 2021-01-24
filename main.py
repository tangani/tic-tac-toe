from tkinter import *
import numpy as np


class TicTacToe:
	# ------------------------------------------------------------------
	# Initialization Functions:
	# ------------------------------------------------------------------
	def __init__(self):

		self.size_of_board = 600
		self.width = 600
		self.height = 600
		self.symbol_size = (self.width / 3 - self.height / 8) / 2

		self.x_coordinates = np.zeros(shape=(1, 4))
		self.y_coordinates = np.zeros(shape=(4, 1))

		self.symbol_thickness = 3
		self.symbol_x_color = '#EE4035'
		self.symbol_o_color = '#0492CF'
		self.green_color = '#7BC043'

		self.window = Tk()
		self.window.title('Tic-Tac-Toe')
		self.canvas = Canvas(self.window, width=self.width, height=self.height)
		self.canvas.pack(fill=BOTH, expand=True)

		# Input from user in form of clicks
		self.window.bind('<Button-1>', self.click)
		self.window.bind('<Configure>', self.initialize_board)

		# self.initialize_board()
		self.player_x_turns = True
		self.board_status = np.zeros(shape=(3, 3))

		self.player_x_starts = True
		self.reset_board = False
		self.game_over = False
		self.tie = False
		self.X_wins = False
		self.O_wins = False

		self.X_score = 0
		self.O_score = 0
		self.tie_score = 0

	def mainloop(self):
		self.window.mainloop()

	def initialize_board(self, event):
		self.width = self.canvas.winfo_width() if self.canvas.winfo_width() != 1 else 600
		self.height = self.canvas.winfo_height() if self.canvas.winfo_width() != 1 else 600
		self.canvas.delete('grid_line')
		self.canvas.delete("all")

		count = 0
		for i in range(0, self.width, np.math.floor(self.width / 3)):
			if count <= 2:
				self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')
			self.x_coordinates[:, count] = i
			count += 1

		count = 0
		for i in range(0, self.height, np.math.floor(self.height / 3)):
			if count <= 2:
				self.canvas.create_line([(0, i), (self.width, i)], tag='grid_line')
			self.y_coordinates[count] = i
			count += 1

		# Redraw the board
		for i in range(3):
			if self.board_status[i][0] == -1:
				self.draw_x([i, 0])
			elif self.board_status[i][0] == 1:
				self.draw_o([i, 0])

			if self.board_status[i][1] == -1:
				self.draw_x([i, 1])
			elif self.board_status[i][1] == 1:
				self.draw_o([i, 1])

			if self.board_status[i][2] == -1:
				self.draw_x([i, 2])
			elif self.board_status[i][2] == 1:
				self.draw_o([i, 2])

	def play_again(self):
		# self.window.bind('<Button-1>', self.initialize_board)
		# self.initialize_board()
		self.player_x_starts = not self.player_x_starts
		self.player_x_turns = self.player_x_starts
		self.board_status = np.zeros(shape=(3, 3))

	# ------------------------------------------------------------------
	# Drawing Functions:
	# The modules required to draw required game based object on canvas
	# ------------------------------------------------------------------

	def draw_o(self, logical_position):
		logical_position = np.array(logical_position)
		x0, x1, y0, y1, x_depth, y_depth = self.convert_logical_to_grid_position(logical_position)
		self.canvas.create_oval(x0 + x_depth, y0 + y_depth, x1 - x_depth, y1 - y_depth, width=self.symbol_thickness,
								outline=self.symbol_o_color)

	def draw_x(self, logical_position):
		x0, x1, y0, y1, x_depth, y_depth = self.convert_logical_to_grid_position(logical_position)
		self.canvas.create_line(x0 + x_depth, y0 + y_depth, x1 - x_depth, y1 - y_depth,
								width=self.symbol_thickness, fill=self.symbol_x_color)
		self.canvas.create_line(x1 - x_depth, y0 + y_depth, x0 + x_depth, y1 - y_depth,
								width=self.symbol_thickness, fill=self.symbol_x_color)

	def display_game_over(self):

		if self.X_wins:
			self.X_score += 1
			text = 'Winner: Player 1 (X)'
			color = self.symbol_x_color
		# width = self.canvas.winfo_width() / 2
		# height = 5
		elif self.O_wins:
			self.O_score += 1
			text = 'Winner: Player 2 (O)'
			color = self.symbol_o_color
		else:
			self.tie_score += 1
			text = 'Its a tie'
			color = 'gray'

		self.canvas.delete("all")
		self.canvas.create_text(self.width / 2, self.height / 3, font="cmr 60 bold", fill=color, text=text)

		score_text = 'Scores \n'
		self.canvas.create_text(self.width / 2, 5 * self.height / 8, font="cmr 40 bold", fill=self.green_color,
								text=score_text)

		score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
		score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
		score_text += 'Tie                    : ' + str(self.tie_score)
		self.canvas.create_text(self.width / 2, 3 * self.height / 4, font="cmr 30 bold", fill=self.green_color,
								text=score_text)
		self.reset_board = True

		score_text = 'Click to play again \n'
		self.canvas.create_text(self.width / 2, 15 * self.height / 16, font="cmr 20 bold", fill="gray",
								text=score_text)

	# ------------------------------------------------------------------
	# Logical Functions:
	# The modules required to carry out game logic
	# ------------------------------------------------------------------

	def convert_logical_to_grid_position(self, logical_position):
		x0 = self.x_coordinates[0, logical_position[0]]
		x1 = self.x_coordinates[0, logical_position[0] + 1]
		y0 = self.y_coordinates[logical_position[1], 0]
		y1 = self.y_coordinates[logical_position[1] + 1, 0]
		x_depth = self.width / 50
		y_depth = self.height / 50
		return x0, x1, y0, y1, x_depth, y_depth

	def convert_grid_to_logical_position(self, grid_position):
		grid_position = np.array(grid_position)
		return np.array([grid_position[0] // (self.width // 3), grid_position[1] // (self.height // 3)])

	def is_grid_occupied(self, logical_position):
		if self.board_status[logical_position[0]][logical_position[1]] == 0:
			return False
		else:
			return True

	def is_winner(self, player):

		player = -1 if player == 'X' else 1

		# Three in a row
		for i in range(3):
			if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
				return True
			if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
				return True

		# Diagonals
		if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
			return True

		if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
			return True

		return False

	def is_tie(self):

		r, c = np.where(self.board_status == 0)
		tie = False
		if len(r) == 0:
			tie = True

		return tie

	def is_game_over(self):
		# Either someone wins or all grid occupied
		self.X_wins = self.is_winner('X')
		if not self.X_wins:
			self.O_wins = self.is_winner('O')

		if not self.O_wins:
			self.tie = self.is_tie()

		game_over = self.X_wins or self.O_wins or self.tie

		if self.X_wins:
			print('X wins')
		if self.O_wins:
			print('O wins')
		if self.tie:
			print('Its a tie')

		return game_over

	def click(self, event):
		grid_position = [event.x, event.y]
		# print("Event x:", event.x, "Event Y:", event.y)
		logical_position = self.convert_grid_to_logical_position(grid_position)

		if not self.reset_board:
			if self.player_x_turns:
				if not self.is_grid_occupied(logical_position):
					self.draw_x(logical_position)
					self.board_status[logical_position[0]][logical_position[1]] = -1
					self.player_x_turns = not self.player_x_turns
			else:
				if not self.is_grid_occupied(logical_position):
					self.draw_o(logical_position)
					self.board_status[logical_position[0]][logical_position[1]] = 1
					self.player_x_turns = not self.player_x_turns

			# Check if game is concluded
			if self.is_game_over():
				self.display_game_over()
		# print('Done')
		else:  # Play Again
			self.canvas.delete("all")
			# self.window.bind('<Button-1>', self.initialize_board)
			self.play_again()
			self.reset_board = False


game_instance = TicTacToe()
game_instance.mainloop()
