import time
import random

# New set of questions and multiple-choice answers
questions = [
    "What is the capital city of France?",
    "Who wrote 'Hamlet'?",
    "What is the chemical symbol for gold?",
    "Which planet is known as the Red Planet?",
    "In what year did the Titanic sink?",
    "What is the largest mammal in the world?",
    "Who painted the Mona Lisa?",
    "What is the hardest natural substance on Earth?",
    "Who is known as the father of computer science?",
    "What is the smallest prime number?"
]

options = {
    0: ["Paris", "Berlin", "Madrid", "Rome"],
    1: ["William Shakespeare", "Charles Dickens", "Leo Tolstoy", "Mark Twain"],
    2: ["Au", "Ag", "Fe", "O"],
    3: ["Earth", "Mars", "Jupiter", "Venus"],
    4: ["1912", "1905", "1898", "1923"],
    5: ["Blue Whale", "African Elephant", "Giraffe", "Great White Shark"],
    6: ["Vincent Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
    7: ["Diamond", "Gold", "Iron", "Quartz"],
    8: ["Alan Turing", "Thomas Edison", "Albert Einstein", "Nikola Tesla"],
    9: ["1", "2", "3", "5"]
}

correct_answers = {
    0: "Paris",
    1: "William Shakespeare",
    2: "Au",
    3: "Mars",
    4: "1912",
    5: "Blue Whale",
    6: "Leonardo da Vinci",
    7: "Diamond",
    8: "Alan Turing",
    9: "2"
}

def quiz_game():
    score = 0
    question_indices = list(range(len(questions)))
    random.shuffle(question_indices)

    for index in question_indices:
        print(f"Question: {questions[index]}")
        for i, option in enumerate(options[index]):
            print(f"{i + 1}. {option}")
        
        answer = input("Enter the number of your answer: ")

        try:
            if options[index][int(answer) - 1] == correct_answers[index]:
                print("Correct!")
                score += 10
            else:
                print("Incorrect.")
        except (IndexError, ValueError):
            print("Invalid response. No points awarded.")

    print(f"Your final score is {score}.")
    print("Thanks for playing!")

quiz_game()  
