import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
wn.bgcolor("skyblue")
t2.shape("turtle")
t2.color("green")
t2.pencolor("black")
t2.penup()
t2.goto(0,0)
t1.speed(0)
t1.penup()
result=0
print "Welcome to the Bomin's game!"

def Square():
    t1.goto(-400,100)
    t1.pencolor("blue")
    t1.pendown()
    for i in range(0,4):
        t1.fd(200)
        t1.left(90)
    t1.penup()
    t1.goto(-400,250)
    t1.pendown()
    t1.fd(100)
    t1.back(50)
    t1.right(90)
    t1.fd(50)
    t1.penup()
    t1.goto(-390,290)
    t1.pendown()
    t1.setheading(0)
    t1.fillcolor("white")
    t1.begin_fill()
    for i in range(0,4):
        t1.fd(30)
        t1.right(90)
    t1.end_fill()
    t1.setheading(0)
    t1.penup()
    t1.goto(-300,200)
    t1.pendown()
    t1.fd(100)
    t1.back(50)
    t1.left(90)
    t1.fd(50)
    t1.back(50)
    t1.setheading(0)
    t1.penup()
    t1.goto(-350,150)
    t1.pendown()
    t1.fd(100)
    t1.right(90)
    t1.fd(50)
    t1.setheading(0)
    t1.penup()

def getCoords():
    myfile=open('circle.txt')
    coords=list()
    for i in myfile:
        cirpos=i.split(',')
        coords.append([cirpos[0],cirpos[1].strip()])
    myfile.close()
    return coords
coords=getCoords()

def Circle(coords):
    for coord in coords:
        x1=int(coords[0][0])
        y1=int(coords[0][1])
    t1.color("black")
    t1.fillcolor("black")
    t1.goto(x1,y1)
    t1.pendown()
    t1.begin_fill()
    t1.circle(100)
    t1.end_fill()
    t1.penup()
    t1.goto(-50,250)
    t1.pencolor("white")
    t1.pendown()
    t1.left(45)
    t1.fd(30)
    t1.back(60)
    t1.fd(30)
    t1.right(90)
    t1.fd(30)
    t1.back(60)
    t1.fd(30)
    t1.left(45)
    t1.penup()
    t1.goto(50,250)
    t1.pendown()
    t1.left(45)
    t1.fd(30)
    t1.back(60)
    t1.fd(30)
    t1.right(90)
    t1.fd(30)
    t1.back(60)
    t1.fd(30)
    t1.left(45)
    t1.penup()
    t1.goto(0,150)
    t1.fillcolor("white")
    t1.begin_fill()
    t1.circle(25)
    t1.end_fill()
    t1.penup()
    
def Triangle():
    t1.goto(200,100)
    t1.pencolor("white")
    t1.pendown()
    for i in range(0,3):
        t1.fd(200)
        t1.left(120)
    t1.penup()
    t1.goto(350,100)
    t1.pendown()
    t1.left(120)
    t1.fd(100)
    t1.left(120)
    t1.fd(50)
    t1.left(120)
    t1.fd(20)
    t1.fillcolor("blue")
    t1.begin_fill()
    t1.circle(10)
    t1.end_fill()
    t1.setheading(0)
    t1.penup()

def great():
    (x,y)=t2.pos()
    global result
    if -390<=x<=-360 and 260<=y<=290:
        result=result+10
        print ("Your score : %d" %result)
        t2.goto(0,0)

def bad():
    (x,y)=t2.pos()
    global result
    if -90<x<90 and 110<y<290:
        result=result-result
        print ("Your score : %d. You choose death." %result)
        t2.goto(0,0)

def easy():
    (x,y)=t2.pos()
    global result
    if 285<=x<=315 and 125<=y<=145:
        result=result+5
        print ("Your score : %d" %result)
        t2.goto(0,0)

def setting():
    Square()
    Triangle()
    Circle(coords)

def w():
    t2.forward(25)
    great()
    bad()
    easy()
def a():
    t2.left(45)
def d():
    t2.right(45)
def s():
    t2.back(25)

wn.onkey(w, "Up")
wn.onkey(a, "Left")
wn.onkey(d, "Right")
wn.onkey(s, "Down")

setting()
wn.listen()
turtle.mainloop()

raw_input('Your final score is %d. if you want exit this game, press the enter.' %result)