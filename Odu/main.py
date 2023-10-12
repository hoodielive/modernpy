import random

# Load the statements from the text file into a list
with open('odus.txt', 'r') as file:
    statements = file.readlines()

# Shuffle the statements randomly
random.shuffle(statements)

# Main quiz loop
for statement in statements:
    # Split the statement and Odu information
    parts = statement.strip().split('-')
    statement_text = parts[0].strip()
    correct_odu = parts[1].strip()
    
    # Display the statement to the user
    print("\nStatement:")
    print(statement_text)
    
    # Prompt the user to enter the correct Odu
    user_input = input("Enter the correct Odu: ").strip()
    
    # Check if the user's input matches the correct Odu
    if user_input == correct_odu:
        print("Correct!\n")
    else:
        print(f"Wrong. The correct Odu is {correct_odu}\n")

print("Quiz completed!")

