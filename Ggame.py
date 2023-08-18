import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Initialize the number of attempts made to 0
attempts = 0

# Ask for user's name
name = input("Hello! What's your name? ")

# Loop for 5 attempts
while attempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < 1:
        print("Too low!")
    elif guess > 10:
        print("Too high!")
    elif guess == target_number:
        print("Congratulations, {}! You guessed correctly.".format(name))
        break

# Print the result if the user failed to guess correctly in 5 attempts
if attempts == 5 and guess != target_number:
    print("Sorry, {}, you were not able to guess correctly.".format(name))
