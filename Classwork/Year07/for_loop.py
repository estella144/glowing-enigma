pocketMoney = 0.50
totalMoney = 0.00

for week in range(20): 
    print("It is week " + str(week)) 
    print("You will get £ " + str(pocketMoney))
    totalMoney += pocketMoney
    pocketMoney = pocketMoney * 2

print(totalMoney)
