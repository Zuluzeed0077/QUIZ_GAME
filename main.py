import random
from questions import QUIZ_QUESTIONS

contestant_1 = input("Enter the name of contestant 1: ")
while contestant_1 == "":
    print("Invalid input. Please enter a valid name for contestant 1.")
    contestant_1 = input("Enter the name of contestant 1: ")
contestant_2 = input("Enter the name of contestant 2: ")
while contestant_2 == "":
    print("Invalid input. Please enter a valid name for contestant 2.")
    contestant_2 = input("Enter the name of contestant 2: ")

print(f"\nWelcome {contestant_1} and {contestant_2} to the competition!")
print("Let's start the quiz!\n")

scores = {contestant_1: 0, contestant_2: 0}

# Alternate questions so each contestant gets different questions
random.shuffle(QUIZ_QUESTIONS)
for idx, question in enumerate(QUIZ_QUESTIONS):
    current = contestant_1 if idx % 2 == 0 else contestant_2
    print(f"Question {question['id']} for {current}: {question['question']}")
    for option in question["options"]:
        print(option)

    answer = input(f"\n{current}, enter your answer (A/B/C/D): ").upper().strip()
    while True:
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
    for question in QUIZ_QUESTIONS:
        optionss = [option[3:] for option in question["options"]]
        option_shuffle = []
        for option in optionss:
            option_shuffle.append(option)
        for question in QUIZ_QUESTIONS:
            

            
    if answer == question["answer"].strip():
        print("Correct!👍\n")
        scores[current] += 1
    else:
        print(f"Wrong!👎 The correct answer was {question['answer']}.\n")

print("Final scores:")
print(f"{contestant_1}: {scores[contestant_1]} points")
print(f"{contestant_2}: {scores[contestant_2]} points")

if scores[contestant_1] > scores[contestant_2]:
    print(f"Winner: {contestant_1}!")
elif scores[contestant_2] > scores[contestant_1]:
    print(f"Winner: {contestant_2}!")
else:
    print("It's a tie!")
