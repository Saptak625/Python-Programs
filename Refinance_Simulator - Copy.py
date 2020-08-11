#Input
principle = float(input("What is the principle? Please put number value only. "))
money = float(input("About how much do you want to pay per month? $"))
time = str(input("What combination of loans do you want to use? Enter time in months seperated by commas."))
interest_rate = str(input("What combination of interest_rates of the corresponding loans do you want to use? Enter the annual interest_rate seperated by commas. Numbers only please."))
#Logic
current_principle=principle
loan_number = 0
index = 1
total_interest = 0
#RNG Key Transfer Starts
# convert to the list
list = time.split(",")
# convert each element as integers
time_list = []
for elements in list:
    time_list.append(int(elements))
# convert to the list
list_1 = interest_rate.split(",")
# convert each element as integers
ainterest_rate_list = []
for elements in list_1:
    ainterest_rate_list.append(float(elements))
#RNG Key Transfer Ends 
for u in range((len(time_list))):
    loan_number = loan_number + 1
    ainterest_rate = ainterest_rate_list[(index -1)]
    time = time_list[(index -1)]
    print(f"Loan Number: {loan_number}")
    print(f"Principle Left: ${current_principle}")
    print(f"Annual Interest Rate: {ainterest_rate}%")
    print(f"Loan Term in Months: {time}") 
    if u == (len(time_list) - 1):
        principle_limit = 0
        ainterest_rate = ainterest_rate_list[(index -1)]
        time = time_list[(index -1)]
    else:
        ainterest_rate = ainterest_rate_list[index]
        time = time_list[index]
        minterest_rate = ainterest_rate/1200
        principle_limit = float(money * (((1+minterest_rate)**time) -1)) / float(minterest_rate * ((1+minterest_rate)**time))
    for x in range(time):
        mtime=x+1
        interest = current_principle*(ainterest_rate/1200)
        total_interest = total_interest + interest
        money_paid = money-interest
        current_principle=current_principle-money_paid
        if current_principle <= principle_limit:
            if u == (len(time_list) - 1):
                print(f"Month: {mtime}")
                print(f"You paid off your loan.")
                print(f"Your overall interest is ${total_interest}.")
            else:
                print(f"Month: {mtime}")
                print(f"You reached your principle limit of ${principle_limit}.")
                print(f"Your overall interest so far is ${total_interest}.")
            if loan_number == 1:
                print(f"Your overall interest for this loan is ${total_interest}.")
                total_interest_1 = total_interest
            else:
                ltotal_interest = total_interest - total_interest_1
                print(f"Your overall interest for this loan is ${ltotal_interest}.")
            break
        else:
            print(f"Month: {mtime}")
            print(f"Your interest this month is ${interest}. You paid ${money_paid} to your principle. Your principle left is ${current_principle}.")
    index = index + 1
            
    
    

