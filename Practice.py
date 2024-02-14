import random

#we will add an inventory for a global access:
inventory = []

#
def start_game():
    print("Welcome to the game")
    name = input("what is your name , adventurer? :")
    print(f"Let the adventure begin, {name}!")
    choose_path(name)

#Adding another function for more interactivity:
def trade_with_merchant(name, treasure):
    print(f"A mysterious merchant appears offering a trade for your {treasure}.")
    trade = input(f"Do you want to trade your {treasure} with the merchant for a magical shield for the journey? (yes/no): ").lower()
    if trade == "yes":
        print(f"Congrats {name}, you traded {treasure} for a magical shield!")
        #inventory to append the item:
        inventory.append('magical shield')   
    else:
        print(f"{name} decided to keep the {treasure}.")        
        
#Updating2 
def encounter_treasure(name):
    treasures = ['diamonds', 'ancient sword', 'secret map']
    treasure = random.choice(treasures)
    print(f"Oh !! Congrats, {name} You've encountered a treasure that has {treasure}")
    # we have to call trade function here for a batter inter.:
    trade_with_merchant(name, treasure)
    enter_forest(name, inventory)

#
def encounter_monster(name):
    monster = random.choice(['dragon', 'friendly dragon', 'pirate'])
    print(f"Oh no, {name} You've encountered a {monster}!")    
    

#
def enter_forest(name, inventory):
    print(f"{name} approaches a dark forest full of unkown creatures.")
    if 'magical shield' in inventory:
        print("The magical shield will provide light for you.")
        continue_journey(name)
    elif 'ancient sword' in inventory:
        print("You can rely on this sword to face whatever challenge in this forest.")
        continue_journey(name)
    elif 'secret map' in inventory:
        print("Your map is useless in this area, you can not go it is dangerous without a weapon.")
        continue_journey(name)
    else:
        print("You can lose your diamonds, if I were you I won't go!!") 
        end_game(name)               






#
def choose_path(name):
    path = input(f"You are in crossroad {name}. Would you like to go left or right? (left/right): ").lower()
    if path == 'left':
        encounter_treasure(name)
    elif path == 'right':
        encounter_monster(name)
    else:
        print("Please enter a valid direction, Try again")
        choose_path(name) #Recusrion to restart the choice

#continue
def continue_journey(name):
    print(f"{name} continues on the adventure, facing new challenges.")

#end game
def end_game(name):
    print(f"{name} decided to return home with the treasure and live a happy life.")
    print('Game Over')

# start the game
start_game()
       