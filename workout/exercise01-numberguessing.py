from random import randint as rand

# Dry run. cheat

def guessing_game():
    answer = rand(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))
        if user_guess == answer:
            print(f'Right! The answer is {user_guess} ')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is to low! ')
        else:
            print(f'Your guess of {user_guess} is too high! ')

guessing_game()
