# findall returns a list of all the pattern found in the data without returning the info that are returned by finditer
# finditer returns an object while findall returns a list

import re

pattern = 'ab'
data = 'abaabbab'

print(re.findall(pattern, data))

