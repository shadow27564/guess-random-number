import random
print("Welcome to the random number guessing game")
secret_number=random.randint(1,20)
attempts = 20

while True:
    guess= input("Guess a number between 1 and 20:")

    if not guess.isdigit():
        print("Please enter a valid number that is between 1 and 20")
        continue

    guess = int(guess)
    attempts +=1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} tries")
        break
    elif guess < secret_number:
        print("Too low. Try again")
    else:
        print("Too high. Try again")