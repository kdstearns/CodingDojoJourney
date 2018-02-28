import random
class Call(object):
	def __init__(self,name,phone,time,reason):
		self.id = random.randint(0,1000)
		self.name = name
		self.phone = phone
		self.time = time
		self.reason = reason

	def display(self):
		print "Id: {}".format(self.id)
		print "Name: {}".format(self.name)
		print "Phone: {}".format(self.phone)
		print "Time: {}".format(self.time)
		print "Reason: {}".format(self.reason)
		return self

class CallCenter(Call):
	def __init__(self,name,phone,time,reason):
		super(CallCenter,self).__init__(name,phone,time,reason)
		self.calls = []
		self.queue = len(self.calls)

	def add(self):
		self.calls.append(1)
		self.queue += 1
		# print self.calls
		return self

	def remove(self):
		del self.calls[0]
		self.queue -= 1
		# print self.calls
		return self

	def info(self):
		print "Name: {}, Phone #: {}, Queue: {}".format(self.name,self.phone,self.queue)
		
caller1 = Call("Kyla", "214-995-2655", "8:05PM", "tech support")
caller1.display()
caller2 = CallCenter("Chelsea", "214-870-2351", "10:30AM", "wasted")
caller2.add().add().add().add().remove().display().info()