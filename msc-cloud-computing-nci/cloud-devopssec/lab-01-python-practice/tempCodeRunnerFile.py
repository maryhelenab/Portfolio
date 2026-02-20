
from problem1_greeting import User

class BankAccount:

	def __init__(self, user, account_number, id, balance=0):
		self.user = user
		self.account_number = account_number
		self.id = id
		self.balance = balance

	def show_balance(self):
		print(f"Account holder: {self.user.name}")
		print(f"Current balance: €{self.balance}")

	
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposit successful. New balance: €{self.balance}")
		else:
			print("Invalid deposit amount.")

#create a User object
user1 = User("Maryhelen Bastos")

# Creating a bank account
account1 = BankAccount(user1, 1, 2992384, 500)

# Showing initial balance
account1.show_balance()

# Depositing money
account1.deposit(200)