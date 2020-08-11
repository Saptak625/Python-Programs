#Input
principle = float(input("What is the principle? Please put number value only. "))
interest_rate = float(input("What is the interest per year? Please put number value only. "))
total_time = int(input("Over how many months is the term over? "))
#Logic
lower_limit = int(principle/total_time)
current_principle=principle
#Upper limit calculation
upper_limit_money = float(principle + (principle * (((interest_rate/100)*total_time)/12)))
import math
upper_limit = math.ceil(upper_limit_money/total_time)
money = lower_limit + 1
#Run-through for integer
while money <= upper_limit:
    for x in range(total_time):
        interest = current_principle*(interest_rate/1200)
        money_paid = money-interest
        current_principle=current_principle-money_paid
    if current_principle <= 0:
        break
    else:
        money = money + 1
        current_principle=principle
#Run-through for first digit
current_principle=principle
money = money - 1
while 1>0:
    for x in range(total_time):
        interest = current_principle*(interest_rate/1200)
        money_paid = money-interest
        current_principle=current_principle-money_paid
    if current_principle <= 0:
        break
    else:
        money = money + 0.1
        current_principle=principle
#Run-through for second digit
current_principle=principle
money = money - 0.1
while 1>0:
    for x in range(total_time):
        interest = current_principle*(interest_rate/1200)
        money_paid = money-interest
        current_principle=current_principle-money_paid
    if current_principle <= 0:
        break
    else:
        money = money + 0.01
        current_principle=principle
money = round(money, 2)
print(f"You must pay ${money} per month.")        
    
