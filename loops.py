i = 0
R = int(input("Enter Number of Rows: "))
while i < R+1:
  print("❤️"*i)
  i = 1 +i

for i in range(0,R+1):
  print("❤️"*i)

#Task  Numbers
#double player stats
Stats = [10,30,60]
StatsPowered = Stats[:]
r = 0
for i in StatsPowered:
  StatsPowered[r] = i*2
  r=r+1
print(StatsPowered)