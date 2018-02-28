# TRY WRITING IN JS FIRST
# var y = []
# for(var x = 1; x <=12; x++)
# {
# 	console.log(x);
# 	y.push = x + x;
# }
# console.log(y);

orig_list = [x,1,2,3,4,5,6,7,8,9,10,11,12]
#think about how to how to set it up to replace each position in this list and then create a block with your loop
x = 0
y = 0
for count in range (0,12):
	if x < 2:
		x = x + 1
		print x
	if x >= 2:
		y = x * 2
		print y