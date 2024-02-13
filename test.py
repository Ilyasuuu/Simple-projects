class Character:

    def __init__(self, name, health, strength):
        self.__name = name # i will apply encapsulation # private attribute # also This is done by prefixing the attribute name with two underscores (__). Private attributes are not accessible from outside the class, which protects the class's internal state.
        self.__health = health
        self.__strength = strength
        self.inventory = Inventory() #Composition
        #Getter and Setter Methods: To access or modify private attributes.
    def get_health(self):
        return self.__health
    
    def set_health(self, value):
        if value >= 0:
            self.__health = value
        else:
            print("Health cannot be  negative")        
    #
    def get_name(self):
        return self.__name
    #
    def get_strength(self):
        return self.__strength
    def set_strength(self, value):
        if value >= 0:
            self.__strength = value
        else:
            print("Health cannot be  negative")    

    
    #
    def attack(self):
        print(f"{self.__name} is attacking!")

    def defend(self):
        print(f"{self.__name} is defending!")


    def choose_action(self):
        action = input("What should the hero do? (attack/defend): ")
        if action.lower() == "attack":
            self.attack()
        elif action.lower() == "defend":
            self.defend()
        else:
            print("Unknown action. Please choose 'attack' or 'defend'.")
            return self.choose_action()
# We'll make the combat turn-based, where the hero and the monster take turns to perform actions. This introduces the concept of state management within objects.    
    def take_damage(self, damage):
        self.__health -= 20 
        print(f"{self.__name} had taken {20} damage and has {self.__health} health left.")   

class Inventory: #Composition another concept of OOP,  where a class is composed of one or more objects from other classes, indicating a "has-a" relationship. This is useful for creating complex objects that are made up of other objects.
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)




class Monster:
    def __init__(self, name, health, strength):
        
        self.__name = name
        self.__health = health
        self.__strength = strength
    #
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    def set_health(self, value):
        if value >= 0:
            self.__health = value
        else:
            print("Health cannot be  negative")  

    def get_strength(self):
        return self.__strength
    def set_strength(self, value):
        if value >= 0:
            self.__strength = value
        else:
            print("Health cannot be  negative")      


    #     
    def attack(self):
        print(f"{self.__name} is pushing!")
    
    def scream(self):  
        print(f"{self.__name} is so loud!")

    
    def choose_action(self):          
        action = input("what do you want the monster to do? (attack/scream): ")
        if action.lower() == "attack":
            self.attack()
        elif action.lower() == "scream":
            self.scream()
        else:
            print("Unknown action. Please choose 'attack' or 'scream'.")
            return self.choose_action()

    def take_damage(self, damage):
        self.__health -= 50
        print(f"{self.__name} has taken {50} damage and has {self.__health} health left.")


# inheritance : The Wizard class inherits all attributes and methods from Character but also adds a new method, cast_spell.
# Polymorphism: allows objects of different classes to be treated as objects of a common superclass. maybe i will override a the existing method by a new one
class Wizard(Character):
    def cast_spell(self):
        print(f"{self.get_name()} casts a powerful spell ")
    
    def attack(self):
        self.cast_spell() # ovverides the attack method
class Final_Boss(Monster):
    def cast_spell(self):
        print(f"{self.get_name()} casts a cursing spell ") #lol  

    def attack(self):
        self.cast_spell()

# For simplicity, let's assume each attack action reduces the opponent's health by a fixed amount. We'll simulate a round of combat to illustrate the concept.

def simulate_combat(hero, monster):
    turn = 0  # Even numbers for hero's turn, odd for monster's turn
    while hero.get_health() > 0 and monster.get_health() > 0:
        if turn % 2 == 0:  # Hero's turn
            print(f"\n{hero.get_name()}'s turn:")
            hero_action = hero.choose_action()
            if hero_action == "attack":
                monster.take_damage(hero.get_strength())
                print(f"{monster.get_name()} has {monster.get_health()} health left.")
        else:  # Monster's turn
            print(f"{monster.get_name()}'s turn:")
            monster_action = monster.choose_action()
            if monster_action == "attack":
                 hero.take_damage(monster.get_strength())
                 print(f"{hero.get_name()} has {hero.get_health()} health left")
                
        turn += 1

    # Determine winner
    if hero.get_health() > 0:
        print(f"\n{hero.get_name()} has triumphed!")
    else:
        print(f"\n{monster.get_name()} has won!")


# changing the instance to the wizard class # if i don't there is no overriding.
hero = Wizard('Ilyas', 100, 50)
monster = Final_Boss('Zac', 200, 100)
simulate_combat(hero, monster)

#hero_action = hero.choose_action()
#monster_action = monster.choose_action()

