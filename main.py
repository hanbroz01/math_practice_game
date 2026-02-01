"""
# ----------------------------
# 🧮 Math Practice Game
# ----------------------------

- Players practice Addition, Subtraction, and Multiplication.
- Generates random math questions with input validation.
- Tracks scores and maintains a high score across sessions.
- Provides immediate feedback and multiple questions per round.

Demonstrates basic Python programming: loops, conditionals, 
functions, user input handling, file reading/writing, and randomization.
"""

import random

# Settings (change these in the code)
MAX_NUMBER_ADD = 20       # Maximum number for addition problems
MAX_NUMBER_SUB = 15       # Maximum number for subtraction problems
MAX_NUMBER_MUL = 10       # Maximum number for multiplication problems
NUM_QUESTIONS = 10        # Number of questions per game session


# Welcome message
print("\nWelcome to the Math Practice Program!\n") 
print("You can practice Addition (+), Subtraction (-), or Multiplication (x)\n")


try: 
    # Try to open the scores file to read previous high scores
    with open("scores.txt", "r") as f:
        scores = f.readlines()  # read all lines into a list
        if scores:  # check if the file is not empty
            # Extract the numerical score from each line and find the maximum
            high_score = max(int(line.split()[0]) for line in scores)
            print(f"Previous high score: {high_score}/{NUM_QUESTIONS}\n")
        else:
            # File exists but empty, start with 0
            high_score = 0
except FileNotFoundError:
    # If the file doesn't exist yet, start with 0
    high_score = 0
    print("No previous score has been recorded. Let's start fresh!\n")



while True:
    # keep looping until user gives valid input
    while True:   
        operation = input("Which operation would you like to practice?\n" # User chooses operation
                        "Press 1 for Addition\n"
                        "Press 2 for Subtraction\n"
                        "Press 3 for Multiplication\n"
        ) 
        if operation in ["1", "2", "3"]:
            break #exits loop if user enters valid input
        else:
            print("Invalid choice. Please enter either 1, 2, or 3 to begin.\n")

    score = 0

    for i in range(NUM_QUESTIONS):
        
        #defines the max numbers for each operation
        if operation == "1":    
            max_num = MAX_NUMBER_ADD #Addition
        elif operation == "2":
            max_num = MAX_NUMBER_SUB #substraction
        elif operation == "3":
            max_num = MAX_NUMBER_MUL #multiplication

        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)

# Handle subtraction to avoid negative answers
        if operation == "2":
            if num1 < num2:
                num1, num2 = num2, num1
            correct_answer = num1 - num2
            question = f"{num1} - {num2} = ? "
        elif operation == "1":
            correct_answer = num1 + num2
            question = f"{num1} + {num2} = ? "
        elif operation == "3":
            correct_answer = num1 * num2
            question = f"{num1} x {num2} = ? "

        while True: #keep looking till user enters a number
            try: 
                user_answer = int(input(question)) # Ask user for answer
                break
            except ValueError:
                print("Please enter numbers only. Letters are not excepted.")

        # Check answer
        if user_answer == correct_answer:
            score += 1
            print("Correct! \n")
            print(f"Your score is now: {score}\n")
            print(f"Question {i+1} of {NUM_QUESTIONS}\n")

        else:
            print(f"Oops! The correct answer was {correct_answer} \n")
            print(f"Your current score: {score}\n")

        print(f"Question {i+1} of {NUM_QUESTIONS}\n")

    # Final score
    print(f"You got {score} out of {NUM_QUESTIONS} correct! \n")
    print("Thanks for practicing!")

    if score > high_score:
        high_score = score
        print(f"New High Score: {high_score}/{NUM_QUESTIONS}!\n")
    else:
        print(f"Current High Score: {high_score}/{NUM_QUESTIONS}!\n")

    # Update the scores file with the new high score
    # 'w' mode overwrites the file with the latest high score
    with open("scores.txt", "w") as f:  
        f.write(f"{high_score} out of {NUM_QUESTIONS}\n")              

    while True:
        user_input = input("Do you want to keep practising?\n"
            "Type Yes to continue.\n" 
            "Type No to exit game.\n"
            ).upper()

        if user_input in ["YES", "Y"]:
                print("Great! Let's start a new round.\n")
                break #breaks to main loop
        elif user_input in ["NO", "N"]:
            print("Thanks for playing! See you next time!")
            print(f"Current High Score: {high_score}/{NUM_QUESTIONS}!\n")
            exit() #exits game 
        else:
            print("Please type Yes or No.\n")                        
        