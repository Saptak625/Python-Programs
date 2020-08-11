principle = float(input("What is your priciple? "))
ainterest_rate = float(input("What is the annual interest rate? "))
total_time = int(input("Over how many months is the term over? "))
#Calculation
minterest_rate = ainterest_rate/1200
money = float((principle * ((1 + minterest_rate)**total_time) * minterest_rate))/ float((((1 + minterest_rate)**(total_time) - 1)))
money = round(money, 2)
print(f"You will need to pay ${money}.")
