# re.match() is used when a certain pattern is needed to be searched at the beginning of the data
# regular expression objects:- re.compile(pattern, flags)

import re

pattern = re.compile(r'python', re.IGNORECASE)
data = 'hello, pythoN is powerful and widely used'

match = re.match(pattern, data)

if match:
    print('found', match.group())

else:
    print('not found')