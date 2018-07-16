import pygame, sys
import bib.color as color
import bib.draw as draw

myPlayerData = ["1", False]
gBool = False
oneCollorBalls = []
twoCollorBalls = []


class Table():
    def __init__(self):
        self.ballOutXFalsePos = 0.0
        self.ballOutXTruePos = 0.0

    def myTable(self):
        # my table
        myTable = draw.setPenColor(color.GREEN)
        myTable = draw.filledRectangle(0.01, 0.25, 0.98, 0.44)
        myTableBorder = draw.setPenRadius(0.04)
        myTableBorder = draw.setPenColor(color.Color(00, 80, 00))
        myTableBorder = draw.rectangle(0.01, 0.25, 0.98, 0.44)

    def tableResults(self):
        global myPlayerData
        draw.setPenColor(color.LIGHT_GRAY)
        draw.filledPolygon([0.0, 1.0, 1.0, 0.0], [0.76, 0.76, 1.0, 1.0])
        draw.setPenColor(color.WHITE)
        # draw.text(0.1, 0.9, "P1: ")
        # draw.text(0.1, 0.85, "P2: ")
        draw.text(0.135, 0.95, "Balls:")
        draw.setPenRadius(0.001)
        draw.line(0.1, 0.83, 0.9, 0.83)
        draw.setPenColor(color.DARK_GREEN)
        draw.setPenRadius(0.005)
        draw.line(0.0, 0.76, 1.0, 0.76)
        draw.setPenColor(color.WHITE)
        draw.text(0.85, 0.8, "Player: ")
        draw.text(0.9, 0.8, str(myPlayerData[0]))

    def myBorders(self):
        # bottom-left
        holeY1 = [0.238, 0.238, 0.263, 0.29, 0.266]
        holeX1 = [0.0, 0.028, 0.048, 0.023, 0.0]
        hole = draw.setPenColor(color.BLACK)
        hole = draw.filledPolygon(holeX1, holeY1)
        # top-right
        holeY2 = [0.701, 0.701, 0.676, 0.649, 0.671]  # 61px
        holeX2 = [1.0, 0.972, 0.952, 0.977, 1.0]
        hole = draw.setPenRadius(0.005)
        hole = draw.setPenColor(color.BLACK)
        hole = draw.filledPolygon(holeX2, holeY2)
        # top-left
        holeY3 = [0.701, 0.701, 0.676, 0.649, 0.671]
        holeX3 = [0.0, 0.028, 0.048, 0.023, 0.0]
        hole = draw.setPenRadius(0.005)
        hole = draw.setPenColor(color.BLACK)
        hole = draw.filledPolygon(holeX3, holeY3)
        # bottom-right
        holeY4 = [0.238, 0.238, 0.263, 0.29, 0.266]
        holeX4 = [1.0, 0.972, 0.952, 0.977, 1.0]
        hole = draw.setPenRadius(0.005)
        hole = draw.setPenColor(color.BLACK)
        hole = draw.filledPolygon(holeX4, holeY4)
        # bottom-middle
        holeY5 = [0.238, 0.238, 0.262, 0.262]
        holeX5 = [0.482, 0.518, 0.518, 0.482]
        hole = draw.setPenRadius(0.005)
        hole = draw.setPenColor(color.BLACK)
        hole = draw.filledPolygon(holeX5, holeY5)
        # top-middle
        holeY6 = [0.677, 0.677, 0.701, 0.701]
        holeX6 = [0.482, 0.518, 0.518, 0.482]
        hole = draw.setPenRadius(0.005)
        hole = draw.setPenColor(color.BLACK)
        hole = draw.filledPolygon(holeX6, holeY6)

    def myBorderLines(self):
        lineMark = draw.setPenRadius(0.001)
        # bottom
        lineMark = draw.line(0.1565, 0.238, 0.1565, 0.262)
        lineMark = draw.line(0.265, 0.238, 0.265, 0.262)
        lineMark = draw.line(0.3735, 0.238, 0.3735, 0.262)
        lineMark = draw.line(0.6265, 0.238, 0.6265, 0.262)
        lineMark = draw.line(0.735, 0.238, 0.735, 0.262)
        lineMark = draw.line(0.8435, 0.238, 0.8435, 0.262)
        # top
        lineMark = draw.line(0.1565, 0.701, 0.1565, 0.677)
        lineMark = draw.line(0.265, 0.701, 0.265, 0.677)
        lineMark = draw.line(0.3735, 0.701, 0.3735, 0.677)
        lineMark = draw.line(0.6265, 0.701, 0.6265, 0.677)
        lineMark = draw.line(0.735, 0.701, 0.735, 0.677)
        lineMark = draw.line(0.8435, 0.701, 0.8435, 0.677)
        # left
        lineMark = draw.line(0.0, 0.5525, 0.023, 0.5525)
        lineMark = draw.line(0.0, 0.456, 0.023, 0.456)
        lineMark = draw.line(0.0, 0.3595, 0.023, 0.3595)
        # right
        lineMark = draw.line(0.978, 0.5525, 1.0, 0.5525)
        lineMark = draw.line(0.978, 0.456, 1.0, 0.456)
        lineMark = draw.line(0.978, 0.3595, 1.0, 0.3595)

    def borderBang(self, ball):
        if ball.isBallInTheHole == False:
            if ball.position[0] < 0.034 or ball.position[0] > 0.966:
                ball.vector[0] = -ball.vector[0]
            if ball.position[1] < 0.274 or ball.position[1] > 0.664:
                ball.vector[1] = -ball.vector[1]

            x = ball.vector[0] * 0.001
            while ball.position[0] < 0.034 or ball.position[0] > 0.966:
                ball.position[0] += x
            y = ball.vector[1] * 0.001
            while ball.position[1] < 0.274 or ball.position[1] > 0.664:
                ball.position[1] += y

    def ballInHole(self, other, mousePosition):
        # bottom-left
        global gBool, oneCollorBalls
        player_set = False
        p1_above = False
        if other.position[0] <= 0.0399 and other.position[1] <= 0.284:
            if other.ballNumber == 0:
                draw.setPenColor(color.RED)
                draw.text(0.1, 0.1, "die Kugel ist in einem der Löcher")
                other.position[0] = 0.135
                other.position[1] = 0.8
                other.vector[0] = 0.0
                other.vector[1] = 0.0
                other.isBallInTheHole = True

            else:
                if myPlayerData[0] == 1 and gBool == False:
                    gBool = True
                    player_set = True
                    p1_above = True
                if myPlayerData[0] == 2 and gBool == False:
                    gBool = True
                    player_set = True
                if other.ballNumber < 8:
                    oneCollorBalls.append(other.ballNumber)
                if other.ballNumber > 8:
                    twoCollorBalls.append(other.ballNumber)

                if other.ballNumber == 8 and len(oneCollorBalls) < 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 2 won")
                if other.ballNumber == 8 and len(twoCollorBalls) < 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 2 won")

                yFalse = 0.9
                yTrue = 0.85
                if other.ballMarker == True:
                    y = yTrue
                    self.ballOutXTruePos += 0.035
                    other.position = [0.1 + self.ballOutXTruePos, y]
                else:
                    y = yFalse
                    self.ballOutXFalsePos += 0.035
                    other.position = [0.1 + self.ballOutXFalsePos, y]

                other.isBallInTheHole = True
                other.vector = [0.0, 0.0]

        # top-right
        if other.position[0] >= 0.96 and other.position[1] >= 0.658:
            if other.ballNumber == 0:
                draw.setPenColor(color.RED)
                draw.text(0.1, 0.1, "die Kugel ist in einem der Löcher")
                other.position[0] = 0.135
                other.position[1] = 0.8
                other.vector[0] = 0.0
                other.vector[1] = 0.0
                other.isBallInTheHole = True

            else:
                if myPlayerData[0] == 1 and gBool == False:
                    gBool = True
                    player_set = True
                    p1_above = True
                if myPlayerData[0] == 2 and gBool == False:
                    gBool = True
                    player_set = True
                if other.ballNumber < 8:
                    oneCollorBalls.append(other.ballNumber)
                if other.ballNumber > 8:
                    twoCollorBalls.append(other.ballNumber)

                if other.ballNumber == 8 and len(oneCollorBalls) < 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 2 won")
                if other.ballNumber == 8 and len(twoCollorBalls) < 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 2 won")
                yFalse = 0.9
                yTrue = 0.85
                if other.ballMarker == True:
                    y = yTrue
                    self.ballOutXTruePos += 0.035
                    other.position = [0.1 + self.ballOutXTruePos, y]
                else:
                    y = yFalse
                    self.ballOutXFalsePos += 0.035
                    other.position = [0.1 + self.ballOutXFalsePos, y]

                other.isBallInTheHole = True
                other.vector = [0.0, 0.0]

        # bottom-right
        if other.position[0] >= 0.963 and other.position[1] <= 0.284:
            if other.ballNumber == 0:
                draw.setPenColor(color.RED)
                draw.text(0.1, 0.1, "die Kugel ist in einem der Löcher")
                other.position[0] = 0.135
                other.position[1] = 0.8
                other.vector[0] = 0.0
                other.vector[1] = 0.0
                other.isBallInTheHole = True

            else:
                if myPlayerData[0] == 1 and gBool == False:
                    gBool = True
                    player_set = True
                    p1_above = True
                if myPlayerData[0] == 2 and gBool == False:
                    gBool = True
                    player_set = True
                if other.ballNumber < 8:
                    oneCollorBalls.append(other.ballNumber)
                if other.ballNumber > 8:
                    twoCollorBalls.append(other.ballNumber)

                if other.ballNumber == 8 and len(oneCollorBalls) < 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 2 won")
                if other.ballNumber == 8 and len(twoCollorBalls) < 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 2 won")
                yFalse = 0.9
                yTrue = 0.85
                if other.ballMarker == True:
                    y = yTrue
                    self.ballOutXTruePos += 0.035
                    other.position = [0.1 + self.ballOutXTruePos, y]
                else:
                    y = yFalse
                    self.ballOutXFalsePos += 0.035
                    other.position = [0.1 + self.ballOutXFalsePos, y]

                other.isBallInTheHole = True
                other.vector = [0.0, 0.0]

        # top-left
        if other.position[0] <= 0.038 and other.position[1] >= 0.658:
            if other.ballNumber == 0:
                draw.setPenColor(color.RED)
                draw.text(0.1, 0.1, "die Kugel ist in einem der Löcher")
                other.position[0] = 0.135
                other.position[1] = 0.8
                other.vector[0] = 0.0
                other.vector[1] = 0.0
                other.isBallInTheHole = True

            else:
                if myPlayerData[0] == 1 and gBool == False:
                    gBool = True
                    player_set = True
                    p1_above = True
                if myPlayerData[0] == 2 and gBool == False:
                    gBool = True
                    player_set = True
                if other.ballNumber < 8:
                    oneCollorBalls.append(other.ballNumber)
                if other.ballNumber > 8:
                    twoCollorBalls.append(other.ballNumber)

                if other.ballNumber == 8 and len(oneCollorBalls) < 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 2 won")
                if other.ballNumber == 8 and len(twoCollorBalls) < 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 2 won")
                yFalse = 0.9
                yTrue = 0.85
                if other.ballMarker == True:
                    y = yTrue
                    self.ballOutXTruePos += 0.035
                    other.position = [0.1 + self.ballOutXTruePos, y]
                else:
                    y = yFalse
                    self.ballOutXFalsePos += 0.035
                    other.position = [0.1 + self.ballOutXFalsePos, y]

                other.isBallInTheHole = True
                other.vector = [0.0, 0.0]

        # middle-top
        if other.position[0] >= 0.482 and other.position[0] <= 0.518 and other.position[1] >= 0.663:
            if other.ballNumber == 0:
                draw.setPenColor(color.RED)
                draw.text(0.1, 0.1, "die Kugel ist in einem der Löcher")
                other.position[0] = 0.135
                other.position[1] = 0.8
                other.vector[0] = 0.0
                other.vector[1] = 0.0
                other.isBallInTheHole = True

            else:
                if myPlayerData[0] == 1 and gBool == False:
                    gBool = True
                    player_set = True
                    p1_above = True
                if myPlayerData[0] == 2 and gBool == False:
                    gBool = True
                    player_set = True
                if other.ballNumber < 8:
                    oneCollorBalls.append(other.ballNumber)
                if other.ballNumber > 8:
                    twoCollorBalls.append(other.ballNumber)

                if other.ballNumber == 8 and len(oneCollorBalls) < 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 2 won")
                if other.ballNumber == 8 and len(twoCollorBalls) < 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 2 won")
                yFalse = 0.9
                yTrue = 0.85
                if other.ballMarker == True:
                    y = yTrue
                    self.ballOutXTruePos += 0.035
                    other.position = [0.1 + self.ballOutXTruePos, y]
                else:
                    y = yFalse
                    self.ballOutXFalsePos += 0.035
                    other.position = [0.1 + self.ballOutXFalsePos, y]

                other.isBallInTheHole = True
                other.vector = [0.0, 0.0]

        # bottom-mittle
        if other.position[0] >= 0.482 and other.position[0] <= 0.518 and other.position[1] <= 0.275:
            if other.ballNumber == 0:
                draw.setPenColor(color.RED)
                draw.text(0.1, 0.1, "die Kugel ist in einem der Löcher")
                other.position[0] = 0.135
                other.position[1] = 0.8
                other.vector[0] = 0.0
                other.vector[1] = 0.0
                other.isBallInTheHole = True

            else:
                if myPlayerData[0] == 1 and gBool == False:
                    gBool = True
                    player_set = True
                    p1_above = True
                if myPlayerData[0] == 2 and gBool == False:
                    gBool = True
                    player_set = True
                if other.ballNumber < 8:
                    oneCollorBalls.append(other.ballNumber)
                if other.ballNumber > 8:
                    twoCollorBalls.append(other.ballNumber)

                if other.ballNumber == 8 and len(oneCollorBalls) < 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 2 won")
                if other.ballNumber == 8 and len(twoCollorBalls) < 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 1:
                    draw.text(0.65, 0.95, "Player 1 won")
                if other.ballNumber == 8 and len(oneCollorBalls) == 7 and myPlayerData[0] == 2:
                    draw.text(0.65, 0.95, "Player 2 won")
                yFalse = 0.9
                yTrue = 0.85
                if other.ballMarker == True:
                    y = yTrue
                    self.ballOutXTruePos += 0.035
                    other.position = [0.1 + self.ballOutXTruePos, y]
                else:
                    y = yFalse
                    self.ballOutXFalsePos += 0.035
                    other.position = [0.1 + self.ballOutXFalsePos, y]

                other.isBallInTheHole = True
                other.vector = [0.0, 0.0]
        return player_set, p1_above

    def playerOnClick(self, data):
        global myPlayerData
        myPlayerData = [data, gBool]
