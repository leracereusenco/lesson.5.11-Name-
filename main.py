import turtle #biblioteca care permite sa desenam

draw = turtle.Turtle() #draw - nume, turtle.Turtle() - initializare

#for i in range(4): #se deseneaza un patrat (are 4 laturi)
    #draw.forward(250) #lungimea, care se masoara in pixel
    #draw.right(90) #se intoarce intr-o parte si cu ce unghi (cate grade)


#Tot aceeasi, dar mai simplu
#num_sides = 360
#side_lenght = 5
#angle = 360.0 / num_sides

#for i in range(num_sides):
    #draw.forward(side_lenght)
    #draw.left(angle)


#window = turtle.Screen()
#window.bgcolor("red") #culoarea backgroundului
#window.title("My Window for Turtle") #se schimba numele

#draw.color("yellow") #se schimba culoarea desenului

#def shapefunc(size, sides):
    #for i in range(sides):
        #draw.fd(size)
        #draw.right(360 / sides)
        #size = size - 5 #latura se va scurta de fiecare data cu cate 5 pixels

#shapefunc(150, 4)
#shapefunc(160, 4)
#shapefunc(170, 4)
#shapefunc(180, 4)
#shapefunc(190, 4)
#shapefunc(200, 4)
#shapefunc(190, 1)

#window2 = turtle.Screen()
#turtle.speed(30) #viteza
#pen = turtle.Pen()
#turtle.speed(90)
# = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'white']
#window2.bgcolor('black')

#for i in range(360):
    #turtle.circle(2 * i)
    #turtle.circle(-2 * i)
    #turtle.left(i)

    #var = i/100 + 1
    #pen.pencolor(color[i%9])
    #pen.width(var)
    #pen.forward(i)
    #pen.left(189)


pen = turtle.Pen()
pen.penup() #se ridica pixul
pen.goto(-300, 100) #schimba coordonatele inceputului desenului
pen.pencolor('purple')

def drawL():
    pen.pendown() #se coboara pixul, se poate desena
    pen.right(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(55)

def drawE():
    pen.pendown()  # se coboara pixul, se poate desena
    pen.forward(50)
    pen.right(180)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(35)
    pen.right(180)
    pen.forward(35)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)

def drawR():
    pen.pendown()
    pen.right(90)
    pen.forward(100)
    pen.right(180)
    pen.forward(100)
    pen.right(90)
    for i in range(12):
        pen.forward(7)
        pen.right(180/12)
    pen.forward(7)
    pen.right(235)
    pen.forward(60)

def drawA():
    pen.pendown()
    pen.right(50)
    pen.forward(100)
    pen.right(180)
    pen.forward(100)
    pen.right(155)
    pen.forward(100)
    pen.right(180)
    pen.forward(50)
    pen.left(80)
    pen.forward(25)



drawL()
pen.penup()
pen.goto(-220, 100)
drawE()
pen.penup()
pen.goto(-140, 100)
drawR()
pen.penup()
pen.goto(-65, 100)
drawA()
pen.penup()
pen.goto(0, 0)













turtle.done()
turtle.exitonclick()





