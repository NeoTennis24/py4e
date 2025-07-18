#Rewrite Practice2 to give employee time and half over 40 hours

h= input('How many hours did you work? ') 
pr= input('What is your pay rate? ')
hfloat= float(h)
prfloat= float(pr)
otp= float(hfloat-40) * float(1.5) * prfloat
regpay= float(40) * prfloat

if hfloat > 40:
	  print(otp + regpay)
else:
	print("Regliar")
	print(prfloat * hfloat)





  