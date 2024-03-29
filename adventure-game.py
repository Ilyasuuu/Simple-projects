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
import time


class Hero:
    """Represents the game's hero, with a name, inventory, and current location."""

    def __init__(self, name):
        self.name = name
        self.location = None             #Will be updated to start location.
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
        self.neighbors = {}
        self.failures = 0           #New attribute for neighboring locations.
        self.lockout_time = None         

    def add_neighbor(self, direction, neighbor):
        """Adds a neighboring location with the associated direction."""
        self.neighbors[direction] = neighbor
        
    def is_locked(self):
        if self.lockout_time and time.time() < self.lockout_time:
            return True
        return False
    
    def lockout(self):
        self.lockout_time = time.time() + 300  # Lockout for 5 minutes

    

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
        self.riddles = [Riddle("What has keys but can't open locks?", "piano"),
                    Riddle("What has a head and a tail, but no body?", "coin"),
                    Riddle("What has a neck but no head?", "bottle"),
                    Riddle("What has a thumb and four fingers but is not alive?", "glove"),
                    Riddle("What has a bottom at the top?", "leg"),
                    Riddle("What has a ring but no finger?", "telephone"),
                    Riddle("What has a foot but no legs?", "snail"),
                    Riddle("What has a heart that doesn't beat?", "artichoke"),
                    Riddle("What has a bed but never sleeps?", "river"),
                    Riddle("What has a face that doesn't frown?", "clock"),]

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
        self.locations["Dark Village"].add_neighbor("south", self.locations["Hero's Village"])
        self.locations["Hero's Village"].add_neighbor("west", self.locations["Dracula's Castle"])
        self.locations["Dracula's Castle"].add_neighbor("east", self.locations["Hero's Village"])
        self.locations["Hero's Village"].add_neighbor("east", self.locations["Haunted Forest"])
        self.locations["Haunted Forest"].add_neighbor("west", self.locations["Hero's Village"])
        self.locations["Hero's Village"].add_neighbor("south", self.locations["Graveyard"])
        self.locations["Graveyard"].add_neighbor("north", self.locations["Hero's Village"])
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

    
    def start(self):
        """Starts the main game loop."""
        while True:
            if self.hero and self.hero.location:
                print("\nCurrent Location:", self.hero.location.name)
                actions = ["move", "inventory", "quit"]
                if self.hero.location.riddles:
                    actions.insert(1, "solve riddle")  # Add solving riddle option if the location has riddles
            else:
                print("Hero or location is not initialized.")

            print("Available actions:", ', '.join(actions))
            action = input("What would you like to do? ").lower().strip()

            if action == "move":
                self.handle_move()
            elif action == "solve riddle":
                self.handle_solve_riddle()    
            elif action == "inventory":
                self.show_inventory()
            elif action == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Not a valid action. Please try again.")
        
    def handle_move(self):
        """Handles the hero's movement from one location to another."""
        if self.hero:
            direction = input("Which direction? [north, south, east, west] ").lower().strip()
            self.hero.move(direction)
        else:
            print("Hero is not initialized.")

    
    
                
    def handle_solve_riddle(self):
        """Handles the logic for solving a riddle at the current location."""    
        if self.hero is None:
            print("Hero is not initialized.")
            return

        location = self.hero.location
        if location is not None and location.is_locked():
            print("This location is temporarily locked. Please wait.")
            return

        correct_answers = 0
        while correct_answers < 5 and location and location.riddles:
            if location is not None and location.riddles:
                riddle = random.choice(location.riddles)
                print(f"Riddle: {riddle.question}")
                answer = input("Your answer: ").strip().lower()

                if answer == riddle.answer.lower():
                    print("Correct!")
                    correct_answers += 1
                    if location is not None:
                        location.riddles.remove(riddle)  # Optionally remove the riddle if it shouldn't be asked again
                else:
                    print("Incorrect.")
                    if location is not None:
                        location.failures += 1
                        if location.failures == 3:
                            print("Too many wrong answers. This location is temporarily locked.")
                            location.lockout()
                            break  # Exit the riddle challenge due to too many failures

            if correct_answers == 5:
                print("Congratulations! You've solved all the riddles in this location.")
                self.hero.inventory.append(location.key)  # Add the key to the hero's inventory
                print(f"You've received the key: {location.key}")
                # Here, you can handle unlocking a new location or awarding the player

        if self.hero and self.hero.location:
            actions = ["move", "inventory", "quit"]
            if self.hero.location.riddles:
                actions.insert(1, "solve riddle")  # Add solving riddle option if the location has riddles
            print("Available actions:", ', '.join(actions))
    
    




                

      

    def show_inventory(self):
        """Displays the hero's current inventory."""
        if self.hero and self.hero.inventory:
            print("Inventory:", ", ".join(self.hero.inventory))
        else:
            print("Your inventory is empty.")

       

game = Game()
game.start()
