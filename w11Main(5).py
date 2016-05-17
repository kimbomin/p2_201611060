coord=[(100,100),(200,200)]
x1=coord[0][0]
y1=coord[0][1]
x2=coord[1][0]
y2=coord[1][1]

curpos=(150,100)
x=curpos[0]
y=curpos[1]

def isinRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye

line1=[(50,100),(150,100)]

xy=(70,100)

x1=line1[0][0]-1
y1=line1[0][1]-1
x2=line1[1][0]+1
y2=line1[1][1]+1
x=xy[0]
y=xy[1]
print x1<=x<=x2 and y1<=y<=y2

def isOnLine(point,pos1,po2):
    x1=line1[0][0]-1
    y1=line1[0][1]-1
    x2=line1[1][0]+1
    y2=line1[1][1]+1
    return isinRectangle(point,[(x1,y1),(x2,y2)])

print isOnLine((70,100),(50,100),(150,100))
print isOnLine((70,101),(50,100),(150,100))
print isOnLine((40,101),(50,100),(150,100))

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()

t2.penup()
t2.setpos(200,200)
t2.pendown()

coord=[(200,100),(300,200)]

def drawS():
    for i in range(4):
        t2.fd(100)
        t2.right(90)
        
drawS()

def keyup():
    pt=t1.pos()
    print "up",pt
    t1.write(pt)
    t1.forward(45)
    if isinRectangle(pt,coord):
        t2.pencolor("blue")
        t2.penup()
        t2.setpos(100,100)
        t2.pendown()
        drawS()
        
def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pt=t1.pos()
    print "down",pt
    t1.write(pt)
    t1.back(45)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")

def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)

def addMouse():
    wn.onclick(mousegoto)

def gamePlay():
    import turtle
    addKeys()
    wn.listen()
    turtle.mainloop()
    
def lab10():
    gamePlay()
    
lab10()