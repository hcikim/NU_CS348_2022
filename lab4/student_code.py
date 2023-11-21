# Student Name: Taewook Kim

import common

X = common.constants.X
O = common.constants.O
zero = common.constants.NONE

infi = float('inf')

def check_status(board):
	
	status = common.game_status(board)
	
	if status == X: # X win
		return 5

	elif status == O: # O win
		return -5

	elif status == zero and 0 not in board: # tie
		return 0

	else:
		msg = 'unfinished'
		return msg


def max_value(board, turn):
		
	v = -infi
	utility = check_status(board)

	if utility != 'unfinished':
		return utility

	# for all empty board position P
	for i in range(len(board)):
		y = int(i / 3)
		k = y * 3
		x = i - k

		if common.get_cell(board, y, x) == 0:
			# place X at P on board
			common.set_cell(board, y, x, turn)
			
			value = min_value(board, O)

			if value > v:
				v = value

			# remove X from P
			common.set_cell(board, y, x, zero)

	return v


def min_value(board, turn):
	
	v = infi
	utility = check_status(board)

	if utility != 'unfinished':
		return utility

	# for all empty board position P
	for i in range(len(board)):
		y = int(i / 3)
		k = y * 3
		x = i - k

		if common.get_cell(board, y, x) == 0:
			# place O at P on board
			common.set_cell(board, y, x, turn)
			
			value = max_value(board, X)

			if value < v:
				v = value

			# remove O from P
			common.set_cell(board, y, x, zero)

	return v


def ab_max_value(board, turn, alpha, beta):

	v = -infi
	utility = check_status(board)

	if utility != 'unfinished':
		return utility

	# for all empty board position P
	for i in range(len(board)):
		y = int(i / 3)
		k = y * 3
		x = i - k

		if common.get_cell(board, y, x) == 0:
			# place X at P on board
			common.set_cell(board, y, x, turn)
			
			value = ab_min_value(board, O, alpha, beta)

			if value > v:
				v = value

			# remove X from P
			common.set_cell(board, y, x, zero)

			if v >= beta:
				return v

			if v > alpha:
				alpha = v

	return v


def ab_min_value(board, turn, alpha, beta):

	v = infi
	utility = check_status(board)

	if utility != 'unfinished':
		return utility

	# for all empty board position P
	for i in range(len(board)):
		y = int(i / 3)
		k = y * 3
		x = i - k

		if common.get_cell(board, y, x) == 0:
			# place O at P on board
			common.set_cell(board, y, x, turn)
			
			value = ab_max_value(board, X, alpha, beta)

			if value < v:
				v = value

			# remove O from P
			common.set_cell(board, y, x, zero)

			if v <= alpha:
				return v

			if v < beta:
				beta = v

	return v


def prune(board, turn, alpha, beta):

	v = None

	if turn == X:
		v = ab_max_value(board, turn, alpha, beta)
	
	if turn == O:
		v = ab_min_value(board, turn, alpha, beta)
	
	if v == 5:
		return X

	elif v == -5:
		return O

	else:
		return zero


def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	
	v = None

	if turn == X:
		v = max_value(board, turn)
	
	if turn == O:
		v = min_value(board, turn)
	
	if v == 5:
		return X

	elif v == -5:
		return O

	else:
		return zero

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

	# alpha: Max's best option on path to root
	a = -infi
	# beta: Min's best option on path to root
	b = infi

	return prune(board, turn, a, b)
