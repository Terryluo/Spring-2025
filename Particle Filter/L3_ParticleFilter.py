######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################
import random

from Utilities.robot_pf import *

# PARTICLE FILTER LESSON MODULES
print("PARTICLE FILTER LESSON MODULES", end="")

# --------------------------------------------------------------------
# 8. USING A ROBOT CLASS
print("\n8. USING A ROBOT CLASS")
# For this lesson, (and the following lesson #9),
# please familiarize yourself with the robot class.

myrobot = robot()
myrobot.set(10, 10, 0)
print(myrobot)
myrobot = myrobot.move(pi/2, 10)
print(myrobot)
print(myrobot.sense())

# --------------------------------------------------------------------
# 10. MOVING ROBOT
print("\n10. MOVING ROBOT")
# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.
# Your program should print out the result of
# your two sense measurements.

myrobot10 = robot()
# starts at 30.0, 50.0, heading North (pi/2)
myrobot10.set(30.0, 50.0, pi / 2)
print(myrobot10)
# turns clockwise pi/2, moves 15 meters
myrobot10 = myrobot10.move(- pi / 2, 15)
print(myrobot10)
# senses
print(myrobot10.sense())
# turns clockwise by pi / 2, moves 10 meters
myrobot10 = myrobot10.move(- pi / 2, 10)
print(myrobot10)
print(myrobot10.sense())

# --------------------------------------------------------------------
# 11. ADD NOISE
print("\n11. ADD NOISE")
# Now add noise to your robot as follows:
# forward_noise = 5.0, turn_noise = 0.1, sense_noise = 5.0.
myrobot11 = robot()
myrobot11.set_noise(5.0, 0.1, 5.0)
#
# Once again, your robot starts at 30, 50,
# heading north (pi/2),
myrobot11.set(30.0, 50.0, pi / 2)
print(myrobot11)
# then turns clockwise by pi/2, moves 15 meters, senses,
myrobot11 = myrobot11.move(- pi / 2, 15)
print(myrobot11)
print(myrobot11.sense())
# then turns clockwise by pi/2 again, moves 10 m, then senses again.
myrobot11 = myrobot11.move(- pi / 2, 10)
print(myrobot11)
print(myrobot11.sense())


# --------------------------------------------------------------------
# 13. CREATING PARTICLES
print("\n13. CREATING PARTICLES")
# Now we want to create particles,
# p[i] = robot(). In this assignment, write
# code that will assign 1000 such particles
# to a list.
# Your program should print out the length
# of your list (don't cheat by making an
# arbitrary list of 1000 elements!)

N = 1000
p = []
for i in range(N):
    myrobot13 = robot()
    myrobot13.set_noise(5.0, 0.1, 5.0)
    myrobot13.set(30.0, 50.0, pi / 2)
    myrobot13 = myrobot13.move(- pi / 2, 15)
    myrobot13 = myrobot13.move(- pi / 2, 10)
    p.append(myrobot13)
#print(len(p))
#print(p)

# --------------------------------------------------------------------
# 14. ROBOT PARTICLES
print("\n14. ROBOT PARTICLES")
# Now we want to simulate robot
# motion with our particles.
# Each particle should turn by 0.1
# and then move by 5.

N = 1000
p1 = []
for i in range(N):
    x = robot()
    p1.append(x)

p2 = []
for i in range(N):
    p2.append(p1[i].move(0.1, 5.0))
#print(p2)

# --------------------------------------------------------------------
# 15. IMPORTANCE WEIGHT
print("\n15. IMPORTANCE WEIGHTS")
# Now we want to give weight to our
# particles. This program will print a
# list of 1000 particle weights.

myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()

# Copy and paste your solution code from the previous exercises (#13 and #14)
# Note that there will need to be a small modification for setting noise to the
# previous code as stated in the video

p15_1 = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p15_1.append(x)

p15_2 = []
for i in range(N):
    p15_2.append(p15_1[i].move(0.1, 5.0))

w = []
'''
  Here is some note:
  1. calculate the current measurement and the sense() Z
  2. generate 1000 samples(sampling) that gives the probability that would close to Z
  3. maintaining the high probability particles, and letting the low probability particles die. (use resampling method)

'''
normalized_weight = 0.0
for i in range(N):
    w.append(p15_2[i].measurement_prob(Z))
    normalized_weight += w[i]

#print(w)
#print(normalized_weight) # the sum here is not equals to 1

alphas = []
sum_alphas = 0
for i in range(N):
    alphas.append(w[i] / normalized_weight)
    sum_alphas += alphas[i]

#print(alphas)
#print(sum_alphas)


# --------------------------------------------------------------------
# 20. NEW PARTICLE
print("\n20. NEW PARTICLE")
# In this exercise, try to write a program that
# will resample particles according to their weights.
# Particles with higher weights should be sampled
# more frequently (in proportion to their weight).

p3 = []
# TODO: ADD CODE HERE
p = p3

p20_1 =[]
index = int(random.random() * N)
beta = 0
mw = max(w)
for i in range(N):
    beta += random.random() * 2 * mw
    while w[index] < beta:
        beta = beta - w[index]
        index = (index + 1) % N
    p20_1.append(p15_2[index])

#print(p20_1)

# --------------------------------------------------------------------
# 21. RESAMPLING WHEEL
print("\n21. RESAMPLING WHEEL")
# In this exercise, you should implement the
# resampler shown in the previous video.
'''
The pseudocode in the video should be like this (instead of an if-else block):

while w[index] < beta:
    beta = beta - w[index]
    index = (index + 1) % N

select p[index]
'''
myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()

N = 1000
p = []

# Copy and paste your solution code from the previous exercise (#15)

p3 = []
# TODO: ADD CODE HERE
p = p3

# --------------------------------------------------------------------
# 23. ORIENTATION 2
print("\n23. ORIENTATION 2")
# In this exercise, write a program that will
# run your previous code twice.

N = 1000
T = 3
myrobot23 = robot()
p23 = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p23.append(x)

for j in range(T):  # do it twice
    myrobot23 = myrobot23.move(0.1, 5.0)
    Z = myrobot23.sense()

    p23_1 = []
    for k in range(N):
        p23_1.append(p23[i].move(0.1, 5.0))
    p23 = p23_1


    p23_1_w = []
    for l in range(N):
        p23_1_w.append(p23[l].measurement_prob(Z))

    p23_2 = []
    p23_index = int(random.random() * N)
    beta = 0
    mw = max(p23_1_w)
    for m in range(N):
        beta += random.random() * 2 * mw
        while p23_1_w[p23_index] < beta:
            beta = beta - p23_1_w[p23_index]
            p23_index = (p23_index + 1) % N
        p23_2.append(p23[p23_index])
    p23 = p23_2


# Copy and paste your code from the previous exercise (#21)
# TODO: CHANGE/UPDATE CODE HERE

# print(p23)

# --------------------------------------------------------------------
# 24. ERROR
print("\n24. ERROR")
# In this exercise, write a program that will
# print out the quality of your solution
# using the eval function. (Should print T times!)

T = 10
N = 1000
myrobot24 = robot()
p24 = []

# Copy and paste your code from the previous exercise (#23)
# TODO: CHANGE/UPDATE CODE HERE
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p24.append(x)

for j in range(T):  # do it twice
    myrobot24 = myrobot24.move(0.1, 5.0)
    Z_24 = myrobot24.sense()

    p24_1 = []
    for k in range(N):
        p24_1.append(p24[i].move(0.1, 5.0))
    p24 = p24_1

    p24_1_w = []
    for l in range(N):
        p24_1_w.append(p24[l].measurement_prob(Z_24))

    p24_2 = []
    p24_index = int(random.random() * N)
    beta = 0
    mw_24 = max(p24_1_w)
    for m in range(N):
        beta += random.random() * 2.0 * mw_24
        while p24_1_w[p24_index] < beta:
            beta = beta - p24_1_w[p24_index]
            p24_index = (p24_index + 1) % N
        p24_2.append(p24[p24_index])
    p24 = p24_2

    print(eval(myrobot24, p24))