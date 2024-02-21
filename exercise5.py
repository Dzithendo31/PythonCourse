import math
coordinates = [(5, 4), (1, 1) , (6, 10), (9, 10)]

#Distance from the origin
answers = [math.sqrt(x**2 + y**2) for x,y in coordinates]
print(answers)

#Using Unpacking

  