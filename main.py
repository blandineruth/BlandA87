print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "12345":
 print("Welcome Mark!")
  
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
  
elif username == "ruth" and password == "ayite":
 print("Welcome Ayite ruth!")
else:
 print("Go away!")

print ()

# Correction du code :  l'instruction elif 


print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")

elif username == "suzanne":
  print("Hey there Suzanne!")
  
else:
  print("Go away!")

