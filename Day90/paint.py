from turtle import *

def line(start, end):
    up()
    goto(start[0], start[1])
    down()
    goto(end[0], end[1])


def square(start, end):
    up()
    goto(start[0], start[1])
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

def tap(x, y):
    print(x, y)
    start = state['start']
    if start is None:
        state['start'] = (x, y)
    else:
        shape = state['shape']
        end = (x, y)
        shape(start, end)
        state['start'] = None


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'k')
onkey(lambda: color('green'), 'g')
done()