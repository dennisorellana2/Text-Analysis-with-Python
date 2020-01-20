#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Starter Code -
# Based on Toby Donaldson's Python: Visual QuickStart Guide
# function print_file_stats (location 5347)
# with thanks to Elwyn Fleming for the starter code
# Modified for UMUC DATA 620 by Dennis Orellana
# Last updated:  12/11/2019
# Program to open a text file named 'Andrew Johnson.txt'
# This program will give a word count of all the words in the file
# and give the top 30 words.
# It has not been modified to do any stop wording 


# Open the input file
s = open("Andrew Johnson.txt", 'r',encoding="utf-8").read()

# count characters 
num_chars = len(s)

# count lines 
num_lines = s.count('\n')


words = s.split()
d = {}
for w in words:
    if w in d:    
       d[w] += 1
    else:
       d[w] = 1
# Now let's delete some of the stop words
# the word "the" is a junky stop word, so let's remove from dictionary
if "the" in d:
    del d["the"]

# I'm going to delete a few other junky stop words here
if "of" in d:
    del d["of"]
if "to" in d:
    del d["to"]
if "in" in d:
    del d["in"]
if "said" in d:
    del d["said"]
if "and" in d:
    del d["and"]
if "a" in d:
    del d["a"]  
num_words = sum(d[w] for w in d)

lst = [(d[w], w) for w in d]
lst.sort()
lst.reverse()


print('Your input file has characters = ' + str(num_chars))
print('Your input file has num_lines = ' + str(num_lines))
print('Your input file has num_words = ' + str(num_words))

print('\n The 30 most frequent words are \n')

i = 1
for count, word in lst[:30]:
    print('%2s.  %4s %s' % (i, count, word))
    i += 1

# End of script
