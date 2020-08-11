#Playfair Cipher Decryption
#Incorrect Info Warning
print('Any wrong info given to the decrypter will result in the output to be nonsense.')
#Asks for message
message_numbers=[]
message=str(input("Enter your encrypted message: "))
alpha_chr_len=int(0)
message=message.lower()
finished_message=[]
for letter in message:
    finished_message.append(letter)
#Changing message into number form
message_numbers=[]
for letter in finished_message:
    message_num=int(ord(letter)-97)
    if message_num>=0 and message_num<=25:
        message_numbers.append(message_num)
        alpha_chr_len=int(alpha_chr_len+1)
while 9 in message_numbers:
    j_index= message_numbers.index(9)
    message_numbers.insert(j_index,8)
    message_numbers.remove(9)
if (alpha_chr_len%2)==1:
    message_numbers.append(16)
    alpha_chr_len=int(alpha_chr_len+1)
#RSA Key Transfer Starts
print("Enter the rows one by one used in encryption without brackets. Each row always has 5 integer values. For example, 12, 3, 16, 24, 10: ")
#Row 1 Input
# input comma separated elements as string 
inputstring=str(input('Row 1: '))
# convert to the list
list = inputstring.split(",")
# convert each element as integers
row_1 = []
for elements in list:
    row_1.append(int(elements))
#Row 2 Input
# input comma separated elements as string 
inputstring=str(input('Row 2: '))
# convert to the list
list = inputstring.split(",")
# convert each element as integers
row_2 = []
for elements in list:
    row_2.append(int(elements))
#Row 3 Input
# input comma separated elements as string 
inputstring=str(input('Row 3: '))
# convert to the list
list = inputstring.split(",")
# convert each element as integers
row_3 = []
for elements in list:
    row_3.append(int(elements))
#Row 4 Input
# input comma separated elements as string 
inputstring=str(input('Row 4: '))
# convert to the list
list = inputstring.split(",")
# convert each element as integers
row_4 = []
for elements in list:
    row_4.append(int(elements))
#Row 5 Input
# input comma separated elements as string 
inputstring=str(input('Row 5: '))
# convert to the list
list = inputstring.split(",")
# convert each element as integers
row_5 = []
for elements in list:
    row_5.append(int(elements))
#Making colums out of rows
column_1=[row_1[0],row_2[0],row_3[0],row_4[0],row_5[0]]
column_2=[row_1[1],row_2[1],row_3[1],row_4[1],row_5[1]]
column_3=[row_1[2],row_2[2],row_3[2],row_4[2],row_5[2]]
column_4=[row_1[3],row_2[3],row_3[3],row_4[3],row_5[3]]
column_5=[row_1[4],row_2[4],row_3[4],row_4[4],row_5[4]]
#Encrption Rules
variant_1=0
variant_2=1
encrypted_nums=[]
for i in range(alpha_chr_len//2):
    first_num=message_numbers[variant_1]
    second_num=message_numbers[variant_2]
    #Two_Letter Rule
    if first_num==second_num:
        second_num=ord('q')-97
    #Rule 2
    if (first_num in row_1) and (second_num in row_1):
        first_num_index=int(row_1.index(first_num))
        second_num_index=int(row_1.index(second_num))
        encrypted_letter_1=row_1[((first_num_index)-1)%5]
        encrypted_letter_2=row_1[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_2) and (second_num in row_2):
        first_num_index=int(row_2.index(first_num))
        second_num_index=int(row_2.index(second_num))
        encrypted_letter_1=row_2[((first_num_index)-1)%5]
        encrypted_letter_2=row_2[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_3) and (second_num in row_3):
        first_num_index=int(row_3.index(first_num))
        second_num_index=int(row_3.index(second_num))
        encrypted_letter_1=row_3[((first_num_index)-1)%5]
        encrypted_letter_2=row_3[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_4) and (second_num in row_4):
        first_num_index=int(row_4.index(first_num))
        second_num_index=int(row_4.index(second_num))
        encrypted_letter_1=row_4[((first_num_index)-1)%5]
        encrypted_letter_2=row_4[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_5) and (second_num in row_5):
        first_num_index=int(row_5.index(first_num))
        second_num_index=int(row_5.index(second_num))
        encrypted_letter_1=row_5[((first_num_index)-1)%5]
        encrypted_letter_2=row_5[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    #Rule 3
    elif (first_num in column_1) and (second_num in column_1):
        first_num_index=int(column_1.index(first_num))
        second_num_index=int(column_1.index(second_num))
        encrypted_letter_1=column_1[((first_num_index)-1)%5]
        encrypted_letter_2=column_1[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_2) and (second_num in column_2):
        first_num_index=int(column_2.index(first_num))
        second_num_index=int(column_2.index(second_num))
        encrypted_letter_1=column_2[((first_num_index)-1)%5]
        encrypted_letter_2=column_2[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_3) and (second_num in column_3):
        first_num_index=int(column_3.index(first_num))
        second_num_index=int(column_3.index(second_num))
        encrypted_letter_1=column_3[((first_num_index)-1)%5]
        encrypted_letter_2=column_3[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_4) and (second_num in column_4):
        first_num_index=int(column_4.index(first_num))
        second_num_index=int(column_4.index(second_num))
        encrypted_letter_1=column_4[((first_num_index)-1)%5]
        encrypted_letter_2=column_4[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_5) and (second_num in column_5):
        first_num_index=int(column_5.index(first_num))
        second_num_index=int(column_5.index(second_num))
        encrypted_letter_1=column_5[((first_num_index)-1)%5]
        encrypted_letter_2=column_5[((second_num_index)-1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)    
    #Rule 1
    else:
        if first_num in row_1:
            first_num_index=int(row_1.index(first_num))
            if second_num in row_2:
                second_num_index=int(row_2.index(second_num))
                encrypted_letter_1=row_1[second_num_index]
                encrypted_letter_2=row_2[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)   
            elif second_num in row_3:
                second_num_index=int(row_3.index(second_num))
                encrypted_letter_1=row_1[second_num_index]
                encrypted_letter_2=row_3[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_4:
                second_num_index=int(row_4.index(second_num))
                encrypted_letter_1=row_1[second_num_index]
                encrypted_letter_2=row_4[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_5:
                second_num_index=int(row_5.index(second_num))
                encrypted_letter_1=row_1[second_num_index]
                encrypted_letter_2=row_5[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            else:
                print("Error")
        elif first_num in row_2:
            first_num_index=int(row_2.index(first_num))
            if second_num in row_1:
                second_num_index=int(row_2.index(second_num))
                encrypted_letter_1=row_2[second_num_index]
                encrypted_letter_2=row_1[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_3:
                second_num_index=int(row_3.index(second_num))
                encrypted_letter_1=row_2[second_num_index]
                encrypted_letter_2=row_3[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_4:
                second_num_index=int(row_4.index(second_num))
                encrypted_letter_1=row_2[second_num_index]
                encrypted_letter_2=row_4[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_5:
                second_num_index=int(row_5.index(second_num))
                encrypted_letter_1=row_2[second_num_index]
                encrypted_letter_2=row_5[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            else:
                print("Error")
        elif first_num in row_3:
            first_num_index=int(row_3.index(first_num))
            if second_num in row_1:
                second_num_index=int(row_1.index(second_num))
                encrypted_letter_1=row_3[second_num_index]
                encrypted_letter_2=row_1[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_2:
                second_num_index=int(row_2.index(second_num))
                encrypted_letter_1=row_3[second_num_index]
                encrypted_letter_2=row_2[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_4:
                second_num_index=int(row_4.index(second_num))
                encrypted_letter_1=row_3[second_num_index]
                encrypted_letter_2=row_4[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_5:
                second_num_index=int(row_5.index(second_num))
                encrypted_letter_1=row_3[second_num_index]
                encrypted_letter_2=row_5[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            else:
                print("Error")
        elif first_num in row_4:
            first_num_index=int(row_4.index(first_num))
            if second_num in row_1:
                second_num_index=int(row_1.index(second_num))
                encrypted_letter_1=row_4[second_num_index]
                encrypted_letter_2=row_1[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_2:
                second_num_index=int(row_2.index(second_num))
                encrypted_letter_1=row_4[second_num_index]
                encrypted_letter_2=row_2[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_3:
                second_num_index=int(row_3.index(second_num))
                encrypted_letter_1=row_4[second_num_index]
                encrypted_letter_2=row_3[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_5:
                second_num_index=int(row_5.index(second_num))
                encrypted_letter_1=row_4[second_num_index]
                encrypted_letter_2=row_5[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            else:
                print("Error")
        elif first_num in row_5:
            first_num_index=int(row_5.index(first_num))
            if second_num in row_1:
                second_num_index=int(row_1.index(second_num))
                encrypted_letter_1=row_5[second_num_index]
                encrypted_letter_2=row_1[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_2:
                second_num_index=int(row_2.index(second_num))
                encrypted_letter_1=row_5[second_num_index]
                encrypted_letter_2=row_2[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_3:
                second_num_index=int(row_3.index(second_num))
                encrypted_letter_1=row_5[second_num_index]
                encrypted_letter_2=row_3[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            elif second_num in row_4:
                second_num_index=int(row_4.index(second_num))
                encrypted_letter_1=row_5[second_num_index]
                encrypted_letter_2=row_4[first_num_index]
                encrypted_nums.append(encrypted_letter_1)
                encrypted_nums.append(encrypted_letter_2)
            else:
                print("Error")
        else:
            print("Error")
    variant_1=variant_1+2
    variant_2=variant_2+2
#Making encrypted message back to letters
encrypted_message=""
for num in encrypted_nums:
    encrypted_letter=chr((int(num)+97))
    encrypted_message=encrypted_message+encrypted_letter
#Final Display
print('Your decrypted message is: ', encrypted_message)
print('The array used to decrypt the message is: ') 
print('Row 1: ',row_1)
print('Row 2: ',row_2)
print('Row 3: ',row_3)
print('Row 4: ',row_4)
print('Row 5: ',row_5)
