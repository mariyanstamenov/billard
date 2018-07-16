import time
import bib.draw.py  as draw
import bib.color
import pygame
"""
def borderBang(self):
    myXPosition, myYPosition = self.position
    xVector, yVector = self.vector
    if myXPosition < 0.033 or myXPosition > 0.967:
        xVector = -xVector
    if myYPosition < 0.273 or myYPosition > 0.665:
        yVector = -yVector
    self.vector = (xVector, yVector)



def ballsBang(self, other):
    thisXPosition, thisYPosition = self.position
    otherXPosition, otherYPosition = other.position
    xVector, yVector = self.vector
    if ((thisXPosition - otherXPosition) ** 2 + (thisYPosition - otherYPosition) ** 2) <= (2 * 0.01988) ** 2:
        selfXPosition, selfYPosition = self.position
        otherXPosition, otherYPosition = other.position
        # print(-selfXPosition, -selfYPosition)
        if selfXPosition > otherXPosition and selfYPosition > otherYPosition:
            myOtherVectors = (xVector, yVector)
            # self.vector=(-,-yVector)
        elif selfXPosition < otherXPosition and selfYPosition < otherYPosition:
            myOtherVectors = (-xVector, -yVector)
            # self.vector = (-xVector, yVector)
        elif selfXPosition < otherXPosition and selfYPosition > otherYPosition:
            myOtherVectors = (-xVector, yVector)
            # self.vector = (-xVector, yVector)
        elif selfXPosition > otherXPosition and selfYPosition < otherYPosition:
            myOtherVectors = (xVector, -yVector)
            # self.vector = (-xVector, yVector)

        self.position = (selfXPosition, selfYPosition)
        self.nextPositionSecondBall(other, myOtherVectors)
    else:
        return False

    def borderBang(self, ball, data):
        # data = x actual myposition , y actual myposition, x actual vector, y actual vector
        myXPosition, myYPosition = data[0]
        xVector, yVector = data[1]

        if myXPosition < 0.034 or myXPosition > 0.966:
            while myXPosition < 0.034:
            # nach rechts
            while myXPosition > 0.966:
            # nach links
            xVector = -xVector
        if myYPosition < 0.274 or myYPosition > 0.664:
            yVector = -yVector

        ball.setVectors(xVector, yVector)
"""

a = time.time()
b = time.time()

if draw.mousePressed():
    print("yes")