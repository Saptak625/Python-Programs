#Playfair Cipher Encryption
#RSA Generator
from random import shuffle
alphabet = [i for i in range(26)]
shuffle(alphabet)
alphabet.remove(9)
#Defines rows and columns for encryption algorithm
row_1=[alphabet[0],alphabet[1],alphabet[2],alphabet[3],alphabet[4]]
row_2=[alphabet[5],alphabet[6],alphabet[7],alphabet[8],alphabet[9]]
row_3=[alphabet[10],alphabet[11],alphabet[12],alphabet[13],alphabet[14]]
row_4=[alphabet[15],alphabet[16],alphabet[17],alphabet[18],alphabet[19]]
row_5=[alphabet[20],alphabet[21],alphabet[22],alphabet[23],alphabet[24]]
column_1=[alphabet[0],alphabet[5],alphabet[10],alphabet[15],alphabet[20]]
column_2=[alphabet[1],alphabet[6],alphabet[11],alphabet[16],alphabet[21]]
column_3=[alphabet[2],alphabet[7],alphabet[12],alphabet[17],alphabet[22]]
column_4=[alphabet[3],alphabet[8],alphabet[13],alphabet[18],alphabet[23]]
column_5=[alphabet[4],alphabet[9],alphabet[14],alphabet[19],alphabet[24]]
#Punctuation Warning
print("All punctuation, numbers, or symbols in the message will be transformed to spaces and will not show up after the decrytion process. Any spaces in the program after this filtering will not appear either. Therefore, only letters will appear in the message. This improves the security of the messages sent. The longer your message is the harder it is to break. However, even short messages are strong and hard to brute force as this uses a version of the one-time pad.")
#Asks for message
message_numbers=[]
message=str(input("Enter your message: "))
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
        encrypted_letter_1=row_1[((first_num_index)+1)%5]
        encrypted_letter_2=row_1[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_2) and (second_num in row_2):
        first_num_index=int(row_2.index(first_num))
        second_num_index=int(row_2.index(second_num))
        encrypted_letter_1=row_2[((first_num_index)+1)%5]
        encrypted_letter_2=row_2[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_3) and (second_num in row_3):
        first_num_index=int(row_3.index(first_num))
        second_num_index=int(row_3.index(second_num))
        encrypted_letter_1=row_3[((first_num_index)+1)%5]
        encrypted_letter_2=row_3[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_4) and (second_num in row_4):
        first_num_index=int(row_4.index(first_num))
        second_num_index=int(row_4.index(second_num))
        encrypted_letter_1=row_4[((first_num_index)+1)%5]
        encrypted_letter_2=row_4[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in row_5) and (second_num in row_5):
        first_num_index=int(row_5.index(first_num))
        second_num_index=int(row_5.index(second_num))
        encrypted_letter_1=row_5[((first_num_index)+1)%5]
        encrypted_letter_2=row_5[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    #Rule 3
    elif (first_num in column_1) and (second_num in column_1):
        first_num_index=int(column_1.index(first_num))
        second_num_index=int(column_1.index(second_num))
        encrypted_letter_1=column_1[((first_num_index)+1)%5]
        encrypted_letter_2=column_1[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_2) and (second_num in column_2):
        first_num_index=int(column_2.index(first_num))
        second_num_index=int(column_2.index(second_num))
        encrypted_letter_1=column_2[((first_num_index)+1)%5]
        encrypted_letter_2=column_2[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_3) and (second_num in column_3):
        first_num_index=int(column_3.index(first_num))
        second_num_index=int(column_3.index(second_num))
        encrypted_letter_1=column_3[((first_num_index)+1)%5]
        encrypted_letter_2=column_3[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_4) and (second_num in column_4):
        first_num_index=int(column_4.index(first_num))
        second_num_index=int(column_4.index(second_num))
        encrypted_letter_1=column_4[((first_num_index)+1)%5]
        encrypted_letter_2=column_4[((second_num_index)+1)%5]
        encrypted_nums.append(encrypted_letter_1)
        encrypted_nums.append(encrypted_letter_2)
    elif (first_num in column_5) and (second_num in column_5):
        first_num_index=int(column_5.index(first_num))
        second_num_index=int(column_5.index(second_num))
        encrypted_letter_1=column_5[((first_num_index)+1)%5]
        encrypted_letter_2=column_5[((second_num_index)+1)%5]
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
            if second_num in row_2:
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
print('Your encrypted message is: ', encrypted_message)
print('In order to decrypt the message, you will need the following array written in 5 rows of 5 elements: ') 
print('Row 1: ',row_1)
print('Row 2: ',row_2)
print('Row 3: ',row_3)
print('Row 4: ',row_4)
print('Row 5: ',row_5)
