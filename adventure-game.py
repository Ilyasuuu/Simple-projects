#Step 1: Define the Basic Classes.
#Classes for: HERO, LOCATION, RIDDLE, GAME.

#Why Start Here?

#-Starting with class definitions helps us understand the "blueprint" of our game.
#-It's like planning our LEGO city before we start building it.
#-This ensures we know what pieces we have and how they fit together.

#Hero Class:
    #Our Hero will have attributes like name, location, and inventory, 
    #(to store keys) and methods to move between locations.

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.location =  None     #Will be updated to start location.
        self.inventory = []         #Will store keys.

    def move_to(self, new_location):
        #Update the hero's location.
        self.location = new_location
        print(f"{self.name} moved to {new_location.name}")

    def add_to_inventory(self, item):
        # Add an item to the hero's inventory.
        self.inventory.append(item)
        print(f"{item} added to inventory")

    def move(self, direction):
        # Move the hero to a neighboring location in the specified direction
        if self.location is not None and direction in self.location.neighbors:
            self.location = self.location.neighbors[direction]
            print(f"{self.name} has moved to {self.location.name}")
        else:
            print("You can't go that way.")    

    def solve_riddle(self, riddle_index):
        #Attempt to solve a riddle riddle based on its index in the location's riddle list.
        if self.location is not None:
            current_riddle = self.location.riddles[riddle_index]
            user_answer = input(f"Solve the riddle: {current_riddle.question}").lower()
            if user_answer.lower() == current_riddle.answer.lower():
                print("Correct!")
            else:
                print("Wrong answer. Try again.")
            
            #later we will expand it with features like hints or limited attempts.



#Location Class:
    #Each location will have a name, description, and a set of riddles.
    #We'll expand this later to include more features like neighboring locations. 

class Location:
    def __init__(self, name, riddles):
        self.name = name
        self.riddles = riddles      #This will be a list of riddle objects.
        self.neighbors = {}         #New attribute for neighboring locations.
    def add_neighbor(self, direction, neighbor):
        #Adds a neighboring location with the associated direction
        self.neighbors[direction] = neighbor
        


#Riddle Class:
    #This class represents a single riddle, with the riddle text and the answer.

class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


#Game Class:
    #The Game class will manage the game state, including the hero, locations, and the game loop.

class Game:
    def __init__(self):
        self.hero = None        #This will be initialized when the game starts.
        self.locations = []     #We'll add location here.
            
            #Additonal game setuo will be added here.


    def add_location(self, location):
        #Add a new location to the game
        self.locations.append(location)

    #Additional game methods will be added here.        
        

def setup_game():
    #Create riddles:
    riddles = [Riddle("What has keys but can't open locks?", "A piano"),
                Riddle("What has a neck but no head?", "A bottle"),
                Riddle("What has a head and a tail, but no body?", "A coin"),
                Riddle("What has a thumb and four fingers but is not alive?", "A glove"),
                Riddle("What has a face and two hands but no arms or legs?", "A clock"),
                Riddle("What has a bottom at the top?", "A leg"),
                Riddle("What has a neck but no head?", "A bottle"),
                Riddle("What has a head and a tail, but no body?", "A coin"),
                Riddle("What has a thumb and four fingers but is not alive?", "A glove"),
                Riddle("What has a face and two hands but no arms or legs?", "A clock"),
                Riddle("What has a heart that doesn't beat?", "A artichoke"),
                Riddle("What has a bed but never sleeps?", "A river"),
                Riddle("What has a face that doesn't frown?", "A clock"),
                Riddle("What has a bottom at the top?", "A leg"),
                Riddle("What has a ring but no finger?", "A telephone"),
                Riddle("What has a head and a tail but no body?", "A coin"),
                Riddle("What has a foot but no legs?", "A snail"),
                Riddle("What has a heart that doesn't beat?", "A artichoke"),
                Riddle("What has a bed but never sleeps?", "A river"),
                Riddle("What has a face that doesn't frown?", "A clock"),]

    #Create locations:

    Dark_Village = Location("Dark Village", [riddles[random.randint(0, 4)]])
    Dracula_Castle = Location("Dracula's Castle",[riddles[random.randint(5, 9)]] )
    Haunted_Forest = Location("Haunted Forest", [riddles[random.randint(10, 14)]])
    Graveyard = Location("Graveyard", [riddles[random.randint(15, 19)]])

    #Define connections:

    Dark_Village.add_neighbor("north", Dracula_Castle)
    Dracula_Castle.add_neighbor("south", Dark_Village)
    Dracula_Castle.add_neighbor("west", Haunted_Forest)              #Direction are like: ##graveyard    # MAYBE LATER I WILL LET THE HERO FIND A TELEPORTATION DEVICE TO MOVE BETWEEN LOCATIONS.
    Haunted_Forest.add_neighbor("east", Dracula_Castle)                                       # ^             
    Haunted_Forest.add_neighbor("north", Graveyard)                                           #H.F   <   #D.C 
    Graveyard.add_neighbor("south", Haunted_Forest)                                                      #^                        
                                                                                                         #D.V
    
    #Create hero and start in his current village:
    hero_name = input('Enter the name of your hero: ')
    hero = Hero(hero_name)


    #initial location:
    Hero_village = Location("Hero's Village", [])
    Hero_village.add_neighbor("north", Dark_Village)

    hero.location = Hero_village

        # Inform the user of their current location
    print(f"{hero.name}, your journey begins in your home village.")
    print("Your mom needs the cure for her illness.")
    print(f"Are you ready {hero.name} to gather the 4 keys to unlock the cure for your mom's illness?")
    print(f"Well Safe travels! {hero.name}!")                                                                                


setup_game()


