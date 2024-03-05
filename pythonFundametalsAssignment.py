# Question 1
# Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93}
]
#Sort
n = 1
sorted_list = sorted(students,key=lambda x:x["grade"],reverse=True)
for student in sorted_list:
    student["rank"] = n
    n+=1
#sorted_list = [student["rank"] = n, for student in sorted_list]   
print(sorted_list)

#Question 2
# Question 2
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]


for emp in employees:
    [emp.update(sal) for sal in salaries if emp['id'] == sal['id'] ]
#Theye are now merged on employee
print(employees)




#Question 3
# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400}
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.
new_products = filter(lambda product:product['category'] == "Electronics" and product['price']<500,products)
print(list(new_products))

# Setup Code
orders = [
    {"order_id": 1, "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}]},
    {"order_id": 2, "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}]}
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.
products = {}
for order in orders:
    for item in order["items"]:
        if item['product'] in products:
            products[item['product']] += item['quantity']
        else:
            products[item['product']] = item['quantity']

print(products)

#Question 5
# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"}
]
# Expected Task: Summarize the total amount spent per category.
summary = {}
for trans in transactions:
    summary[trans['category']] = summary.get(trans['category'],0) + trans['amount']

print(summary)

#Question 6
# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100}
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.
group = {}
for sale in sales:
    group[sale['salesperson']] = group.get(sale['salesperson'],0) + sale['amount']
print(group)

#Question 7
# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.
spells_sorted = sorted(spells,key=lambda x:x[1])
print(spells_sorted)

# Question 8
# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.
ingredientsNew = map(lambda String: String + ": 3 grams",ingredients)
print(list(ingredientsNew))

#Question 9
# Setup Code
books = [{"title": "A History of Magic", "pages": 100}, {"title": "Magical Drafts and Potions", "pages": 150}]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.
booksNew = list(map(lambda booc:booc['title'].upper(),list(filter(lambda book:book['pages']>120,books))))
print(booksNew)

#Question 10



#Question 11
class PotionError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = " is not a valid ingredient for the Love Potion."
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught PotionError: {self.value} -> {self.message}"
    
#Question 12
# Setup Code
library = [{"title": "Unfogging the Future", "author": "Cassandra Vablatsky"}, {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"}]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.
lib = []
lib = [book  for book in library if (book['author'] == "Bathilda Bagshot")]
print(lib)


#Question 13
# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40}
]
# Expected Task: Aggregate points for each house and print the total.

houses = {}

for house in house_points:
    houses[house['house']] = houses.get(house['house'],0) + house['points']

print(houses)