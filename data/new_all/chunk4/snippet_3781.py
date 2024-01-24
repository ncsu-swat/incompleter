# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68157511/typeerror-when-drawing-circle-in-pygame
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(638924)

except ImportError:
    pass

def Circle(screen,body,fixture,PPM):
    _l_(638952)

    shape = _a_(638926, _n_(638925, "fixture", lambda: fixture), "shape")
    _l_(638927)
    radius = _a_(638929, _n_(638928, "shape", lambda: shape), "radius")
    _l_(638930)
    position = (_c_(638936, _n_(638931, "int", lambda: int), _a_(638934, _a_(638933, _n_(638932, "body", lambda: body), "position"), "x") * _n_(638935, "PPM", lambda: PPM)),_c_(638942, _n_(638937, "int", lambda: int), _a_(638940, _a_(638939, _n_(638938, "body", lambda: body), "position"), "y") * _n_(638941, "PPM", lambda: PPM)))
    _l_(638943)
    
    _c_(638950, _a_(638946, _a_(638945, _n_(638944, "pygame", lambda: pygame), "draw"), "circle"), _n_(638947, "screen", lambda: screen), (255,0,0), _n_(638948, "position", lambda: position), _n_(638949, "radius", lambda: radius))
    _l_(638951)


def Draw(screen,PPM,bodies):
    _l_(638973)

    for body in _n_(638953, "bodies", lambda: bodies):
        _l_(638972)

        for fixture in _a_(638955, _n_(638954, "body", lambda: body), "fixtures"):
            _l_(638971)

            try:
                _l_(638964)

                _c_(638961, _n_(638956, "Circle", lambda: Circle), _n_(638957, "screen", lambda: screen),_n_(638958, "body", lambda: body),_n_(638959, "fixture", lambda: fixture),_n_(638960, "PPM", lambda: PPM))
                _l_(638962)
            except:
                _l_(638963)

pass            _c_(638969, _n_(638965, "Circle", lambda: Circle), _n_(638966, "screen", lambda: screen),_n_(638967, "body", lambda: body),_n_(638968, "fixture", lambda: fixture))
            _l_(638970)