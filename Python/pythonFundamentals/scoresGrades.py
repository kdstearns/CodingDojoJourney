def scores():
	for count in range(0,10):
		import random
		random_num = random.randint(60,100)
		print random_num
		if random_num in range(60,70):
			print "Score: {}; Your grade is D".format(random_num)
		elif random_num in range(70,80):
			print "Score: {}; Your grade is C".format(random_num)
		elif random_num in range(80,90):
			print "Score: {}; Your grade is B".format(random_num)
		elif random_num in range(90,101):
			print "Score: {}; Your grade is A".format(random_num)	
	print "End of the program. Bye!"
print scores()