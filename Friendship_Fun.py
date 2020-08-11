from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
str = ''
import random
while str!="QUIT":
    clear()
    list = []
    x=0
    string = ""
    comparison = ['Mr. Raines', 'Luis', 'Sean', 'Ramy', 'Zach', 'Akshay', 'Aarushi', 'Ishita','Camille', 'Nandita', 'Abby', 'Samshita', 'Olivia', 'Anya', 'Vamsi', 'Ananya', 'Ashima','Sid','Rishita', 'Simran', 'Niyoosha', 'Ishika', 'Naishu', 'Connor']
    print("Enter 10 people's names and it will tell you the percentage of people that are correct. Note this program will tell the truth 60% of the time! Make sure to spell the names correctly. Proper or Formal Names will be marked correct. All names are written in shortest proper name address! Also, note that the list stored in this program also has 16 other people to just throw you guys off! There are only 8.") 
    import random
    for i in range(10):
        string=input('Enter name: ')
        randint = random.randrange(1,100)
        if string in comparison:
            if int(randint)<=60:
                x=x+1
            else:
                x=x
    percentage = int(x*10)
    print(f"Your guesses are {percentage}% right.")
    print("Note the above statments.")
    print("Program Repeating in 5 seconds")
    sleep(5)

    



    
