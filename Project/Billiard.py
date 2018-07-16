import pygame as pygame
import sys
import bib.color as color
import bib.draw as draw
import kugel
import tisch
import os
import threading
from tkinter import *
import random, math
import time

global playerOnClick
root = Tk()


def motion(event):
    print('motion {}, {}'.format(event.x, event.y))


tableClass = tisch.Table()
ball = kugel.Ball()
whiteBall = ball
y = 0.456
x = 0.3
j = 2
r = 0.013

one = kugel.Ball([0.7,0.456], color.YELLOW, True, 1)
balls = [whiteBall, one]

ballColors = [color.BLUE, color.RED, color.PINK, color.ORANGE, color.DARK_GREEN, color.DARK_BLUE, color.YELLOW,
              color.BLUE, color.RED, color.PINK, color.ORANGE, color.DARK_GREEN, color.DARK_BLUE]
ballColors.insert(3, color.BLACK)

# false for one color
ballRandomBool = [True, False, True, False, True, False, False, False, True, False, True, False, True, False]
ballRandomBool.insert(3, True)

ballNumber = [2, 3, 4, 8, 6, 5, 9, 7, 13, 10, 11, 15, 14, 12]

for data in range(4):

    x -= math.sqrt(3) * r
    y -= r

    for i in range(data + 2):
        theeBall = kugel.Ball([x, y], ballColors[j - 2], ballRandomBool[j - 2], ballNumber[j - 2])
        balls += [theeBall]
        y += 2 * r
        if i == data + 1:
            y = 0.456 - (r * (data + 1))
        j += 1

draw.setCanvasSize(800, 800)
player_set = False
while True:
    # print(time.time())
    # draw.line(0.5, 0.5, draw.mousePosition()[0], draw.mousePosition()[1])
    tableClass.myTable()
    tableClass.myBorders()
    tableClass.myBorderLines()
    tableClass.tableResults()
    whiteBall.myQueue(draw.mousePosition())
    for thisBall in balls:
        thisBall.myBall()
        thisBall.ballFriction()
    for thisBall in balls:
        thisBall.nextPosition()
        tableClass.borderBang(thisBall)

        tmp_player, tmp_p1 = tableClass.ballInHole(thisBall, draw.mousePosition())
        if tmp_player:
            player_set = True
            p1_above = tmp_p1

        for other in balls[1:len(balls)]:
            if thisBall != other:
                thisBall.ballsBang(other)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            kugel.Ball().ballPowerStart(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            global playerOnClick
            x, y = draw.mousePosition()
            root.bind(motion)
            print("\nBilliard.py: x{},y{}", x, y, "..")
            x, y = draw.mousePosition()
            ball.newKick([x, y])
            data = ball.player()
            tableClass.playerOnClick(data)

    if player_set:
        if p1_above:
            draw.setPenColor(color.WHITE)
            draw.text(0.1, 0.9, "P1: ")
            draw.text(0.1, 0.85, "P2: ")
        else:
            draw.setPenColor(color.WHITE)
            draw.text(0.1, 0.9, "P2: ")
            draw.text(0.1, 0.85, "P1: ")

    draw.show(10)
    draw.clear()
