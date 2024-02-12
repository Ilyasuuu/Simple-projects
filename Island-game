#You're stranded on a mysterious island after a shipwreck.
#The goal is to explore the island, solve riddles, 
from datetime import datetime




island_areas =  {
    "beach": {
        "description": "A sandy beach with a beautiful view of the ocean.",
        "north": "forest", },
        # other directions maybe later
    
    "forest": {
        "description": "A dense forest with tall trees and hidden paths.",
        "south": "beach",
        "west": "cave", },
        # other directions maybe later
    
    "cave": {
        "description": "A dark, mysterious cave. It looks like it holds many secrets.",
        "east": "forest", }
                }
        # other directions maybe later 
#i want to add a riddle to the each island area for example riddle1 for the beach ...
riddles = { 
        "beach" : {"question": "I am tall when I am young, and I am short when I am old. What am I?", "answer": "candle" },
        
        "forest" : {"question": "What can you break, even if you never pick it up or touch it?", "answer": "promise"},

        "cave" : {"question": "What can’t talk but will reply when spoken to?", "answer": "echo"}
        }




current_location = "beach" # starting location
inventory = [riddle['answer'][0] for riddle in riddles.values()]

# Print an intro message to the player:
print("You can type 'go north' or 'go south' or 'go west' or 'go east' to move around the island.")
print("\nIf you type a direction and it says unvalid it means that you can't go that way.")
print("\nBut keep trying new directions and you'll find your way around.")
print("\nDuring your navigation you will find riddles, you can check your inventory for a hint.")
print("\nBut the hints you will see, only one letter which is the first letter of the answer is right.")
print("\nYour current location is: " + current_location)



# Main game loop:

while True:
    # Time Check
    current_time = datetime.now()
    hour = current_time.hour

    # Check if it's daylight (7 AM to 6 PM) or dark (6 PM to 7 AM)
    if 7 <= hour < 18:
        print("\nIt's daylight. You can explore the island.")
    else:
        print("It's dark. It might be safer to take shelter.")

    print(island_areas[current_location]["description"])
    command = input(">").lower().strip()

    direction = command.split()[1] if "go" in command and len(command.split()) > 1 else command

    if direction in island_areas[current_location]:
        next_location = island_areas[current_location][direction]
        if next_location in riddles:
            while True:
                print("Do you want to check your inventory for a hint? (yes/no)")
                if input(">").lower().strip() == "yes":
                    print("Inventory:", inventory)
                print(riddles[next_location]["question"])
                answer = input("Answer: ").lower().strip()
                if answer == riddles[next_location]["answer"]:
                    print("That's correct!")
                    current_location = next_location
                    break
                else:
                    print("That's not right. Try again.")
        else:
            current_location = next_location
    else:
        print("Unvalid direction.")  










    