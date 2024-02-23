#They are one line functions
add = lambda a, b: a + b
print(add(6, 7))

#NAmeless function
#Implicitly return(automaticlally
#Treated as first class citizen.

#Using Map
#take a list(no set) and a function maybe lambda
#returned as a Map object, which will need to be changed in List with a method
#Can it be a 2D List with a lambda of two paramenters


def square(x):
  return x * x


super = map(square, [10, 20, 30])
super2 = map(lambda x: x * x, [10, 20, 24])

print(list(super))


def map_own(fr, arr):
  c = 0
  for i in arr:
    arr[c] = fr(i)
    c = c+1
  return arr


print(map_own(lambda x: x * 2, [10, 30, 60]))


def sayHello1():
  def msg():
    return 'Hello, 🎊'
  return msg

print(sayHello1()())

#Factory function
mul = lambda x: lambda y: x * y
#Example for 5
mul_5 = mul(5)
mul_5 = mul(10)
#Functional Programming


print(mul(3)(6))