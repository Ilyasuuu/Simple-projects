def start_game():
    print("Welcome to the game")
    name = input("what is your name , adventurer? :")
    print(f"Let the adventure begin, {name}!")
    choose_path()

def encounter_treasure():
    print("You've encountered a treasure full of diamonds")

def encounter_monster():
    print("You've encountered a friendly dragon")    

def choose_path():
    path = input("You are in crossroad. Would you like to go left or right? (left/right): ")
    if path == 'left':
        encounter_treasure()
    elif path == 'right':
        encounter_monster()
    else:
        print("Please enter a valid direction, Try again")
        choose_path() #Recusrion to restart the choice


start_game()
choose_path()        