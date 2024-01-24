# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69802113/typeerror-init-takes-3-positional-arguments-but-4-were-given-keyboard-com
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(409124)

except ImportError:
    pass
try:
    import random
    _l_(409126)

except ImportError:
    pass

BLACK = (  0,   0,   0)
_l_(409127)
WHITE = (255, 255, 255)
_l_(409128)
RED   = (255,   0,   0)
_l_(409129)

class Block(_a_(409132, _a_(409131, _n_(409130, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(409157)

    def __init__(self, color, width, height):
        _l_(409156)

        _c_(409135, _a_(409134, _n_(409133, "super", lambda: super)(), "__init__"))
        _l_(409136)
        _n_(409137, "self", lambda: self).image = _c_(409142, _a_(409139, _n_(409138, "pygame", lambda: pygame), "Surface"), [_n_(409140, "width", lambda: width), _n_(409141, "height", lambda: height)])
        _l_(409143)
        _c_(409148, _a_(409146, _a_(409145, _n_(409144, "self", lambda: self), "image"), "fill"), _n_(409147, "color", lambda: color))
        _l_(409149)
        _n_(409150, "self", lambda: self).rect = _c_(409154, _a_(409153, _a_(409152, _n_(409151, "self", lambda: self), "image"), "get_rect"))
        _l_(409155)

class Player(_n_(409158, "Block", lambda: Block)):
    _l_(409209)


    def __init__(self, x, y):
        _l_(409192)

        _c_(409161, _a_(409160, _n_(409159, "super", lambda: super)(), "__init__"))
        _l_(409162)

        _n_(409163, "self", lambda: self).image = _c_(409166, _a_(409165, _n_(409164, "pygame", lambda: pygame), "Surface"), [15, 15])
        _l_(409167)
        _c_(409172, _a_(409170, _a_(409169, _n_(409168, "self", lambda: self), "image"), "fill"), _n_(409171, "BLACK", lambda: BLACK))
        _l_(409173)

        _n_(409174, "self", lambda: self).rect = _c_(409178, _a_(409177, _a_(409176, _n_(409175, "self", lambda: self), "image"), "get_rect"))
        _l_(409179)
        _a_(409181, _n_(409180, "self", lambda: self), "rect").x = _n_(409182, "x", lambda: x)
        _l_(409183)
        _a_(409185, _n_(409184, "self", lambda: self), "rect").y = _n_(409186, "y", lambda: y)
        _l_(409187)

        _n_(409188, "self", lambda: self).change_x = 0
        _l_(409189)
        _n_(409190, "self", lambda: self).change_y = 0
        _l_(409191)

    def changespeed(self, x, y):
        _l_(409199)

        _n_(409193, "self", lambda: self).change_x += _n_(409194, "x", lambda: x)
        _l_(409195)
        _n_(409196, "self", lambda: self).change_y += _n_(409197, "y", lambda: y)
        _l_(409198)
 
    def update(self):
        _l_(409208)

        _a_(409201, _n_(409200, "self", lambda: self), "rect").x += _n_(409202, "self", lambda: self).change_x
        _l_(409203)
        _a_(409205, _n_(409204, "self", lambda: self), "rect").y += _n_(409206, "self", lambda: self).change_y
        _l_(409207)

_c_(409212, _a_(409211, _n_(409210, "pygame", lambda: pygame), "init"))
_l_(409213)

screen_width = 700
_l_(409214)
screen_height = 400
_l_(409215)
screen = _c_(409221, _a_(409218, _a_(409217, _n_(409216, "pygame", lambda: pygame), "display"), "set_mode"), [_n_(409219, "screen_width", lambda: screen_width), _n_(409220, "screen_height", lambda: screen_height)])
_l_(409222)


block_list = _c_(409226, _a_(409225, _a_(409224, _n_(409223, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(409227)

all_sprites_list = _c_(409231, _a_(409230, _a_(409229, _n_(409228, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(409232)

for i in _c_(409234, _n_(409233, "range", lambda: range), 50):
    _l_(409262)

    block = _c_(409236, _n_(409235, "Block", lambda: Block), 200, 20,20)
    _l_(409237)

    _a_(409239, _n_(409238, "block", lambda: block), "rect").x = _c_(409243, _a_(409241, _n_(409240, "random", lambda: random), "randrange"), _n_(409242, "screen_width", lambda: screen_width))
    _l_(409244)
    _a_(409246, _n_(409245, "block", lambda: block), "rect").y = _c_(409250, _a_(409248, _n_(409247, "random", lambda: random), "randrange"), _n_(409249, "screen_height", lambda: screen_height))
    _l_(409251)

    _c_(409255, _a_(409253, _n_(409252, "block_list", lambda: block_list), "add"), _n_(409254, "block", lambda: block))
    _l_(409256)
    _c_(409260, _a_(409258, _n_(409257, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(409259, "block", lambda: block))
    _l_(409261)


player = _c_(409265, _n_(409263, "Player", lambda: Player), _n_(409264, "RED", lambda: RED), 20, 20)
_l_(409266)
_c_(409270, _a_(409268, _n_(409267, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(409269, "player", lambda: player))
_l_(409271)


done = False
_l_(409272)

clock = _c_(409276, _a_(409275, _a_(409274, _n_(409273, "pygame", lambda: pygame), "time"), "Clock"))
_l_(409277)

score = 0
_l_(409278)

while not _n_(409279, "done", lambda: done):
    _l_(409355)

    for event in _c_(409283, _a_(409282, _a_(409281, _n_(409280, "pygame", lambda: pygame), "event"), "get")):
        _l_(409304)

        if _a_(409285, _n_(409284, "event", lambda: event), "type") == _a_(409287, _n_(409286, "pygame", lambda: pygame), "QUIT"):
            _l_(409303)

            done = True
            _l_(409288)
        elif _a_(409290, _n_(409289, "event", lambda: event), "type") == _a_(409292, _n_(409291, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(409302)

            if _a_(409294, _n_(409293, "event", lambda: event), "key") == _a_(409296, _n_(409295, "pygame", lambda: pygame), "K_LEFT"):
                _l_(409301)

                _n_(409297, "player", lambda: player).rect_x = _a_(409299, _n_(409298, "player", lambda: player), "change_x")
                _l_(409300)

    _c_(409308, _a_(409306, _n_(409305, "screen", lambda: screen), "fill"), _n_(409307, "WHITE", lambda: WHITE))
    _l_(409309)

    pos = _c_(409313, _a_(409312, _a_(409311, _n_(409310, "pygame", lambda: pygame), "mouse"), "get_pos"))
    _l_(409314)

    _a_(409316, _n_(409315, "player", lambda: player), "rect").x = _a_(409319, _a_(409318, _n_(409317, "player", lambda: player), "rect"), "x")
    _l_(409320)
    _a_(409322, _n_(409321, "player", lambda: player), "rect").y = _a_(409325, _a_(409324, _n_(409323, "player", lambda: player), "rect"), "y")
    _l_(409326)


    blocks_hit_list = _c_(409332, _a_(409329, _a_(409328, _n_(409327, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(409330, "player", lambda: player), _n_(409331, "block_list", lambda: block_list), True)
    _l_(409333)


    for block in _n_(409334, "blocks_hit_list", lambda: blocks_hit_list):
        _l_(409340)

        score += 1
        _l_(409335)
        _c_(409338, _n_(409336, "print", lambda: print), _n_(409337, "score", lambda: score))
        _l_(409339)


    _c_(409344, _a_(409342, _n_(409341, "all_sprites_list", lambda: all_sprites_list), "draw"), _n_(409343, "screen", lambda: screen))
    _l_(409345)

    _c_(409349, _a_(409348, _a_(409347, _n_(409346, "pygame", lambda: pygame), "display"), "flip"))
    _l_(409350)

    _c_(409353, _a_(409352, _n_(409351, "clock", lambda: clock), "tick"), 60)
    _l_(409354)

_c_(409358, _a_(409357, _n_(409356, "pygame", lambda: pygame), "quit"))
_l_(409359)