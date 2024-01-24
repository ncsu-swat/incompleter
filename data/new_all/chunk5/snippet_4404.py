# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56959631/im-getting-a-nameerror-from-using-the-event-function-from-pygame
#Drawing Rectangles (later used as buttons)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
batteryBtn = _c_(680490, _a_(680487, _a_(680486, _n_(680485, "pygame", lambda: pygame), "draw"), "rect"), _n_(680488, "display", lambda: display), _n_(680489, "red", lambda: red), (0,0,100,50))
_l_(680491)
bulbBtn = _c_(680497, _a_(680494, _a_(680493, _n_(680492, "pygame", lambda: pygame), "draw"), "rect"), _n_(680495, "display", lambda: display), _n_(680496, "green", lambda: green), (100,0,100,50))
_l_(680498)
resistorBtn = _c_(680504, _a_(680501, _a_(680500, _n_(680499, "pygame", lambda: pygame), "draw"), "rect"), _n_(680502, "display", lambda: display), _n_(680503, "blue", lambda: blue), (200,0,100,50))
_l_(680505)

#Initialising the images
img1 = _c_(680509, _a_(680508, _a_(680507, _n_(680506, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\Battery.jpg')
_l_(680510)
img2 = _c_(680514, _a_(680513, _a_(680512, _n_(680511, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\bulbOn.jpg')
_l_(680515)
img3 = _c_(680519, _a_(680518, _a_(680517, _n_(680516, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\bulbOff.jpg')
_l_(680520)
img4 = _c_(680524, _a_(680523, _a_(680522, _n_(680521, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\Resistor.jpg')
_l_(680525)

if _a_(680527, _n_(680526, "event", lambda: event), "type") == _a_(680529, _n_(680528, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
    _l_(680543)

    if _a_(680531, _n_(680530, "event", lambda: event), "button") == 1:
        _l_(680542)

        if _c_(680535, _a_(680533, _n_(680532, "batteryBtn", lambda: batteryBtn), "collidepoint"), _n_(680534, "pos", lambda: pos)):
            _l_(680541)

            _c_(680539, _a_(680537, _n_(680536, "display", lambda: display), "blit"), _n_(680538, "img1", lambda: img1), (0, 100))
            _l_(680540)