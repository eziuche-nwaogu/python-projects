import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Ask for user's name
name = input("Hello! What's your name? ")

# Initialize the number of attempts made and a list to store the guesses
attempts = 0
guesses = []

# Loop for 5 attempts
while attempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))

    # Calculate remaining attempts

    if guess < 1:
        print("Too low!")
    if guess > 10:
        print("Too high!")
    if guess == target_number:
        print("Congratulations, {}! You guessed correctly.".format(name))
        break

    attempts += 1
    tries_left = 5 - attempts
    guesses.append(guess)

    if tries_left > 0:
        print("Incorrect guess! Tries left: {}".format(tries_left))

# Print the result if the user failed to guess correctly in 5 attempts
if attempts == 5 and guess != target_number:
    print("Sorry, {}. You were not able to guess the correct number.".format(name))

# Print the record of attempts made
print("Record of attempts: ", guesses)


# import random

# number = random.randint(1, 10)

# player_name = input("Hello, What's your name? ")
# number_of_guesses = 0
# print("Okey! " + player_name + " I am guessing a number between 1 and 10:")

# while number_of_guesses < 5:
#     guess = int(input("Enter the number here: "))
#     number_of_guesses += 1

#     if guess < number:
#         print("Your guess is too low")
#     if guess > number:
#         print("Your guess is too high")
#     if guess == number:
#         break

# if guess == number:
#     print("You guessed the number in " + str(number_of_guesses) + " tries!")
# else:
#     print("You did not guess the number, The number was " + str(number))
