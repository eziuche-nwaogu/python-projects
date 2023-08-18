import random

number = random.randint(1, 10)

name = input("Hello, What is your name: ")
# initialize for the attempts

attempts = 0

while attempts < 5:
    guess = int(input("Guess a number between 1 and 10!: "))
    # trials_left = 5 - attempts - 1

    attempts += 1

    if guess < 1:
        print("Your guess is too low")
    if guess > 10:
        print("Your guess is too high")
    if guess == number:
        print("Congratulations, {}! You guessed correctly.".format(name))
        break

    if guess == number:
        print("You guessed the number in " + str(number) + " tries!")
else:
    print("You did not guess the number, The number was " + str(number))
