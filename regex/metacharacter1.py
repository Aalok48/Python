import re

pattern = r'\d'
data = 'The price of this item is 100'
match_pattern = re.finditer(pattern, data)
for match in match_pattern:
    print(match)

print(re.findall(pattern, data))