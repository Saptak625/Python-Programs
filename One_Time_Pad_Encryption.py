#One Time Pad Encrypter
#Punctuation Warning
print("All punctuation, numbers, or symbols in the message will be transformed to spaces and will not show up after the decrytion process. This improves the security of the messages sent. The longer your message is the harder it is to break. However, even short messages are strong and hard to brute force as this uses a version of the one-time pad.")
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
    else:
        message_space=" "
        message_numbers.append(message_space)
#Alphabet to be used
import random
alphabet_choice=int(random.randint(1,10))
#Alphabet Generator
alphabet1=['z','a','b','y','x','c','d','w','v','e','f','u','t','g','h','s','r','i','j','q','p','k','l','o','n','m']
alphabet2=['z','m','a','n','y','l','b','o','x','k','c','p','w','j','d','q','v','i','e','r','u','h','f','s','t','g']
alphabet3=['g','t','u','h','f','s','v','i','e','r','w','j','d','q','x','k','c','p','y','l','b','o','z','m','a','n']
alphabet4=['a','z','y','b','c','x','w','d','e','v','u','f','g','t','s','h','i','r','q','j','k','p','o','l','m','n']
alphabet5=['a','t','n','g','z','h','m','u','b','s','o','f','y','i','l','v','c','r','p','e','x','j','k','w','d','q']
alphabet6=['f','n','s','a','u','l','h','y','e','o','r','b','v','k','i','x','d','p','q','c','w','j','t','m','g','z']
alphabet7=['v','o','h','a','j','c','f','m','t','k','r','y','u','n','w','p','i','b','g','d','e','l','s','z','q','x']
alphabet8=['d','j','f','l','r','x','w','z','u','o','i','c','g','a','e','k','q','m','s','y','v','p','t','n','h','b']
alphabet9=['j','e','z','u','p','k','f','a','v','q','l','g','b','w','r','m','h','c','x','s','n','i','d','y','t','o']
alphabet10=['h','m','r','w','b','g','l','q','v','a','f','k','p','u','z','e','j','o','t','y','d','i','n','s','x','c']
alphabet1num=[]
alphabet2num=[]
alphabet3num=[]
alphabet4num=[]
alphabet5num=[]
alphabet6num=[]
alphabet7num=[]
alphabet8num=[]
alphabet9num=[]
alphabet10num=[]
for letter in alphabet1:
    num=ord(letter)-97
    alphabet1num.append(num)
for letter in alphabet2:
    num=ord(letter)-97
    alphabet2num.append(num)
for letter in alphabet3:
    num=ord(letter)-97
    alphabet3num.append(num)
for letter in alphabet4:
    num=ord(letter)-97
    alphabet4num.append(num)
for letter in alphabet5:
    num=ord(letter)-97
    alphabet5num.append(num)
for letter in alphabet6:
    num=ord(letter)-97
    alphabet6num.append(num)
for letter in alphabet7:
    num=ord(letter)-97
    alphabet7num.append(num)
for letter in alphabet8:
    num=ord(letter)-97
    alphabet8num.append(num)
for letter in alphabet9:
    num=ord(letter)-97
    alphabet9num.append(num)
for letter in alphabet10:
    num=ord(letter)-97
    alphabet10num.append(num)
#Creates a common variable to perform encryption process faster
if alphabet_choice == 1:
    alphabet_chosen=alphabet1num
elif alphabet_choice == 2:
    alphabet_chosen=alphabet2num
elif alphabet_choice == 3:
    alphabet_chosen=alphabet3num
elif alphabet_choice == 4:
    alphabet_chosen=alphabet4num
elif alphabet_choice == 5:
    alphabet_chosen=alphabet5num
elif alphabet_choice == 6:
    alphabet_chosen=alphabet6num
elif alphabet_choice == 7:
    alphabet_chosen=alphabet7num
elif alphabet_choice == 8:
    alphabet_chosen=alphabet8num
elif alphabet_choice == 9:
    alphabet_chosen=alphabet9num
elif alphabet_choice == 10:
    alphabet_chosen=alphabet10num
else:
    print("ERROR")
#Sets Starting Letter:A and stores value
starting_letter=0
#RNG Generation
keynums=[]
for nums in range(alpha_chr_len):
    import random
    random_int=int(random.randint(0, 25))
    keynums.append(random_int)
keys=keynums
#Encryption Process Starts
encrypted_num_list=[]
variant=0
for letters in message_numbers:
    if isinstance(letters, int) == True:
        start_position=starting_letter
        end_position=letters
        shift_index=int(int(end_position)-int(start_position))
        key_value=keys[variant]
        key_index=alphabet_chosen.index(key_value)
        encrypted_num_index=(int(int(key_index)+shift_index))%26
        encrypted_num=alphabet_chosen[encrypted_num_index]
        encrypted_num_list.append(encrypted_num)
        variant=variant+1
    else:
        encrypted_num_list.append(" ")
#Encryption Process Ends
#Making encrypted message back to letters
encrypted_message=""
for num in encrypted_num_list:
    if isinstance(num, int) == True:
        encrypted_letter=chr((int(num)+97))
        encrypted_message=encrypted_message+encrypted_letter
    else:
        encrypted_message=encrypted_message+str(" ")
#Final Display
print("Your encrypted message is: ", encrypted_message)
print("In order to decrypt your encrypted message, you will need: ")
print(f"Cipher Alphabet: {alphabet_choice}")
print(f"Keylist:{keys}")
print("The keylist used in decryption will be elements of the list without the the brackets.")
print("If you give the program any incorrect info of how to decrypt, the message will be meaningless.")
