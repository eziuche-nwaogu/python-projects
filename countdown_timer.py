import time


def countdown():
    timer = int(input("Enter the time in seconds: "))
    while timer:
        mins, secs = divmod(timer, 60)
        count = "{:02d}:{:02d}".format(mins, secs)
        print(count, end="\r")
        timer -= 1
        time.sleep(1)
    print("Countdown finished")


countdown()
