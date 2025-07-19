#Define a function to calculate pay based on hours worked and pay rate
#This function will handle overtime pay for hours over 40
def calculate_pay(hours, rate):
	if hours > 40:
		otp = (hours - 40) * 1.5 * rate
		regpay = 40 * rate
		totpay= (otp + regpay)
		print("Gross Pay $",totpay)
    
	else:
		pay = hours * rate
		print("Gross Pay $",pay)
		

h = input('How many hours did you work? ')
pr = input('What is your pay rate? ')
hfloat = float(h)
prfloat = float(pr)
calculate_pay(hfloat, prfloat)
# The function calculate_pay is called with the hours and rate inputs




