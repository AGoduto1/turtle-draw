# TurtleDrawing 
# Reading a text file line by line.
# 
# By: Angelo Goduto
#
# All rights reserved

import turtle
import math

TEXTFILENAME = 'turtle-draw.txt'

turtleScreen = turtle.Screen()
turtleScreen.setup(450, 450)

# Todo: Ask user for the file name.

print('TurtleDraw')

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()


print('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw.color(color)
        turtleDraw.goto(x,y)

        turtleDraw.pendown()

    if (len(parts) == 1):
        turtleDraw.penup()

    line = turtleDrawTextfile.readline()

# I think I'm right there for this problem, I just can't seem to figure out what to put so it grabs from the text file.
    # turtleDistance = math.dist(x, y)
    # print(turtleDistance)

# Todo: Print the total near the bottom
turtle.done()

input("\nPress 'enter' to close Application...")
turtleDrawTextfile.close()

print('\nEnd')