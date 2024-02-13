class Character:

    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        print(f"{self.name} is attacking!")

    def defend(self):
        print(f"{self.name} is defending!")


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
        self.health -= damage 
        print(f"{self.name} had taken {damage} damage and has {self.health} health left.")   


class Monster:
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        print(f"{self.name} is pushing!")
    
    def scream(self):  
        print(f"{self.name} is so loud!")

    
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
        self.health -= damage
        print(f"{self.name} has taken {damage} damage and has {self.health} health left.")        

# For simplicity, let's assume each attack action reduces the opponent's health by a fixed amount. We'll simulate a round of combat to illustrate the concept.

def simulate_combat(hero, monster):
    turn = 0  # Even numbers for hero's turn, odd for monster's turn
    while hero.health > 0 and monster.health > 0:
        if turn % 2 == 0:  # Hero's turn
            print("\nHero's turn:")
            hero_action = hero.choose_action()
            if hero_action == "attack":
                monster.take_damage(hero.strength)
        else:  # Monster's turn
            print("\nMonster's turn:")
            monster_action = monster.choose_action()
            if monster_action == "attack":
                hero.take_damage(monster.strength)
                
        turn += 1

    # Determine winner
    if hero.health > 0:
        print("\nThe hero has triumphed!")
    else:
        print("\nThe monster has won!")



hero = Character('Ilyas', 100, 50)
monster = Monster('Zac', 200, 100)

simulate_combat(hero, monster)
hero_action = hero.choose_action()
monster_action = monster.choose_action()

