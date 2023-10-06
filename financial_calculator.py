import math
print("Display Text")

amount = float(input("Amount of money deposited: "))
rate = float(input("Interest rate as percentage: "))
time = int(input("The number of years invested: "))
# nr = int(input("Number of months repayment: "))
interestType = int(input("Please enter type C:0 or S:1: "))

if interestType == 0:
    # ans = amount * (1 + rate/100) * math.pow(time)
    ans = amount* (math.pow(1 + rate/100, time))
    print(ans)
elif interestType == 1:
    ans = amount * (1 + (rate/100) *time) 
    print(ans)




