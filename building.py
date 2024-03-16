





import csv
import random

def load_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)    
        riddles = [(row[0], row[1]) for row in csv_reader if len(row) >= 2]
    return riddles
    
# Assuming 'riddles.csv' is structured correctly and available
riddles = load_file('riddles.csv')

class Player:
    def __init__(self, name):
        self.name = name
        self.floor = 1
        self.room = 1
        self.key = []
    
    def move_to_next_room(self):
        self.room += 1  # Always increment the room number
        
        # Calculate the current floor based on the room number
        # Assuming there are 5 rooms per floor
        self.floor = (self.room - 1) // 5 + 1
        
        if self.room % 5 == 1:
            self.add_key(f"key {self.floor - 1}")  # Example: key1, key2, key3, key4, key5
            print(f"Welcome to floor {self.floor}! Moved to room {self.room}.")
        else:
            print(f"Moved to room {self.room} on floor {self.floor}.")
            
        
        


    def add_key(self, key):
        self.key.append(key)
        print(f" You got your: {key}.")

class Game:
    def __init__(self, player_name, riddles):
        self.player = Player(name=player_name)
        self.riddles = riddles
        self.score = 0
        self.mistakes = 0
    

    def start(self):    
        print(f"Welcome {self.player.name}! You're in room {self.player.room} on floor {self.player.floor}.")
            
        while self.player.room <= 20:  # Keep playing until all rooms are completed
            print(f"Entering room {self.player.room}...")
            self.solve_riddles()  # Attempt to solve riddles for the current room
                
                # Check if the game has reached its conclusion
            if self.player.room > 20:
                print("Congratulations! You've escaped the building and won the game!")
                break  # Exit the game loop
            
        else:  # This part runs if the loop completed normally, without a break
            print("Thank you for playing!")

    def select_riddles_for_room(self):
        # Simplified example of selecting 5 unique riddles for the current room
        return random.sample(self.riddles, 5)

    def solve_riddles(self):
    
        room_riddles = self.select_riddles_for_room()
        solved_riddles = 0
            
        for riddle in room_riddles:
            print(f"Riddle: {riddle[0]}")
            player_answer = input("Your answer is: ").strip()

            
            if player_answer.lower() == riddle[1].lower():
                print("Correct answer")
                self.score +=1
                solved_riddles += 1
                if solved_riddles == 5:
                    print("Congratulations! You've solved all riddles in this room.")
                    self.player.move_to_next_room()
                    break        # Move to the next room or floor logic here
            else:
                print('Wrong answer, try again.')
                self.mistakes += 1
                if self.mistakes == 3:
                    self.mistakes = 0  # Reset mistakes for the new set of riddles
                    print("You've made 3 mistakes. Let's try a new set of riddles.")
                    break    # Restart the current room's riddles
            
                           


# Example usage
player_name = "Player1"
game = Game(player_name, riddles)
game.start()
