from user import User

# Problem 2: Write an application that displays the
# recommended weight given the user’s age and height
# (in centimeters) using the following formula:
# RW = (height - 100 + age % 10) * 0.90

class RW(User):

	def __init__ (self, name, age, height):
		super().__init__(name)
		self.age = age
		self.height = height
	
	def calculate_rw(self):
		return (self.height - 100 + self.age % 10) * 0.90

	def show_rw(self):
		rw = self.calculate_rw()
		print(f"{self.name}, your recommende weight is: {rw:.2f} kg")


#main programa
name = input("Enter your full name: ")
age = int(input("Enter your age:"))
height_input = float(input("Enter your height (in centimeters): "))

def validate_height(height):
	if height <= 0:
		raise ValueError("Height must be a positive number.")
	if height < 3: # If height is less than 3, assume it's in meters
		height = height * 100
	return height

height = validate_height(height_input)
user = RW(name, age, height)
user.show_rw()
