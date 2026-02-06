class Calculat:

	def __ini__(self, caps, shirts, hoodies):
		self.caps = caps
		self.shirts = shirts
		self.hoodies = hoodies

	def calculate(self):
		value = (self.caps * 5) + (self.shirts * 10) + (self.hoodies * 20)
		print(f"The value total is: {value}")

# Main Programm
caps = int(input("Enter the quantidade os caps: "))
shirts = int(input("Enter the quantidade os shirts: "))
hoodies = int(input("Enter the quantidade os hoodies: "))


value = Calculat