birthYear =  int(input("what generation ar you a part of ? "))
if birthYear <= 1925 : 
   print(" the generation is traditionnalist")
elif birthYear >= 1926 and birthYear <= 1946: 
  print("you are tradi")
elif birthYear >= 1947 and birthYear <= 1964:
    print("Hey, Baby Boomer! How you doing?")
elif birthYear >= 1965 and birthYear <= 1981:
    print("Gen X! What's up?")
elif birthYear >= 1982 and birthYear <= 1995:
    print("Millenials! The age of tech!")
elif birthYear >= 1996:
    print("Hey, Gen Z! TikTok much?")
else: 
    print("Try again!")