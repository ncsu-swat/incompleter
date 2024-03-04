#Source: https://stackoverflow.com/questions/36120585/attributeerror-int-object-has-no-attribute-fd
import turtle

t = turtle.Turtle()
turtle.mainloop()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

draw(5, 10, 15)