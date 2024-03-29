#Das Code Encrypter
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
#Ask what alphabet to be used
alphabet_choice=int(input("Please enter an integer from 1-10 to choose as your cipher alphabet:"))
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
starting_letter_choice=str(input("Please enter a starting letter:"))
starting_letter_choice=starting_letter_choice.lower()
starting_letter=ord(starting_letter_choice)-97
#Asks how to generate keys
print("How would you like to generate the keyword? Using the KEA or the RNG? For the RNG, the values are randomly assigned and an ordered list is used to display the keys used. ")
keyword_gen=str(input("KEA or RNG?:"))
keyword_gen=keyword_gen.upper()
if keyword_gen == "KEA":
    #Asks keyword and converts it into all lowercase
    mystr=str(input("Enter Keyword:"))
    mystr=mystr.lower()
    #Makes the keyword into ASCII
    mykeylist=[]
    mykeylist1=[]
    for i in mystr:
        numKey=ord(i)-97
        mykeylist.append(numKey)
        mykeylist1.append(numKey)
    #Keyword Elongation Algorithm start
    #SEQUENCE 1 Starts
    # +1 
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+1)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -1
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-1)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +2
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+2)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -2
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-2)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +3
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+3)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -3
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-3)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +4
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+4)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -4
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-4)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +5
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+5)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -5
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-5)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +7
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+7)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -7
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-7)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +9
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+9)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -9
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-9)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +11
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+11)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -11
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-11)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +13
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+13)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -13
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-13)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +17
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+17)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -17
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-17)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +19
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+19)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -19
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-19)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +23
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+23)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -23
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-23)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +25
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+25)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -25
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-25)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 1 Ends

    #SEQUENCE 2 Starts
    # +2
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+2)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -2
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-2)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +4
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+4)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -4
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-4)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 2 End

    #SEQUENCE 3 Start
    # +3
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+3)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -3
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-3)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +9
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+9)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -9
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-9)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 3 End

    #SEQUENCE 4 Start
    # +4
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+4)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -4
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-4)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 4 End

    #SEQUENCE 5 Start
    # +5
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+5)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -5
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-5)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +25
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+25)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -25
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-25)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 5 End

    #SEQUENCE 6 Start
    # +6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -6
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-6)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 6 End

    #SEQUENCE 7 Start
    # +7
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+7)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -7
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-7)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 7 End

    #SEQUENCE 8 Start
    # +8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -8
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-8)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 8 End

    #SEQUENCE 9 Start
    # +9
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+9)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -9
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-9)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 9 End

    #SEQUENCE 10 Start
    # +10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -10
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-10)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 10 End

    #SEQUENCE 11 Start
    # +11
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+11)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -11
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-11)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 11 End

    #SEQUENCE 12 Start
    # +12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -12
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-12)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 12 End

    #SEQUENCE 13 Start
    # +13
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+13)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -13
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-13)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # +26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 13 End

    #SEQUENCE 14 Start
    # +14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -14
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-14)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 14 End

    #SEQUENCE 15 Start
    # +15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -15
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-15)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 15 End

    #SEQUENCE 16 Start
    # +16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -16
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-16)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 16 End

    #SEQUENCE 17 Start
    # +17
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+17)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -17
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-17)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 17 End

    #SEQUENCE 18 Start
    # +18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -18
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-18)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 18 End

    #SEQUENCE 19 Start
    # +19
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+19)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -19
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-19)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 19 End

    #SEQUENCE 20 Start
    # +20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x+20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -20
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-20)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 20 End

    #SEQUENCE 21 Start
    # +21
    changedkeylist=mykeylist1
    for i,x in enumerate(changedkeylist):
        newvalue=(x+21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-21)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 21 End

    #SEQUENCE 22 Start
    # +22
    changedkeylist=mykeylist1
    for i,x in enumerate(changedkeylist):
        newvalue=(x+22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -22
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-22)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 22 End

    #SEQUENCE 23 Start
    # +23
    changedkeylist=mykeylist1
    for i,x in enumerate(changedkeylist):
        newvalue=(x+23)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -23
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-23)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 23 End

    #SEQUENCE 24 Start
    # +24
    changedkeylist=mykeylist1
    for i,x in enumerate(changedkeylist):
        newvalue=(x+24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -24
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-24)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 24 End

    #SEQUENCE 25 Start
    # +25
    changedkeylist=mykeylist1
    for i,x in enumerate(changedkeylist):
        newvalue=(x+25)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -21
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-25)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 25 End

    #SEQUENCE 26 Start
    # +26
    changedkeylist=mykeylist1
    for i,x in enumerate(changedkeylist):
        newvalue=(x+26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    # -26
    changedkeylist=mykeylist1
    for i, x in enumerate(changedkeylist):
        newvalue=(x-26)%26
        changedkeylist[i]=newvalue
    mykeylist=mykeylist+changedkeylist
    #SEQUENCE 26 End
    #Keyword Elongation Algorithm end
    length_limit=len(mykeylist)
    keys=mykeylist
else:
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
if keyword_gen == "KEA":
    print("Your encrypted message is: ", encrypted_message)
    print("In order to decrypt your encrypted message, you will need: ")
    print(f"Cipher Alphabet: {alphabet_choice}")
    print(f"Starting Letter: {starting_letter_choice}")
    print(f"Keyword Generation: {keyword_gen}")
    print(f"Keyword:{mystr}")
    print("If you give the program any incorrect info of how to decrypt, the message will be meaningless.")
else:
    print("Your encrypted message is: ", encrypted_message)
    print("In order to decrypt your encrypted message, you will need: ")
    print(f"Cipher Alphabet: {alphabet_choice}")
    print(f"Starting Letter: {starting_letter_choice}")
    print(f"Keyword Generation: {keyword_gen}")
    print(f"Keylist:{keys}")
    print("The keylist used in decryption will be elements of the list without the the brackets.")
    print("If you give the program any incorrect info of how to decrypt, the message will be meaningless.")
    
