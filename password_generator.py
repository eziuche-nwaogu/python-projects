import random


def passwds():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\()''*+,-./:;<=>?@[]^_`{|}~"
    number = int(input("Enter the number of passwords you want to be generated: "))
    lenght = int(input("Enter your desired passowrd lenght: "))
    for i in range(number):
        passwords = ""
        for j in range(lenght):
            passwords += random.choice(chars)
        print(passwords)


passwds()
