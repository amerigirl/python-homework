#calculating the bill and the tip (rounded)
# asks user for total bill and the percentage of the tip you want
#multiply the two values together to find the tip
#add that value to the original amount
#ask how many people are splitting the bill
#output the answer on the screen

print("Tip Calculator")
print("Alright, let's figure this out!")
totalBill = float(input("What is the total bill? "))
print("We certainly had fun now didn't we, lol?")
tip = int(input("What will our tip be tonight?"))

billPlusTip = totalBill * (tip/100)

finalTotal = totalBill + billPlusTip
print("Ok, here's our total bill", finalTotal)


peopleInParty = int(input("Ok, how many of us are there again?"))

endTotal = finalTotal / peopleInParty
endTotal = (round(endTotal, 2))
print("great, that means we each owe", endTotal, "payup people!")
