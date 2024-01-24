# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56959631/im-getting-a-nameerror-from-using-the-event-function-from-pygame
#Drawing Rectangles (later used as buttons)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
batteryBtn = _c_(659387, _a_(659384, _a_(659383, _n_(659382, "pygame", lambda: pygame), "draw"), "rect"), _n_(659385, "display", lambda: display), _n_(659386, "red", lambda: red), (0,0,100,50))
_l_(659388)
bulbBtn = _c_(659394, _a_(659391, _a_(659390, _n_(659389, "pygame", lambda: pygame), "draw"), "rect"), _n_(659392, "display", lambda: display), _n_(659393, "green", lambda: green), (100,0,100,50))
_l_(659395)
resistorBtn = _c_(659401, _a_(659398, _a_(659397, _n_(659396, "pygame", lambda: pygame), "draw"), "rect"), _n_(659399, "display", lambda: display), _n_(659400, "blue", lambda: blue), (200,0,100,50))
_l_(659402)

#Initialising the images
img1 = _c_(659406, _a_(659405, _a_(659404, _n_(659403, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\Battery.jpg')
_l_(659407)
img2 = _c_(659411, _a_(659410, _a_(659409, _n_(659408, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\bulbOn.jpg')
_l_(659412)
img3 = _c_(659416, _a_(659415, _a_(659414, _n_(659413, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\bulbOff.jpg')
_l_(659417)
img4 = _c_(659421, _a_(659420, _a_(659419, _n_(659418, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\Resistor.jpg')
_l_(659422)

if _a_(659424, _n_(659423, "event", lambda: event), "type") == _a_(659426, _n_(659425, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
    _l_(659440)

    if _a_(659428, _n_(659427, "event", lambda: event), "button") == 1:
        _l_(659439)

        if _c_(659432, _a_(659430, _n_(659429, "batteryBtn", lambda: batteryBtn), "collidepoint"), _n_(659431, "pos", lambda: pos)):
            _l_(659438)

            _c_(659436, _a_(659434, _n_(659433, "display", lambda: display), "blit"), _n_(659435, "img1", lambda: img1), (0, 100))
            _l_(659437)