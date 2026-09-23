from questions import QUIZ_QUESTIONS

contestant_1 = input("Enter the name of contestant 1: ")
contestant_2 = input("Enter the name of contestant 2: ")

print(f"\nWelcome {contestant_1} and {contestant_2} to the competition!")
print("Let's start the quiz!\n")

scores = {contestant_1: 0, contestant_2: 0}

# Alternate questions so each contestant gets different questions
for idx, question in enumerate(QUIZ_QUESTIONS):
    current = contestant_1 if idx % 2 == 0 else contestant_2
    print(f"Question {question['id']} for {current}: {question['question']}")
    for option in question["options"]:
        print(option)

    answer = input(f"\n{current}, enter your answer (A/B/C/D): ").upper().strip()
    if answer == question["answer"].upper():
        print("Correct!\n")
        scores[current] += 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.\n")

print("Final scores:")
print(f"{contestant_1}: {scores[contestant_1]} points")
print(f"{contestant_2}: {scores[contestant_2]} points")

if scores[contestant_1] > scores[contestant_2]:
    print(f"Winner: {contestant_1}!")
elif scores[contestant_2] > scores[contestant_1]:
    print(f"Winner: {contestant_2}!")
else:
    print("It's a tie!")