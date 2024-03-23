#Source: https://stackoverflow.com/questions/51654811/attributeerror-turtle-object-has-no-attribute-pencolour
import turtle

t = turtle.Pen()    
t.speed(0)
colours = ["green", "blue", "dark purple", "grey"]

for x in range(100):
    t.pencolour( colours[ x % 4] )
    t.cirlce(2*x)
    t.left(91)