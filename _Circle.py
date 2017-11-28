import turtle
from graphics import *
import random

s=3
win = GraphWin("My Fart", 100*s, 100*s)
seq = [s*20, s*40, s*60, s*80]



def 


def main(color):
    
    c = Circle(Point(random.choice(seq),random.choice(seq)), 10)
    c.setFill(color)
    c.draw(win)
    ##print(win.getMouse()) # pause for click in window
    ##win.close()

col = ['blue', 'green', 'red', 'yellow']
n=4
COL=col[:n]


for i in COL:
    main(i)
    


