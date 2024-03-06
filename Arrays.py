marks = [98,75,40,45,80,60]
print(type(marks))

#Version 01
x = len(marks) - 3
print(marks[:x])
#Version 02
print(marks[:-3])

#Remove, it chnages the array
marks.remove(40)
print(marks)

#Adding two List
#Duplicate list with *


#Copy a list
lis = [1000,1500,400]
lisCopy = lis

#Second
lis.append(1000)
print(lisCopy)