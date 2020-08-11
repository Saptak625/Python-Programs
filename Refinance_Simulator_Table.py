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
#Defining Lists
loan_number_list = []
loan_time_list = []
a_interest_rate_list = []
principle_limit_list = []
current_principle_list = []
mtime_list = []
interest_list = []
money_list = []
total_interest_list = []
money_paid_list = []
l_total_interest_list = []
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
    if u == (len(time_list) - 1):
        principle_limit = 0
        ainterest_rate = ainterest_rate_list[(index-1)]
        time = time_list[(index-1)]
    else:
        ainterest_rate = ainterest_rate_list[index]
        time = time_list[index]
        minterest_rate = ainterest_rate/1200
        principle_limit = round(float(money * (((1+minterest_rate)**time) -1)) / float(minterest_rate * ((1+minterest_rate)**time)),2)
        ainterest_rate = ainterest_rate_list[(index -1)]
        time = time_list[(index -1)]
    #0th month of the loans
    mtime_list.append(0)
    a_interest_rate_list.append(0)
    current_principle_list.append(current_principle)
    money_list.append(0)
    interest_list.append(0)
    total_interest_list.append(0)
    loan_number_list.append(loan_number)
    loan_time_list.append(time)
    money_paid_list.append(0)
    principle_limit_list.append(principle_limit)
    l_total_interest_list.append(0)
    o_loan_number=loan_number
    for x in range(time):
        mtime=x+1
        interest = round(current_principle*(ainterest_rate/1200),2)
        total_interest = round(total_interest + interest, 2)
        money_paid = round(money-interest)
        current_principle= round(current_principle-money_paid)
        #Loan Interest Calculation
        if loan_number == 1:
            total_interest_1 = total_interest
            l_total_interest_list.append(round(total_interest,2))
        elif o_loan_number!=loan_number:
            total_interest_1 = total_interest
            ltotal_interest_list.append(0)
        else:
            ltotal_interest = round(total_interest - total_interest_1,2)
            l_total_interest_list.append(ltotal_interest)
        if current_principle <= principle_limit:
            if u == (len(time_list) - 1):
                mtime_list.append(mtime)
                a_interest_rate_list.append(ainterest_rate)
                current_principle_list.append(0)
                money_list.append(money)
                interest_list.append(interest)
                total_interest_list.append(total_interest)
                loan_number_list.append(loan_number)
                loan_time_list.append(time)
                money_paid_list.append(money_paid)
                principle_limit_list.append(principle_limit)
            else:
                mtime_list.append(mtime)
                a_interest_rate_list.append(ainterest_rate)
                current_principle_list.append(current_principle)
                money_list.append(money)
                interest_list.append(interest)
                total_interest_list.append(total_interest)
                loan_number_list.append(loan_number)
                loan_time_list.append(time)
                money_paid_list.append(money_paid)
                principle_limit_list.append(principle_limit)
            break
        else:
            mtime_list.append(mtime)
            a_interest_rate_list.append(ainterest_rate)
            current_principle_list.append(current_principle)
            money_list.append(money)
            interest_list.append(interest)
            total_interest_list.append(total_interest)
            loan_number_list.append(loan_number)
            loan_time_list.append(time)
            money_paid_list.append(money_paid)
            principle_limit_list.append(principle_limit)
    index = index + 1

print (current_principle_list, current_principle_list[144])
