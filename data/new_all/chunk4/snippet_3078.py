# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48653466/how-to-avoid-typeerror-from-attempt-to-divide
#A program that allows people to enter information and calculate how much a tip should be
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from graphics import *
    _l_(631792)

except ImportError:
    pass
try:
    import math
    _l_(631794)

except ImportError:
    pass
#setting up the window
win = _c_(631796, _n_(631795, "GraphWin", lambda: GraphWin), "Tip Calculator", 400, 400)
_l_(631797)
_c_(631800, _a_(631799, _n_(631798, "win", lambda: win), "setBackground"), "teal")
_l_(631801)
#setting up the input
checksub = _c_(631805, _n_(631802, "Text", lambda: Text), _c_(631804, _n_(631803, "Point", lambda: Point), 150, 150,), "What is the subtotal of the check?:")
_l_(631806)
_c_(631810, _a_(631808, _n_(631807, "checksub", lambda: checksub), "draw"), _n_(631809, "win", lambda: win))
_l_(631811)
checksub2 = _c_(631815, _n_(631812, "Entry", lambda: Entry), _c_(631814, _n_(631813, "Point", lambda: Point), 300,152), 5)
_l_(631816)
_c_(631820, _a_(631818, _n_(631817, "checksub2", lambda: checksub2), "draw"), _n_(631819, "win", lambda: win))
_l_(631821)

tiprate = _c_(631825, _n_(631822, "Text", lambda: Text), _c_(631824, _n_(631823, "Point", lambda: Point), 150,190), "What is the tip rate?:")
_l_(631826)
_c_(631830, _a_(631828, _n_(631827, "tiprate", lambda: tiprate), "draw"), _n_(631829, "win", lambda: win))
_l_(631831)
tiprate2 = _c_(631835, _n_(631832, "Entry", lambda: Entry), _c_(631834, _n_(631833, "Point", lambda: Point), 250,190), 3)
_l_(631836)
_c_(631840, _a_(631838, _n_(631837, "tiprate2", lambda: tiprate2), "draw"), _n_(631839, "win", lambda: win))
_l_(631841)
#button
Buttontext = _c_(631845, _n_(631842, "Text", lambda: Text), _c_(631844, _n_(631843, "Point", lambda: Point), 150,210), "Compute")
_l_(631846)
_c_(631850, _a_(631848, _n_(631847, "Buttontext", lambda: Buttontext), "draw"), _n_(631849, "win", lambda: win))
_l_(631851)
Buttonbox = _c_(631857, _n_(631852, "Rectangle", lambda: Rectangle), _c_(631854, _n_(631853, "Point", lambda: Point), 100,230),_c_(631856, _n_(631855, "Point", lambda: Point), 200,199))
_l_(631858)
_c_(631862, _a_(631860, _n_(631859, "Buttonbox", lambda: Buttonbox), "draw"), _n_(631861, "win", lambda: win))
_l_(631863)
#Calculations
_c_(631866, _a_(631865, _n_(631864, "win", lambda: win), "getMouse"))
_l_(631867)
tip = _c_(631870, _a_(631869, _n_(631868, "tiprate2", lambda: tiprate2), "getText"))
_l_(631871)
check = _c_(631874, _a_(631873, _n_(631872, "checksub2", lambda: checksub2), "getText"))
_l_(631875)
_c_(631878, _n_(631876, "float", lambda: float), taxsum = _n_(631877, "check", lambda: check) / 4)
_l_(631879)
_c_(631883, _n_(631880, "float", lambda: float), checktax = _n_(631881, "taxsum", lambda: taxsum) + _n_(631882, "check", lambda: check))
_l_(631884)
_c_(631888, _n_(631885, "float", lambda: float), tipsum = _n_(631886, "checktax", lambda: checktax) / _n_(631887, "tip", lambda: tip))
_l_(631889)
_c_(631893, _n_(631890, "float", lambda: float), checksum = (_n_(631891, "tipsum", lambda: tipsum) + _n_(631892, "checktax", lambda: checktax)))
_l_(631894)
#presenting the output
tipoutput = _c_(631898, _n_(631895, "Text", lambda: Text), _c_(631897, _n_(631896, "Point", lambda: Point), 150,250), "The tip rate is: tipsum")
_l_(631899)
_c_(631903, _a_(631901, _n_(631900, "tipoutput", lambda: tipoutput), "draw"), _n_(631902, "win", lambda: win))
_l_(631904)
checkoutput = _c_(631908, _n_(631905, "Text", lambda: Text), _c_(631907, _n_(631906, "Point", lambda: Point), 150,260), "The Check total is: checksum")
_l_(631909)
_c_(631913, _a_(631911, _n_(631910, "checkoutput", lambda: checkoutput), "draw"), _n_(631912, "win", lambda: win))
_l_(631914)