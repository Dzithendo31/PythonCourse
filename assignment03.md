## Argument vs Parameter
a parameter is a variable that when a method is defined the parameter is placed(a placeHolder)
- Parameters are also used to define the function signature by specifying the kind of data the function should receive.
 
But an **argument** is placed in the place of a parameter when a the Function is called, this means its an actual vlaue passedto the function or method when invoked.

### example
```python
def add(a, b): # a and b are parameters
return a + b

result = add(3, 5) # 3 and 5 are arguments
```
## Curring and Partials Functions

My research tells me that a Curried function can take multiple arguments, but one at a time, Which will mean taking a function as an argument or returning, thus a High order function.
Currying is the process of transforming a function that takes multiple arguments into a sequence of functions that each take a single argument
```python
def add(x):
    def add_y(y):
        return x + y
    return add_y

# Usage
add_curried = add(5)
print(add_curried(3))  # Output: 8
```

**Now Partial Application** the process of fixing a number of arguments to a function, producing another function of smaller arity (number of arguments).

for example, if we have add(x,y,z), we can change it to fixx the value of x and y, to produce a function add_partial(z), which will add from x and y, which is like the same we did with mul_5.


