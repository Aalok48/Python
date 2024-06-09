# finditer() in re module

# syntax:- re.finditer(pattern, data, flags = 0)

import re

pattern = re.compile(r'ab')
data = 'abaababaa'
find = re.finditer(pattern, data)
for match in find:
    print(match)
    print(match.group())
    print(match.start())  # match.start() returns the start index of every pattern matched
    print(match.end())