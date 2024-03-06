#a way to pack your logic together
#abtraction, you don't need to know how it works in order to use it
def sum(a,b):
  #Body of the Function
  return a + b
print(sum(2,3))

#Default Vlaues in Functions.
def driving_test(age,car="Truck"):
  if age >= 18:
    return f"You can drive {car}"
  else:
    return f"Try Later for {car}"

print(driving_test(14))
print(driving_test(14, "Benz"))