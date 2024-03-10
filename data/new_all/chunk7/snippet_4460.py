# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56959631/im-getting-a-nameerror-from-using-the-event-function-from-pygame
#Drawing Rectangles (later used as buttons)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
batteryBtn = _c_(695202, _a_(695199, _a_(695198, _n_(695197, "pygame", lambda: pygame), "draw"), "rect"), _n_(695200, "display", lambda: display), _n_(695201, "red", lambda: red), (0,0,100,50))
_l_(695203)
bulbBtn = _c_(695209, _a_(695206, _a_(695205, _n_(695204, "pygame", lambda: pygame), "draw"), "rect"), _n_(695207, "display", lambda: display), _n_(695208, "green", lambda: green), (100,0,100,50))
_l_(695210)
resistorBtn = _c_(695216, _a_(695213, _a_(695212, _n_(695211, "pygame", lambda: pygame), "draw"), "rect"), _n_(695214, "display", lambda: display), _n_(695215, "blue", lambda: blue), (200,0,100,50))
_l_(695217)

#Initialising the images
img1 = _c_(695221, _a_(695220, _a_(695219, _n_(695218, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\Battery.jpg')
_l_(695222)
img2 = _c_(695226, _a_(695225, _a_(695224, _n_(695223, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\bulbOn.jpg')
_l_(695227)
img3 = _c_(695231, _a_(695230, _a_(695229, _n_(695228, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\bulbOff.jpg')
_l_(695232)
img4 = _c_(695236, _a_(695235, _a_(695234, _n_(695233, "pygame", lambda: pygame), "image"), "load"), r'C:\Users\Amine\Pictures\Resistor.jpg')
_l_(695237)

if _a_(695239, _n_(695238, "event", lambda: event), "type") == _a_(695241, _n_(695240, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
    _l_(695255)

    if _a_(695243, _n_(695242, "event", lambda: event), "button") == 1:
        _l_(695254)

        if _c_(695247, _a_(695245, _n_(695244, "batteryBtn", lambda: batteryBtn), "collidepoint"), _n_(695246, "pos", lambda: pos)):
            _l_(695253)

            _c_(695251, _a_(695249, _n_(695248, "display", lambda: display), "blit"), _n_(695250, "img1", lambda: img1), (0, 100))
            _l_(695252)