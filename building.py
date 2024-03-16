import csv
import random

class Game:
    MAX_ROOMS = 20
    ROOMS_PER_FLOOR = 5
    
    def __init__(self, player_name, filename='riddles.csv'):
        self.player = Player(player_name)
        self.riddles = self.load_file(filename)
        self.current_riddles = []
        self.score = 0
        self.mistakes = 0
    
    def load_file(self, filename):
        with open(filename, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)    
            return [(row[0], row[1]) for row in csv_reader if len(row) >= 2]

    def start(self):
        print(f"Welcome {self.player.name}! You're starting your adventure.")
        while self.player.room <= Game.MAX_ROOMS:
            if not self.current_riddles:
                self.current_riddles = self.select_riddles_for_room()
            self.solve_riddles()
            
            if self.player.room > Game.MAX_ROOMS:
                print("Congratulations! You've escaped the building and won the game!")
                break

    def select_riddles_for_room(self):
        return random.sample(self.riddles, 5)

    def solve_riddles(self):
        # Optimized riddle-solving logic
        room_riddles = self.select_riddles_for_room()
        solved_riddles = 0
            
        for riddle in room_riddles:
            print(f"Riddle: {riddle[0]}")
            player_answer = input("Your answer is: ").strip()

            
            if player_answer.lower() == riddle[1].lower():
                print("Correct answer")
                solved_riddles += 1
                if solved_riddles == 5:
                    print("Congratulations! You've solved all riddles in this room.")
                    self.player.move_to_next_room()
                    break        # Move to the next room or floor logic here
            else:
                print('Wrong answer, try again.')
                self.score += 1
                self.mistakes += 1
                if self.mistakes == 3:
                    self.mistakes = 0  # Reset mistakes for the new set of riddles
                    print("You've made 3 mistakes. Let's try a new set of riddles.")
                    break    # Restart the current room's riddles


class Player:
    def __init__(self, name):
        self.name = name
        self.floor = 1
        self.room = 1
        self.keys = []

    def move_to_next_room(self):
        self.room += 1
        self.floor = (self.room - 1) // Game.ROOMS_PER_FLOOR + 1
        print(f"Moved to room {self.room} on floor {self.floor}.")
        if self.room % Game.ROOMS_PER_FLOOR == 1:
            print(f"Welcome to floor {self.floor}!")

    def add_key(self):
        self.keys.append(f"Key for room {self.room}")
        print(f" You got a key for room {self.room}.")

# Example usage
game = Game("Player1")
game.start()
