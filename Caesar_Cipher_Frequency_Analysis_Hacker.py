#Input of encrypted message
message=str(input('Enter encrypted message: '))
#Changing Message into Numbers
finished_message=[]
for letter in message:
	finished_message.append(letter)
message_numbers=[]
message_numbers_2=[]
message_char=[]
for letter in finished_message:
	message_num=int(ord(letter)-97)
	if message_num>=0 and message_num<=25:
		message_numbers.append(message_num)
		message_numbers_2.append(message_num)
		if message_num not in message_char:
			message_char.append(message_num)
	else:
		message_space=" "
		message_numbers.append(message_space)
#Finding Most Common Number
frequency_list=[]
for char in message_char:
	frequency= message_numbers_2.count(char)
	frequency_list.append(frequency)
m_occur=[]
maximum=max(frequency_list)
for ind in range(len(frequency_list)):
	term=frequency_list[ind]
	if term==maximum:
		m_occur.append(message_char[ind])
#Check if m_occur is length 3 or greater
current_length=len(m_occur)
while len(m_occur)<int(current_length+3):
	maximum=maximum-1
	for ind in range(len(frequency_list)):
		term=frequency_list[ind]
		if term==maximum:
			m_occur.append(message_char[ind])
#print(m_occur,message_char,frequency_list)
#Shift Key Checks
print('Your hacked messages:')
encrypted_list=[]
n=0
for choice in m_occur:
        encryptednumlist=[]
        encrypted_message=""
        stat_1=(message_numbers_2.count(choice))
        stat_2=(len(message_numbers_2))
        shiftkey=choice-int((ord('e'))-97)
        for letters in message_numbers:
                if isinstance(letters,int)==True:
                        encrypted_num=(((int(letters))-(int(shiftkey)))%26)+97
                        encryptednumlist.append(encrypted_num)
                else:
                        encryptednumlist.append(message_space)
        #Back to Characters
        for nums in encryptednumlist:
                if isinstance(nums,int)==True:
                        character=chr(int(nums))
                        encrypted_message=encrypted_message+character
                else:
                        encrypted_message=encrypted_message+' '
        encrypted_list.append(encrypted_message)
        if (stat_1/stat_2)>=float(0.125):
                n=1
                print('')
                print(encrypted_message)
                print('')

if n==0:
        k=0
        for m in encrypted_list:
                if "you" in encrypted_message:
                        n=n+1
                if "is" in encrypted_message:
                        n=n+1
                if "in" in encrypted_message:
                        n=n+1
                if "at" in encrypted_message:
                        n=n+1
                if "he" in encrypted_message:
                        n=n+1
                if "me" in encrypted_message:
                        n=n+1
                if "will" in encrypted_message:
                        n=n+1
                if "go" in encrypted_message:
                        n=n+1
                if "and" in encrypted_message:
                        n=n+1
                if "so" in encrypted_message:
                        n=n+1
                if "as" in encrypted_message:
                        n=n+1
                if "an" in encrypted_message:
                        n=n+1
                if "no" in encrypted_message:
                        n=n+1
                if "yes" in encrypted_message:
                        n=n+1
                if "us" in encrypted_message:
                        n=n+1
                if "am" in encrypted_message:
                        n=n+1
                if "the" in encrypted_message:
                        n=n+1
                if "of" in encrypted_message:
                        n=n+1
                if "that" in encrypted_message:
                        n=n+1
                if "of" in encrypted_message:
                        n=n+1
                if "are" in encrypted_message:
                        n=n+1
                if "red" in encrypted_message:
                        n=n+1
                if "blue" in encrypted_message:
                        n=n+1
                if "with" in encrypted_message:
                        n=n+1
                if "with" in encrypted_message:
                        n=n+1
                if "even" in encrypted_message:
                        n=n+1
                if "but" in encrypted_message:
                        n=n+1
                if "up" in encrypted_message:
                        n=n+1
                if "each" in encrypted_message:
                        n=n+1
                if "down" in encrypted_message:
                        n=n+1
                if "get" in encrypted_message:
                        n=n+1
                if "meet" in encrypted_message:
                        n=n+1
                if "which" in encrypted_message:
                        n=n+1
                if "who" in encrypted_message:
                        n=n+1
                if "where" in encrypted_message:
                        n=n+1
                if len(m)<=20 and n>=1:
                        print('')
                        print(m)
                        print('')
                        k=1
                if len(encrypted_message)>20:
                        if ((len(encrypted_message))/40)<=n:
                                print('')
                                print(m)
                                print('')
                                k=1
        if k!=1:
                for m in encrypted_list:
                        print('')
                        print(m)
                        print('')
