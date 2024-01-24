# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32294479/typeerror-draw-missing-1-required-positional-argument-surface
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Block(_a_(408478, _a_(408477, _n_(408476, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(408506)

    def __init__(self, color, width, height):
        _l_(408505)

        _c_(408481, _a_(408480, _n_(408479, "super", lambda: super)(), "__init__"))
        _l_(408482)
        _n_(408483, "self", lambda: self).image = _c_(408488, _a_(408485, _n_(408484, "pygame", lambda: pygame), "Surface"), [_n_(408486, "width", lambda: width), _n_(408487, "height", lambda: height)])
        _l_(408489)
        _c_(408494, _a_(408492, _a_(408491, _n_(408490, "self", lambda: self), "image"), "fill"), _n_(408493, "color", lambda: color))
        _l_(408495)
        _n_(408496, "self", lambda: self).rect = _c_(408500, _a_(408499, _a_(408498, _n_(408497, "self", lambda: self), "image"), "get_rect"))
        _l_(408501)
        _n_(408502, "self", lambda: self).width = _n_(408503, "width", lambda: width)
        _l_(408504)

screen_width = 700
_l_(408507)
screen_height = 500
_l_(408508)
size = (_n_(408509, "screen_width", lambda: screen_width), _n_(408510, "screen_height", lambda: screen_height))
_l_(408511)
screen = _c_(408516, _a_(408514, _a_(408513, _n_(408512, "pygame", lambda: pygame), "display"), "set_mode"), _n_(408515, "size", lambda: size))
_l_(408517)

# Sprites lists
all_sprites_list = _a_(408520, _a_(408519, _n_(408518, "pygame", lambda: pygame), "sprite"), "Group")
_l_(408521)

# Create the player
block_width = 30
_l_(408522)
block_height = 15
_l_(408523)
player = _c_(408528, _n_(408524, "Block", lambda: Block), _n_(408525, "BLUE", lambda: BLUE), _n_(408526, "block_width", lambda: block_width), _n_(408527, "block_height", lambda: block_height))
_l_(408529)
# Set the initial position for the player in the center of the screen
_a_(408531, _n_(408530, "player", lambda: player), "rect").x = _n_(408532, "screen_width", lambda: screen_width)/2 - _n_(408533, "block_width", lambda: block_width)/2
_l_(408534)
_a_(408536, _n_(408535, "player", lambda: player), "rect").y = _n_(408537, "screen_height", lambda: screen_height)/2 - _n_(408538, "block_height", lambda: block_height)/2
_l_(408539)
# Add the player to all_sprites_list
_c_(408543, _a_(408541, _n_(408540, "all_sprites_list", lambda: all_sprites_list), "add"), _n_(408542, "player", lambda: player))
_l_(408544)

# -------- Main Program Loop -----------
while not _n_(408545, "done", lambda: done):
    _l_(408572)

    # --- Main event loop
    for event in _c_(408549, _a_(408548, _a_(408547, _n_(408546, "pygame", lambda: pygame), "event"), "get")):
        _l_(408556)

        if _a_(408551, _n_(408550, "event", lambda: event), "type") == _a_(408553, _n_(408552, "pygame", lambda: pygame), "QUIT"):
            _l_(408555)

            done = True
            _l_(408554)

    _c_(408560, _a_(408558, _n_(408557, "screen", lambda: screen), "fill"), _n_(408559, "WHITE", lambda: WHITE))
    _l_(408561)
    _c_(408565, _a_(408563, _n_(408562, "all_sprites_list", lambda: all_sprites_list), "draw"), _n_(408564, "screen", lambda: screen))
    _l_(408566)

    _c_(408570, _a_(408569, _a_(408568, _n_(408567, "pygame", lambda: pygame), "display"), "flip"))
    _l_(408571)