# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57868309/how-to-fix-attributeerror-graphwin-object-has-no-attribute-yup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from graphics import *
    _l_(444980)

except ImportError:
    pass

_c_(444985, _n_(444981, "print", lambda: print), _c_(444984, _n_(444982, "dir", lambda: dir), _n_(444983, "GraphWin", lambda: GraphWin)))
_l_(444986)

def main():
    _l_(445085)

    win = _c_(444988, _n_(444987, "GraphWin", lambda: GraphWin), 'Face', 200, 150) # give title and dimensions
    _l_(444989) # give title and dimensions
    _c_(444992, _a_(444991, _n_(444990, "win", lambda: win), "yUp")) # make right side up coordinates!
    _l_(444993) # make right side up coordinates!

    head = _c_(444997, _n_(444994, "Circle", lambda: Circle), _c_(444996, _n_(444995, "Point", lambda: Point), 40,100), 25) # set center and radius
    _l_(444998) # set center and radius
    _c_(445001, _a_(445000, _n_(444999, "head", lambda: head), "setFill"), "yellow")
    _l_(445002)
    _c_(445006, _a_(445004, _n_(445003, "head", lambda: head), "draw"), _n_(445005, "win", lambda: win))
    _l_(445007)

    eye1 = _c_(445011, _n_(445008, "Circle", lambda: Circle), _c_(445010, _n_(445009, "Point", lambda: Point), 30, 105), 5)
    _l_(445012)
    _c_(445015, _a_(445014, _n_(445013, "eye1", lambda: eye1), "setFill"), 'blue')
    _l_(445016)
    _c_(445020, _a_(445018, _n_(445017, "eye1", lambda: eye1), "draw"), _n_(445019, "win", lambda: win))
    _l_(445021)

    eye2 = _c_(445027, _n_(445022, "Line", lambda: Line), _c_(445024, _n_(445023, "Point", lambda: Point), 45, 105), _c_(445026, _n_(445025, "Point", lambda: Point), 55, 105)) # set endpoints
    _l_(445028) # set endpoints
    _c_(445031, _a_(445030, _n_(445029, "eye2", lambda: eye2), "setWidth"), 3)
    _l_(445032)
    _c_(445036, _a_(445034, _n_(445033, "eye2", lambda: eye2), "draw"), _n_(445035, "win", lambda: win))
    _l_(445037)

    mouth = _c_(445043, _n_(445038, "Oval", lambda: Oval), _c_(445040, _n_(445039, "Point", lambda: Point), 30, 90), _c_(445042, _n_(445041, "Point", lambda: Point), 50, 85)) # set corners of bounding box
    _l_(445044) # set corners of bounding box
    _c_(445047, _a_(445046, _n_(445045, "mouth", lambda: mouth), "setFill"), "red")
    _l_(445048)
    _c_(445052, _a_(445050, _n_(445049, "mouth", lambda: mouth), "draw"), _n_(445051, "win", lambda: win))
    _l_(445053)

    label = _c_(445057, _n_(445054, "Text", lambda: Text), _c_(445056, _n_(445055, "Point", lambda: Point), 100, 120), 'A face')
    _l_(445058)
    _c_(445062, _a_(445060, _n_(445059, "label", lambda: label), "draw"), _n_(445061, "win", lambda: win))
    _l_(445063)

    message = _c_(445070, _n_(445064, "Text", lambda: Text), _c_(445069, _n_(445065, "Point", lambda: Point), _c_(445068, _a_(445067, _n_(445066, "win", lambda: win), "getWidth"))/2, 20), 'Click anywhere to quit.')
    _l_(445071)
    _c_(445075, _a_(445073, _n_(445072, "message", lambda: message), "draw"), _n_(445074, "win", lambda: win))
    _l_(445076)
    _c_(445079, _a_(445078, _n_(445077, "win", lambda: win), "getMouse"))
    _l_(445080)
    _c_(445083, _a_(445082, _n_(445081, "win", lambda: win), "close"))
    _l_(445084)

_c_(445087, _n_(445086, "main", lambda: main))
_l_(445088)