numbers = [8,5,7,4,6,2]


future = []
for i in numbers:
  if (i%2 == 0): #Even
    future.append("Even")
  else:
    future.append("Odd")

print(future)
#You using the List comprehensiv
future = ["Even" if (i%2 == 0) else "Odd" for i in numbers  ]
print(future)
