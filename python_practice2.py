#Write a program that prompts users for hours
#and rate per hour to compute gross pay

h= input('How many hours did you work? ') 
rph= input('What is your rate per hour? ') 
#h and rph are str, wrap them in float to int
gp= float(h) * float(rph)
print("Gross Pay:", gp)