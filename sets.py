#Sets its like List, but can only have unqiue values
#its mutable 
# Why would we want to use a set.
# {}

tech_gadgets = {'phone','laptop','watch'}
#print(tech_gadgets)

#Cannot have dupes, it will not allow you to have 
tech_gadgets = {'phone','laptop','watch','watch'}
#print(tech_gadgets)

#adding to a set
#Order is not guranteed, there is no gurantee that it will be at the end
tech_gadgets.add("E-reader")
#print(tech_gadgets)

#adding from a List, Tuple and Dictionary
more_gads = ('drone','sticks')
more_gads2 = {'drone':1,'sticks':54}
tech_gadgets.update(more_gads)
#print(tech_gadgets)

#Delete and Discard
#With .remove you'll get an error 
tech_gadgets.discard('heyy')
tech_gadgets.discard('heyy')

#Create an empty set
x = {} #This is a dictionary
emptySet = set()
emptySet.add("Enter")
#print(emptySet)

#Common Items
tech_gadgets2 = {'TVe','laptop','Swchtc','PS5'}
print(tech_gadgets.intersection(tech_gadgets2))
print(tech_gadgets.union(tech_gadgets2))
#There one that are different at a persopeactive
#So it will give you based on what you
print(tech_gadgets.difference(tech_gadgets2))

#opposite of Intersection is sysmetric_difference
print(tech_gadgets.symmetric_difference(tech_gadgets2))

#Quick Tas