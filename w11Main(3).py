import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

t1.shape("turtle")

t1.pencolor("green")

wn.bgpic("C:\Users\KBM\Desktop\myMaze.gif")

def w():
    t1.fd(50)

def a():
    t1.left(90)

def s():
    t1.back(50)

def d():
    t1.right(90)

def addKeys():
    wn.onkey(w,"Up")
    wn.onkey(a,"Left")
    wn.onkey(s,"Down")
    wn.onkey(d,"Right")


def mousegoto(x,y):
    t1.setpos(x,y)
    if 300<x<400 and 200<y<300:
        print "YES_YES_YES!!"

def addMouse():
    wn.onclick(mousegoto)

addMouse()

addKeys()

wn.listen()

def drawSquareAt(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)

drawSquareAt(100,(300,300))

t1.penup()
t1.home()

turtle.mainloop()