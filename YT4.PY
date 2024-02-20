import turtle
pen = turtle.Turtle()
pen.hideturtle()

pen.forward(120)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(50)

pen.penup()
pen.goto(7, 8)
pen.write('SHREE RAM', fant = ('Courier', 12, 'normal'))
pen.pendown()

def button click(x, y):
if (x > 0) and (x < 81) and (y > 0) and (y < 30):
print('JAI SHREE RAM JII)
pen.screen.bgpic('Shree_ram.gif')
pen.screen.bgcolor('black')
pen.speed(5)
pen.up()
pen.lt (270)
pen.pencolor('white')
pen.fd(950)
pen.down()
pen.pensize(5)
pen.rt(90)
pen.fd (480)
pen.fd(1875)


