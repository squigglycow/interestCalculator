def moveDecimalPoint(num, places):
		'''Move the decimal place in a given number.

		Parameters:
			num (int/float): The number in which you are modifying.
			places (int): The number of decimal places to move.
		
		Returns:
			(float)
		
		Example:
			moveDecimalPoint(11.05, -2) #returns: 0.1105
		'''
		from decimal import Decimal

		num_decimal = Decimal(str(num))  # Convert the input number to a Decimal object
		scaling_factor = Decimal(10 ** places)  # Create a scaling factor as a Decimal object

		result = num_decimal * scaling_factor  # Perform the operation using Decimal objects
		return float(result)  # Convert the result back to a float




days = 1
paymentEveryXDays = int(input("Days between payment (if you pay biweekly-14, monthly-30, and so forth): "))
payment = float(input("How much are you paying toward the loan - payment will occur every x days?: "))
paymentWait = int(input("How many days in the future will payments start? (0 if payment starts today): "))
loanBalance = float(input("Balance of the loan: "))
loanInterest = float(input("Interest of the loan (enter numeric/decimal value only): "))
loanInterest = moveDecimalPoint(loanInterest, -2) #moveDecimal would shift an answer of 3.48 to 0.0348 so it can correctly do interest
loanInterest = loanInterest/365 + 1 #this is the interest rate factor, the effective amount of interest earned per day
totalInterestAccrued = 0


while loanBalance > 0:
	temp = loanBalance
	loanBalance = loanBalance*loanInterest
	totalInterestAccrued = loanBalance - temp + totalInterestAccrued
	
	if days > paymentWait:
		if days % paymentEveryXDays == 0:
			loanBalance = loanBalance - payment
	
	#print("Total interest accrued: ", totalInterestAccrued)
	#print(loanBalance)
	days = days + 1
	week = (days/7)

print("Remaining balance of loan:", loanBalance, "It took this many weeks:", week)
print("Total interest accrued: ", totalInterestAccrued)