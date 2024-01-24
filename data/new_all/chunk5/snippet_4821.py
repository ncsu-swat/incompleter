# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41974709/typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(688583)

except ImportError:
    pass
try:
    import pytmx
    _l_(688585)

except ImportError:
    pass

_c_(688588, _a_(688587, _n_(688586, "pygame", lambda: pygame), "init"))
_l_(688589)

class tiledMap():
    _l_(688653)

    def __init__(self):
        _l_(688611)

        _n_(688590, "self", lambda: self).gameMap = _c_(688593, _a_(688592, _n_(688591, "pytmx", lambda: pytmx), "load_pygame"), "maps\_testingMap.tmx")
        _l_(688594)
        _n_(688595, "self", lambda: self).mapWidth = _a_(688598, _a_(688597, _n_(688596, "self", lambda: self), "gameMap"), "width") * _a_(688601, _a_(688600, _n_(688599, "self", lambda: self), "gameMap"), "tilewidth")
        _l_(688602)
        _n_(688603, "self", lambda: self).mapHeight = _a_(688606, _a_(688605, _n_(688604, "self", lambda: self), "gameMap"), "height") * _a_(688609, _a_(688608, _n_(688607, "self", lambda: self), "gameMap"), "tilewidth")
        _l_(688610)

    def render(self, surface):
        _l_(688636)

        for layer in _a_(688614, _a_(688613, _n_(688612, "self", lambda: self), "gameMap"), "visible_layers"):
            _l_(688635)

            for x,y,gid in _n_(688615, "layer", lambda: layer):
                _l_(688634)

                tile = _c_(688619, _a_(688617, _n_(688616, "pytmx", lambda: pytmx), "get_tile_image_by_gid"), _n_(688618, "gid", lambda: gid))
                _l_(688620)
                _c_(688632, _a_(688622, _n_(688621, "surface", lambda: surface), "blit"), _n_(688623, "tile", lambda: tile), (_n_(688624, "x", lambda: x) * _a_(688627, _a_(688626, _n_(688625, "self", lambda: self), "gameMap"), "tilewidth"), _n_(688628, "y", lambda: y) * _a_(688631, _a_(688630, _n_(688629, "self", lambda: self), "gameMap"), "tileheight")))
                _l_(688633)

    def makeSurface(self):
        _l_(688652)

        tiledSurface = _c_(688643, _a_(688638, _n_(688637, "pygame", lambda: pygame), "surface"), (_a_(688640, _n_(688639, "self", lambda: self), "mapWidth"), _a_(688642, _n_(688641, "self", lambda: self), "mapWidth")))
        _l_(688644)
        _c_(688648, _a_(688646, _n_(688645, "self", lambda: self), "render"), _n_(688647, "tiledSurface", lambda: tiledSurface))
        _l_(688649)
        aux = _n_(688650, "tiledSurface", lambda: tiledSurface)
        _l_(688651)
        return aux