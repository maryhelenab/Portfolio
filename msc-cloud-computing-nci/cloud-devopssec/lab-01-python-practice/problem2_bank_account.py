# Problem 2 - Bank Account Class

class BankAccount: # Create a Class
	#A class is a blueprint for creating objects

	def __init__(self, owner, balance = 0):
		self.owner = owner     			
		self.balance = balance

	def deposit(self, amount):          
		self.balance += amount
		print 

