person1 = input("Enter yout Name: ")
h1 = int(input("Provide Height in cm: "))
#Person 02
person2 = input("Enter your Name: ")
h2 = int(input("Provide Height in cm: "))

#if (h1>h2):
#  print(f"{person1} is taller than {person2}")
#else:
#  print(f"{person2} is taller than {person1}")
if (h1>h2):
  print(f"{person1} is taller than {person2}")
elif (h1 == h2):
  print(f"{person1} and {person2} are same same")
else:
  print(f"{person2} is taller than {person1}")