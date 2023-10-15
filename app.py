#challenge

pourboire = float(input("what is the pourboire ? "))
print(pourboire)
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = round( pourboire * myBill + myBill)
answer = round(answer/numberOfPeople)
print("You all owe", answer)
