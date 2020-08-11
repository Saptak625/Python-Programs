key = ''
t_input_storage = []
p_input_storage = []
while key != 'DONE':
    from random import *
    print('You are a mentally ill person and someone precious to you got murdered! What will you do?')
    print('Key is to survive as long as possible or reach the "You have cleared the game" message.')
    print('')
    print("1: Immediate Revenge")
    print("2: Find more info")
    print("3: Absolutly Nothing")
    integer = int(input('Please enter your choice as a number(1,2,3):  '))
    t_input_storage.append(integer)
    print('')
    if integer == 1:
        #Done
        r = random()
        if r <=0.25:
            print('Oh no! You died from a heart attack from stress!')
            print('Game Over!')
        else:
            print('You go on a killing spree! You get caught and get executed!')
            print('Game Over!')
    elif integer == 2:
        print('You found the more info on the murderer. What will you do now?')
        print('')
        print('1: Tell Officials')
        print('2: Revenge')
        integer = int(input('Please enter your choice as a number:  '))
        t_input_storage.append(integer)
        print('')
        if integer == 1:
            #Done
            print("The officials did nothing! They didn't listen to you! What will you do?")
            print('')
            print('1: Revenge')
            print('2: Tell them again')
            print('3: Nothing')
            integer = int(input('Please enter your choice as a number:  '))
            t_input_storage.append(integer)
            print('')
            if integer == 1:
                #Insert everything from revenge else
                print('You have decided you want revenge. You are formulating your plan. What will you do?')
                print('')
                print('1: Kill everyone with a positive relationship with the murderer AND killing the murderer.')
                print('2: Kill only the friends and family of murderer')
                print('3: Just kill the murderer.')
                integer = int(input('Please enter your choice as a number:  '))
                t_input_storage.append(integer)
                print('')
                if integer == 1:
                    print('You kill everyone. However, you wonder what to do now.')
                    print('')
                    print('1: Continue regular life')
                    print('2: Hide')
                    integer = int(input('Please enter your choice as a number:  '))
                    t_input_storage.append(integer)
                    print('')
                    if integer == 1:
                        print('You are caught and executed.')
                        print('Game Over!')
                    else:
                        print('Where will you hide?')
                        print('')
                        print('1: Jungle')
                        print('2: Mountains')
                        print('3: City')
                        integer = int(input('Please enter your choice as a number:  '))
                        t_input_storage.append(integer)
                        print('')
                        if integer == 1:
                            print('You died from major injuries from a jaguar.')
                            print('Game Over!')
                        elif integer == 2:
                            print('Congratulations! You have survived! You have cleared the level!')
                        else:
                            print('You were caught and sent to prison for the rest of your life.')
                            print('Game Over!')
                elif integer == 2:
                    r = random()
                    if r<=0.4:
                        print('The murderer kills the rest of your family and frends. You die of guilt and depression.')
                        print('Game Over!')
                    elif 0.4<r<=0.5:
                        print('The murderer dies from built up stress. What will you do now?')
                        print('')
                        print('1: Continue regular life')
                        print('2: Hide')
                        integer = int(input('Please enter your choice as a number:  '))
                        t_input_storage.append(integer)
                        print('')
                        if integer == 1:
                            print('You get caught and executed.')
                            print('Game Over!')
                        else:
                            print('Where will you hide?')
                            print('')
                            print('1: Jungle')
                            print('2: Mountains')
                            print('3: City')
                            integer = int(input('Please enter your choice as a number:  '))
                            t_input_storage.append(integer)
                            print('')
                            if integer == 1:
                                print('You died from major injuries from a jaguar.')
                                print('Game Over!')
                            elif integer == 2:
                                print('Congratulations! You have survived! You have cleared the level!')
                            else:
                                print('You were caught and sent to prison for the rest of your life.')
                                print('Game Over!')    
                else:
                    print('The murderer kills you!')
                    print('Game Over!')
            else:
                print('You have died from a heart attack caused up because of stress.')
        else:
            print('You have decided you want revenge. You are formulating your plan. What will you do?')
            print('')
            print('1: Kill everyone with a positive relationship with the murderer AND killing the murderer.')
            print('2: Kill only the friends and family of murderer')
            print('3: Just kill the murderer.')
            integer = int(input('Please enter your choice as a number:  '))
            t_input_storage.append(integer)
            print('')
            if integer == 1:
                print('You kill everyone. However, you wonder what to do now.')
                print('')
                print('1: Continue regular life')
                print('2: Hide')
                integer = int(input('Please enter your choice as a number:  '))
                t_input_storage.append(integer)
                print('')
                if integer == 1:
                    print('You are caught and executed.')
                    print('Game Over!')
                else:
                    print('Where will you hide?')
                    print('')
                    print('1: Jungle')
                    print('2: Mountains')
                    print('3: City')
                    integer = int(input('Please enter your choice as a number:  '))
                    t_input_storage.append(integer)
                    print('')
                    if integer == 1:
                        print('You died from major injuries from a jaguar.')
                        print('Game Over!')
                    elif integer == 2:
                        print('Congratulations! You have survived! You have cleared the level!')
                    else:
                        print('You were caught and sent to prison for the rest of your life.')
                        print('Game Over!')
            elif integer == 2:
                r = random()
                if r<=0.4:
                    print('The murderer kills the rest of your family and frends. You die of guilt and depression.')
                    print('Game Over!')
                elif 0.4<r<=0.5:
                    print('The murderer dies from built up stress. What will you do now?')
                    print('')
                    print('1: Continue regular life')
                    print('2: Hide')
                    integer = int(input('Please enter your choice as a number:  '))
                    t_input_storage.append(integer)
                    print('')
                    if integer == 1:
                        print('You get caught and executed.')
                        print('Game Over!')
                    else:
                        print('Where will you hide?')
                        print('')
                        print('1: Jungle')
                        print('2: Mountains')
                        print('3: City')
                        integer = int(input('Please enter your choice as a number:  '))
                        t_input_storage.append(integer)
                        print('')
                        if integer == 1:
                            print('You died from major injuries from a jaguar.')
                            print('Game Over!')
                        elif integer == 2:
                            print('Congratulations! You have survived! You have cleared the level!')
                        else:
                            print('You were caught and sent to prison for the rest of your life.')
                            print('Game Over!')    
            else:
                print('The murderer kills you!')
                print('Game Over!')
    else:
        #Done
        r= random()
        if r<=0.5:
            print('You now have depression and commited suicide!')
            print('Game Over!')
        else:
            print('You go insane and murdered tens of people. You now decide to kill yourself.')
            print('Game Over!')
        
    key = str(input('Tell Saptak you are done!'))
    p_input_storage.append(t_input_storage)
    for x in range(1,100):
        print('')
print(p_input_storage)
            
                    
