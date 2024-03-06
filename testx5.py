# Setup Code
#Question 17
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures
#Filter the phonenix in the isht and 
def Filter(adopter,creature):
    if adopter[1] == creature[1]:
        return
#Question 18
# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
potions = ["Enigmatic", "Mystic", "Celestial"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.
count = 1
for i in ingredients:
    for j in ingredients:
        print(f"Combining {i} and {j} produces a {potions[count]} Potion.")
        count+=1

#Question 19
# Setup Code
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]}
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.

for d in data:
    if "tag1" in d['tags']:
        d['tags'].append("tag4")
print(data)

#Question 20
# Setup Code
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False}
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").
tasksSorted = sorted(tasks, key=lambda x: (x["completed"], {"High": 1, "Medium": 2, "Low": 3}[x["priority"]]))
print(tasksSorted)