#building game
#the player can move around 4 floors
#each floor has 5 rooms and each room has five riddles
#get the key if answer them correctly      #3 mistake lead to restart the game and the room riddle change everytime
#unlock at least 3 rooms to go to the next floor
#hints are available            #at first you will be only able to move around the 2 first floors freely unitl you solve at least 6 rooms to move to the 3 floor
#Ability to move freely between the floors if you want to go back and solve the other rooms.
#unlock the roof to escape the building
#time limit for each room
#score system



import random
import csv



def load_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)    
        riddles = [(row[0],row[1]) for row in csv_reader]
    return riddles
    
riddles = load_file('riddles.csv')


class Player:
    def __init__(self, name, floor, room):
        self.name = name
        self.floor = floor
        self.room = room
        self.inventory = []
        
    def move(self, direction):
        if direction == "left":
            if self.room > 1:
                self.room -= 1    
            else:
                print("You can't go left from here this is the first room.")
        elif direction == "right":
            if self.room < 6:
                self.room += 1
            else:
                print("No more rooms in this floor for now.")
        elif direction == "up":
            if self.floor < 4:
                self.floor += 1
            else:
                print("You didn't unlock the roof yet.")    
        elif direction == "down":
            if self.floor > 1:
                self.floor -= 1
            else:
                print("You are already in the first floor.")      

    def inventory(self, key):
        self.inventory.append(key)
        print(f"You got the key for the room {self.room} in the floor {self.floor}.")

class Game:
    def __init__(self, player, riddles):
        self.player = Player(name = player, floor = 1, room = 1)
        self.riddles = riddles
        self.score = 0
        self.hints = 3               #3 hints for each roon                                     
        self.mistakes = 0

    def solve_riddles(self):
        current_riddle = random.choice(self.riddles)
        print(f"Riddle : {current_riddle[0]}")
        player_answer = input("Your answer is :")

        if player_answer.lower() == current_riddle[1].lower():
            print("Correct answer, you got the key.")
            self.score += 1
        else:
            print('Wrong answer, try again.')
            self.mistakes += 1    







    def start(self):
        print("Welcome to the building game, you are in the first floor in the first room.")
        while True:
            if 
            
