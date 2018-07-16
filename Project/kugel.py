import pygame, sys
import bib.draw as draw
import bib.color as color
import math, time

power = 0.0
player = 1


class Ball():
    def __init__(self, position=[0.735, 0.456], ballColor=color.WHITE, ballMarker=True, ballNumber=0):
        self.position = position
        # self.speed = 0.005
        self.vector = [0, 0]
        self.radius = 0.014
        self.ballColor = ballColor
        self.ballMarker = ballMarker
        self.ballNumber = ballNumber
        self.ballBorder = False
        self.isTrue = False
        self.whiteBallBangPosition = 0
        self.isWhiteBallThere = False
        self.isBallInTheHole = False
        self.ballXOutPosition = 0.0
        self.startTime = 0.0
        self.endTime = 0.0
        self.startTime = 0.0
        self.endTime = 0.0

    def myReturnPosition(self):
        myArray = [self.position, self.vector]
        return myArray

    def myBall(self):
        # for white ball #
        if self.ballNumber == 0 and self.isWhiteBallThere == True:
            x, y = self.position
            # myColor = self.ballColor
            # draw.setPenColor(myColor)
            # draw.filledCircle(x, y, r)
            draw.setPenColor(color.WHITE)
            draw.circle(x, y, self.radius)
            self.isWhiteBallThere = True

        # for one color-ball #
        elif self.ballMarker == True:
            x, y = self.position
            draw.setPenRadius(0.01)
            draw.setPenColor(self.ballColor)
            draw.filledCircle(x, y, self.radius)
            draw.setPenColor(color.WHITE)
            draw.setPenRadius(0.01)
            draw.setPenColor(color.WHITE)
            draw.setFontSize(18)
            draw.text(x - 0.0012, y, str(self.ballNumber))

        # for two colors-ball #
        elif self.ballMarker == False:
            x, y = self.position
            draw.setPenRadius(0.01)
            draw.setPenColor(self.ballColor)
            draw.circle(x, y, self.radius)
            draw.setPenColor(color.WHITE)
            draw.setFontSize(18)
            draw.text(x - 0.0012, y, str(self.ballNumber))

    ###########vectors correctly!
    def nextPosition(self):
        newXPosition, newYPosition = self.position
        xVector, yVector = self.vector

        newXPosition += xVector
        newYPosition += yVector

        self.position = [newXPosition, newYPosition]

    def ballFriction(self):
        self.vector[0] *= 0.95
        self.vector[1] *= 0.95

    # new click
    def newKick(self, newPosition):
        global power
        if self.isBallInTheHole == False:
            myXVector, myYVector = newPosition
            myXPosition, myYPosition = self.position
            print(newPosition, power)
            myXVector = ((myXPosition - myXVector) * power) * 1
            myYVector = ((myYPosition - myYVector) * power) * 1

            newPosition = [myXVector, myYVector]
            self.vector = newPosition
            print("\nmy vectors from newKick()-X-Y: ", self.vector, " ---\n")
        else:
            self.position[0] = 0.735
            self.position[1] = draw.mousePosition()[1]
            self.vector[0] = 0.0
            self.vector[1] = 0.0
            self.isBallInTheHole = False

    def ballsBang(self, other):
        xSelfVector, ySelfVector = self.vector
        xOtherVector, yOtherVector = other.vector
        if self.isBallInTheHole == False:
            xSelfVector *= -0.001
            ySelfVector *= -0.001
            xOtherVector *= -0.001
            yOtherVector *= -0.001
            collide = False
            while (((self.position[0] - other.position[0]) ** 2 + (self.position[1] - other.position[1]) ** 2) <= (
                        2 * self.radius) ** 2 and
                       (abs(self.vector[0]) > 0.0001 or abs(self.vector[1]) > 0.0001 or abs(
                           other.vector[0]) > 0.0001 or abs(other.vector[1]) > 0.0001)):
                collide = True

                self.position[0] += xSelfVector
                self.position[1] += ySelfVector
                other.position[0] += xOtherVector
                other.position[1] += yOtherVector

            if collide:
                newXVec = -(self.position[0] - other.position[0])
                newYVec = -(self.position[1] - other.position[1])
                l = math.sqrt(self.vector[0] ** 2 + self.vector[1] ** 2) / (
                    2 * math.sqrt(2) * math.sqrt(newXVec ** 2 + newYVec ** 2))
                other.vector[0] = l * newXVec
                other.vector[1] = l * newYVec

                self.vector[0] = (self.vector[0] - other.vector[0])  # -(other.vector[0])# - self.vector[0])
                self.vector[1] = (self.vector[1] - other.vector[1])  # -(other.vector[1])# - self.vector[1])

    def myQueue(self, myMouse):
        if self.isBallInTheHole == False:
            if abs(self.vector[0]) < 0.001 and abs(self.vector[1] < 0.0001):
                # draw.line(self.position[0], self.position[1], myMouse[0], myMouse[1])
                xQ, yQ = myMouse
                xB, yB = self.position
                a = xQ - xB
                b = yQ - yB

                data = math.sqrt(a ** 2 + b ** 2)

                a /= data
                b /= data

                fX = (xB - 1 * a - a * 0.15)
                fY = (yB - 1 * b - b * 0.15)

                firststartX = xB + 0.025 * a
                firststartY = yB + 0.025 * b
                firstendX = xB + 0.0005 * a + a * 0.15
                firstendY = yB + 0.0005 * b + b * 0.15

                startWhiteX = xB + 0.15 * a
                startWhiteY = yB + 0.15 * b
                endWhiteX = xB + 0.12 * a + a * 0.15
                endWhiteY = yB + 0.12 * b + b * 0.15

                bSX = xB + 0.23 * a
                bSY = yB + 0.23 * b
                bEX = xB + 0.14 * a + a * 0.15
                bEY = yB + 0.14 * b + b * 0.15

                draw.setPenColor(color.Color(245, 246, 246))
                draw.setPenRadius(0.004)
                draw.line(firststartX, firststartY, firstendX, firstendY)

                draw.setPenColor(color.BROWN)
                draw.setPenRadius(0.0051)
                draw.line(startWhiteX, startWhiteY, endWhiteX, endWhiteY)

                draw.setPenColor(color.BLACK)
                draw.setPenRadius(0.0066)
                draw.line(bSX, bSY, bEX, bEY)

                draw.setPenColor(color.WHITE)
                draw.setPenRadius(0.001)
                draw.line(self.position[0], self.position[1], fX, fY)

                data = math.sqrt((self.position[0] - myMouse[0]) ** 2 + (self.position[1] - myMouse[1]) ** 2)
                """
                if data < 0.2:
                    self.power = 0.13
                elif data >= 0.2 or data < 0.3:
                    self.power = 0.19
                elif data >= 0.3 or data < 0.5:
                    self.power = 0.23
                else:
                    self.power = 0.29
                """

    def ballPowerStart(self, event):
        global power
        if event.key == pygame.K_1:
            print("1")
            power = 0.1
            print(power)
            draw.setPenColor(color.GREEN)
            draw.line(0.0, 0.05, 0.1, 0.05)
        if event.key == pygame.K_2:
            print("2")
            power = 0.22
            draw.setPenColor(color.GREEN)
            print(power)
            draw.line(0.0, 0.05, 0.15, 0.05)
        if event.key == pygame.K_3:
            print("3")
            power = 0.35
            draw.setPenColor(color.GREEN)
            draw.line(0.0, 0.05, 0.2, 0.05)
            print(power)
        if event.key == pygame.K_4:
            print("4")
            power = 0.47
            draw.setPenColor(color.ORANGE)
            draw.line(0.0, 0.05, 0.3, 0.05)
            print(power)
        if event.key == pygame.K_5:
            print("4")
            power = 0.6
            draw.setPenColor(color.ORANGE)
            draw.line(0.0, 0.05, 0.35, 0.05)
            print(power)
        if event.key == pygame.K_6:
            print("4")
            power = 0.75
            draw.setPenColor(color.ORANGE)
            draw.line(0.0, 0.05, 0.4, 0.05)
            print(power)
        if event.key == pygame.K_7:
            print("4")
            power = 0.9
            draw.setPenColor(color.RED)
            draw.line(0.0, 0.05, 0.5, 0.05)
            print(power)
        if event.key == pygame.K_8:
            print("4")
            power = 1
            draw.setPenColor(color.RED)
            draw.line(0.0, 0.05, 0.55, 0.05)
            print(power)
        if event.key == pygame.K_9:
            print("4")
            power = 1.2
            draw.setPenColor(color.DARK_RED)
            draw.line(0.0, 0.05, 0.6, 0.05)
            print(power)

    def player(self):
        global player
        player *= -1

        if player < 0:
            return 1
        else:
            return 2
