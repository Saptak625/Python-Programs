#Input
import math
print('This program uses modular arithmetic with the Gregorian Calender to predict the day of the week given the date. In the format, if the date is say January 1st, 2020, write 1/1/2020.')
input_date = input("Enter Date in MM/DD/YYYY format: ")
#Processing Input
string_list = input_date.split("/")
date_list = list(map(int, string_list))
#Logic
month = date_list[0]
date_code = date_list[1]
year = date_list[2]
#Leap Year Check
if (year/4)==round(year/4):
	if (year/100)!=round(year/100):
		leap = 1
	else:
		if (year/400)==round(year/400):
			leap = 1
		else:
			leap = 0
else:
	leap = 0
#Month Code
if month == 1:
	if leap == 1:
		month_code = 5
	else:
		month_code = 6
elif month == 2:
	if leap == 1:
		month_code = 1
	else:
		month_code = 2
elif month == 3:
	month_code = 2
elif month == 4:
	month_code = 5
elif month == 5:
	month_code = 0
elif month == 6:
	month_code = 3
elif month == 7:
	month_code = 5
elif month == 8:
	month_code = 1
elif month == 9:
	month_code = 4
elif month == 10:
	month_code = 6
elif month == 11:
	month_code = 2
elif month == 12:
	month_code = 4
else:
	print('Error: Month is not defined correctly.')	
#Year Code
year_var=year
while 2000<=year_var<=2050:
	if year_var<2000:
		year_var=year_var+28
	else:
		year_var=year_var-28
#Year Code Calculation
start=year_var-2000	
addition=int(math.floor(start/4))
start=start+addition
division=int(math.floor(start/7))
year_code = start - int(division*7)
#Final Modular Aritmetic Calculation
total = year_code+month_code+date_code
modulo = total%7
#Final Output and Processing
if modulo==1:
	str='Monday.'
elif modulo==2:
	str='Tuesday.'
elif modulo==3:
	str='Wednesday.'
elif modulo==4:
	str='Thursday.'
elif modulo==5:
	str='Friday.'
elif modulo==6:
	str='Saturday.'
else:
	str='Sunday.'

#Final Output
print(f'The date {input_date} will fall on a {str}')
