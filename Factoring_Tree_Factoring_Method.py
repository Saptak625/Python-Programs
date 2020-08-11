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
#Making prime factorization into all factors
index=-1
first_storage_list=[]
second_storage_list = []
temp_list = []
final_list = []
while list!=[]:
    if index==-1:
        first_storage = list[0]
        second_storage = list[1]
        seed=first_storage[0]
        for x in range(int((first_storage[1])+1)):
            first_storage_list.append(int(seed**x))
        seed=second_storage[0]   
        for x in range(int((second_storage[1])+1)):
            second_storage_list.append(int(seed**x))
        #Multiplication of all terms in list
        for x in first_storage_list:
            for y in second_storage_list:
                multiplication= int(x*y)
                if multiplication not in temp_list:
                    temp_list.append(multiplication)
        del list[0]
        del list[0]
        index=index+1
    elif index>-1:
        temp_list_2 = []
        second_storage = list[0]
        seed=second_storage[0]
        second_storage_list = []
        for x in range(int((second_storage[1])+1)):
            second_storage_list.append(int(seed**x))
        #Multiplication between multiplied list and new list
        for x in temp_list:
            for y in second_storage_list:
                multiplication= int(x*y)
                if multiplication not in temp_list_2:
                    temp_list_2.append(multiplication)
        temp_list=temp_list_2
        del list[0]
final_list=temp_list
final_list.sort()
print("The factors are",final_list)
