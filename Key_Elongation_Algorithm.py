#Asks keyword and converts it into all lowercase
mystr=str(input("Enter Keyword all lwcaps:"))
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
print(mykeylist)
print(len(mykeylist))


