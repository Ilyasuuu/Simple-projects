import random

#we will add an inventory for a global access:
inventory = []

#
def start_game():
    print("Welcome to the game")
    name = input("what is your name , adventurer? :")
    print(f"Let the adventure begin, {name}!")
    choose_path(name)

#Adiing another function for more interactivity:
def trade_with_merchant(name, treasure):
    print(f"A mysterious merchant appears offering a trade for your {treasure}.")
    trade = input(f"Do you want to trade your {treasure} with the merchant for a magical shield for the journey? (yes/no): ").lower()
    if trade == "yes":
        print(f"Congrats {name}, you traded {treasure} for a magical shield!")
        #inventory to append the item:
        inventory.append('magical shield')   
    else:
        print(f"{name} decided to keep the {treasure}.")        
        
#Updating 
def encounter_treasure(name):
    treasures = ['diamonds', 'ancient sword', 'secret map']
    treasure = random.choice(treasures)
    print(f"Oh !! Congrats, {name} You've encountered a treasure that has {treasure}")
    # we have to call trade function here for a batter inter.:
    trade_with_merchant(name, treasure)


#
def encounter_monster(name):
    monster = random.choice(['dragon', 'friendly dragon', 'pirate'])
    print(f"Oh no, {name} You've encountered a {monster}!")    

def choose_path(name):
    path = input(f"You are in crossroad {name}. Would you like to go left or right? (left/right): ").lower()
    if path == 'left':
        encounter_treasure(name)
    elif path == 'right':
        encounter_monster(name)
    else:
        print("Please enter a valid direction, Try again")
        choose_path(name) #Recusrion to restart the choice





# start the game
start_game()
       