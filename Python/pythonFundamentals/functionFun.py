# ODD/EVEN
def odd_even():
	for count in range(1,2001):
		if count % 2 == 0:
			print "Number is {}. This is an even number.".format(count)

		else:
			print "Number is {}. This is an odd number.".format(count)
print odd_even()

# MULTIPLY
def multiply(arr,num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

# HACKER CHALLENGE
def layered_multiples(arr):
	new_array = []
	for index1 in range(len(arr)):
		switch = []
		for index2 in range(arr[index1]):
			switch.append(1)
		new_array.append(switch)
	return new_array
x = layered_multiples(b)
print x