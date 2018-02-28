class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
		
	def display_all(self):
		print "Price: ${}".format(self.price)
		print "Speed: {}mph".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Mileage: {}mi".format(self.mileage)
		print "Tax: {}%".format(self.tax)
		return self

car1 = Car("30000","15","Full","15000")
car2 = Car("45000","45","Almost Empty","32500") 
car3 = Car("60000","63","Half Full","63000") 
car4 = Car("75000","70","Empty","5000") 
car5 = Car("9000","30","Full","28750")
car6 = Car("80000","85","Running on Fumes","88000")

