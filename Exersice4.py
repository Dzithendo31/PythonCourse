
avengers = ["Hulk","Iron man","Black widow","Captain america","Spider man","Thor",]

aveNums = []
for i in avengers:
  aveNums.append(len(i))
print(aveNums)

New = []
for i in avengers:
  if (len(i)>10):
    New.append(i)
print(New)