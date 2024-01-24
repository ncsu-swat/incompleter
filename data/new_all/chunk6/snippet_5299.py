# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67255437/typeerror-not-supported-between-instances-of-method-and-int-but-in-thi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(374365)

    _c_(374335, _a_(374334, _n_(374333, "wn", lambda: wn), "update"))  
    _l_(374336)  
    
    # Move the ball
    _c_(374344, _a_(374338, _n_(374337, "ball", lambda: ball), "setx"), _c_(374341, _a_(374340, _n_(374339, "ball", lambda: ball), "xcor")) + _a_(374343, _n_(374342, "ball", lambda: ball), "dx")) 
    _l_(374345) 
    _c_(374353, _a_(374347, _n_(374346, "ball", lambda: ball), "sety"), _c_(374350, _a_(374349, _n_(374348, "ball", lambda: ball), "ycor")) + _a_(374352, _n_(374351, "ball", lambda: ball), "dy"))
    _l_(374354)

    # Borders
    if _c_(374357, _a_(374356, _n_(374355, "ball", lambda: ball), "ycor")) > 290:
        _l_(374364)

        _c_(374360, _a_(374359, _n_(374358, "ball", lambda: ball), "sety"), 290)
        _l_(374361)
        _n_(374362, "ball", lambda: ball).dy *= -1
        _l_(374363)