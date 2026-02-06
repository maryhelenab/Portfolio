# Problem 4: Having just started college, Bob has been busy
# looking for a part-time job to fund his new college social life
# and after only two weeks of looking he has managed to get
# two job offers! Each job comes with different hours, basic rates
# of pay and over-time rates so he needs to work out which
# would get him the most money. Develop an application that
# would allow Bob to enter his basic pay rate, his number of
# regular hours work per week and his number of overtime
# hours per week. The application should then calculate and
# display Bob’s total basic pay for the week, his overtime pay for
# the week and his total pay including overtime. Note: The
# overtime rate is 1.5 times the basic rate of pay.

# basicpayrate = float(input("Enter your basic pay rate por hour: "))
# regularhours = float(input("Enter your hours per week: "))
# overtimehours = float(input("Enter your number of overtime hours per week: "))
# value_week_hours = regularhours * basicpayrate
# overtimehours_week = overtimehours * (basicpayrate*1.5)
# total_week = (value_week_hours) + (overtimehours_week)

# print(f"Basic pay per week: {value_week_hours:.2f}")
# print(f"Overtime pay per week: {overtimehours_week:.2f}")
# print(f"Total pay per week: {total_week:.2f}")

# Validation function for only positive values

def get_positive_float(field_name):
	while True:
		try:
			value = float(input(f"Enter your {field_name}: "))
			if value < 0:
				print(f"Invalid {field_name}.\n Please enter a number greater than or equal to 0.")
			else:
				return value
		except ValueError:
			print("Invalid {field_name}.\n Please enter a numeric value.")
	
class JobPay:

	def __init__(self, basic_rate, regular_hours, overtime_hours):
		if basic_rate < 0 or regular_hours < 0 or overtime_hours < 0:
			raise ValueError("Pay rate and hours must be non-negative values.")
		self.basic_rate = basic_rate
		self.regular_hours = regular_hours
		self.overtime_hours = overtime_hours
	
	def basic_pay(self):
		return self.regular_hours * self.basic_rate
	
	def overtime_pay(self):
		if self.overtime_hours <= 0:
			return 0
		return self.overtime_hours * (self.basic_rate * 1.5)
	
	def total_pay(self):
		return self.basic_pay() + self.overtime_pay()

# Main Programm
print("\n--- Job A ---")
basic_rate = get_positive_float("Basic pay rate per hour (Job A)")
regular_hours = get_positive_float("Regular hours per week (Job A)")
overtime_hours = get_positive_float("Overtime hours per week (Job A)")
job = JobPay(basic_rate, regular_hours, overtime_hours)

print(f"Basic pay this week: {job.basic_pay():.2f}")
print(f"Overtime pay this week: {job.overtime_pay():.2f}")
print(f"Total pay this week: {job.total_pay():.2f}")

print("\n--- Job B ---")

basic_rate_b = get_positive_float("basic pay rate per hour (Job B)")
regular_hours_b = get_positive_float("regular hours per week (Job B)")
overtime_hours_b = get_positive_float("overtime hours per week (Job B)")

print(f"Basic pay this week: {job.basic_pay():.2f}")
print(f"Overtime pay this week: {job.overtime_pay():.2f}")
print(f"Total pay this week: {job.total_pay():.2f}")

job_b = JobPay(basic_rate_b, regular_hours_b, overtime_hours_b)

print("\n--- Comparison ---")

total_a = job.total_pay()
total_b = job_b.total_pay()

if total_a > total_b:
	print("Job A pays more than Job B. \n")
elif total_b > total_a:
    print("Job B pays more than Job A. \n")
else:
    print("Both jobs pay the same amount. \n")
