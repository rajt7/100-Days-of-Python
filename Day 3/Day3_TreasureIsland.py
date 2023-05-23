print('''
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|  
''')

print("Welcome to Treasue Island.")
print("Your mission is to find the treasure.")
direction = input('''You are at a cross road. where do you want to go? Type "left" or "right"\n''')

if direction.lower() == "left" :
    print('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
    swim_or_wait = input()

    if swim_or_wait.lower() == "wait" :
        print('''You arrive at the island unharmed. There is a house with 3 doors.  One red, one yellow and one blue. Which colour do you choose?\n''')
        colour = input()
        if colour.lower() == "red" :
            print("You enter a room of fire. Game Over!!")
        elif colour.lower() == "yellow" :
            print("You Win!!!")
        elif colour.lower() == "blue" :
            print("You enter a room of beasts. Game Over!!")
        else :
            print("Game Over!!")
    else :
        print("You are attacked by a trout. Game Over!!")
else :
    print("Fall into a hole. Game Over!!")