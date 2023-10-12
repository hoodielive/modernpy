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
        statement_parts = statement.strip().split('. ', 1)
        if len(statement_parts) != 2:
            continue

        number, statement_text = statement_parts
        user_answer = input(f"\nStatement {number}:\n{statement_text}\nEnter the correct Odu: ")

        # Extract the Odu from the statement
        correct_odu = statement_text.split('. ')[0]

        if user_answer.strip() == correct_odu:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct Odu is: {correct_odu}")

    print(f"Quiz completed! You got {correct_answers} out of {len(statements)} statements correct.")

if __name__ == "__main__":
    statements = load_statements("statements.txt")
    start_quiz(statements)

