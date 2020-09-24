userstring = input("Please enter your string(Max: 4000 characters): ")

print("The your string is", len(userstring), "characters long")

if len(userstring) >= 2:
 print(userstring[0:2] + userstring[-2:4000])
else:
  print("Empty String")
 
if len(userstring) < 3:
  print(userstring)
elif userstring[-3:4000] == "ing":
  print(userstring + "ly")
else:
  print(userstring + "ing")