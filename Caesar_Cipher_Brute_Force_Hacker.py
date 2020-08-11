#Input of encrypted message
message=str(input('Enter encrypted message: '))
#Changing Message into Numbers
finished_message=[]
for letter in message:
    finished_message.append(letter)
message_numbers=[]
for letter in finished_message:
    message_num=int(ord(letter)-97)
    if message_num>=0 and message_num<=25:
        message_numbers.append(message_num)
    else:
        message_space=" "
        message_numbers.append(message_space)
#Brute Force
encrypted_list=[]
output_list=[]
k=0
for shiftkey in range(26):
	#Encryption
	encryptednumlist=[]
	for letters in message_numbers:
	    if isinstance(letters, int) == True:
	        encryptednum=((int(letters)+int(shiftkey))%26)+97
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
	encrypted_list.append(encrypted_message)
	n=0
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
	if len(encrypted_message)<=15 and n>=1:
		print(f'The message is {encrypted_message}')
		k=1
	if len(encrypted_message)>15:
		if ((len(encrypted_message))/30)<=n:
			print(f'The message is {encrypted_message}')
			k=1
if k!=1:
	output_list=encrypted_list
	for e in encrypted_list:
		print(' ')
		print(e)
		print(' ')

