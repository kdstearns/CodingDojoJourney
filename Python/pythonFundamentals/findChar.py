word_list = ['hello', 'world','my','name','is','Anna']
char = 'o'

def findChar(var):
	new_list = []
	for element in var:
		if char in element:
			new_list.append(element)

	print new_list

findChar(word_list)