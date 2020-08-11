#Input
principle = float(input("What is the principle? Please put number value only. "))
interest_rate = float(input("What is the interest rate per year? Please put number value only. "))
total_time = int(input("Over how many months is the term over? "))
money = float(input("About how much do you want to pay per month? $"))
overpaying = float(input("Overpaying payment? "))
overpaying_time = int(input("How often is the payment?"))
debug = int(input('Debug: 1 or Final: 2 '))
#Logic
current_principle=principle
total_interest=0
for x in range(total_time):
    time=x+1
    interest = current_principle*(interest_rate/1200)
    total_interest = total_interest + interest
    money_paid = money-interest
    current_principle=current_principle-money_paid
    if time/overpaying_time == round(time/overpaying_time):
        current_principle=current_principle-overpaying
    if current_principle <= 0:
        print(f"You paid off your priciple in {time} months.")
        print(f"Your overall interest was ${total_interest}.")
        break
    else:
        if debug==1:
            print(f"Month: {time}")
            print(f"Your interest this month is ${interest}. You paid ${money_paid} to your principle. Your principle left is ${current_principle}.")
                
    
    
