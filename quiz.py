
# Questions and answers
questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
    {"question": "Which animal is known as the King of the Jungle?", "answer": "Lion"},
    {"question": "What is the boiling point of water (in Celsius)?", "answer": "100"},
]

# Quiz logic
score = 0

print("Welcome to the Quiz!")
print("---------------------")

# Loop through questions
for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.strip().lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")

# Display final score
print(f"\nYou scored {score} out of {len(questions)}.")
