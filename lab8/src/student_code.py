# Student Name: Taewook Kim

import common

def part_one_classifier(data_train, data_test):
	w = common.init_data(1, 3)[0]
	length = len(data_train)
	accuracy = 0
	
	while accuracy / length <= 0.95:
		accuracy = 0

		for i in range(length):
			feature = [data_train[i][0], data_train[i][1]]
			value = int(data_train[i][2])
			
			c = classifier_one(feature, w)

			if c == value:
				accuracy += 1

			else:
				w[0] += 0.01 * (value - c)
				w[1] += 0.01 * (value - c) * feature[0]
				w[2] += 0.01 * (value - c) * feature[1]

	for idx, example in enumerate(data_test):
		f = [example[0], example[1]]
		c = classifier_one(f, w)
		data_test[idx][2] = c


def classifier_one(f, w):
	# dot product
	dot = w[0] + w[1] * f[0] + w[2] * f[1]

	if dot < 0:
		return 0
	else:
		return 1


def part_two_classifier(data_train, data_test):
	w = common.init_data(10, 2)
	length = len(data_train)
	accuracy = 0

	while accuracy / length <= 0.95:
		accuracy = 0

		for i in range(length):
			feature = [data_train[i][0], data_train[i][1]]
			value = int(data_train[i][2])
			
			c = classifier_two(feature, w)

			if c == value:
				accuracy += 1

			else:
				w[value][0] += 0.01 * feature[0]
				w[value][1] += 0.01 * feature[1]
				w[c][0] -= 0.01 * feature[0]
				w[c][1] -= 0.01 * feature[1]

	for idx, example in enumerate(data_test):
		f = [example[0], example[1]]
		
		c = classifier_two(f, w)
		data_test[idx][2] = c


def classifier_two(feature, w):
	maximum = -float('inf')
	max_idx = None

	for i in range(common.constants.NUM_CLASSES):
		dot = w[i][0] * feature[0] + w[i][1] * feature[1]

		if maximum < dot:
			maximum = dot
			max_idx = i

	return max_idx
