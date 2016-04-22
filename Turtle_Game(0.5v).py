import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
oldhead=t1.heading()
wn.bgcolor("black")

def drawSat(size,pos):
    t1.setheading(oldhead)
    t1.pencolor("red")
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.left(90)
        
def drawTat(size,pos):
    t1.setheading(oldhead)
    t1.pencolor("orange")
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,3):
        t1.forward(size)
        t1.left(120)
        
def drawStarat(size,pos):
    t1.setheading(oldhead)
    t1.pencolor("yellow")
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,5):
        t1.forward(size)
        t1.left(144)

drawSat(100,(-300,0))
drawTat(100,(0,300))
drawStarat(100,(300,0))

t1.penup()
t1.home()
t1.pencolor("green")

def w():
    t1.forward(45)
def a():
    t1.left(45)
def d():
    t1.right(45)
def s():
    t1.back(45)

wn.onkey(w, "Up")
wn.onkey(a, "Left")
wn.onkey(d, "Right")
wn.onkey(s, "Down")

wn.listen()

raw_input("If you want to exit this game, press the enter key")