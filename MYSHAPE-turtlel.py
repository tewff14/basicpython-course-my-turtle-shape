import turtle
tao = turtle.Pen()
tao.shape('turtle')

def myShape():
    for i in range(3) :
        tao.forward(100)
        tao.left(120)

myShape()
