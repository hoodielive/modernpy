import random

# Function to load statements from the file
def load_statements(file_name):
    with open('odus.txt', 'r', encoding='utf-8') as file:
        statements = file.readlines()
    return statements

# Function to start the quiz
def start_quiz(statements):
    random.shuffle(statements)
    correct_answers = 0

    for statement in statements:
        # Split the statement into parts based on the period and a space
        parts = statement.strip().split('. ')
        if len(parts) != 2:
            continue

        # Extract the number and statement text
        number, statement_text = parts

        # Extract the word right after the number and period
        statement_word = statement_text.split(' ', 1)[0]

        user_answer = input(f"\nStatement:\n{number}. [Hidden] [Hidden] speaks of [Hidden] and [Hidden].\nEnter the correct word (Odu): ")

        if user_answer.strip() == statement_word:
            print("Correct!")
            correct_answers += 1
        else:
            print("Wrong. The correct word (Odu) is hidden.")

    print(f"Quiz completed! You got {correct_answers} out of {len(statements)} words correct.")

if __name__ == "__main__":
    statements = load_statements("odus.txt")
    start_quiz(statements)

