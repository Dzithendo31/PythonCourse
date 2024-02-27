import re

post = "loving the #sunny weather in #California. #travel #Fun"


#get all the hashtagsa
#output = 
# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

# Output
['#sunny', '#California', '#travel', '#fun']

hash = re.findall(r'#\w+', post)
print(hash)