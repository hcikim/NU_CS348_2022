#Student Name: Taewook Kim

def order(data):

	for i in range(1, len(data)):

		tmp = data[i]
		j = i - 1

		while(j >=0 and tmp < data[j]):
			
			data[j + 1] = data[j]
			j = j - 1

		data[j + 1] = tmp

	return 0