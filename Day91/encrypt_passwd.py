import turtle
import math

earth = turtle.Turtle()

def way_to_orbit(x,y, object, colors):
    object.dot(50, "yellow")
    object.color("white")
    object.fillcolor(colors)
    object.shape("circle")
    object.penup()
    object.setposition(x, y)
    object.pendown()


def ellipse(planeta):

    loop = True
    planeta_xvel = 0
    planeta_yvel = 1

    while loop:
        planeta_xvel += math.cos(math.radians(planeta.towards(0, 0))) * (1000 / (planeta.xcor() ** 2 + planeta.ycor() ** 2))
        planeta_yvel += math.sin(math.radians(planeta.towards(0, 0))) * (1000 / (planeta.xcor() ** 2 + planeta.ycor() ** 2))
        planeta.setposition(planeta.xcor() + planeta_xvel, planeta.ycor() + planeta_yvel)




way_to_orbit(375, 0, earth, "blue")

ellipse(earth)


turtle.done()