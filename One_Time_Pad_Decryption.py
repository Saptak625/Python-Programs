#Das Code Decrypter
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
    else:
        message_space=" "
        message_numbers.append(message_space)
#Ask what alphabet to be used
alphabet_choice=int(input("Please enter the cipher alphabet (a number from 1-10) used to encrypt the message:"))
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
#Asks for Starting Letter and stores value
starting_letter=ord('a')-97
#RNG Key Transfer Starts
# input comma separated elements as string 
inputstring = str (input("Enter keylist used in encryption without brackets. For example, 12, 3, 16, 24, 10: "))
# convert to the list
list = inputstring.split(",")
# convert each element as integers
keys = []
for elements in list:
        keys.append(int(elements))
#RNG Key Transfer Ends
#Decryption Process Starts
decrypted_num_list=[]
variant=0
for letters in message_numbers:
    if isinstance(letters, int) == True:
        start_position=alphabet_chosen.index(keys[variant])
        end_position=int(alphabet_chosen.index(letters))
        shift_index=int(int(end_position)-int(start_position))
        decrypted_num_index=int(int(starting_letter)+int(shift_index))%26
        decrypted_num=decrypted_num_index
        decrypted_num_list.append(decrypted_num)
        variant=variant+1
    else:
        decrypted_num_list.append(" ")
#Decryption Process Ends
#Making decrypted message back to letters
decrypted_message=""
for num in decrypted_num_list:
    if isinstance(num, int) == True:
        decrypted_letter=chr((int(num)+97))
        decrypted_message=decrypted_message+decrypted_letter
    else:
        decrypted_message=decrypted_message+str(" ")
#Final Display
print("Your decrypted message is: ", decrypted_message)
print("Information given to program to decrypt:")
print(f"Cipher Alphabet: {alphabet_choice}")
print(f"Keylist:{keys}")

