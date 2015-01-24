##############################
## Generating List of Fake Genders

number = raw_input ("How many records would you like to generate?")
number = int(number)

import random
i = -1

for i in range (number):
	gender = ['Male','Female']
	genderchoice = random.choice(gender)
	identifier = i+1
	record = [identifier, genderchoice]
	print record
	i = i + 1


##############################
## Corrupting

## Request information on the number of corruptions to make

corruptper= float(raw_input ("What percentage of records would you like to corrupt?\n Please use integers"))
records_for_corruption = record
corrupt_amount = round((corruptper /100) * number,0)

## Corrupt the gender records; leave the identifier.
## Corruption will be to replace with missing values

gender_corrupt = random.sample(number, corrupt_amount)
array = 
s.replace(0, np.nan).ffill()

print "Number %r" % number
print "We will corrupt %r records to meet %r percent of corruption" % (corrupt_amount, corruptper)