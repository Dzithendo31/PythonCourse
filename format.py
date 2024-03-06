from math import pi as P
from datetime import datetime

salary = 400_500_000_000
print(f"My pay is R{salary:,}")


#Decimal Points
print(f"pi value is {P:.4f}")
#Binary and Hexidecimals are there

#Format your Text also maybe some pading
name = 'Lilitha'
print(f":{name:<10}:")
#Cnetre
print(f":{name:^20}:")

print(f":{name:#<10}:")
#Cnetre
print(f":{name:#^20}:")

#% centage
dzin = 0.925
print(f"The test are test {dzin:.2%}")


now = datetime.now()
print(now)

#Nice formating
print(f"Current Date is {now:%d/%m/%y}")