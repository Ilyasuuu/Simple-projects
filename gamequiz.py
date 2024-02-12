#Create a text-based quiz game in Python 
#The user guesses the name of an anime character based on a series of hints.
#The user has 3 guesses for each question.
#The program will keep track of the score and at the end print out the final score.
#The program will also keep track of the time it took to complete the quiz.
#keep track of the number of attempts and provide feedback to the user.
#Assign points to each question. The harder the question, the more points it is worth.
#the score will depend on the number of hints used.
#move to the next question when the time is up.
#We will use a loop to go through each question in the quiz.
#Ensure the game ends after the last question.
#We will use a list to store the questions and answers.
#We will use a dictionary to store the points for each question.
#We will use a dictionary to store the number of attempts for each question.
#We will use a dictionary to store the feedback for each question.
#We will use a dictionary to store the number of hints used for each question.

import time
import random 



# List of question identifiers
questions = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", 
             "Question 6", "Question 7", "Question 8", "Question 9", "Question 10"]

# Full text of each question
question_text = {
    "Question 1": "Who is the captain of the Straw Hat Pirates?",
    "Question 2": "What is the name of Monkey D. Luffy's signature attack?",
    "Question 3": "What is the name of the world government organization in One Piece?",
    "Question 4": "Which island is known as the 'Pirate Island' in the One Piece world?",
    "Question 5": "Who is the archaeologist and historian on the Straw Hat Pirates crew?",
    "Question 6": "What is the name of Roronoa Zoro's unique sword style?",
    "Question 7": "Who is known as the 'Thousand Sunny's' shipwright?",
    "Question 8": "What is the name of the Devil Fruit that grants the ability to create earthquakes?",
    "Question 9": "What is the name of the Pirate Empress who is known for her beauty and strength?",
    "Question 10": "What is last island in the Grand Line called?"
}

# Dictionary of answers
answers = {
    "Question 1": "Monkey D. Luffy",
    "Question 2": "Gomu Gomu no Pistol",
    "Question 3": "World Government",
    "Question 4": "Sabaody Archipelago",
    "Question 5": "Nico Robin",
    "Question 6": "Santoryu",
    "Question 7": "Franky",
    "Question 8": "Gura Gura no Mi",
    "Question 9": "Boa Hancock",
    "Question 10": "Laugh Tale"
}

# Dictionary of hints
hints = {"Question 1": ["He is the main character of the series."],
         "Question 2": ["It is his fruit + something he used as his first attack."],
         "Question 3": ["It is the name of the government."],
         "Question 4": ["It is the name of the island, it start with s and a for the second."],
         "Question 5": ["She was working with crocodile in the past."],
         "Question 6": ["It is the name of the sword style. Start with an S"],
         "Question 7": ["He is a cyborg."],
         "Question 8": ["It is the name of the fruit. Start with a G"],
         "Question 9": ["She is the leader of the Kuja tribe."],
         "Question 10": ["It is the last island in the Grand Line. Start with an L"],}

# Difficulty settings
difficulty_settings = {
    "medium": {"time_limit": 60, "allowed_guesses": 4, "hint_penalty": 1},
    "hard": {"time_limit": 50, "allowed_guesses": 2, "hint_penalty": 1}
}

# Start the quiz timer
quiz_start_time = time.time()

# User chooses difficulty level


print("Choose a difficulty level: Medium, Hard")
# Loop until a valid input is received
while True:
    difficulty = input().lower()  # Get user input and convert it to lowercase

    # Check if the input is valid
    if difficulty == 'm' or difficulty == 'medium':
        difficulty = 'medium'  # Normalize input to 'medium'
        break  # Exit loop on valid input
    elif difficulty == 'h' or difficulty == 'hard':
        break  # Exit loop on valid input
    else:
        # Prompt the user again on invalid input
        print("Invalid input. Please type 'm' or  'Medium' , 'h' or 'Hard'.")



time_limit = difficulty_settings[difficulty]["time_limit"]
allowed_guesses = difficulty_settings[difficulty]["allowed_guesses"]
hint_penalty = difficulty_settings[difficulty]["hint_penalty"]

# Randomize the order of questions
random.shuffle(questions)

score = 0

# Main quiz loop
for question_id in questions:
    print(question_text[question_id])
    
    available_points = 2
    hint_used = False
    guesses = 0

    while guesses < allowed_guesses:
        user_input = input("Type 'hint' for a hint, 'answer' to answer, or 'skip' to skip: ")

        if user_input.lower() == 'hint' and not hint_used:
            print(hints[question_id])
            hint_used = True
            available_points -= hint_penalty
        elif user_input.lower() == 'answer':
            start_time = time.time()
            user_answer = input("Your answer: ")
            end_time = time.time()

            if end_time - start_time > time_limit:
                print("Time's up!")
                break

            if user_answer.lower() == answers[question_id].lower():
                print("Correct!")
                score += available_points
                break
            else:
                guesses += 1
                print(f"Wrong answer. You have {allowed_guesses - guesses} guesses left.")
        elif user_input.lower() == 'skip':
            print(f"Skipping question. The correct answer was {answers[question_id]}.")
            break
        else:
            print("Invalid input.I think you used your hint, you only had one. Please type 'answer', or 'skip'.")

    if guesses == allowed_guesses:
        print(f"Out of guesses. The correct answer was {answers[question_id]}.")

        
        
#End the quiz
quiz_end_time = time.time()
total_quiz_time = quiz_end_time - quiz_start_time

#calculate and format the total time taken
total_minutes = int(total_quiz_time // 60)
total_seconds = int(total_quiz_time % 60)
time_taken = f"{total_minutes} minutes and {total_seconds} seconds"

#Generating feedback based on the score
feedback = "Great job!" if score > len(questions) * 2 else "Nice try!"
# After all questions, print the final score
print("\nQuiz Summary")
print(f"Your final score is: {score}/{len(questions) * 2}")        
print(f"Total time taken: {time_taken}")
print(feedback)
