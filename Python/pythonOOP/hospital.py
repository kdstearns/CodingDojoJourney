import random
class Patient(object):
	def __init__(self,name,allergies):
		self.id = random.randint(0,99999)
		self.name = name
		self.allergies = allergies
	bedNum = 0

	def displayInfo(self):
		print "Name: {}".format(self.name)
		print "Id: {}".format(self.id)
		print "Allergies: {}".format(self.allergies)
		return self

class Hospital(object):
	def __init__(self):
		self.patients = []
		self.hospName = "Harmony Grove Hospital"
		self.capacity = 350
		self.bedCount = []
		for element in range (1, self.capacity+1):
			self.bedCount.append(element)

	def admit(self, patient):
		self.patients.append(patient.name)
		# print self.patients
		if len(self.patients) < self.capacity:
			# print self.bedCount
			patient.bedNum = self.bedCount[0]
			# print patient.bedNum
			self.bedCount.remove(patient.bedNum)
			# print self.bedCount
			print "Welcome to {}. Your Bed # is: {}".format(self.hospName,patient.bedNum)	
		else:
			print "We are full and will have to refer you to another facility."
		return self

	def discharge(self, patient):
		self.bedCount.append(patient.bedNum)
		patient.bedNum = 0
		self.patients.remove(patient.name)
		# print self.patients
		# print self.bedCount
		# print patient.bedNum
		print "{}, Thank you for choosing {}. You have been checked out.".format(patient.name, self.hospName)
		return self

hospital1 = Hospital()
patient1 = Patient("Ashley Boucher", "peanuts")
patient1.displayInfo()
hospital1.admit(patient1)

patient2 = Patient("Karen Carney", "dairy")
patient2.displayInfo()
hospital1.admit(patient2)

patient3 = Patient("Julianne Nutt", "none")
patient3.displayInfo()
hospital1.admit(patient3)

hospital1.discharge(patient1)