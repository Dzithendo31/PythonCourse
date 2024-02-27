import re

# names array
names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]
# output =
twist = []
for name in names:
  twist.append(re.sub(r'(\w+)\s+(\w+)',r'\2, \1',name))

print(twist)
#Regex Credit Card Numbers


#Rules
#16 digits
#They start with 4

#Regex will allow you 