# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64863278/what-is-the-solution-to-this-type-error-list-indices-must-be-integers-or-slices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
startX=_c_(400149, _a_(400147, _n_(400146, "random", lambda: random), "randint"), 20,_n_(400148, "cellWidth", lambda: cellWidth))
_l_(400150)
startY=_c_(400154, _a_(400152, _n_(400151, "random", lambda: random), "randint"), 20,_n_(400153, "cellHeight", lambda: cellHeight))
_l_(400155)
snakeCoords=[{"x":_n_(400156, "startX", lambda: startX),"y":_n_(400157, "startY", lambda: startY)},
             {"x":_n_(400158, "startX", lambda: startX)-1,"y":_n_(400159, "startY", lambda: startY)},
             {"x":_n_(400160, "startX", lambda: startX)-2,"y":_n_(400161, "startY", lambda: startY)}]
_l_(400162)