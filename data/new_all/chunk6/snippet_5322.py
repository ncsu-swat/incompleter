# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67255437/typeerror-not-supported-between-instances-of-method-and-int-but-in-thi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(354083)

    _c_(354053, _a_(354052, _n_(354051, "wn", lambda: wn), "update"))  
    _l_(354054)  
    
    # Move the ball
    _c_(354062, _a_(354056, _n_(354055, "ball", lambda: ball), "setx"), _c_(354059, _a_(354058, _n_(354057, "ball", lambda: ball), "xcor")) + _a_(354061, _n_(354060, "ball", lambda: ball), "dx")) 
    _l_(354063) 
    _c_(354071, _a_(354065, _n_(354064, "ball", lambda: ball), "sety"), _c_(354068, _a_(354067, _n_(354066, "ball", lambda: ball), "ycor")) + _a_(354070, _n_(354069, "ball", lambda: ball), "dy"))
    _l_(354072)

    # Borders
    if _c_(354075, _a_(354074, _n_(354073, "ball", lambda: ball), "ycor")) > 290:
        _l_(354082)

        _c_(354078, _a_(354077, _n_(354076, "ball", lambda: ball), "sety"), 290)
        _l_(354079)
        _n_(354080, "ball", lambda: ball).dy *= -1
        _l_(354081)