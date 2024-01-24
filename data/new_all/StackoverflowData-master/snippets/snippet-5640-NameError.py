#Source: https://stackoverflow.com/questions/56527543/attributeerror-turtle-object-has-no-attribute-onscreenclick
c = turtle.Turtle('arrow'); c.color('black'); c.shapesize(csize); 
c.penup()
c.speed(5);

c.onscreenclick(c.goto)
c.listen()