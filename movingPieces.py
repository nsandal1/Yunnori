import random
from graphics import *

window = GraphWin("gameWindow", 1000, 1000)
myImage = Image(Point(400,400), "Yun.gif")
myImage.draw(window)


# Drawing the pieces for each player (Assume 2 players)
class Piece(object):
    d = Circle(Point(50, 50), 10)
    d.draw(window)
    POne2 = Circle(Point(50, 50), 10)
    POne2.draw(window)
    POne3 = Circle(Point(50, 50), 10)
    POne3.draw(window)
    print(d.getCenter())
    # Changing the colors of pieces
    print("Please choose blue, green, purple, yellow as your piece color:")
    while True:
        answer = input()
        if answer == "blue":
            d.setFill("blue")
            break
        elif answer == "green":
            d.setFill("green")
            break
        elif answer == "purple":
            d.setFill("purple")
            break
        else:
            d.setFill("yellow")
            break

    # Moving the pieces based on the roll (a random number generator)
    def moveTo(self):
        oldPos = self.d.getCenter()
        oldX, oldY = oldPos.getX(), oldPos.getY()
        roll = 0.1
        newX, newY = oldPos.getX() + roll, oldPos.getY() + roll
        self.d.move(newX, newY)


#Determining whether the piece is queued, on the board, or completed its final lap
#    def alive(c):
#        stillPlaying = True
#        while True:
#            if c == (


def main():
    move = Piece()
    move.moveTo()
    while True:
        click = window.getMouse()
        move.moveTo()

# """
#         newX, newY = newPos.getX(), newPos.getY()
#         moveX = newX - oldX
#         moveY = newY - oldY
#         c.move(moveX, moveY)
#
# """
main()