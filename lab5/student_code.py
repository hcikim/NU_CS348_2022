# Student Name: Taewook Kim

import common

_empty = 0

#helpful, but not needed
class variables:
	counter=0

def is_completed(sudoku):
	cnt = 0

	for i in range(len(sudoku)):
		if 0 in sudoku[i]:
			return False
		else:
			cnt += 1

	if cnt != 0:
		return True

def backtrack(sudoku):

	variables.counter += 1

	status = is_completed(sudoku)
	
	if status:
		return True

	else:

		y, x = get_empty_elements(sudoku)

		for v in range(1, 10):
			availability = common.can_yx_be_z(sudoku, y, x, v)
			
			if availability:
				sudoku[y][x] = v
				R = backtrack(sudoku)

				if R == True:
					return True

				sudoku[y][x] = 0

		return False

def get_empty_elements(sudoku):

	for y in range(len(sudoku)):
		for x in range(len(sudoku)):
			if sudoku[y][x] == _empty:
				return y, x

def update_domain(domain, y, x, v):

	del domain[str(y) + ', ' + str(x)]
	empty = False
	
	for i in range(9):	
		y_b = int(y / 3) * 3 + int(i / 3)
		x_b = int(x / 3) * 3 + i % 3

		if str(y) + ', ' + str(i) in domain and len(domain[str(y) + ', ' + str(i)]) != 0 and v in domain[str(y) + ', ' + str(i)]:
			index = domain[str(y) + ', ' + str(i)].index(v)
			domain[str(y) + ', ' + str(i)].pop(index)

			if len(domain[str(y) + ', ' + str(i)]) == 0:
				empty = True
				
		if str(i) + ', ' + str(x) in domain and len(domain[str(i) + ', ' + str(x)]) != 0 and v in domain[str(i) + ', ' + str(x)]:
			index = domain[str(i) + ', ' + str(x)].index(v)
			domain[str(i) + ', ' + str(x)].pop(index)

			if len(domain[str(i) + ', ' + str(x)]) == 0:
				empty = True
				
		if str(y_b) + ', ' + str(x_b) in domain and len(domain[str(y_b) + ', ' + str(x_b)]) != 0 and v in domain[str(y_b) + ', ' + str(x_b)]:
			index = domain[str(y_b) + ', ' + str(x_b)].index(v)
			domain[str(y_b) + ', ' + str(x_b)].pop(index)

			if len(domain[str(y_b) + ', ' + str(x_b)]) == 0:
				empty = True

	return empty, domain


def forwardcheck(sudoku, domain):

	variables.counter += 1
	status = is_completed(sudoku)
	
	if status:
		return True

	else:
		y, x = get_empty_elements(sudoku)
		
		for v in range(1, 10):
			availability = common.can_yx_be_z(sudoku, y, x, v)
			
			if availability:
				old_domain = {key: value[:] for key, value in domain.items()}
				emp, new_domain = update_domain(domain, y, x, v)

				if emp != True:

					sudoku[y][x] = v
					R = forwardcheck(sudoku, new_domain)

					if R == True:
						return True

					sudoku[y][x] = 0

				domain = old_domain

		return False


def sudoku_backtracking(sudoku):
	variables.counter = 0
	#put your code here

	backtrack(sudoku)

	return variables.counter

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#put your code here

	# create domain dict
	domain = {}
	
	# initialize domain
	for y in range(len(sudoku)):
		for x in range(len(sudoku)):
			if sudoku[y][x] != _empty:
				continue

			else:
				tmp = []
				for i in range(1, 10):
					if common.can_yx_be_z(sudoku, y ,x, i):
						tmp.append(i)

				domain[str(y) + ', ' + str(x)] = tmp

	forwardcheck(sudoku, domain)

	return variables.counter
