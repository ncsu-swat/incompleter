# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62823806/random-brick-color-typeerror-pygame-color-object-is-not-callable
    # brick init
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
brick = _c_(400277, _a_(400274, _n_(400273, "pygame", lambda: pygame), "Surface"), [_n_(400275, "brick_width", lambda: brick_width), _n_(400276, "brick_height", lambda: brick_height)]),_n_(400278, "brick_color", lambda: brick_color) # surface for a single brick
_l_(400279) # surface for a single brick
_c_(400287, _a_(400282, _a_(400281, _n_(400280, "pygame", lambda: pygame), "draw"), "rect"), _n_(400283, "brick", lambda: brick)[0], _n_(400284, "brick", lambda: brick)[1], [0, 0, _n_(400285, "brick_width", lambda: brick_width), _n_(400286, "brick_height", lambda: brick_height)])
_l_(400288)



bricks = [] # list of *coordinates* of the bricks
_l_(400289) # list of *coordinates* of the bricks

# initialize coordinates of bricks

for y in _c_(400292, _n_(400290, "range", lambda: range), _n_(400291, "num_brick_rows", lambda: num_brick_rows)):
    _l_(400315)

    brickY = (_n_(400293, "y", lambda: y) * _n_(400294, "brick_row_height", lambda: brick_row_height)) + _n_(400295, "brick_offset_y", lambda: brick_offset_y)    
    _l_(400296)    
    for x in _c_(400299, _n_(400297, "range", lambda: range), _n_(400298, "num_bricks_in_row", lambda: num_bricks_in_row)):
        _l_(400314)

        brickX = (_n_(400300, "x", lambda: x) * _n_(400301, "brick_column_width", lambda: brick_column_width)) + _n_(400302, "brick_offset_x", lambda: brick_offset_x)
        _l_(400303)
        color_of_brick = _c_(400305, _n_(400304, "brick_color", lambda: brick_color))
        _l_(400306)
        _c_(400312, _a_(400308, _n_(400307, "bricks", lambda: bricks), "append"), (_n_(400309, "brickX", lambda: brickX), _n_(400310, "brickY", lambda: brickY)),_n_(400311, "color_of_brick", lambda: color_of_brick)) # coordinates are in fact tuples (x,y)
        _l_(400313) # coordinates are in fact tuples (x,y)