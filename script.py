#Overview:  a single-player game similar to battleships where the player has a certain number of shots to sink the enemy ships.
# the program will randomly generate the coordinates for a bigship and a littleship
# the player will then shoot one shot at a time until the boats are sunk - a win - or he runs out of shots - a loss.

#global values and variables
from xml.etree.ElementTree import C14NWriterTarget
import random

gridlimit_alphabet = "abcdefg" #x-bounds of the pond
gridlimit_int = list(str(range(1, len(gridlimit_alphabet)+1, 1))) #y-bounds of the pond
player_1 = "" #username
player_1_bigship = [] #coordinates of the bigship
player_1_littleship = [] #coordinates of the littleship
shots_fired = [] #all shots fired by player_1


for i in range(3):
    player_1_bigship.append((gridlimit_alphabet[random.randint(0, len(gridlimit_alphabet)-1)]) + str(random.randint(1, len(gridlimit_alphabet))))
for i in range(2):
    player_1_littleship.append((gridlimit_alphabet[random.randint(0, len(gridlimit_alphabet)-1)]) + str(random.randint(1, len(gridlimit_alphabet))))


#turn sequence

def shot_tracker(shot):
    counter = 0
    if counter < 15:
        
        if shot[0] in gridlimit_alphabet and shot[-1] in gridlimit_int: #checks that the shot is valid
            if shot in shots_fired: #checks that the shot is unique
                print("You already shot there. Try again.")
                if counter < 15:
                    print("Take another shot")
                    shot = input()
                    return shot_tracker(shot)
            else:
                shots_fired.append(shot) 
                counter += 1
                if shot in player_1_bigship:
                    player_1_bigship.pop(shot)
                    if len(player_1_bigship) == 0 :
                        print("You sank his bigship!")
                    else:
                        print("Ohhh you hit something out there!")
                elif shot in player_1_littleship:
                    player_1_littleship.pop(shot)
                    if len(player_1_littleship) == 0:
                        print("You sank his littleship!")
                    else: print("Ohhh you hit something out there!")
                else:
                    print("Plop! You missed the ship but you hit the pond!")
        else: 
            print("That shot went wide of the pond!  Make sure your first coordinate is within " + gridlimit_alphabet[0] + " and " + str(gridlimit_alphabet[-1]) + " and your second coordinate is between 1 and " + str(len(gridlimit_alphabet)) + ".")
            if counter < 15:
                print("Take another shot")
                shot = input()
                return shot_tracker(shot)    
        
        if len(player_1_bigship) == 0 and len(player_1_littleship) == 0:
            print("The enemy is clean out of littleships. You win!")
            print("Game Over")
        else:
            print("The battle continues!")
            if counter < 15:
                print("Take another shot")
                shot = input()
                return shot_tracker(shot)    


        
#initializing

print("What is your name?")
name = input()
print("Welcome to the pond, " + name + "!. Are you ready to hunt littleships?")
ready = input()
print("Take your shot!  Make sure it is a letter within " + gridlimit_alphabet[0] + " and " + str(gridlimit_alphabet[-1]) + ", and a number between 1 and " + str(len(gridlimit_alphabet)) + ".")
shot = input()

first_shot = shot_tracker(shot)

