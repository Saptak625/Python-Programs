#Input
number= int(input("Enter a whole number to factor. "))

#Factoring Tree
list=[]
b=2
import math
while b<=math.sqrt(number):
    if number/b==round(number/b):
        t=0
        for i in list:
            if i[0]==b:
                t=1
                break
        if t==1:
            index = list.index(i)
            list[index][1]= list[index][1] + 1
        else:
            list.append([b,1])
        number=int(number/b)
        b=2
            
    else:
        b=b+1

#Appending last prime number
t=0
for i in list:
    if i[0]==number:
        t=1
        break
if t==1:
    index = list.index(i)
    list[index][1]= int(list[index][1] + 1)
elif t==0:    
    list.append([number,1])
print(list)

