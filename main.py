# Programmers: Ethan and Cameron
# Course:  CS151
# Due Date: 10/4/2024
# Lab Assignment: Lab 03
# Problem Statement:
# Data In:
# Data Out:
# Credits:

#import math
import math


#inputs for hill type and speed
hill_type = input('enter hill type ')
speed = int(input('enter speed '))

#hill type if statments
if hill_type == 'normal':
    height = 46
    points_meter = 2
    par = 90

elif hill_type == 'large':
    height = 70
    points_meter = 1.8
    par = 120

#error checking
elif hill_type != 'normal' or hill_type != 'large':
    hill_type = input('enter hill type ')
    if hill_type == 'normal':
        height = 46
        points_meter = 2
        par = 90

    elif hill_type == 'large':
        height = 70
        points_meter = 1.8
        par = 120


#air time & distance calculations
air_time = math.sqrt((2*height)/9.8)
distance = speed*air_time

#point calculation
points = 60+(distance-par)*points_meter

#outputs
if points >= 61:
    print(points, 'great job for doing better than par!')
elif points < 10:
    print(points, 'what happened?')
else:
    print(points, 'sorry, you didnt go very far.')



