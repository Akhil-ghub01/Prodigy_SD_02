import random

def guessing_game():
    target = random.randint(1, 100) 
    attempts = 0  
    print("Guessing Game")
    print("Enter a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter the guess: ")) 
            attempts += 1  

            if guess < target:
                print("Guessed number is lower than the target! Try again.")
            elif guess > target:
                print("Guessed number is higher than the target! Try again.")
            else:
                print(f"Congratulations! You have guessed the number {target}.")
                print(f"It took you {attempts} attempts.")
                break  
        except ValueError:
            print("Enter a valid integer")

guessing_game()
