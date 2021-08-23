import turtle

screen = turtle.getscreen()
point = turtle.Turtle()

def move(pos=(0,0)):
	point.penup()
	point.goto(pos)
	point.pendown()

pos_cub_x = -100
pos_cub_y = -100
line = 100
move((pos_cub_x, pos_cub_y))
for i in range(11):
	for i in range(4):
		point.forward(line)
		point.right(90)
	line = line - 20
	pos_cub_x -= 20
	pos_cub_y -= 10
	move((pos_cub_y, pos_cub_y))

pos_c_x = 150
pos_c_y = -100
line = 100
move((pos_c_x, pos_c_y))
for i in range(5):
	for i in range(4):
		point.forward(line)
		point.right(90)
	line -= 20
	pos_c_x += 10
	pos_c_y -= 10
	move((pos_c_x, pos_c_y))

move((-50,200))
for i in range(5):
	point.forward(100)
	point.right(144)


move()
point.seth(0)
point.left(15)
point.forward(100)

move()

point.right(180)
point.circle(5,180)
point.right(12)
point.forward(100)
point.circle(15, 195)

point.circle(5, 100)
point.right(90)
point.forward(5)
point.left(70)
point.forward(5)
point.left(30)
point.forward(5)
point.circle(10,30)
point.right(30)
point.forward(10)

move((28.53,9.27))
point.forward(25)
move(((70.38,17.39)))
point.forward(30)

move()
turtle.done()

