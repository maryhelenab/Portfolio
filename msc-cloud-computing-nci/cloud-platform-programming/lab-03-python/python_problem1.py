#  Problem 1: Develop an application that asks the user
# for her/his name, and then greets them with their
# name.

class User: # Created Class

	def __init__ (self, name):
		self.name = name

	def greet(self):
		print(f'Welcome {self.name}!') 

# Only run this code if this file is being run directly.
if __name__ == "__main__":

	# Ask the user for their name
	name = input("Enter your full name: ")

	# Create a User object
	user = User(name)

	# Greet the user
	user.greet()
		



