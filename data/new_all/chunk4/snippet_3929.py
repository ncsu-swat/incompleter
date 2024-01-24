# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65227471/pygame-snake-game-typeerror-randomize-position-missing-1-required-positional
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(611547)

except ImportError:
    pass
try:
    import sys
    _l_(611549)

except ImportError:
    pass
try:
    import random
    _l_(611551)

except ImportError:
    pass


class snake(_n_(611552, "object", lambda: object)):
    _l_(611742)

    def __init__(self):
        _l_(611570)

        _n_(611553, "self", lambda: self).length = 1
        _l_(611554)
        _n_(611555, "self", lambda: self).positions = [((_n_(611556, "SCREEN_WIDTH", lambda: SCREEN_WIDTH) / 2), (_n_(611557, "SCREEN_HEIGHT", lambda: SCREEN_HEIGHT) / 2))]
        _l_(611558)
        _n_(611559, "self", lambda: self).direction = _c_(611566, _a_(611561, _n_(611560, "random", lambda: random), "choice"), [_n_(611562, "UP", lambda: UP), _n_(611563, "DOWN", lambda: DOWN), _n_(611564, "LEFT", lambda: LEFT), _n_(611565, "RIGHT", lambda: RIGHT)])
        _l_(611567)
        _n_(611568, "self", lambda: self).color = (17, 24, 47)
        _l_(611569)

    def get_head_position(self):
        _l_(611574)

        aux = _a_(611572, _n_(611571, "self", lambda: self), "positions")[0]
        _l_(611573)
        return aux

    def turn(self, point):
        _l_(611586)

        if _a_(611576, _n_(611575, "self", lambda: self), "length") > 1 and (_n_(611577, "point", lambda: point)[0] * -1, _n_(611578, "point", lambda: point)[1] * -1) == _a_(611580, _n_(611579, "self", lambda: self), "direction"):
            _l_(611585)

            aux = ""
            _l_(611581)
            return aux
        else:
            _n_(611582, "self", lambda: self).direction = _n_(611583, "point", lambda: point)
            _l_(611584)

    def move(self):
        _l_(611633)

        cur = _c_(611589, _a_(611588, _n_(611587, "self", lambda: self), "get_head_position"))
        _l_(611590)
        x, y = _a_(611592, _n_(611591, "self", lambda: self), "direction")
        _l_(611593)
        new = (((_n_(611594, "cur", lambda: cur)[0] + (_n_(611595, "x", lambda: x) * _n_(611596, "GRIDSIZE", lambda: GRIDSIZE))) % _n_(611597, "SCREEN_WIDTH", lambda: SCREEN_WIDTH)), (_n_(611598, "cur", lambda: cur)[1] + (_n_(611599, "y", lambda: y) * _n_(611600, "GRIDSIZE", lambda: GRIDSIZE))) % _n_(611601, "SCREEN_HEIGHT", lambda: SCREEN_HEIGHT))
        _l_(611602)
        if _c_(611606, _n_(611603, "len", lambda: len), _a_(611605, _n_(611604, "self", lambda: self), "positions")) > 2 and _n_(611607, "new", lambda: new) in _a_(611609, _n_(611608, "self", lambda: self), "positions")[2:]:
            _l_(611632)

            _c_(611612, _a_(611611, _n_(611610, "self", lambda: self), "reset"))
            _l_(611613)
        else:
            _c_(611618, _a_(611616, _a_(611615, _n_(611614, "self", lambda: self), "positions"), "insert"), 0, _n_(611617, "new", lambda: new))
            _l_(611619)
            if _c_(611623, _n_(611620, "len", lambda: len), _a_(611622, _n_(611621, "self", lambda: self), "positions")) > _a_(611625, _n_(611624, "self", lambda: self), "length"):
                _l_(611631)

                _c_(611629, _a_(611628, _a_(611627, _n_(611626, "self", lambda: self), "positions"), "pop"))
                _l_(611630)

    def reset(self):
        _l_(611649)

        _n_(611634, "self", lambda: self).length = 1
        _l_(611635)
        _n_(611636, "self", lambda: self).positions = [((_n_(611637, "SCREEN_WIDTH", lambda: SCREEN_WIDTH) / 2), (_n_(611638, "SCREEN_HEIGHT", lambda: SCREEN_HEIGHT) / 2))]
        _l_(611639)
        _n_(611640, "self", lambda: self).direction = _c_(611647, _a_(611642, _n_(611641, "random", lambda: random), "choice"), [_n_(611643, "UP", lambda: UP), _n_(611644, "DOWN", lambda: DOWN), _n_(611645, "LEFT", lambda: LEFT), _n_(611646, "RIGHT", lambda: RIGHT)])
        _l_(611648)

    def draw(self, surface):
        _l_(611677)

        for p in _a_(611651, _n_(611650, "self", lambda: self), "positions"):
            _l_(611676)

            r = _c_(611658, _a_(611653, _n_(611652, "pygame", lambda: pygame), "Rect"), (_n_(611654, "p", lambda: p)[0], _n_(611655, "p", lambda: p)[1]), (_n_(611656, "GRIDSIZE", lambda: GRIDSIZE), _n_(611657, "GRIDSIZE", lambda: GRIDSIZE)))
            _l_(611659)
            _c_(611667, _a_(611662, _a_(611661, _n_(611660, "pygame", lambda: pygame), "draw"), "rect"), _n_(611663, "surface", lambda: surface), _a_(611665, _n_(611664, "self", lambda: self), "color"), _n_(611666, "r", lambda: r))
            _l_(611668)
            _c_(611674, _a_(611671, _a_(611670, _n_(611669, "pygame", lambda: pygame), "draw"), "rect"), _n_(611672, "surface", lambda: surface), (93, 216, 228), _n_(611673, "r", lambda: r), 1)
            _l_(611675)

    def handle_keys(self):
        _l_(611741)

        for event in _c_(611681, _a_(611680, _a_(611679, _n_(611678, "pygame", lambda: pygame), "event"), "get")):
            _l_(611740)

            if _a_(611683, _n_(611682, "event", lambda: event), "type") == _a_(611685, _n_(611684, "pygame", lambda: pygame), "QUIT"):
                _l_(611739)

                _c_(611688, _a_(611687, _n_(611686, "pygame", lambda: pygame), "quit"))
                _l_(611689)
                _c_(611692, _a_(611691, _n_(611690, "sys", lambda: sys), "exit"))
                _l_(611693)
            elif _a_(611695, _n_(611694, "event", lambda: event), "type") == _a_(611697, _n_(611696, "pygame", lambda: pygame), "KEYDOWN"):
                _l_(611738)

                if _a_(611699, _n_(611698, "event", lambda: event), "key") == _a_(611701, _n_(611700, "pygame", lambda: pygame), "K_UP"):
                    _l_(611737)

                    _c_(611705, _a_(611703, _n_(611702, "self", lambda: self), "turn"), _n_(611704, "UP", lambda: UP))
                    _l_(611706)
                elif _a_(611708, _n_(611707, "event", lambda: event), "key") == _a_(611710, _n_(611709, "pygame", lambda: pygame), "K_DOWN"):
                    _l_(611736)

                    _c_(611714, _a_(611712, _n_(611711, "self", lambda: self), "turn"), _n_(611713, "DOWN", lambda: DOWN))
                    _l_(611715)
                elif _a_(611717, _n_(611716, "event", lambda: event), "key") == _a_(611719, _n_(611718, "pygame", lambda: pygame), "K_LEFT"):
                    _l_(611735)

                    _c_(611723, _a_(611721, _n_(611720, "self", lambda: self), "turn"), _n_(611722, "LEFT", lambda: LEFT))
                    _l_(611724)
                elif _a_(611726, _n_(611725, "event", lambda: event), "key") == _a_(611728, _n_(611727, "pygame", lambda: pygame), "K_RIGHT"):
                    _l_(611734)

                    _c_(611732, _a_(611730, _n_(611729, "self", lambda: self), "turn"), _n_(611731, "RIGHT", lambda: RIGHT))
                    _l_(611733)


class food(_n_(611743, "object", lambda: object)):
    _l_(611793)

    def __init__(self):
        _l_(611752)

        _n_(611744, "self", lambda: self).position = (0, 0)
        _l_(611745)
        _n_(611746, "self", lambda: self).color = (223, 163, 49)
        _l_(611747)
        _c_(611750, _a_(611749, _n_(611748, "self", lambda: self), "randomize_position"))
        _l_(611751)

    def randomize_position(self):
        _l_(611765)

        _n_(611753, "self", lambda: self).position = (_c_(611757, _a_(611755, _n_(611754, "random", lambda: random), "randint"), 0, _n_(611756, "GRID_WIDTH", lambda: GRID_WIDTH) - 1) * _n_(611758, "GRIDSIZE", lambda: GRIDSIZE), _c_(611762, _a_(611760, _n_(611759, "random", lambda: random), "randint"), 0, _n_(611761, "GRID_HEIGHT", lambda: GRID_HEIGHT) - 1) * _n_(611763, "GRIDSIZE", lambda: GRIDSIZE))
        _l_(611764)

    def draw(self, surface):
        _l_(611792)

        r = _c_(611774, _a_(611767, _n_(611766, "pygame", lambda: pygame), "Rect"), (_a_(611769, _n_(611768, "self", lambda: self), "position")[0], _a_(611771, _n_(611770, "self", lambda: self), "position")[1]), (_n_(611772, "GRIDSIZE", lambda: GRIDSIZE), _n_(611773, "GRIDSIZE", lambda: GRIDSIZE)))
        _l_(611775)
        _c_(611783, _a_(611778, _a_(611777, _n_(611776, "pygame", lambda: pygame), "draw"), "rect"), _n_(611779, "surface", lambda: surface), _a_(611781, _n_(611780, "self", lambda: self), "color"), _n_(611782, "r", lambda: r))
        _l_(611784)
        _c_(611790, _a_(611787, _a_(611786, _n_(611785, "pygame", lambda: pygame), "draw"), "rect"), _n_(611788, "surface", lambda: surface), (93, 216, 228), _n_(611789, "r", lambda: r), 1)
        _l_(611791)


def drawGrid(surface):
    _l_(611843)

    for y in _c_(611798, _n_(611794, "range", lambda: range), 0, _c_(611797, _n_(611795, "int", lambda: int), _n_(611796, "GRID_HEIGHT", lambda: GRID_HEIGHT))):
        _l_(611842)

        for x in _c_(611803, _n_(611799, "range", lambda: range), 0, _c_(611802, _n_(611800, "int", lambda: int), _n_(611801, "GRID_WIDTH", lambda: GRID_WIDTH))):
            _l_(611841)

            if (_n_(611804, "x", lambda: x) + _n_(611805, "y", lambda: y)) % 2 == 0:
                _l_(611840)

                r = _c_(611814, _a_(611807, _n_(611806, "pygame", lambda: pygame), "Rect"), (_n_(611808, "x", lambda: x) * _n_(611809, "GRIDSIZE", lambda: GRIDSIZE), _n_(611810, "y", lambda: y) * _n_(611811, "GRIDSIZE", lambda: GRIDSIZE)), (_n_(611812, "GRIDSIZE", lambda: GRIDSIZE), _n_(611813, "GRIDSIZE", lambda: GRIDSIZE)))
                _l_(611815)
                _c_(611821, _a_(611818, _a_(611817, _n_(611816, "pygame", lambda: pygame), "draw"), "rect"), _n_(611819, "surface", lambda: surface), (93, 216, 228), _n_(611820, "r", lambda: r))
                _l_(611822)
            else:
                rr = _c_(611831, _a_(611824, _n_(611823, "pygame", lambda: pygame), "Rect"), (_n_(611825, "x", lambda: x) * _n_(611826, "GRIDSIZE", lambda: GRIDSIZE), _n_(611827, "y", lambda: y) * _n_(611828, "GRIDSIZE", lambda: GRIDSIZE)), (_n_(611829, "GRIDSIZE", lambda: GRIDSIZE), _n_(611830, "GRIDSIZE", lambda: GRIDSIZE)))
                _l_(611832)
                _c_(611838, _a_(611835, _a_(611834, _n_(611833, "pygame", lambda: pygame), "draw"), "rect"), _n_(611836, "surface", lambda: surface), (84, 194, 205), _n_(611837, "rr", lambda: rr))
                _l_(611839)


SCREEN_WIDTH = 400
_l_(611844)
SCREEN_HEIGHT = 400
_l_(611845)

GRIDSIZE = 20
_l_(611846)
GRID_WIDTH = _n_(611847, "SCREEN_HEIGHT", lambda: SCREEN_HEIGHT) / _n_(611848, "GRIDSIZE", lambda: GRIDSIZE)
_l_(611849)
GRID_HEIGHT = _n_(611850, "SCREEN_WIDTH", lambda: SCREEN_WIDTH) / _n_(611851, "GRIDSIZE", lambda: GRIDSIZE)
_l_(611852)

UP = (0, -1)
_l_(611853)
DOWN = (0, 1)
_l_(611854)
LEFT = (-1, 0)
_l_(611855)
RIGHT = (1, 0)
_l_(611856)


def main():
    _l_(611962)

    _c_(611859, _a_(611858, _n_(611857, "pygame", lambda: pygame), "init"))
    _l_(611860)

    clock = _c_(611864, _a_(611863, _a_(611862, _n_(611861, "pygame", lambda: pygame), "time"), "Clock"))
    _l_(611865)
    screen = _c_(611871, _a_(611868, _a_(611867, _n_(611866, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(611869, "SCREEN_WIDTH", lambda: SCREEN_WIDTH), _n_(611870, "SCREEN_HEIGHT", lambda: SCREEN_HEIGHT)), 0, 32)
    _l_(611872)

    surface = _c_(611878, _a_(611874, _n_(611873, "pygame", lambda: pygame), "Surface"), _c_(611877, _a_(611876, _n_(611875, "screen", lambda: screen), "get_size")))
    _l_(611879)
    surface = _c_(611882, _a_(611881, _n_(611880, "surface", lambda: surface), "convert"))
    _l_(611883)
    _c_(611886, _n_(611884, "drawGrid", lambda: drawGrid), _n_(611885, "surface", lambda: surface))
    _l_(611887)

    snake1 = _c_(611889, _n_(611888, "snake", lambda: snake))
    _l_(611890)
    food1 = _c_(611892, _n_(611891, "food", lambda: food))
    _l_(611893)

    myfont = _c_(611897, _a_(611896, _a_(611895, _n_(611894, "pygame", lambda: pygame), "font"), "SysFont"), "monospace", 16)
    _l_(611898)

    score = 0
    _l_(611899)
    while True:
        _l_(611961)

        _c_(611902, _a_(611901, _n_(611900, "clock", lambda: clock), "tick"), 10)
        _l_(611903)
        _c_(611906, _a_(611905, _n_(611904, "snake1", lambda: snake1), "handle_keys"))
        _l_(611907)
        _c_(611910, _n_(611908, "drawGrid", lambda: drawGrid), _n_(611909, "surface", lambda: surface))
        _l_(611911)
        _c_(611914, _a_(611913, _n_(611912, "snake1", lambda: snake1), "move"))
        _l_(611915)
        if _c_(611918, _a_(611917, _n_(611916, "snake1", lambda: snake1), "get_head_position")) == _a_(611920, _n_(611919, "food1", lambda: food1), "position"):
            _l_(611928)

            _n_(611921, "snake1", lambda: snake1).length += 1
            _l_(611922)
            score += 1
            _l_(611923)
            _c_(611926, _a_(611925, _n_(611924, "food", lambda: food), "randomize_position"))
            _l_(611927)
        _c_(611932, _a_(611930, _n_(611929, "snake1", lambda: snake1), "draw"), _n_(611931, "surface", lambda: surface))
        _l_(611933)
        _c_(611937, _a_(611935, _n_(611934, "food1", lambda: food1), "draw"), _n_(611936, "surface", lambda: surface))
        _l_(611938)
        _c_(611942, _a_(611940, _n_(611939, "screen", lambda: screen), "blit"), _n_(611941, "surface", lambda: surface), (0, 0))
        _l_(611943)
        text = _c_(611949, _a_(611945, _n_(611944, "myfont", lambda: myfont), "render"), _c_(611948, _a_(611946, "Score {0}", "format"), _n_(611947, "score", lambda: score)), 1, (0, 0, 0))
        _l_(611950)
        _c_(611954, _a_(611952, _n_(611951, "screen", lambda: screen), "blit"), _n_(611953, "text", lambda: text), (5, 10))
        _l_(611955)
        _c_(611959, _a_(611958, _a_(611957, _n_(611956, "pygame", lambda: pygame), "display"), "update"))
        _l_(611960)


_c_(611964, _n_(611963, "main", lambda: main))
_l_(611965)