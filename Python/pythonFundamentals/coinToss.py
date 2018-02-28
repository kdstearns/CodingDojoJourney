import random
def coinToss():
	head = 0
	tail = 0
	print "Starting the program"
	for count in range(0,5000):
		num = random.random()
		print num
		num_rounded = round(num)
		print num_rounded
		if num_rounded == 0:
			head += 1
			print "Attempt #{} Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far.".format(count,head,tail)
		if num_rounded == 1:
			tail += 1
			print "Attempt #{} Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far.".format(count,head,tail)
	print "Ending the program, thank you!"
print coinToss()