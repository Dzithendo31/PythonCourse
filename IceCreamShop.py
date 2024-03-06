# #flavours = {"Vanilla":3,"Lime":2,"Chocolate":3}
# Stock1 = "V"
# Stock2 = "L"
# Stock3 = "C"
# inputX = int(input("Choose Flavour 1.Vannila 2.Lime 3.Choclate"))
# if (inputX == 1 and Stock1 != ""):
#   print("Vannila Availiable")
# elif(inputX == 2 and Stock2 != ""):
#   print("Lime Availiable")
# elif(inputX == 3 and Stock3 != ""):
#   print("Choc Availiable")
# else:
#   print("Stock Not Availiable")

# #Version 02 --- Using the Dry Principle
# Stock = "vannila, Lime, Choc"
# input2 = input("Choose Flavour")
# if (input2 in Stock):
#   print("We have it Bro")
# else:
#   print("We say we don't gott it it Bro")

#Whats a Ternary Operator

#Version 03
Stock = "vannila, Lime, Choc"
input2 = input("Choose Flavour: ")
print("Available") if (input2 in Stock ) else print("Unavailable")
