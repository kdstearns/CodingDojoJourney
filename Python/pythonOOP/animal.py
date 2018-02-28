class Animal(object):
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run (self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Your health level is at {}".format(self.health)
		return self

animal1 = Animal("Giraffe", 15)
animal2 = Animal("Lemur", 5)
animal1.walk().walk().walk().run().run().displayHealth()
animal2.pet().fly()displayHealth()  # does not allow to pet, fly or print I am a Dragon!

class Dog(Animal):
	def __init__(self):
		self.health = 150

	def pet(self):
		self.health += 5
		return self

Dog().walk().walk().walk().run().run().pet().displayHealth()
Dog().fly().displayHealth() # does not allow to fly or print I am a Dragon!

class Dragon(Animal):
	def __init__(self):
		self.health = 170
		super(Dragon,self).displayHealth()
		print "I am a Dragon!"

	def fly(self):
		self.health -= 10
		return self

Dragon().fly().displayHealth()