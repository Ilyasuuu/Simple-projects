# generate a random number between 1 and 100
# and ask the user to guess it
# if the user guesses the number, tell them they're right
# if the user guesses wrong, tell them if they're too high or too low
# and let them guess again


import random


print("Welcome to the game where you have to guess the right number between 1 and 10000")


# Generate a random number between 1 and 100
secret_number = random.randint(1, 10000)

player_guess = None

while player_guess != secret_number:
    user_input = input('Guess the number between 1 and 10000: ')
    
    # Attempt to convert the user input to an integer
    try:
        player_guess = int(user_input)
        
        # Check if the guess is correct, too high, or too low
        if player_guess == secret_number:
            print(f'{player_guess} is Correct! Congratulations!')
        elif player_guess < secret_number:
            print('Too low. Try again.')
        else:
            print('Too high. Try again.')
            
    except ValueError:
        # Handle the case where the input is not a number
        print('Please enter a valid number.')
