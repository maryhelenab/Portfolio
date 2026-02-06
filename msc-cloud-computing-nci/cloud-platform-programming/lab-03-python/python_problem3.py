# Problem 3: You have been asked to create an
# application for the Student Union shop which sells
# caps for 5, shirts for 10 and hoodies for 20. Your
# application should allow the user to input the quantity
# of each item a student wants to buy and then
# calculate and output the total cost. When you have
# finished the implementation, test your application to
# ensure that the calculations are correct.

class Calculat:

	def __init__(self, caps, shirts, hoodies):
		self.caps = caps
		self.shirts = shirts
		self.hoodies = hoodies

	def calculate(self):
		total = (self.caps * 5) + (self.shirts * 10) + (self.hoodies * 20)
		return total

# Main Programm
caps = int(input("Enter the quantidade os caps: "))
shirts = int(input("Enter the quantidade os shirts: "))
hoodies = int(input("Enter the quantidade os hoodies: "))

sell = Calculat(caps,shirts,hoodies) #created the obj
total_value = sell.calculate() #call the method

print(f"The total value is: {total_value}")
