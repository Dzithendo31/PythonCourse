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
def find_avg(nums):
  return round(sum(nums) / len(nums), 2)


#Original Version
classes_avg = {}
for cls_name, students in classes.items(): #unpacking key:val
  class_students_avg = []
  for student in students:
    class_students_avg.append(find_avg(student['grades']))
  #This is the part where you Create the diction of classes_avg
  classes_avg[cls_name] = find_avg(class_students_avg)
print(classes_avg)

#First with List Comprehension
#So this basically works arounf the logic which you wnat to use
#a best logic would be to utilise list and use sum(), max() and len()
classes_avg = {}
for cls_name, students in classes.items():
  classes_avg[cls_name] = find_avg([find_avg(student['grades']) for student in students])
print(classes_avg)

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
#Another Task
students_avg_dict = {}
for cls_name, students in classes.items():
  students_dict = {}
  for student in students:
    students_dict[student['name']] = find_avg(student['grades'])
  students_avg_dict[cls_name] = students_dict
print("Version 0.1",students_avg_dict)

#with changes of the things by myself
student_dict = {}
for cls_name, students in classes.items():
  students_dict[cls_name] = [find_avg(student['grades']) for student in students]
  print(student_dict)
