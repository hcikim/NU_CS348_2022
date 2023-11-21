# Student Name: Taewook Kim

import common

def search_pizza(board, row, col):
	
	piz_y = None
	piz_x = None

	for i in range(row):
		for j in range(col):
			if board[i][j] == common.constants.PIZZA:
				piz_y = i
				piz_x = j

	return piz_y, piz_x

def print_2D_array(arr):
	for i in range(len(arr)):
		print(arr[i])
	print("\n")

def route(y, x, action, direction):

	if y + 1 <= 5 and direction == 'south':
		return y + 1, x
	
	elif x - 1 >= 0 and direction == 'west':
		return y, x - 1

	elif y - 1 >= 0 and direction == 'north':
		return y - 1, x
	
	elif x + 1 <= 5 and direction == 'east':
		return y, x + 1	
	
	else:
		return y, x


def get_qstate(y, x, action, battery_drop_cost):

	list_q = []

	if action == 1:
		list_q.append([route(y, x, action, 'south'), - battery_drop_cost, 0.7])
		list_q.append([route(y, x, action, 'east'), - battery_drop_cost, 0.15])
		list_q.append([route(y, x, action, 'west'), - battery_drop_cost, 0.15])

	if action == 2:
		list_q.append([route(y, x, action, 'west'), - battery_drop_cost, 0.7])
		list_q.append([route(y, x, action, 'north'), - battery_drop_cost, 0.15])
		list_q.append([route(y, x, action, 'south'), - battery_drop_cost, 0.15])

	if action == 3:
		list_q.append([route(y, x, action, 'north'), - battery_drop_cost, 0.7])
		list_q.append([route(y, x, action, 'east'), - battery_drop_cost, 0.15])
		list_q.append([route(y, x, action, 'west'), - battery_drop_cost, 0.15])

	if action == 4:
		list_q.append([route(y, x, action, 'east'), - battery_drop_cost, 0.7])
		list_q.append([route(y, x, action, 'north'), - battery_drop_cost, 0.15])
		list_q.append([route(y, x, action, 'south'), - battery_drop_cost, 0.15])

	if action == 5:
		list_q.append([route(y, x, action, 'south'), - 2 * battery_drop_cost, 0.8])
		list_q.append([route(y, x, action, 'east'), - 2 * battery_drop_cost, 0.1])
		list_q.append([route(y, x, action, 'west'), - 2 * battery_drop_cost, 0.1])

	if action == 6:
		list_q.append([route(y, x, action, 'west'), - 2 * battery_drop_cost, 0.8])
		list_q.append([route(y, x, action, 'north'), - 2 * battery_drop_cost, 0.1])
		list_q.append([route(y, x, action, 'south'), - 2 * battery_drop_cost, 0.1])

	if action == 7:
		list_q.append([route(y, x, action, 'north'), - 2 * battery_drop_cost, 0.8])
		list_q.append([route(y, x, action, 'east'), - 2 * battery_drop_cost, 0.1])
		list_q.append([route(y, x, action, 'west'), - 2 * battery_drop_cost, 0.1])

	if action == 8:
		list_q.append([route(y, x, action, 'east'), - 2 * battery_drop_cost, 0.8])
		list_q.append([route(y, x, action, 'north'), - 2 * battery_drop_cost, 0.1])
		list_q.append([route(y, x, action, 'south'), - 2 * battery_drop_cost, 0.1])
	
	return list_q


def get_reward(qstate, discount, values):

	reward = 0

	for q in qstate:
		
		probability = q[2]
		rewd = q[1]
		next_y = q[0][0] 
		next_x = q[0][1]

		reward += probability * (rewd + (discount * values[next_y][next_x]))

	return reward


def convergence(values, new_values, threshold):

	row = len(values)
	col = len(values[0])

	max_value = - float('inf')

	for y in range(row):
		for x in range(col):
			if abs(values[y][x] - new_values[y][x]) > max_value:
				max_value = abs(values[y][x] - new_values[y][x])

	if max_value < threshold:
		return True

	return False

lastValue = None


def update_board(old_board, new_board):
    for i in range(len(old_board)):
        for j in range(len(old_board[i])):
            old_board[i][j] = round(new_board[i][j],2) 

def drone_flight_planner (map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone

	row = len(map)
	col = len(map[0])
	
	threshold = 0.001
	converge = False

	while not converge:
		
		new_values = [row[:] for row in values]

		for y in range(row):
			for x in range(col):
				if map[y][x] == common.constants.CUSTOMER:
					new_values[y][x] = delivery_fee
					policies[y][x] = common.constants.EXIT

				elif map[y][x] == common.constants.RIVAL:
					new_values[y][x] = - dronerepair_cost
					policies[y][x] = common.constants.EXIT
				
				else:
					max_value = - float('inf')
					old_action = 0

					for action in range(1, 9):
						qstate = get_qstate(y, x, action, battery_drop_cost)
						v = get_reward(qstate, discount, values)

						if v > max_value:
							new_values[y][x] = v
							max_value = v
							policies[y][x] = action
							old_action = action

						elif v == max_value:
							if old_action < action:
								policies[y][x] = old_action

							elif action <= old_action:
								policies[y][x] = action

		
		converge = convergence(values, new_values, threshold)
		
		for y in range(row):
			for x in range(col):
				values[y][x] = new_values[y][x]

	piz_y, piz_x = search_pizza(map, row, col)
	new_board = [row[:] for row in values]
	update_board(new_board,values)
	print_2D_array(new_board)
	return values[piz_y][piz_x]


	

