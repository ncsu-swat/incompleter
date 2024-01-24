# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67366029/win-display-blitrightimg-arrx-20-arry-20-attributeerror-pygame-surface-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame, sys, random
    _l_(426045)

except ImportError:
    pass

_c_(426048, _a_(426047, _n_(426046, "pygame", lambda: pygame), "init"))
_l_(426049)

win = _c_(426053, _a_(426052, _a_(426051, _n_(426050, "pygame", lambda: pygame), "display"), "set_mode"), (500,500))
_l_(426054)

_c_(426058, _a_(426057, _a_(426056, _n_(426055, "pygame", lambda: pygame), "display"), "set_caption"), "Python Night Funkin'")
_l_(426059)

upImg = _c_(426063, _a_(426062, _a_(426061, _n_(426060, "pygame", lambda: pygame), "image"), "load"), "up.png")
_l_(426064)
downImg = _c_(426068, _a_(426067, _a_(426066, _n_(426065, "pygame", lambda: pygame), "image"), "load"), "down.png")
_l_(426069)
rightImg = _c_(426073, _a_(426072, _a_(426071, _n_(426070, "pygame", lambda: pygame), "image"), "load"), "right.png")
_l_(426074)
leftImg = _c_(426078, _a_(426077, _a_(426076, _n_(426075, "pygame", lambda: pygame), "image"), "load"), "left.png")
_l_(426079)


test = 0
_l_(426080)
x = 0
_l_(426081)
y = 0
_l_(426082)
arrX = 0
_l_(426083)
arrY = 0
_l_(426084)
height = 500
_l_(426085)
width = 500
_l_(426086)
arrHeight = 20
_l_(426087)
arrWidth = 20
_l_(426088)
arrSpeed = 5
_l_(426089)

def drawWindow():
    _l_(426171)

    _c_(426092, _a_(426091, _n_(426090, "win", lambda: win), "fill"), (0,0,0))
    _l_(426093)
    _c_(426098, _a_(426096, _a_(426095, _n_(426094, "pygame", lambda: pygame), "draw"), "rect"), _n_(426097, "win", lambda: win), (20,20,20), (70,370, 60, 60))
    _l_(426099)
    _c_(426104, _a_(426102, _a_(426101, _n_(426100, "pygame", lambda: pygame), "draw"), "rect"), _n_(426103, "win", lambda: win), (20,20,20), (170,370, 60, 60))
    _l_(426105)
    _c_(426110, _a_(426108, _a_(426107, _n_(426106, "pygame", lambda: pygame), "draw"), "rect"), _n_(426109, "win", lambda: win), (20,20,20), (270,370, 60, 60))
    _l_(426111)
    _c_(426116, _a_(426114, _a_(426113, _n_(426112, "pygame", lambda: pygame), "draw"), "rect"), _n_(426115, "win", lambda: win), (20,20,20), (370,370, 60, 60))
    _l_(426117)
    _c_(426124, _a_(426120, _a_(426119, _n_(426118, "pygame", lambda: pygame), "draw"), "rect"), _n_(426121, "win", lambda: win), (255, 0, 0), (_n_(426122, "x", lambda: x)-20, _n_(426123, "y", lambda: y)-20, 40, 40))
    _l_(426125)
    if _n_(426126, "arrX", lambda: arrX) == 100:
        _l_(426135)

        _c_(426133, _a_(426129, _a_(426128, _n_(426127, "win", lambda: win), "display"), "blit"), _n_(426130, "rightImg", lambda: rightImg), (_n_(426131, "arrX", lambda: arrX)-20,_n_(426132, "arrY", lambda: arrY)-20))
        _l_(426134)
    if _n_(426136, "arrX", lambda: arrX) == 200:
        _l_(426145)

        _c_(426143, _a_(426139, _a_(426138, _n_(426137, "win", lambda: win), "display"), "blit"), _n_(426140, "downImg", lambda: downImg), (_n_(426141, "arrX", lambda: arrX)-20,_n_(426142, "arrY", lambda: arrY)-20))
        _l_(426144)
    if _n_(426146, "arrX", lambda: arrX) == 300:
        _l_(426155)

        _c_(426153, _a_(426149, _a_(426148, _n_(426147, "win", lambda: win), "display"), "blit"), _n_(426150, "upImg", lambda: upImg), (_n_(426151, "arrX", lambda: arrX)-20,_n_(426152, "arrY", lambda: arrY)-20))
        _l_(426154)
    if _n_(426156, "arrX", lambda: arrX) == 400:
        _l_(426165)

        _c_(426163, _a_(426159, _a_(426158, _n_(426157, "win", lambda: win), "display"), "blit"), _n_(426160, "leftImg", lambda: leftImg), (_n_(426161, "arrX", lambda: arrX)-20,_n_(426162, "arrY", lambda: arrY)-20))
        _l_(426164)
    _c_(426169, _a_(426168, _a_(426167, _n_(426166, "pygame", lambda: pygame), "display"), "update"))
    _l_(426170)
clock = _c_(426175, _a_(426174, _a_(426173, _n_(426172, "pygame", lambda: pygame), "time"), "Clock"));
_l_(426176)

run = True
_l_(426177)
arrowX = [100, 200, 300, 400]
_l_(426178)
Arrow = []
_l_(426179)
while _n_(426180, "run", lambda: run):
    _l_(426196)

    _c_(426183, _a_(426182, _n_(426181, "clock", lambda: clock), "tick"), 30);
    _l_(426184)
    for event in _c_(426188, _a_(426187, _a_(426186, _n_(426185, "pygame", lambda: pygame), "event"), "get")):
        _l_(426195)

        if _a_(426190, _n_(426189, "event", lambda: event), "type") == _a_(426192, _n_(426191, "pygame", lambda: pygame), "QUIT"):
            _l_(426194)

            run = False
            _l_(426193)