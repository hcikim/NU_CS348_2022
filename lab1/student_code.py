#Student Name: Taewook Kim

import common

_empty = 0
_wall = 1
_start = 2
_end = 3
_explored = 4
_path = 5

width = common.constants.MAP_WIDTH
height = common.constants.MAP_HEIGHT


def find_start_and_end(map):
	s_y = False
	s_x = False
	e_y = False
	e_x = False
	
	row = len(map)
	col = len(map[0])

	for i in range(row):
		for j in range(col):
			if map[i][j] == _start:
				s_y = i
				s_x = j
			if map[i][j] == _end:
				e_y = i
				e_x = j

	print("s_y, s_x:", s_y, s_x)
	print("e_y, e_x:", e_y, e_x)

	return (s_y, s_x, e_y, e_x)


def bfs_explore(map, y, x, frontier, history):

	loc_frontier = frontier
	loc_history = history

	if x + 1 < width: #right
		if map[y][x + 1] == _empty or map[y][x + 1] == _end:
			loc_frontier.append([y, x + 1])
			loc_history[str(y) + ', ' + str(x + 1)] = [y, x]

	if y + 1 < height: #down
		if map[y + 1][x] == _empty or map[y + 1][x] == _end:
			loc_frontier.append([y + 1, x])
			loc_history[str(y + 1) + ', ' + str(x)] = [y, x]

	if 0 <= x - 1: #left
		if map[y][x - 1] == _empty or map[y][x - 1] == _end:
			loc_frontier.append([y, x - 1])
			loc_history[str(y) + ', ' + str(x - 1)] = [y, x]

	if 0 <= y - 1: #up
		if map[y - 1][x] == _empty or map[y - 1][x] == _end:
			loc_frontier.append([y - 1, x])
			loc_history[str(y - 1) + ', ' + str(x)] = [y, x]

	return loc_frontier, loc_history


def dfs_explore(map, y, x, frontier, history):

	loc_frontier = frontier
	loc_history = history

	# reverse order due to stack.pop()
	if 0 <= y - 1: #up
		if map[y - 1][x] == _empty or map[y - 1][x] == _end:
			loc_frontier.append([y - 1, x])
			loc_history[str(y - 1) + ', ' + str(x)] = [y, x]

	if 0 <= x - 1: #left
		if map[y][x - 1] == _empty or map[y][x - 1] == _end:
			loc_frontier.append([y, x - 1])
			loc_history[str(y) + ', ' + str(x - 1)] = [y, x]

	if y + 1 < height: #down
		if map[y + 1][x] == _empty or map[y + 1][x] == _end:
			loc_frontier.append([y + 1, x])
			loc_history[str(y + 1) + ', ' + str(x)] = [y, x]

	if x + 1 < width: #right
		if map[y][x + 1] == _empty or map[y][x + 1] == _end:
			loc_frontier.append([y, x + 1])
			loc_history[str(y) + ', ' + str(x + 1)] = [y, x]

	return loc_frontier, loc_history


def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	stack = []
	history = {}

	sy, sx, ey, ex = find_start_and_end(map)
	stack.append((sy, sx))

	while stack:

		n_y, n_x = stack.pop()
		map[n_y][n_x] = _explored

		if (n_y, n_x) == (ey, ex):
			
			while (n_y, n_x) != (sy, sx):
				if map[n_y][n_x] == _explored:
					map[n_y][n_x] = _path
				n_y, n_x = history[str(n_y) + ', ' + str(n_x)]
			
			map[sy][sx] = _path
			
			found = True
			return found

		stack, history = dfs_explore(map, n_y, n_x, stack, history)

	return found
	

def bf_search(map):
	found = False;
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	queue = []
	history = {}

	sy, sx, ey, ex = find_start_and_end(map)
	queue.append((sy, sx))


	while queue:

		n_y, n_x = queue.pop(0)
		map[n_y][n_x] = _explored

		# if node is goal, then trace back and find path.
		if (n_y, n_x) == (ey, ex):
			while (n_y, n_x) != (sy, sx):
				if map[n_y][n_x] == _explored:
					map[n_y][n_x] = _path
				n_y, n_x = history[str(n_y) + ', ' + str(n_x)]
			
			map[sy][sx] = _path
			
			found = True
			return found

		queue, history = bfs_explore(map, n_y, n_x, queue, history)
	
	return found
