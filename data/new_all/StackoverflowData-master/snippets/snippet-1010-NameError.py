#Source: https://stackoverflow.com/questions/54962989/attributeerror-turtle-object-has-no-attribute-addshape
image1 = "D:\Desktop\computing\Python\snake game\img\snake_head.png"
head = turtle.Turtle()
head.speed(0)
head.addshape(image1)
head.goto(0,0)
head.direction = "stop"