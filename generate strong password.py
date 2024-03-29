#define character sets
#determine password length
#create the pattern
#randomization to enhance security
#Assemble the password


import random
import string

#letters set(upper and lower case)
letters = string.ascii_letters

#numbers set
numbers = string.digits

#special characters set
special_characters = "!@#$%^&*()-_=+[]{};:',.<>/?"


#determine password length
def the_password_length():
    while True:
        try:
            length = int(input("How long do you want your password to be? "))
            if 8 <= length <= 15:
                return length
            else:
                print("Password length must be between 8 and 15 characters")
        except:
            print("Invalid input. Please enter a valid integer.")



def the_generate_password(length):
    password = ""
    for i in range(length):
        if i % 3 == 0:
            # Add a random letter
            password += random.choice(string.ascii_letters)
        elif (i + 2) % 3 == 0:
            # Add a random number
            password += random.choice(string.digits)
        else:
            # Add a random special character
            special_characters = "!@#$%^&*()-_=+[]{};:',.<>/?"
            password += random.choice(special_characters)
    return password

password_length = the_password_length() 
generated_password = the_generate_password(password_length)
print("Generated Password:", generated_password)
