#Input
number= int(input("Enter a whole number to factor. "))

#Factoring Start
import math
end = math.sqrt(number)
b=1
list =[]
#Loop start
while b<end:
    if number/b==round(number/b):
        list.append(b)
        b=b+1
    else:
        b=b+1

#Checks square case
if number/end==round(number/end):
    list.append(end)

#Get rest of list
for f in list:
    c=int(number/f)
    if c not in list:
        list.append(c)

#Sorted List
list.sort()
print(list)
