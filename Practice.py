import random


#
def start_game():
    print("Welcome to the game")
    name = input("what is your name , adventurer? :")
    print(f"Let the adventure begin, {name}!")
    choose_path(name)


#
def encounter_treasure(name):
    treasure = random.choice(['diamonds', 'a sword', 'a secret map'])
    print(f"Oh !! Congrats, {name} You've encountered a treasure that has {treasure}")



#
def encounter_monster(name):
    monster = random.choice(['dragon', 'friendly dragon', 'pirate'])
    print(f"Oh no, {name}You've encountered a {monster}!")    

def choose_path(name):
    path = input(f"You are in crossroad {name}. Would you like to go left or right? (left/right): ")
    if path == 'left':
        encounter_treasure(name)
    elif path == 'right':
        encounter_monster(name)
    else:
        print("Please enter a valid direction, Try again")
        choose_path(name) #Recusrion to restart the choice





# start the game
start_game()
       