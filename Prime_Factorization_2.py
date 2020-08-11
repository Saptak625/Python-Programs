#Input
number= int(input("Enter a whole number to factor. "))

#Factoring Tree
list=[]
b=2
import math
while b<=math.sqrt(number):
    if number/b==round(number/b):
        n=1
        while (number/(b**n))==round(number/(b**n)):
            n=n+1
        n=n-1
        list.append([b,n])
        number=number/(b**n)
    b=b+1
#If last prime only occurs once
if number!=1:
    list.append([int(number),1])
print(list)

