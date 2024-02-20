message = "      🚨dqqdq🔍📱🔑*****secret_code✌️"
code = "SECRET_CODE✌️"

output = message.strip()
i = output.find("🔑")
if (i == -1):
  print("No, secret key")
else:
  output = output[i + 1:]
  #Clear the * and Brackets
  output = output.strip("*")
  output = output.strip("(")
  output = output.upper()

  if (output == code):
    print("Hacker Boy")
  else:
    print("Sorry")

#Task2 id Key is not present, no
#Task3 Trying add Junk at the end
