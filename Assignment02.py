#Hotel

Hotel = [{
  "roomNumber":23,
  "bedType": "single",
  "smoking": False,
  "availability": True
},
{
  "roomNumber":24,
  "bedType": "single",
  "smoking": True,
  "availability": True
},
{
  "roomNumber":25,
  "bedType": "King",
  "smoking": False,
  "availability": True
},

]

#Create a Room for the Hotel
# This Function would be utilised by the hotel management for newly
#approved rooms

def add_room(rooms, roomNumber, bedType,smoking):
  #immediately Availible new Room
  rooms.append({
  "roomNumber":roomNumber,
  "bedType": bedType,
  "smoking": smoking,
  "availability": True
},)
  return f"Room {roomNumber} added and available for use"

def bookRoom(rooms,preferredBedType,smokingPreference):
  for room in rooms:
    if (room['bedType']==preferredBedType and room['smoking'] == smokingPreference):
      #Then we found the room
      #Set it to not Available
      room["availability"] = False
      return f"Room {room['roomNumber']} Booked"
  return "Room unavailable"

def listAvailable(rooms):
  print([room for room in rooms if room["availability"] == True])
def toBoolean(ans):
  if ans == 'Y' or ans == 'y':
    return True
  return False
# print(Hotel)
# #Add a Room
# print(add_room(Hotel,26,'Queen',False))

# #Booking a Room
# print(bookRoom(Hotel,'King',False))
# print(bookRoom(Hotel,'Queen',False))

# #List the Rooms
# listAvailable(Hotel)


#User InterFace
print("Welcome To Hotel South Africa Booking System😁")
userInput = int(input("Choose Num 1.Add Room 2.Book Room 3.Check Availabile: 4.Quit "))
while (userInput != 4):
  if(userInput == 1):
    #get the details
    roomNum = int(input("Enter new room Number: "))
    bedtype = input("Enter new room BedType: ")
    smoking = input("Enter new room Smoking policy Y/N: ")
    print(add_room(Hotel,roomNum,bedtype,toBoolean(smoking)))
  elif(userInput == 2):
    #Book a room
    #get the details
    bedtype = input("Enter preffered room BedType: ")
    smoking = input("Enter preffered room Smoking policy Y/N: ")
    print(bookRoom(Hotel,bedtype,toBoolean(smoking)))
  elif (userInput == 3):
    listAvailable(Hotel)
  userInput = int(input("/nChoose Num 1.Add Room 2.Book Room 3.Check Availabile: 4.Quit "))