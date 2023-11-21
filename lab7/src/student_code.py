# Student Name: Taewook Kim

import common
import math #note, for this lab only, your are allowed to import math


def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	
	height = len(image)
	width = len(image[0])

	line = common.Line()
	line.m = 0
	line.b = 0

	votes = common.init_space(2000, 2000)

	for y in range(height):
		for x in range(width):
			
			# if a pixel is black
			if image[y][x] == 0:
				m = - 10
				
				while m < 10:
					b = m * (- x) + y
					
					if - 1000 <= b and b < 1000:
						m_index = math.floor((m * 100) + 1000)
						b_index = math.floor(b + 1000)
						
						votes[b_index][m_index] += 1

					m = m + 0.01

	max_val = - float('inf')
	line_m = 0
	line_b = 0

	for y in range(len(votes)):
		for x in range(len(votes[y])):
			if votes[y][x] > max_val:
				max_val = votes[y][x]
				line_b = y
				line_m = x

	line.m = (line_m - 1000) / 100
	line.b = line_b - 1000

	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	height = len(image)
	width = len(image[0])

	votes = common.init_space(200, 200)

	for y in range(height):
		for x in range(width):
			
			# if a pixel is black
			if image[y][x] == 0:
				for b in range(len(votes)):
					for a in range(len(votes[b])):
						r_sqr = math.pow((x - a), 2) + math.pow((y - b), 2)

						if 890 <= r_sqr and r_sqr <= 910:
							votes[b][a] += 1

	circles = 0

	for y in range(len(votes)):
		for x in range(len(votes[y])):
			if votes[y][x] > 44:
				circles += 1
	
	return_counts = round(circles / 2)

	return return_counts
				