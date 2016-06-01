import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def getCoordsFromFile():
    frec=open('reccoords.txt')
    coords=[]
    for line in frec:
        line1=line.split(',')
        coords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
    frec.close()
    return coords

mycoords=getCoordsFromFile()

def drawSquareWithCoords(mycoords):
    for coord in mycoords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
    print x1,y1,x2,y2
    t1.penup()
    t1.goto(x1,y1)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.right(90)

drawSquareWithCoords(mycoords)