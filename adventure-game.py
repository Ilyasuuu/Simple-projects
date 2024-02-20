#Step 1: Define the Basic Classes.
#Classes for: HERO, LOCATION, RIDDLE, GAME.

#Why Start Here?

#-Starting with class definitions helps us understand the "blueprint" of our game.
#-It's like planning our LEGO city before we start building it.
#-This ensures we know what pieces we have and how they fit together.

#Hero Class:
    #Our Hero will have attributes like name, location, and inventory, 
    #(to store keys) and methods to move between locations.

class Hero:
    def __init__(self, name):
        self.name = name
        self.location = None        #Will be updated to start location.
        self.inventory = []         #Will store keys.

    def move_to(self, new_location):
        #Update the hero's location.
        self.location = new_location
        print(f"{self.name} moved to {new_location.name}")

    def add_to_inventory(self, item):
        #Add an item to the hero's inventory.
        self.inventory.append(item)
        print(f"{item} added to inventory")


#Location Class:
    #Each location will have a name, description, and a set of riddles.
    #We'll expand this later to include more features like neighboring locations. 

class Location:
    def __init__(self, name, riddles):
        self.name = name
        self.riddles = riddles      #This will be a list of riddle objects.


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