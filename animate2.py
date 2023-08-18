import turtle as T
import random

s = T.Screen()
art = T.Turtle()
art.speed(0)
art.width(0.5)
T.bgcolor("darkmagenta")
art.pencolor("gold")


def shape(angle, side, limit):
    reverseDirection = 500
    art.forward(side)

    if side % (reverseDirection * 2) == 0:
        angle += 2
    elif side % reverseDirection == 0:
        angle -= 2
    art.right(angle)
    side += 2
    if side < limit:
        shape(angle, side, limit)


angle = 179
side = 0
limit = 1000
shape(angle, side, limit)
T.done()
