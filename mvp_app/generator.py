##############################

## Import requirements
## NOTE: Must do sudo pip install XlsxWriter
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random
import xlsxwriter

##############################

## Generator - Create list with the identifier
def identifier(num):
	identifier = []
	identifier = [i+1 for i in xrange(num)]
	return identifier

## Generator - Create a list of random genders
def genderrecord(num):
	genderrecord = []
	for i in range (num):
		gender = ['Male','Female']
		genderchoice = random.choice(gender)
		genderrecord.append(genderchoice)
		i = i + 1
	return genderrecord

## Corruptor - Request information on the number of corruptions to make

def gender_corrupting_perc(num):
	corruptper= float(raw_input ("What percentage of records would you like to corrupt?"))
	records_for_corruption = num
	corrupt_amount = int(round((corruptper /100) * num,0))
	if (corruptper >=1) and (corrupt_amount == 0):
		corrupt_amount = 1
	return corrupt_amount

## Corruptor - Replace values with "."

def missing_corrupt_func(copydf, newdf, corrupt_amount):
	remove = np.random.choice(range(len(copydf)), corrupt_amount, replace=False)
	j = 0
	for j in range(len(remove)):
		place = remove[j]
		newdf[place] = "."  
		j = j+1
	return newdf 
	
########################################

## Asking users how many records to generate and creating index

number = int(raw_input ("How many records would you like to generate?"))
identifier = identifier(number)

## Creating random genders

genderrecord = genderrecord (number)

## Storing genders and index into a dataframe

record = pd.DataFrame( {"Identifier" : identifier,
						"Gender" : genderrecord })

## Printing "Clean" file to excel

writer = pd.ExcelWriter('CleanData', engine='xlsxwriter')
record.to_excel(writer, sheet_name='Sheet1')
writer.save()

## Copying column to corrupt

newdf = record["Gender"].copy()

# Creating corrupted column

newdf2 = missing_corrupt_func(record, newdf, gender_corrupting_perc(number))

## Add back corrupted column into the dataframe

record2 = record
record2["Gender"] = newdf2

## Printing "Corrupted" file to excel

writer = pd.ExcelWriter('CorruptData', engine='xlsxwriter')
record2.to_excel(writer, sheet_name='Sheet1')
writer.save()
