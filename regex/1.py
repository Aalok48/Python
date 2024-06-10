import re

# here | denotes 'or'
pattern =  'dog|cat'
data = 'Dog and cat are two pet animals that I have but i prefer dog over cat.'
match_data = re.finditer(pattern, data)
for i in match_data:
    print(i)

print(re.findall(pattern, data))