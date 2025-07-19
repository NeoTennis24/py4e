#Rewrite Practice2 to give employee time and half over 40 hours

h= input('How many hours did you work? ') 
pr= input('What is your pay rate? ')
# Wrap inputs in Try/Except to handle non-numeric input
try:
	hfloat = float(h)
	prfloat = float(pr)
except:
	print("Please enter valid numeric values for hours and pay rate.")
	exit()
# Calculate overtime pay for hours over 40
otp = float(hfloat - 40) * float(1.5) * prfloat
regpay = float(40) * prfloat

if hfloat > 40:
	  print(otp + regpay)
else:
  
	print(prfloat * hfloat)