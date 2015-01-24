#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Corruptor Functions
#If using corruptor functions, must preserve 
#original list
#functions used
#output list
#This allows us to recreate process
#even though we are using probablistic code

#This is better executed as a reverse spell check\

from random import randint

'''
1)      Missing Value corrupter

a.       “Replaces attribute value with an empty string.”

2)      Character edit corrupter

a.       “This function randomly selects a position in an attribute value (based on real-world studies more likely towards the middle or end of a value”

3)      Keyboard corrupter:

a.       “This function simulates a typing error and randomly replaces a character with a neighboring character according to the to a keyboard layout matrix.  Different probabilistic can be set for selecting a replacement in a row and or column”

4)      Optical Character recognition corrupter

a.       “This function is based on a look-up file that contains pairs of character sequences that have similar shapes, such as 5 ß> S or m ßàr n.  Such pairs can model OCR errors.”

5)      Phonetic corrupter

a.       “This function simulates phonetic variations (for example for names that sound similar).  It is based on a look-up file that contains pairs of phonetic variations of sub-strings, such as ph ßà f, or rie ßà ry

6)      Categorical value swap corrupter:

a.       “The corruption function can be applied on specific categorical attributes by using a look-up file that contains categorical values and their variations (such as misspellings and nicknames). “
'''

#Spellcheck
#https://github.com/rfk/pyenchant
#https://github.com/koehlma/pygtkspellcheck/blob/master/src/gtkspellcheck/spellcheck.py
#https://pypi.python.org/pypi/pygtkspellcheck/3.0
#http://koehlma.github.io/projects/pygtkspellcheck.html

#SOUNDEX
#https://github.com/l3ib/soundexpy/blob/master/soundexpy.py

#make functions, then make them into a class
class StrCorrupt(str):
    "transformations that corrupt strings"
    def __init__(self, string):
        string.__init__(self)
        

    def emptystr(self):
        "for string value, return empty string"
        return '' 

    def corrupt_char(self):
        "swap last and second to last characters of string"
        liststr = [x for x in self]
        liststr[-1], liststr[-2] = liststr[-2], liststr[-1]
        liststr = "".join(liststr)
        return liststr

    def final_char(self):
        "remove final character"
        return self[:-1]

    def drop_char(self):
	"use pick_position function to choose varation posiiton"
        liststr = [x for x in self]
        randindx = pick_position(self)
        liststr.remove(liststr[randindx])
        liststr = "".join(liststr)
        return liststr

    def pick_position(self):
        "the position is more likely to be in the middle or at the end"    
        "pick the position based on probabilitic model"
        "use the combination of two normal distribution"
        
        # uncomment below line if needed    
        #from random import *
        
        # parameters        
        p = 0.5     # probability of varation happens in the middle or at the end
        l = len(sela)   
        flag = random()
        
        # gauss() will generate a random number from normal distribution    
        # variation is most likely happens in the middle or at the end  
        
        if flag > p: 
            # generate a varation position near the end of the string         
            position = gauss(l,l/15)
            # varation should happen within the string
            if position > l:
                position = 2 * l - position
        
        else:
            # generate a varation position near the middle of the string        
            position = gauss(l/2, l/15)
        
        # return the varation position
        return int(round(position))
