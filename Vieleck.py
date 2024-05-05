from turtle import*

def vieleck(length, corners):
    speed(0)
    for i in range(corners):
        fd(length)
        lt(360/corners)

def rechteck(length, width):
    speed()
    for i in range(2):
        fd(length)
        lt(90)
        fd(width)
        lt(90)