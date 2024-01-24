# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54284662/nameerror-in-python-program-even-though-it-seems-to-be-setup-correctly
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
room_map = [[1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]]
_l_(541284)

WIDTH = 800 # window size
_l_(541285) # window size
HEIGHT = 800
_l_(541286)

top_left_x = 100
_l_(541287)
top_left_y = 150
_l_(541288)

DEMO_OBJECTS = [_a_(541290, _n_(541289, "images", lambda: images), "floor"), _a_(541292, _n_(541291, "images", lambda: images), "pillar")]
_l_(541293)

room_height = 7
_l_(541294)
room_width = 5
_l_(541295)

def draw():
    _l_(541321)

    for y in _c_(541298, _n_(541296, "range", lambda: range), _n_(541297, "room_height", lambda: room_height)):
        _l_(541320)

        for x in _c_(541301, _n_(541299, "range", lambda: range), _n_(541300, "room_width", lambda: room_width)):
            _l_(541319)

            image_to_draw = _n_(541302, "DEMO_OBJECTS", lambda: DEMO_OBJECTS)[_n_(541303, "room_map", lambda: room_map)[_n_(541304, "y", lambda: y)][_n_(541305, "x", lambda: x)]]
            _l_(541306)
            _c_(541317, _a_(541308, _n_(541307, "screen", lambda: screen), "blit"), _n_(541309, "image_to_draw", lambda: image_to_draw),
                        (_n_(541310, "top_left_x", lambda: top_left_x) + (_n_(541311, "x", lambda: x) * 30),
                        _n_(541312, "top_left_y", lambda: top_left_y) + (_n_(541313, "y", lambda: y) * 30) - _c_(541316, _a_(541315, _n_(541314, "image_to_draw", lambda: image_to_draw), "get_height"))))
            _l_(541318)