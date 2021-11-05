# TurtleDrawing 
# Reading a text file line by line.
# 
# By: Angelo Goduto
#
# All rights reserved

import turtle
import math

TEXTFILENAME = 'turtle-draw.txt'

turtleBoarder = turtle.Screen()
turtleBoarder.setup(450, 450)

# Todo: Ask user for the file name.

print('TurtleDraw')

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()


print('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

totalDistance = 0
previousPoint = [0, 0]
# currentPoint = [1, 1]
# print (math.dist(previousPoint, currentPoint))
# input("\nPress 'enter' to close Application...")


while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        currentPoint = [x, y]
        totalDistance = totalDistance + math.dist(previousPoint,currentPoint)
        print(math.dist(previousPoint, currentPoint))
        print(previousPoint)
        print(currentPoint)
        print('Total Distance=' + str(totalDistance))

        # Todo: Find total distance when Pen is Down. Only when pen is down, add distance to total
        
        previousPoint = currentPoint

        turtleDraw.color(color)
        turtleDraw.goto(x,y)

        turtleDraw.pendown()

# Todo: Total Distance Outdside of loop

    if (len(parts) == 1):
        turtleDraw.penup()

    line = turtleDrawTextfile.readline()

# Todo: Print the total near the bottom
turtle.done()

input("\nPress 'enter' to close Application...")
turtleDrawTextfile.close()

print('\nEnd')