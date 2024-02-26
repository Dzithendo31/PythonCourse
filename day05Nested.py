classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}
def getStudentAvg(Student):
  grades = Student["grades"]
  return sum(grades)/len(grades)

def average(Classes):
  output = {}
  for Class in Classes:
    sum = 0
    for student in Classes[Class]:
      sum = sum + getStudentAvg(student)
    ClassAve = sum/len(Classes[Class])
    ClassAve = f"{ClassAve:.2f}"
    output[Class] = ClassAve
  print(output)

def avgClass():
  
#Or you create a new Object


average(classes)


#Task 02
# Task 2
# Student name's unique
output = {
    "Class A": {
        "Alice": 90.5,
        "Bob": 84.5,
        "Charlie": 90
    },
    "Class B": {
        "Dave": 92.5,
        "Eve": 86.5,
        "Frank": 95
    }
}

def task02(classes):
  output = {}
  for className,students in classes.items():
    output[className] = {}
    for student in students:
      output[className][student["name"]] = f"{getStudentAvg(student):.2f}"
  print(output)

task02(classes)

#Task 04
def 
