#Visionere Cipher Decrypter
#Keyword lists
keyword_a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keyword_b=['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
keyword_c=['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
keyword_d=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
keyword_e=['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d']
keyword_f=['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e']
keyword_g=['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f']
keyword_h=['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g']
keyword_i=['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h']
keyword_j=['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i']
keyword_k=['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j']
keyword_l=['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k']
keyword_m=['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l']
keyword_n=['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
keyword_o=['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
keyword_p=['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
keyword_q=['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
keyword_r=['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
keyword_s=['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
keyword_t=['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
keyword_u=['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
keyword_v=['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
keyword_w=['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
keyword_x=['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
keyword_y=['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']
keyword_z=['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
keyword_a_num=[]
keyword_b_num=[]
keyword_c_num=[]
keyword_d_num=[]
keyword_e_num=[]
keyword_f_num=[]
keyword_g_num=[]
keyword_h_num=[]
keyword_i_num=[]
keyword_j_num=[]
keyword_k_num=[]
keyword_l_num=[]
keyword_m_num=[]
keyword_n_num=[]
keyword_o_num=[]
keyword_p_num=[]
keyword_q_num=[]
keyword_r_num=[]
keyword_s_num=[]
keyword_t_num=[]
keyword_u_num=[]
keyword_v_num=[]
keyword_w_num=[]
keyword_x_num=[]
keyword_y_num=[]
keyword_z_num=[]
for letter in keyword_a:
    keyword_num=int(ord(letter))-97
    keyword_a_num.append(keyword_num)
for letter in keyword_b:
    keyword_num=int(ord(letter))-97
    keyword_b_num.append(keyword_num)
for letter in keyword_c:
    keyword_num=int(ord(letter))-97
    keyword_c_num.append(keyword_num)
for letter in keyword_d:
    keyword_num=int(ord(letter))-97
    keyword_d_num.append(keyword_num)
for letter in keyword_e:
    keyword_num=int(ord(letter))-97
    keyword_e_num.append(keyword_num)
for letter in keyword_f:
    keyword_num=int(ord(letter))-97
    keyword_f_num.append(keyword_num)
for letter in keyword_g:
    keyword_num=int(ord(letter))-97
    keyword_g_num.append(keyword_num)
for letter in keyword_h:
    keyword_num=int(ord(letter))-97
    keyword_h_num.append(keyword_num)
for letter in keyword_i:
    keyword_num=int(ord(letter))-97
    keyword_i_num.append(keyword_num)
for letter in keyword_j:
    keyword_num=int(ord(letter))-97
    keyword_j_num.append(keyword_num)
for letter in keyword_k:
    keyword_num=int(ord(letter))-97
    keyword_k_num.append(keyword_num)
for letter in keyword_l:
    keyword_num=int(ord(letter))-97
    keyword_l_num.append(keyword_num)
for letter in keyword_m:
    keyword_num=int(ord(letter))-97
    keyword_m_num.append(keyword_num)
for letter in keyword_n:
    keyword_num=int(ord(letter))-97
    keyword_n_num.append(keyword_num)
for letter in keyword_o:
    keyword_num=int(ord(letter))-97
    keyword_o_num.append(keyword_num)
for letter in keyword_p:
    keyword_num=int(ord(letter))-97
    keyword_p_num.append(keyword_num)
for letter in keyword_q:
    keyword_num=int(ord(letter))-97
    keyword_q_num.append(keyword_num)
for letter in keyword_r:
    keyword_num=int(ord(letter))-97
    keyword_r_num.append(keyword_num)
for letter in keyword_s:
    keyword_num=int(ord(letter))-97
    keyword_s_num.append(keyword_num)
for letter in keyword_t:
    keyword_num=int(ord(letter))-97
    keyword_t_num.append(keyword_num)
for letter in keyword_u:
    keyword_num=int(ord(letter))-97
    keyword_u_num.append(keyword_num)
for letter in keyword_v:
    keyword_num=int(ord(letter))-97
    keyword_v_num.append(keyword_num)
for letter in keyword_w:
    keyword_num=int(ord(letter))-97
    keyword_w_num.append(keyword_num)
for letter in keyword_x:
    keyword_num=int(ord(letter))-97
    keyword_x_num.append(keyword_num)
for letter in keyword_y:
    keyword_num=int(ord(letter))-97
    keyword_y_num.append(keyword_num)
for letter in keyword_z:
    keyword_num=int(ord(letter))-97
    keyword_z_num.append(keyword_num)
#Asks for message
message_numbers=[]
message=str(input("Enter the encrypted message: "))
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
#Asks what keyword to be used and gives length warning
keyword=str(input("Enter Keyword used in Encryption: "))
keyword=keyword.lower()
#Makes the keyword into ASCII
mykeylist=[]
mykeylistfinished=[]
variant=0
for i in keyword:
    numKey=ord(i)-97
    mykeylist.append(numKey)
lenkeyword=len(keyword)
for key in range(alpha_chr_len):
    keylistvalues=int(mykeylist[variant])
    mykeylistfinished.append(int(keylistvalues))
    variant=(int(variant+1))%(int(lenkeyword))
#Decryption using rows and columns
encrypted_message=[]
variant=0
for letters in message_numbers:
    if isinstance(letters, int) == True:
        if keyword_a_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_a_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_b_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_b_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_c_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_c_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_d_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_d_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_e_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_e_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_f_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_f_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_g_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_g_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_h_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_h_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_i_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_i_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_j_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_j_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_k_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_k_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_l_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_l_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_m_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_m_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_n_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_n_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_o_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_o_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_p_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_p_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_q_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_q_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_r_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_r_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_s_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_s_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_t_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_t_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_u_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_u_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_v_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_v_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_w_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_w_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_x_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_x_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_y_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_y_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        elif keyword_z_num[0] == mykeylistfinished[variant]:
            encrypted_message_num=keyword_z_num.index(letters)
            encrypted_message.append(encrypted_message_num)
        else:
            print("ERROR")
        variant=variant+1
    else:
        encrypted_message.append(" ")
#Making encrypted message back to letters
encrypted_message_alpha=""
for num in encrypted_message:
    if isinstance(num, int) == True:
        encrypted_letter=chr((int(num)+97))
        encrypted_message_alpha=encrypted_message_alpha+encrypted_letter
    else:
        encrypted_message_alpha=encrypted_message_alpha+str(" ")
#Final Display
print("Your decrypted message is: ", encrypted_message_alpha)
print("The information used to decrypt: ")
print(f"Keyword: {keyword}")
print("If you give the program any incorrect info of how to decrypt, the message will be meaningless.")
