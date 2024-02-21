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
    """Represents the game's hero, with a name, inventory, and current location."""
    def __init__(self, name):
        self.name = name
        self.location =  None     #Will be updated to start location.
        self.inventory = []         #Will store keys.


    def add_to_inventory(self, item):
        """Add an item to the hero's inventory."""
        self.inventory.append(item)
        print(f"{item} added to inventory")

    def move(self, direction):
        """Move the hero to a neighboring location in the specified direction."""
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
        """Adds a neighboring location with the associated direction."""
        self.neighbors[direction] = neighbor
        


class Riddle:
    """Represents a single riddle with a question and an answer."""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


#Game Class:
    #The Game class will manage the game state, including the hero, locations, and the game loop.

class Game:
    """Manages the overall game emvironment and state."""

    def __init__(self):
        self.hero = None        #This will be initialized when the game starts.
        self.locations = {}     ##We'll add location here.
        self.riddles = []            
        self.setup_game()    
        


    def setup_game(self):
        """Initializes the game, creating hero, locations, and riddles."""        
        self.create_riddles()
        self.setup_locations()
        self.setup_hero()
        self.setup_connections()
        #Additional game setup will be added here.


    def create_riddles(self):
        """Generates a set of riddles for the game."""
        self.riddles = [Riddle("What has keys but can't open locks?", "A piano"),
                    Riddle("What has a head and a tail, but no body?", "A coin"),
                    Riddle("What has a neck but no head?", "A bottle"),
                    Riddle("What has a thumb and four fingers but is not alive?", "A glove"),
                    Riddle("What has a bottom at the top?", "A leg"),
                    Riddle("What has a ring but no finger?", "A telephone"),
                    Riddle("What has a foot but no legs?", "A snail"),
                    Riddle("What has a heart that doesn't beat?", "A artichoke"),
                    Riddle("What has a bed but never sleeps?", "A river"),
                    Riddle("What has a face that doesn't frown?", "A clock"),]

    #Create locations:
    def setup_locations(self):
        """Create and store game locations."""
        self.locations["Hero's Village"] = Location("Hero's Village", [])
        self.locations["Dark Village"] = Location("Dark Village", [random.choice(self.riddles)])
        self.locations["Dracula's Castle"] = Location("Dracula's Castle", [random.choice(self.riddles)])
        self.locations["Haunted Forest"] = Location("Haunted Forest", [random.choice(self.riddles)])
        self.locations["Graveyard"] = Location("Graveyard", [random.choice(self.riddles)])

    #Define connections:
    def setup_connections(self):
        """Create connections between locations."""
        self.locations["Hero's Village"].add_neighbor("north", self.locations["Dark Village"])
        self.locations["Dark Village"].add_neighbor("north", self.locations["Dracula's Castle"])
        self.locations["Dracula's Castle"].add_neighbor("south", self.locations["Dark Village"])
        self.locations["Dracula's Castle"].add_neighbor("west", self.locations["Haunted Forest"])
        self.locations["Haunted Forest"].add_neighbor("east", self.locations["Dracula's Castle"])
        self.locations["Haunted Forest"].add_neighbor("north", self.locations["Graveyard"])
        self.locations["Graveyard"].add_neighbor("south", self.locations["Haunted Forest"])
                                                                                                            #D.V
    
    #Create hero and start in his current village:
    def setup_hero(self):
        """Create the hero and place him in the starting location."""
        hero_name = input('Enter the name of your hero: ')
        self.hero = Hero(hero_name)
        self.hero.location = self.locations["Hero's Village"] 
        print(f"{self.hero.name}, your journey begins in your home village.")
        print(f"Are you ready {self.hero.name} to gather the 4 keys to unlock the cure for your mom's illness?")
        print(f"Well, Safe travels! {self.hero.name}!")    

    
#test the game:
Game()         


