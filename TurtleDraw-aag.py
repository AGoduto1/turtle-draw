# TurtleDrawing 
# Reading a text file line by line.
# 
# By: Angelo Goduto
#
# All rights reserved

import turtle
# import math

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
# tried to figure out how to calculate, I had to include import math at the top
        # def calculateDistance(x1,y1,x2,y2):
        #     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #     return dist.
        # print calculateDistance(x1, y1, x2, y2)
        # dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


        turtleDraw.color(color)
        turtleDraw.goto(x,y)

        turtleDraw.pendown()

    if (len(parts) == 1):
        turtleDraw.penup()

    line = turtleDrawTextfile.readline()

# Todo: Print the total near the bottom
turtle.done()
# def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    # distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    # print('Segment Dist: ', distance)
    # return distance

# def calculate_path(selected_map, dist_travel=0):
    # for i in range(len(selected_map)-1):
    #    dist_travel += calculate_distance(selected_map[i-len(selected_map)+1][0], selected_map[i-len(selected_map)+1][1], selected_map[i][0], selected_map[i][1])
    # return dist_travel

# print('Total Distance: ', calculate_path())

input("\nPress 'enter' to close Application...")
turtleDrawTextfile.close()

# Todo: Wait for the user to press the enter key before closing.

print('\nEnd')