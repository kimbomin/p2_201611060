import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def line():
    t1.penup()
    t1.goto(50,100)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.home()

line()

line1=[(50,100),(150,100)]
x1=line1[0][0]-1
y1=line1[0][1]-1
x2=line1[1][0]+1
y2=line1[1][1]+1

pos1=(x1,y1)
pos2=(x2,y2)

def isOnLine(point,pos1,pos2):
    if x1<=point[0]<=x2 and y1<=point[1]<=y2:
        t1.color('blue')
        line()

def keyup():
    t1.fd(50)
    point=t1.pos()
    isOnLine(point,pos1,pos2)
        
def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    t1.back(45)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")

def mousegoto(x,y):
    t1.setpos(x,y)
    point=t1.pos()
    isOnLine(point,pos1,pos2)

def addMouse():
    wn.onclick(mousegoto)

addKeys()

addMouse()

wn.listen()

turtle.mainloop()