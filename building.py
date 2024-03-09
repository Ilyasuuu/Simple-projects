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




import csv



def load_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)    
        riddles = [(row[0],row[1]) for row in csv_reader]
    return riddles
    
riddles = load_file('riddles.csv')




    
        