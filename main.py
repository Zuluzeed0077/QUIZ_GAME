import random
import string
from questions import QUIZ_QUESTIONS
def welcome_message():
        print(f"\nWelcome {contestant_1} and {contestant_2} to the competition!\n")
        print("Let's start the quiz!\n")
        Question()
   

# Alternate questions so each contestant gets different questions
def Question():
    scores = {contestant_1: 0, contestant_2: 0}

    random.shuffle(QUIZ_QUESTIONS)
    for idx, question in enumerate(QUIZ_QUESTIONS):
        current = contestant_1 if idx % 2 == 0 else contestant_2
        option_shuffle = []
        optionss = [option[3:] for option in question["options"]]
        random.shuffle(optionss)
        print(f"Question {question['id']} for {current}: {question['question']}")
        for idx, option in enumerate(optionss):
            letters = string.ascii_uppercase[idx]
            print(f"{letters}) {option}")

        while True:
            answer = input(f"\n{current}, enter your answer (A/B/C/D): ").upper().strip()
            if answer == "A":
                answer = question["options"][0][3:] # Remove "A) "
                break
            elif answer == "B":
                answer = question["options"][1][3:] # Remove "B) " 
                break
            elif answer == "C":
                answer = question["options"][2][3:] # Remove "C) "
                break
            elif answer == "D":
                answer = question["options"][3][3:] # Remove "D) "
                break
            else:
                print("Invalid option. Please enter A, B, C, or D.") 
                answer = input(f"\n{current}, enter your answer (A/B/C/D): ").upper().strip()

        
        for option in optionss:
            option_shuffle.append(option)
        chosen_index = string.ascii_uppercase.index(answer_letter)
        answer = optionss[chosen_index].strip()
        answer = question["answer"].strip()

        if answer == question["answer"].strip():
            print("Correct!👍\n")
            score_update(scores, current)
        else:
            print(f"Wrong!👎 The correct answer was {question['answer']}.\n")
    score(scores)
 
def score_update(scores, current):
    scores[current] += 1

def score(scores):

    print(f"{contestant_1}: {scores[contestant_1]} points")
    print(f"{contestant_2}: {scores[contestant_2]} points")
    
    if scores[contestant_1] > scores[contestant_2]:
        print(f"Winner: {contestant_1}!")
    elif scores[contestant_2] > scores[contestant_1]:
        print(f"Winner: {contestant_2}!")
    else:
        print("It's a tie!")
        
       

contestant_1 = input("Enter the name of contestant 1: ")
contestant_2 = input("Enter the name of contestant 2: ")
while contestant_1 == "" or  contestant_2 == "":
    print("Invalid input. Please enter a valid name for contestant 1.")
    contestant_1 = input("Enter the name of contestant 1: ")
    print("Invalid input. Please enter a valid name for contestant 2.")
    contestant_2 = input("Enter the name of contestant 2: ")
welcome_message()
