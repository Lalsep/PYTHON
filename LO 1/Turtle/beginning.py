import turtle

orpeg = turtle.Turtle()

# orpeg.forward(100)	
# orpeg.left(45)
# orpeg.forward(100)
# orpeg.right(90)
# orpeg.forward(100)
orpeg.color("blue", "yellow")
orpeg.begin_fill()
n = int(input('Podaj liczbę boków n =   '))
for i in range(n):
	orpeg.forward(20)
	orpeg.left(360/n)
orpeg.penup()
orpeg.right(120)
orpeg.forward(200)
orpeg.left(120)
orpeg.left(90)
orpeg.pendown()

for i in range(4):
	orpeg.forward(100)
	orpeg.left(90)

orpeg.end_fill()

turtle.done()