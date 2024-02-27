import re

# names array
names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]
# output =
switched = []
for name in names:
  switched.append(re.sub(r'(\w+)\s+(\w+)',r'\2, \1',name))

print(switched)
#Regex Credit Card Numbers


#Rules
#16 digits
#They start with 4

#Regex will allow you 