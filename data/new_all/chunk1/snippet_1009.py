# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54962989/attributeerror-turtle-object-has-no-attribute-addshape
# Snake head
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
head = _c_(412385, _a_(412384, _n_(412383, "turtle", lambda: turtle), "Turtle"))                      # create an instance of the class turtle called 'head'
_l_(412386)                      # create an instance of the class turtle called 'head'
_c_(412389, _a_(412388, _n_(412387, "head", lambda: head), "speed"), 0)                               # call the speed method
_l_(412390)                               # call the speed method
_c_(412393, _a_(412392, _n_(412391, "head", lambda: head), "shape"), "square")                        # defines the shape of the snakes head
_l_(412394)                        # defines the shape of the snakes head
_c_(412397, _a_(412396, _n_(412395, "head", lambda: head), "color"), "black")                         # defines the colour of the snakes head
_l_(412398)                         # defines the colour of the snakes head
_c_(412401, _a_(412400, _n_(412399, "head", lambda: head), "penup"))                                # stop the snake from drawing when moving
_l_(412402)                                # stop the snake from drawing when moving
_c_(412405, _a_(412404, _n_(412403, "head", lambda: head), "goto"), 0,0)                              # moves the snakes head to the coordinates 0,0 on the screen.
_l_(412406)                              # moves the snakes head to the coordinates 0,0 on the screen.
_n_(412407, "head", lambda: head).direction = "stop"                     # stops the turtles head from moving strait away
_l_(412408)                     # stops the turtles head from moving strait away