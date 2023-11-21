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


def manhattan(a, b):
	return sum(abs(v1 - v2) for v1, v2 in zip(a,b))


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


def node_explore(map, y, x, start, frontier, history, explored):

	loc_frontier = frontier
	loc_history = history
	g_n = 0

	if len(history) == 0:
		g_n = 0

	else:
		g_n = history[str(y) + ", " + str(x)][1]

	if x + 1 < width and [y, x + 1] not in explored: #right
		if map[y][x + 1] == _empty or map[y][x + 1] == _end:
			loc_frontier.append([y, x + 1])
			loc_history[str(y) + ', ' + str(x + 1)] = [[y, x], g_n + 1]

	if y + 1 < height and [y + 1, x] not in explored: #down
		if map[y + 1][x] == _empty or map[y + 1][x] == _end:
			loc_frontier.append([y + 1, x])
			loc_history[str(y + 1) + ', ' + str(x)] = [[y, x], g_n + 1]

	if 0 <= x - 1 and [y, x - 1] not in explored: #left
		if map[y][x - 1] == _empty or map[y][x - 1] == _end:
			loc_frontier.append([y, x - 1])
			loc_history[str(y) + ', ' + str(x - 1)] = [[y, x], g_n + 1]

	if 0 <= y - 1 and [y - 1, x] not in explored: #up
		if map[y - 1][x] == _empty or map[y - 1][x] == _end:
			loc_frontier.append([y - 1, x])
			loc_history[str(y - 1) + ', ' + str(x)] = [[y, x], g_n + 1]

	return loc_frontier, loc_history


def tie_break(node_next, node_1, node_2):

	f_n_1 = node_1[0]
	f_n_2 = node_2[0]

	n1_x = node_1[1][1]
	n2_x = node_2[1][1]

	n1_y = node_1[1][0]
	n2_y = node_2[1][0]

	if f_n_1 < f_n_2:
		node_next[0] = node_1

	elif n1_x < n2_x:
		node_next[0] = node_1

	elif n1_x == n2_x:
		if n1_y < n2_y:
			node_next[0] = node_1

		elif n1_y > n2_y:
			node_next[0] = node_2

	elif node_next[0] == None:
		node_next[0] = node_2


def get_node(closed, start, history):

	min_f = float('inf')
	new_node = []
	tmp = [None]

	if len(closed) == 1 and len(history) == 0:
		return [start, 0]

	for i in range(len(closed)):

		if closed[i][0] < min_f:
			min_f = closed[i][0]
			new_node = [closed[i][0], closed[i][1],i]

		elif closed[i][0] == min_f:
			if tmp[0] == None:
				tie_break(tmp, [closed[i][0], closed[i][1], i], new_node)
			else:
				tie_break(tmp, new_node, tmp[0])
				tie_break(tmp, [closed[i][0], closed[i][1], i], tmp[0])

	node_val = []

	if tmp[0] == None:
		node_val = [new_node[0], new_node[1], new_node[2]]

	elif new_node[0] < tmp[0][0]:
		node_val = [new_node[0], new_node[1], new_node[2]]

	else:
		if new_node[1][1] < tmp[0][1][1]:
			node_val = [new_node[0], new_node[1], new_node[2]]

		elif new_node[1][1] == tmp[0][1][1]:
			if new_node[1][0] < tmp[0][1][0]:
				node_val = [new_node[0], new_node[1], new_node[2]]

			else:	 
				node_val = [tmp[0][0], tmp[0][1], tmp[0][2]]
				
		else:
			node_val = [tmp[0][0], tmp[0][1], tmp[0][2]]


	return [node_val[1], node_val[2]]


def astar_search(map):
	found = False
	
	frontier = []
	closed = []
	history = {}
	explanded = []

	sy, sx, ey, ex = find_start_and_end(map)
	start = [sy, sx]
	closed.append([sy, sx])

	while len(closed) != 0:

		frontier = []

		node, index = get_node(closed, start,history)
		closed.pop(index)

		n_y, n_x = node[0], node[1]
		curr = map[n_y][n_x]

		# if current node is the goal, stop searching.
		if curr == _end:
			map[sy][sx] = _path
			map[n_y][n_x] = _path

			while [n_y, n_x] != [sy, sx]:
				if map[n_y][n_x] == _explored:
					map[n_y][n_x] = _path
				n_y, n_x = history[str(n_y) + ', ' + str(n_x)][0]
			
			found = True
			return found

		frontier, history = node_explore(map, n_y, n_x, start, frontier, history, explanded)
		map[n_y][n_x] = _explored

		for child in frontier:

			if map[child[0]][child[1]] == _explored:
				continue

			h_n = manhattan([ey, ex], child)
			g_n = history[str(child[0]) + ", " + str(child[1])][1]
			f_n = g_n + h_n
			closed.append([f_n, [child[0], child[1]]])

		explanded.append(node)


	return found
