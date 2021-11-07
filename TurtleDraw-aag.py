# TurtleDrawing 
# Reading a text file line by line.
# 
# Project: TurtleDrawing
# By: Angelo Goduto
# Email: angeloagoduto@lewisu.edu
#
# All rights reserved

import turtle
import math

TEXTFILENAME = 'turtle-draw.txt'
# input('turtle-draw.txt')
# So I tried using input to make a person select the turtle-draw.txt file but I couldn't
# figure out why it wasn't working

turtleBoarder = turtle.Screen()
turtleBoarder.setup(450, 450) #This helped determine the size of the screen

# Todo: Ask user for the file name.

print('TurtleDraw')

turtleDraw = turtle.Turtle()
turtleDraw.speed(10) # This sped up the turtle drawing
turtleDraw.penup()


print('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
turtleLine = turtleDrawTextfile.readline()

totalDistance = 0 # This was the beginning distance
previousPoint = [0, 0]

while turtleLine:
    print(turtleLine, end='')
    parts = turtleLine.split(' ')

    if (len(parts) == 3):
        color = parts[0] # This reads the first line as a color
        x = int(parts[1]) # This reads the second line as the cordinate for 'X'
        y = int(parts[2]) # This reads the third line as the cordinate for 'y'

        currentPoint = [x, y]
        totalDistance = totalDistance + math.dist(previousPoint,currentPoint)        
        print(math.dist(previousPoint, currentPoint))
        print('Previous Point=' + str(previousPoint))
        print('Current Point=' + str(currentPoint))
        print('Total Distance=' + str(totalDistance))
        
        previousPoint = currentPoint

        turtleDraw.color(color)
        turtleDraw.goto(x,y)

        turtleDraw.pendown()

    if (len(parts) == 1):
        turtleDraw.penup()

    turtleLine = turtleDrawTextfile.readline()

turtle.write('Total Distance=' + str(totalDistance))
# Todo: Print the total near the bottom
# I was able to print the total distance, but I couldn't figure out how to have
# the total distance only registered when the pendown
turtle.done()


input("\nPress 'enter' to close Application...") # This requires the user to click enter to finish
turtleDrawTextfile.close()

print('\nEnd')