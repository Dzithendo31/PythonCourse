#Task  Numbers
#double player stats
Stats = [10,30,60]
StatsPowered = Stats[:]
r = 0
for i in StatsPowered:
  StatsPowered[r] = i*2
  r=r+1
print(StatsPowered)