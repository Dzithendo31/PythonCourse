
def cool():
    x = 10
    print()

#Scope is the lifetime of the variable
cool()


#Closure is your own scope + lexical Scope.



#Default value is sharing the refferenc to the mmeory so, 
def fun(nums=[]):
    nums.append(10)
    print(nums)

# fun()
# fun()
# fun()
# fun()
# [10]
# [10, 10]
# [10, 10, 10]
# [10, 10, 10, 10]

def fun2(nums):
    nums = []
    nums.append(10)
    print(nums)
nuns = []
# fun2(nuns)
# fun2(nuns)
# fun2(nuns)
# fun2(nuns)

def fun3(nums=[10]):
    if nums == [10]:
        print(nums)
    else:
        nums.append(10)
        print(nums)

fun3()
fun3()
fun3([70])
