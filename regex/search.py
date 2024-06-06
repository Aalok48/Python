# searching function in python

# search()
# match()
# finditer()
# findall()
# split()

# for re :- re.search(pattern, data)
# pattern to search and data to search in 

import re

pattern = 'python'
data = 'PYTHOn is a very powerful language and widely used'
match = re.search(pattern, data, re.IGNORECASE)  # search returns the first pattern found... if you want all the info of the pattern in the data then use findall 

# re.IGNORECASE ignores the lower or uppercase while searching for the pattern

if match:
    print('found', match.group())   # match.group() returns the pattern that is found in the data

else:
    print('not found')