class Product(object):
	def __init__(self, price, itemName, weight, brand):
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "Sold"
		return self

	def tax(self, tax):
		self.price += self.price * tax
		return self

	def exchange(self, reason):
		if reason == "broken":
			self.price = 0
			self.status = "Broken"
		else:
			self.price -= self.price * 0.2
			self.status = "Used"
		return self

	def displayInfo(self):
		print "Price: ${}".format(self.price)
		print "Name: {}".format(self.itemName)
		print "Weight: {}".format(self.weight)
		print "Brand: {}".format(self.brand)
		print "Status: {}".format(self.status)
		return self

item1 = Product(15,"Shampoo","8oz","Pantene")
item2 = Product(3, "Yogurt", "6oz","Yoplait")

item1.exchange("cracked").displayInfo()
item2.sell().tax(.20).displayInfo()