#Simple Caesar Cipher Decryption
message_numbers=[]
print("The shift key has to be the same in order to get a meaningful result.")
shiftkey=int(input("Enter your shift key number(1-26): "))
print("Make sure that your ciphertext is typed exactly as it was found in the encryption process.")
message=str(input("Enter your ciphertext: "))
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
    else:
        message_space=" "
        message_numbers.append(message_space)
#Decryption
encryptednumlist=[]
for letters in message_numbers:
    if isinstance(letters, int) == True:
        encryptednum=(((int(letters))-(int(shiftkey)))%26)+97
        encryptednumlist.append(encryptednum)
    else:
        encryptednumlist.append(message_space)
#Back to Characters
encrypted_message=""
for nums in encryptednumlist:
    if isinstance(nums, int) == True:
        character=chr(int(nums))
        encrypted_message=encrypted_message+character
    else:
        encrypted_message=encrypted_message+" "
print("Your decrypted message:",encrypted_message)

        
