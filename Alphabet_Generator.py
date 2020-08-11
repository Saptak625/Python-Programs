#Alphabet Generator
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
variant=0
alphabet1=["z"]
while len(alphabet1)<=25:
    alphabet1.append(alphabet[variant])
    alphabet1.append(alphabet[variant+1])
    alphabet1.append(alphabet[24-variant])
    alphabet1.append(alphabet[23-variant])
    variant=variant+1
alphabet2=['z','m','a','n','y','l','b','o','x','k','c','p','w','j','d','q','v','i','e','r','u','h','f','s','t','g']
alphabet3=['g','t','u','h','f','s','v','i','e','r','w','j','d','q','x','k','c','p','y','l','b','o','z','m','a','n']
alphabet4=['a','z','y','b','c','x','w','d','e','v','u','f','g','t','s','h','i','r','q','j','k','p','o','l','m','n']
alphabet5=['a','t','n','g','z','h','m','u','b','s','o','f','y','i','l','v','c','r','d','e','x','j','k','w','d','q']
alphabet6=['f','n','s','a','u','l','h','y','e','o','r','b','v','k','i','x','d','p','q','c','w','j','t','m','g','z']
alphabet7=['v','o','h','a','j','c','f','m','t','k','r','y','u','n','w','p','i','b','g','d','f','l','s','z','q','x']
alphabet8=['d','j','f','l','r','x','w','z','u','o','i','c','g','a','e','k','q','m','s','y','v','p','t','n','h','b']
alphabet9=['j','e','z','u','p','k','f','a','v','q','l','g','b','w','r','m','h','c','x','s','n','i','d','y','t','o']
alphabet10=['h','m','r','w','b','g','l','q','v','a','f','k','r','u','z','e','j','o','t','y','d','i','n','s','x','c']
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
print(alphabet1num,alphabet2num,alphabet3num,alphabet4num,alphabet5num,alphabet6num,alphabet7num,alphabet8num,alphabet9num,alphabet10num)
    
