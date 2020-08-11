#Use Virtual Environment to run
import matplotlib.pyplot as plt
#Getting Input
input=input("Enter Encrypted Message: ")
encrypted_message=input
#Message without spaces
encrypted_message=encrypted_message.replace(' ',"")
#Bigraph Generation
bigraph_list=[]
for i in range(len(encrypted_message)-1):
	first=encrypted_message[i]
	second=encrypted_message[i+1]
	bigraph=first+second
	if bigraph not in bigraph_list:
		bigraph_list.append(bigraph)
#Trigraph Generation
trigraph_list=[]
for i in range(len(encrypted_message)-2):
	first=encrypted_message[i]
	second=encrypted_message[i+1]
	third=encrypted_message[i+2]
	trigraph=first+second+third
	if trigraph not in trigraph_list:
		trigraph_list.append(trigraph)
#Finding Indexes
#Generating storage lists
bigraph_ind=[]
trigraph_ind=[]
for b in bigraph_list:
	bigraph_ind.append([])
for t in trigraph_list:
	trigraph_ind.append([])
#Indexes for bigraphs
for i in range(len(encrypted_message)-1):
	first=encrypted_message[i]
	second=encrypted_message[i+1]
	bigraph=first+second
	for b in bigraph_list:
		if b==bigraph:
			ind=bigraph_list.index(b)
			bigraph_ind[ind].append(i)
#Indexes for trigraphs
for i in range(len(encrypted_message)-2):
	first=encrypted_message[i]
	second=encrypted_message[i+1]
	third=encrypted_message[i+2]
	trigraph=first+second+third
	for t in trigraph_list:
		if t==trigraph:
			ind=trigraph_list.index(t)
			trigraph_ind[ind].append(i)
#Trim lists via append and reload
t_bigraph_list=[]
t_bigraph_ind=[]
for index in range(int(len(bigraph_list))):
	if len(bigraph_ind[index])>=3:
		t_bigraph_list.append(bigraph_list[index])
		t_bigraph_ind.append(bigraph_ind[index])
bigraph_list=t_bigraph_list
bigraph_ind=t_bigraph_ind
t_trigraph_list=[]
t_trigraph_ind=[]
for index in range(int(len(trigraph_list))):
	if len(trigraph_ind[index])>=3:
		t_trigraph_list.append(trigraph_list[index])
		t_trigraph_ind.append(trigraph_ind[index])
trigraph_list=t_trigraph_list
trigraph_ind=t_trigraph_ind
#Multiples
differences=[]
for i in bigraph_ind:
	variant=1
	while variant!=len(i):
		if variant==1:
			length=len(i)-variant
		else:
			length=length-variant
		for ind in range(length):
			comparison_1=i[variant-1]
			comparison_2=i[ind+1]
			differences.append(int(comparison_2-comparison_1))
		variant=variant+1
for i in trigraph_ind:
	variant=1
	while variant!=len(i):
		if variant==1:
			length=len(i)-variant
		else:
			length=length-variant
		for ind in range(length):
			comparison_1=i[variant-1]
			comparison_2=i[ind+1]
			differences.append(int(comparison_2-comparison_1))
		variant=variant+1
final_differences=[]
for num in differences:
        if num>1:
                final_differences.append(num)
factors_list=[]
for val in range(40):
        factors_list.append(0)
for nums in final_differences:
        for factor in range(40):
                if nums%(factor+1)==0:
                        factors_list[factor]=factors_list[factor]+1
x=[]
for i in range(40):
        x.append(i+1)
plt.plot(x,factors_list)
plt.show()
