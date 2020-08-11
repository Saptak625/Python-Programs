import sys
import math
#Warning
print('Some really complex equations may not be balanced by this program. However, 99% of equations can be balanced.')
print('Note that this program is not compatible for brackets. Also, note that this program uses condensed molecular formulas only.')
print('For example,')
print('Incorrect: Ca(NO3)2, (NH4)3PO4, NH4NO3, etc.')
print('Correct: CaN2O6, N3H12PO4, N2H4O3, etc.')
#Input of Products and Reaction
print("Format: H2O+CO2")
reactants=str(input("Type in reactant side: "))
reactants_list=reactants.split('+')
products=str(input("Type in product side: "))
products_list=products.split('+')
#Processing of input
e_reactants=[]
eq_reactants=[]
for i in reactants_list:
    e_reactants.append([])
    eq_reactants.append([])
e_products=[]
eq_products=[]
for i in products_list:
    e_products.append([])
    eq_products.append([])
r_elements=[]
p_elements=[]
element = ''
quantity = ''
for ind in range(len(reactants_list)):
    for string in reactants_list[ind]:
        if string.isdigit():
            quantity=quantity+str(string)
        elif string.isalpha():
            if string.isupper():
                if element=='':
                    element=element+string
                else:
                    if element in e_reactants[ind]:
                        o_quantity=eq_reactants[ind][e_reactants[ind].index(element)]
                        if quantity=='':
                            eq_reactants[ind][e_reactants[ind].index(element)]=int(1+o_quantity)
                        else:
                            eq_reactants[ind][e_reactants[ind].index(element)]=int(int(quantity)+o_quantity)
                    else:
                        o_quantity=0
                        e_reactants[ind].append(element)
                        if quantity=='':
                            eq_reactants[ind].append(int(1))
                        else:
                            eq_reactants[ind].append(int(int(quantity)))
                    element=''
                    quantity=''
                    element=element+string
            elif string.islower():
                element=element+string
    if element in e_reactants[ind]:
        o_quantity=eq_reactants[ind][e_reactants[ind].index(element)]
        if quantity=='':
            eq_reactants[ind][e_reactants[ind].index(element)]=int(1+o_quantity)
        else:
            eq_reactants[ind][e_reactants[ind].index(element)]=int(int(quantity)+o_quantity)
    else:
        o_quantity=0
        e_reactants[ind].append(element)
        if quantity=='':
            eq_reactants[ind].append(int(1))
        else:
            eq_reactants[ind].append(int(int(quantity)))
    element=''
    quantity=''
element = ''
quantity = ''
for ind in range(len(products_list)):
    for string in products_list[ind]:
        if string.isdigit():
            quantity=quantity+str(string)
        elif string.isalpha():
            if string.isupper():
                if element=='':
                    element=element+string
                else:
                    if element in e_products[ind]:
                        o_quantity=eq_products[ind][e_products[ind].index(element)]
                        if quantity=='':
                            eq_products[ind][e_products[ind].index(element)]=int(1+o_quantity)
                        else:
                            eq_products[ind][e_products[ind].index(element)]=int(int(quantity)+o_quantity)
                    else:
                        o_quantity=0
                        e_products[ind].append(element)
                        if quantity=='':
                            eq_products[ind].append(int(1+o_quantity))
                        else:
                            eq_products[ind].append(int(int(quantity)+o_quantity))
                    element=''
                    quantity=''
                    element=element+string
            elif string.islower():
                element=element+string
    if element in e_products[ind]:
        o_quantity=eq_products[ind][e_products[ind].index(element)]
        if quantity=='':
            eq_products[ind][e_products[ind].index(element)]=int(1+o_quantity)
        else:
            eq_products[ind][e_products[ind].index(element)]=int(int(quantity)+o_quantity)
    else:
        o_quantity=0
        e_products[ind].append(element)
        if quantity=='':
            eq_products[ind].append(int(1+o_quantity))
        else:
            eq_products[ind].append(int(int(quantity)+o_quantity))
    element=''
    quantity=''
#Generating all elements
for compound in e_reactants:
    for element in compound:
        if element not in r_elements:
            r_elements.append(element)
for compound in e_products:
    for element in compound:
        if element not in p_elements:
            p_elements.append(element)
if len(r_elements)==len(p_elements):
    elements=r_elements
#Finding all instances of elements
r_instance=[[] for element in elements]
p_instance=[[] for element in elements]
index=0
for element in elements:
    for compound in e_reactants:
        for e in compound:
            if e==element:
                ind=e_reactants.index(compound)
                r_instance[index].append(ind)
    index=index+1
index=0
for element in elements:
    for compound in e_products:
        for e in compound:
            if e==element:
                ind=e_products.index(compound)
                p_instance[index].append(ind)
    index=index+1
#Logic Start
#Making Variable Lists
ra_list=[0 for i in e_reactants]
rb_list=[0 for i in e_reactants]
pa_list=[0 for i in e_products]
pb_list=[0 for i in e_products]
r_scaler_list=[1 for i in e_reactants]
p_scaler_list=[1 for i in e_products]
r_coeffiecient_bool=[False for i in e_reactants]
p_coeffiecient_bool=[False for i in e_products]
#Step 1
used_elements=[]
for ind in range(len(elements)):
    if len(r_instance[ind])==1 and len(p_instance[ind])==1:
        e=elements[ind]
        rc_index=r_instance[ind][0]
        pc_index=p_instance[ind][0]
        #Fetching quantities
        re_index=e_reactants[rc_index].index(e)
        pe_index=e_products[pc_index].index(e)
        r_quantity=eq_reactants[rc_index][re_index]
        p_quantity=eq_products[pc_index][pe_index]
        #Finding list that is empty
        if ra_list[rc_index]==0 and pa_list[pc_index]==0 and rb_list[rc_index]==0 and pb_list[pc_index]==0:
            if 1 not in ra_list and 1 not in pa_list:
                #A-list is open
                if r_quantity>p_quantity:
                    ra_list[rc_index]=1
                    if (r_quantity/p_quantity)==round(r_quantity/p_quantity):
                        pa_list[pc_index]=int(r_quantity/p_quantity)
                    else:
                        gcf=math.gcd(r_quantity,p_quantity)
                        p_scaler_list[pc_index]=int(p_quantity/gcf)
                        pa_list[pc_index]=int(r_quantity/gcf)
                elif r_quantity<p_quantity:
                    pa_list[pc_index]=1
                    if (p_quantity/r_quantity)==round(p_quantity/r_quantity):
                        ra_list[rc_index]=int(p_quantity/r_quantity)
                    else:
                        gcf=math.gcd(r_quantity,p_quantity)
                        r_scaler_list[rc_index]=int(r_quantity/gcf)
                        ra_list[rc_index]=int(p_quantity/gcf)
                else:
                    ra_list[rc_index]=1
                    pa_list[pc_index]=1
                used_elements.append(e)
                r_coeffiecient_bool[rc_index]=True
                p_coeffiecient_bool[pc_index]=True
            else:
                #Check list B
                if 1 not in rb_list and 1 not in pb_list:
                    if r_quantity>p_quantity:
                        rb_list[rc_index]=1
                        if (r_quantity/p_quantity)==round(r_quantity/p_quantity):
                            pb_list[pc_index]=int(r_quantity/p_quantity)
                        else:
                            gcf=math.gcd(r_quantity,p_quantity)
                            p_scaler_list[pc_index]=int(p_quantity/gcf)
                            pb_list[pc_index]=int(r_quantity/gcf)
                    elif r_quantity<p_quantity:
                        pb_list[pc_index]=1
                        if (p_quantity/r_quantity)==round(p_quantity/r_quantity):
                            rb_list[rc_index]=int(p_quantity/r_quantity)
                        else:
                            gcf=math.gcd(r_quantity,p_quantity)
                            r_scaler_list[rc_index]=int(r_quantity/gcf)
                            rb_list[rc_index]=int(p_quantity/gcf)
                    else:
                        rb_list[rc_index]=1
                        pb_list[pc_index]=1
                    used_elements.append(e)
                    r_coeffiecient_bool[rc_index]=True
                    p_coeffiecient_bool[pc_index]=True
                else:
                    sys.exit('This equation uses more than two variables.')
#Removing used elements
used_elements_2=[]               
for i in range(len(elements)):
    ind=int(-i-1)
    if elements[ind] in used_elements:
        used_elements_2.append(elements[ind])
used_elements=used_elements_2
for e in used_elements:
    element_index=elements.index(e)
    elements.remove(e)
    del r_instance[element_index]
    del p_instance[element_index]
used_elements=[]
#Step 2
#1->1 where one coefficient is already fixed
for ind in range(len(elements)):
    if False in r_coeffiecient_bool or False in p_coeffiecient_bool:
        if len(r_instance[ind])==1 and len(p_instance[ind])==1:
            e=elements[ind]
            rc_index=r_instance[ind][0]
            pc_index=p_instance[ind][0]
            #Fetching quantities
            if r_coeffiecient_bool[rc_index] == False or p_coeffiecient_bool[pc_index] == False:
                re_index=e_reactants[rc_index].index(e)
                pe_index=e_products[pc_index].index(e)
                r_quantity=eq_reactants[rc_index][re_index]
                p_quantity=eq_products[pc_index][pe_index]
                if r_coeffiecient_bool[rc_index]==True:
                    #Reaction Side Coefficient 
                    if ra_list[rc_index] != 0:
                        coefficient=int(ra_list[rc_index]/r_scaler_list[rc_index])
                        scaled_quantity=int(r_quantity*coefficient)
                        if (scaled_quantity/p_quantity)==round(scaled_quantity/p_quantity):
                            pa_list[pc_index]=int(scaled_quantity/p_quantity)
                        else:
                            gcf=math.gcd(scaled_quantity,p_quantity)
                            pa_list[pc_index]=int(scaled_quantity/gcf)
                            p_scaler_list[pc_index]=int(p_quantity/gcf)
                    elif rb_list[rc_index] !=0:
                        coefficient=int(rb_list[rc_index]/r_scaler_list[rc_index])
                        scaled_quantity=int(r_quantity*coefficient)
                        if (scaled_quantity/p_quantity)==round(scaled_quantity/p_quantity):
                            pb_list[pc_index]=int(scaled_quantity/p_quantity)
                        else:
                            gcf=math.gcd(scaled_quantity,p_quantity)
                            pb_list[pc_index]=int(scaled_quantity/gcf)
                            p_scaler_list[pc_index]=int(p_quantity/gcf)
                    used_elements.append(e)
                    p_coeffiecient_bool[pc_index]=True
                elif p_coeffiecient_bool[pc_index]==True:
                    #Product Side Coefficient
                    if pa_list[pc_index] != 0:
                        coefficient=int(pa_list[pc_index]/p_scaler_list[pc_index])
                        scaled_quantity=int(p_quantity*coefficient)
                        if (scaled_quantity/r_quantity)==round(scaled_quantity/r_quantity):
                            ra_list[rc_index]=int(scaled_quantity/r_quantity)
                        else:
                            gcf=math.gcd(r_quantity,scaled_quantity)
                            ra_list[rc_index]=int(scaled_quantity/gcf)
                            r_scaler_list[rc_index]=int(r_quantity/gcf)
                    elif pb_list[pc_index] !=0:
                        coefficient=int(pb_list[pc_index]/p_scaler_list[pc_index])
                        scaled_quantity=int(p_quantity*coefficient)
                        if (scaled_quantity/r_quantity)==round(scaled_quantity/r_quantity):
                            rb_list[rc_index]=int(scaled_quantity/r_quantity)
                        else:
                            gcf=math.gcd(r_quantity,scaled_quantity)
                            rb_list[rc_index]=int(scaled_quantity/gcf)
                            r_scaler_list[rc_index]=int(r_quantity/gcf)
                    used_elements.append(e)
                    r_coeffiecient_bool[rc_index]=True
                    #print(elements)
                    #print(used_elements)
#Removing used elements
used_elements_2=[]               
for i in range(len(elements)):
    ind=int(-i-1)
    if elements[ind] in used_elements:
        used_elements_2.append(elements[ind])
used_elements=used_elements_2
for e in used_elements:
    element_index=elements.index(e)
    elements.remove(e)
    del r_instance[element_index]
    del p_instance[element_index]
used_elements=[]
time=0
#Step 3
#All but one instance of a element are known. Use this to define value.
while False in r_coeffiecient_bool or False in p_coeffiecient_bool:
    if time>=500:
        sys.exit('This equation cannot be solved with algebraic method as presented. Please simply the equation by making defining polyatomic ions as their own elements. For example, NaHCO3+HC2H3O2-->NaC2H3O2+H2O+CO2, please simplify into NaHCO3+HY-->NaY+H2O+CO2.')
    length=len(elements)
    for ind in range(length):
        if False in r_coeffiecient_bool or False in p_coeffiecient_bool:
            temp_ra_list=[]
            temp_pa_list=[]
            temp_rb_list=[]
            temp_pb_list=[]
            r_scaled=1
            p_scaled=1
            e=elements[ind]
            total = int(len(r_instance[ind])+len(p_instance[ind]))
            r_obj = r_instance[ind]
            p_obj = p_instance[ind]
            filled = 0
            unfilled_index=None
            for index in r_obj:
                if r_coeffiecient_bool[index] == True:
                    filled=filled+1
                else:
                    unfilled_location='r'
                    unfilled_index=index
            for index in p_obj:
                if p_coeffiecient_bool[index] == True:
                    filled=filled+1
                else:
                    unfilled_location='p'
                    unfilled_index=index
            if (total-1)==filled:
                if unfilled_location=='r':
                    r_obj.remove(unfilled_index)
                    unfilled_quantity=eq_reactants[unfilled_index][e_reactants[unfilled_index].index(e)]
                elif unfilled_location=='p':
                    p_obj.remove(unfilled_index)
                    unfilled_quantity=eq_products[unfilled_index][e_products[unfilled_index].index(e)]
                #Grabs all reactant data
                for r_ind in r_obj:
                    re_ind=e_reactants[r_ind].index(e)
                    quantity=eq_reactants[r_ind][re_ind]
                    coefficient=ra_list[r_ind]
                    if coefficient != 0:
                        scaler=r_scaler_list[r_ind]
                        if scaler ==1:
                            scaled_quantity=int(quantity*coefficient)
                        else:
                            scaled_quantity=float((quantity*coefficient)/scaler)
                            r_scaled=r_scaled*scaler
                        temp_ra_list.append(scaled_quantity)
                    coefficient=rb_list[r_ind]
                    if coefficient != 0:
                        scaler=r_scaler_list[r_ind]
                        if scaler ==1:
                            scaled_quantity=int(quantity*coefficient)
                        else:
                            scaled_quantity=float((quantity*coefficient)/scaler)
                            r_scaled=r_scaled*scaler
                        temp_rb_list.append(scaled_quantity)
                #Grabs all product data
                for p_ind in p_obj:
                    pe_ind=e_products[p_ind].index(e)
                    quantity=eq_products[p_ind][pe_ind]
                    coefficient=pa_list[p_ind]
                    if coefficient != 0:
                        scaler=p_scaler_list[p_ind]
                        if scaler ==1:
                            scaled_quantity=int(quantity*coefficient)
                        else:
                            scaled_quantity=float((quantity*coefficient)/scaler)
                            p_scaled=p_scaled*scaler
                        temp_pa_list.append(scaled_quantity)
                    coefficient=pb_list[p_ind]
                    if coefficient != 0:
                        scaler=p_scaler_list[p_ind]
                        if scaler ==1:
                            scaled_quantity=int(quantity*coefficient)
                        else:
                            scaled_quantity=float((quantity*coefficient)/scaler)
                            p_scaled=p_scaled*scaler
                        temp_pb_list.append(scaled_quantity)
                #Sums of Sides
                #ra
                ra_sum=0
                for coe in temp_ra_list:
                    if r_scaled != 1:
                        coe=int(coe*r_scaled)
                    ra_sum=int(ra_sum+coe)
                #rb
                rb_sum=0
                for coe in temp_rb_list:
                    if r_scaled != 1:
                        coe=int(coe*r_scaled)
                    rb_sum=int(rb_sum+coe)
                #pa
                pa_sum=0
                for coe in temp_pa_list:
                    if p_scaled != 1:
                        coe=int(coe*p_scaled)
                    pa_sum=int(pa_sum+coe)
                #pb
                pb_sum=0
                for coe in temp_pb_list:
                    if p_scaled != 1:
                        coe=int(coe*p_scaled)
                    pb_sum=int(pb_sum+coe)
                #Substraction of sides
                if unfilled_location=='r':
                    #Math 
                    if r_scaled != 1:
                        pa_sum=int(pa_sum*r_scaled)
                        pb_sum=int(pb_sum*r_scaled)
                    if p_scaled != 1:
                        ra_sum=int(ra_sum*p_scaled)
                        rb_sum=int(rb_sum*p_scaled)
                    a_sum= pa_sum-ra_sum
                    b_sum= pb_sum-rb_sum
                elif unfilled_location=='p':
                    #Math 
                    if r_scaled != 1:
                        pa_sum=int(pa_sum*r_scaled)
                        pb_sum=int(pb_sum*r_scaled)
                    if p_scaled != 1:
                        ra_sum=int(ra_sum*p_scaled)
                        rb_sum=int(rb_sum*p_scaled)
                    a_sum= ra_sum-pa_sum
                    b_sum= rb_sum-pb_sum
                scale=r_scaled*p_scaled
                gcf_1=math.gcd(int(scale*unfilled_quantity),a_sum)
                gcf_2=math.gcd(int(scale*unfilled_quantity),b_sum)
                if gcf_1>gcf_2:
                    mod=gcf_1%gcf_2
                    if mod == 0:
                        gcf=gcf_2
                    else:
                        gcf=1
                elif gcf_2>gcf_1:
                    mod=gcf_2%gcf_1
                    if mod == 0:
                        gcf=gcf_1
                    else:
                        gcf=1
                else: 
                    gcf=gcf_1
                #Appending Value
                if unfilled_location=='r':
                    ra_list[unfilled_index]=int(a_sum/gcf)
                    rb_list[unfilled_index]=int(b_sum/gcf)
                    r_scaler_list[unfilled_index]=int((scale*unfilled_quantity)/gcf)
                    r_coeffiecient_bool[unfilled_index]=True
                elif unfilled_location=='p':
                    pa_list[unfilled_index]=int(a_sum/gcf)
                    pb_list[unfilled_index]=int(b_sum/gcf)
                    p_scaler_list[unfilled_index]=int((scale*unfilled_quantity)/gcf)
                    p_coeffiecient_bool[unfilled_index]=True
                used_elements.append(e)
    #Removing used elements
    used_elements_2=[]               
    for i in range(len(elements)):
        ind=int(-i-1)
        if elements[ind] in used_elements:
            used_elements_2.append(elements[ind])
    used_elements=used_elements_2
    for e in used_elements:
        element_index=elements.index(e)
        elements.remove(e)
        del r_instance[element_index]
        del p_instance[element_index]
    used_elements=[]
    #Debugging
    #print(f'Elements left: {elements}')
    #print(r_coeffiecient_bool,p_coeffiecient_bool)
    time=time+1
#Final Algebra
final_r_list=[]
final_p_list=[]
scaled_coefficient_ar=[]
scaled_coefficient_ap=[]
scaled_coefficient_br=[]
scaled_coefficient_bp=[]
substituted_ar=[]
substituted_br=[]
substituted_ap=[]
substituted_bp=[]
if 1 in rb_list or 1 in pb_list:
    f_scale=1
    #Uses both a and b
    #Grabbing element from elements list
    e=elements[0]
    r_indexes=r_instance[0]
    p_indexes=p_instance[0]
    #Grabbing Scaled Coefficients and adding together
    for i in r_indexes:
        quantity=eq_reactants[i][e_reactants[i].index(e)]
        scaler=r_scaler_list[i]
        coefficient_a=ra_list[i]
        coefficient_b=rb_list[i]
        if (f_scale%scaler)!=0:
            f_scale=int(f_scale*scaler)
        #First Scaling
        scaled_coefficient_a=(int(coefficient_a*quantity)/scaler)
        scaled_coefficient_ar.append(scaled_coefficient_a)
        scaled_coefficient_b=(int(coefficient_b*quantity)/scaler)
        scaled_coefficient_br.append(scaled_coefficient_b)
    for i in p_indexes:
        quantity=eq_products[i][e_products[i].index(e)]
        scaler=p_scaler_list[i]
        coefficient_a=pa_list[i]
        coefficient_b=pb_list[i]
        if (f_scale%scaler)!=0:
            f_scale=int(f_scale*scaler)
        #First Scaling
        scaled_coefficient_a=(int(coefficient_a*quantity)/scaler)
        scaled_coefficient_ap.append(scaled_coefficient_a)
        scaled_coefficient_b=(int(coefficient_b*quantity)/scaler)
        scaled_coefficient_bp.append(scaled_coefficient_b)
    #Second Scaling 
    for i in range(len(scaled_coefficient_ar)):
        scaled_coefficient_ar[i]=int(scaled_coefficient_ar[i]*f_scale)
    for i in range(len(scaled_coefficient_br)):
        scaled_coefficient_br[i]=int(scaled_coefficient_br[i]*f_scale)
    for i in range(len(scaled_coefficient_ap)):
        scaled_coefficient_ap[i]=int(scaled_coefficient_ap[i]*f_scale)
    for i in range(len(scaled_coefficient_bp)):
        scaled_coefficient_bp[i]=int(scaled_coefficient_bp[i]*f_scale)
    #Summation
    final_ar_sum=0
    final_br_sum=0
    final_ap_sum=0
    final_bp_sum=0
    for c in scaled_coefficient_ar:
        final_ar_sum=int(final_ar_sum+c)
    for c in scaled_coefficient_br:
        final_br_sum=int(final_br_sum+c)
    for c in scaled_coefficient_ap:
        final_ap_sum=int(final_ap_sum+c)
    for c in scaled_coefficient_bp:
        final_bp_sum=int(final_bp_sum+c)
    #See which way to subtract
    if final_ar_sum>final_ap_sum:
        final_a_sum=int(final_ar_sum-final_ap_sum)
        final_b_sum=int(final_bp_sum-final_br_sum)
    elif final_ar_sum<final_ap_sum:
        final_a_sum=int(final_ap_sum-final_ar_sum)
        final_b_sum=int(final_br_sum-final_bp_sum)
    #Setting Final A and B
    a= final_b_sum
    b= final_a_sum
    #Substitution
    for i in range(len(ra_list)):
        coefficient=ra_list[i]
        scaler=r_scaler_list[i]
        substituted_ar.append(float((coefficient*a)/scaler))
    for i in range(len(pa_list)):
        coefficient=pa_list[i]
        scaler=p_scaler_list[i]
        substituted_ap.append(float((coefficient*a)/scaler))
    for i in range(len(rb_list)):
        coefficient=rb_list[i]
        scaler=r_scaler_list[i]
        substituted_br.append(float((coefficient*b)/scaler))
    for i in range(len(pb_list)):
        coefficient=pb_list[i]
        scaler=p_scaler_list[i]
        substituted_bp.append(float((coefficient*b)/scaler))
    #Finding Final Overall Scaling 
    f_scale=1
    for s in r_scaler_list:
        if (f_scale%s)!=0:
            f_scale=int(f_scale*s)
    for s in p_scaler_list:
        if (f_scale%s)!=0:
            f_scale=int(f_scale*s)       
    #Final A and B list Summations
    for i in range(len(ra_list)):
        final_r_list.append(float(substituted_ar[i]+substituted_br[i]))
    for i in range(len(pa_list)):
        final_p_list.append(float(substituted_ap[i]+substituted_bp[i]))
    #Final Overall Scaling
    for i in range(len(final_r_list)):
        final_r_list[i]=int(final_r_list[i]*f_scale)
    for i in range(len(final_p_list)):
        final_p_list[i]=int(final_p_list[i]*f_scale)
else:
    #Equation uses only one variable
    f_scale=1
    for s in r_scaler_list:
        if (f_scale%s)!=0:
            f_scale=int(f_scale*s)
    for s in p_scaler_list:
        if (f_scale%s)!=0:
            f_scale=int(f_scale*s)
    for i in range(len(ra_list)):
        final_r_list.append(int((ra_list[i]*f_scale)/r_scaler_list[i]))
    for i in range(len(pa_list)):
        final_p_list.append(int((pa_list[i]*f_scale)/p_scaler_list[i]))
#Making sure that simplest equation is displayed
all_nums=final_r_list+final_p_list
for n in range(100):
    check=True
    for i in all_nums:
        if i/(n+1) != int(i/(n+1)):
            check=False
    if check==True:
        highest_num=int(n+1)
for i in range(len(final_r_list)):
    final_r_list[i]=int(final_r_list[i]/highest_num)
for i in range(len(final_p_list)):
    final_p_list[i]=int(final_p_list[i]/highest_num)
#Final Display
final_reactants=''
final_products=''
#Making Balanced Reaction Side
for i in range(len(reactants_list)):
    if i != 0:
        final_reactants=final_reactants+str(' + ')
    c=final_r_list[i]
    final_reactants=final_reactants+str(c)
    reactant=reactants_list[i]
    final_reactants=final_reactants+reactant
#Making Balanced Product Side
for i in range(len(products_list)):
    if i != 0:
        final_products=final_products+str(' + ')
    c=final_p_list[i]
    final_products=final_products+str(c)
    product=products_list[i]
    final_products=final_products+product
#Final Joining of equation
print('Balanced Equation: ')
print(str(final_reactants+' ---> '+final_products))
