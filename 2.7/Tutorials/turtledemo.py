import turtle
bob=turtle.Turtle()
x=int(input("How many sides do you want on your shape"))
ang=360/x
while 0 < x:
    bob.forward(ang)
    bob.right(int(ang))
    x=x-1
turtle.done()
