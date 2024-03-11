import json
from pprint import pprint

sport = {
    "name":"Hope",
    "dbl": lambda x:x*2
}



#First class citizen 

# This will give us an error becuase its not a 
#Can't convert the dictionary because it contains a function
#sportsJSON = json.dumps(sport)

student = {
    "name": "John",
    "age": 25,
    "city": "Exampletown",
    "is_student": False
}
print(type(student),student)
#chnage to JSOn
student_json = json.dumps(student)
print(type(student_json),student_json)


#To change back to a pyhton
newDictionary = json.loads(student_json)
print(newDictionary['name'])


#Exercise
print()
bank_data = '''
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
'''

bank_data_dict = json.loads(bank_data)
# for client in bank_data_dict:
#     if client['isActive']:
#         client['balance'] *= 1.1
bank_data_dict = [{**client,"balance":client['balance']*1.1 if client['isActive'] else client} 
                  for client in bank_data_dict]
#Ban to JSon
bank_data = json.dumps(bank_data_dict,indent=4)
print(bank_data)

#https://www.youtube.com/watch?v=CZ3wIuvmHeM&ab_channel=InfoQ

#Read and write toa JSON
with open("day15bank.json","w") as file:
    json.dump(bank_data,file,indent=4)