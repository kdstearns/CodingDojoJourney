# PART 1
def draw_stars(var):
	new_str = ''
	for index1 in range(len(var)):
		switch = ''
		for index2 in range(var[index1]):
			switch += '*'
		new_str = switch
		print new_str
x = [4,6,1,3,5,7,25]
draw_stars(x)

# # PART 2
# def draw_more_than_stars(var):
# 	for index1 in range(len(var)):
# 		stars = ''
# 		letters = ''
# 		if isinstance(var[index1],int):
# 			for index2 in range(var[index1]):
# 				stars += '*'
# 			print stars
# 		if isinstance(var[index1],str):
# 			letter1 = ''
# 			letter1 += var[index1]
# 			letter1 = letter1[0].lower()
# 			for index2 in range(len(var[index1])):
# 				letters += letter1
# 			print letters

# x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
# draw_more_than_stars(x)

# PART 2 -- BETTER OPTION
def draw_more_than_stars(var):
	i = 0
	for element in var:
		if isinstance(var[i], int):
			print element * "*"
			i += 1
		elif isinstance(var[i], str):
			temp = len(var[i])
			for element in var[i]:
				print temp * element[0].lower()
				break
			i += 1

x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
draw_more_than_stars(x)