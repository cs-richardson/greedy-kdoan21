#program that calculates the minimum number of coins required to give a
#user change

quarter = 0.25
dime = 0.10
nickel = 0.5
penny = 0.1

quarterTotal = 0
dimeTotal = 0
nickelTotal = 0
pennyTotal = 0

change = float(input("How much change(in dollars) is owed? "))
if change < 0.1:
    print("Error, no such coin value exists.")

quarterTotal = change // quarter
quarterSub = quarterTotal * 0.25
change = change - quarterSub
if change != 0:
    dimeTotal = change // dime
    dimeSub = dimeTotal * 0.10
    change = change - dimeSub
    if change != 0:
        nickelTotal = change // nickel
        nickelSub = nickelTotal * 0.5
        change = change - nickelSub
        if change != 0:
            pennyTotal = change // penny
            pennySub = pennyTotal * 0.1
            change = change - pennySub

coinTotal = quarterTotal + dimeTotal + nickelTotal + pennyTotal

print("The minimum number of coins are", coinTotal)



