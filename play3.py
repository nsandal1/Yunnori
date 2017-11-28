from graphics import *
import random

#Graphics for Yunnori
s=3
from graphics import *

window = GraphWin("gameWindow", 1000*s, 1000*s)
myImage = Image(Point(400,400), "baba.gif")
myImage.draw(window)


seq = [s*20, s*40, s*60, s*80]

def main(color):
    c = Circle(Point(random.choice(seq),random.choice(seq)), 10)
    c.setFill(color)
    c.draw(window)
    ##print(win.getMouse()) # pause for click in window
    ##win.close()

col = ['blue', 'green', 'red', 'yellow']
n=2
COL=col[:n]


for i in COL:
    main(i)


##def moveTo(c, newPos):
##    oldPos=c.getCenter()
##    oldX, oldY = oldPos.getX(), oldPos.getY()
##    newX, newY = newPos.getX(), newPos.getY()
##    moveX = newX - oldX
##    moveY = newY - oldY
##    c.move(moveX, moveY)
##    #return c
##
##
##def main():
##    myPoint=window.getMouse()
##    myX, myY = myPoint.getX(), myPoint.getY()
##    mc = Circle(myPoint, 10)
##    mc.setFill(i)
##    mc.draw(window)
##    return mc

window.mainloop()

##c=main()
##for x in range(1,100):
##    newPos = window.getMouse()
##    moveTo(c, newPos)
    
"""
class Player(object):
    stillPlaying=True
    def __init__(self, rolls=0, charac):
        self.rolls=rolls
        self.position=0
        

    def randnum(self, rolls, position):
        roll = "Yes"
        while roll == "Yes":
            list=(-1, 1, 2, 3, 4, 5)
            self.rolls=random.randint(list)
            self.position=self.position+self.rolls
        if self.rolls == 5:
            #Re-enter the "While" loop
            roll == "Yes"


class Node(object):
    def getposition(X, Y):
        player.getNode().getX()
        player.getNode().getY
"""
