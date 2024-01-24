# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42739880/typeerror-not-supported-between-instances-of-block-and-block
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from turtle import *
    _l_(688732)

except ImportError:
    pass

class Block(_n_(688733, "Turtle", lambda: Turtle)):
    _l_(688776)

    def __init__(self, size):
        _l_(688759)

        _n_(688734, "self", lambda: self).size = _n_(688735, "size", lambda: size)
        _l_(688736)
        _c_(688740, _a_(688738, _n_(688737, "Turtle", lambda: Turtle), "__init__"), _n_(688739, "self", lambda: self), shape="square", visible=False)
        _l_(688741)
        _c_(688744, _a_(688743, _n_(688742, "self", lambda: self), "pu"))
        _l_(688745)
        _c_(688749, _a_(688747, _n_(688746, "self", lambda: self), "shapesize"), _n_(688748, "size", lambda: size) * 1.5, 1.5, 2) # square-->rectangle
        _l_(688750) # square-->rectangle
        _c_(688753, _a_(688752, _n_(688751, "self", lambda: self), "fillcolor"), "black")
        _l_(688754)
        _c_(688757, _a_(688756, _n_(688755, "self", lambda: self), "st"))
        _l_(688758)
    def glow(self):
        _l_(688764)

        _c_(688762, _a_(688761, _n_(688760, "self", lambda: self), "fillcolor"), "red")
        _l_(688763)
    def unglow(self):
        _l_(688769)

        _c_(688767, _a_(688766, _n_(688765, "self", lambda: self), "fillcolor"), "black")
        _l_(688768)
    def __repr__(self):
        _l_(688775)

        aux = _c_(688773, _a_(688770, "Block size: {0}", "format"), _a_(688772, _n_(688771, "self", lambda: self), "size"))
        _l_(688774)
        return aux

class Shelf(_n_(688777, "list", lambda: list)):
    _l_(688898)

    def __init__(self, y):
        _l_(688784)

        "create an shelf. y is y-position of first block"
        _l_(688778)
        _n_(688779, "self", lambda: self).y = _n_(688780, "y", lambda: y)
        _l_(688781)
        _n_(688782, "self", lambda: self).x = -150
        _l_(688783)
    def push(self, d):
        _l_(688812)

        width, _, _ = _c_(688787, _a_(688786, _n_(688785, "d", lambda: d), "shapesize"))
        _l_(688788)
        yoffset = _n_(688789, "width", lambda: width)/2 * 20 # to align the blocks by it's bottom edge
        _l_(688790) # to align the blocks by it's bottom edge
        _c_(688796, _a_(688792, _n_(688791, "d", lambda: d), "sety"), _a_(688794, _n_(688793, "self", lambda: self), "y") + _n_(688795, "yoffset", lambda: yoffset))
        _l_(688797)
        _c_(688805, _a_(688799, _n_(688798, "d", lambda: d), "setx"), _a_(688801, _n_(688800, "self", lambda: self), "x")+34*_c_(688804, _n_(688802, "len", lambda: len), _n_(688803, "self", lambda: self)))
        _l_(688806)
        _c_(688810, _a_(688808, _n_(688807, "self", lambda: self), "append"), _n_(688809, "d", lambda: d))
        _l_(688811)
    def _close_gap_from_i(self, i):
        _l_(688825)

        for b in _n_(688813, "self", lambda: self)[_n_(688814, "i", lambda: i):]:
            _l_(688824)

            xpos, _ = _c_(688817, _a_(688816, _n_(688815, "b", lambda: b), "pos"))
            _l_(688818)
            _c_(688822, _a_(688820, _n_(688819, "b", lambda: b), "setx"), _n_(688821, "xpos", lambda: xpos) - 34)
            _l_(688823)
    def _open_gap_from_i(self, i):
        _l_(688838)

        for b in _n_(688826, "self", lambda: self)[_n_(688827, "i", lambda: i):]:
            _l_(688837)

            xpos, _ = _c_(688830, _a_(688829, _n_(688828, "b", lambda: b), "pos"))
            _l_(688831)
            _c_(688835, _a_(688833, _n_(688832, "b", lambda: b), "setx"), _n_(688834, "xpos", lambda: xpos) + 34)
            _l_(688836)
    def pop(self, key):
        _l_(688860)

        b = _c_(688843, _a_(688840, _n_(688839, "list", lambda: list), "pop"), _n_(688841, "self", lambda: self), _n_(688842, "key", lambda: key))
        _l_(688844)
        _c_(688847, _a_(688846, _n_(688845, "b", lambda: b), "glow"))
        _l_(688848)
        _c_(688851, _a_(688850, _n_(688849, "b", lambda: b), "sety"), 200)
        _l_(688852)
        _c_(688856, _a_(688854, _n_(688853, "self", lambda: self), "_close_gap_from_i"), _n_(688855, "key", lambda: key))
        _l_(688857)
        aux = _n_(688858, "b", lambda: b)
        _l_(688859)
        return aux
    def insert(self, key, b):
        _l_(688897)

        _c_(688864, _a_(688862, _n_(688861, "self", lambda: self), "_open_gap_from_i"), _n_(688863, "key", lambda: key))
        _l_(688865)
        _c_(688871, _a_(688867, _n_(688866, "list", lambda: list), "insert"), _n_(688868, "self", lambda: self), _n_(688869, "key", lambda: key), _n_(688870, "b", lambda: b))
        _l_(688872)
        _c_(688878, _a_(688874, _n_(688873, "b", lambda: b), "setx"), _a_(688876, _n_(688875, "self", lambda: self), "x")+34*_n_(688877, "key", lambda: key))
        _l_(688879)
        width, _, _ = _c_(688882, _a_(688881, _n_(688880, "b", lambda: b), "shapesize"))
        _l_(688883)
        yoffset = _n_(688884, "width", lambda: width)/2 * 20 # to align the blocks by it's bottom edge
        _l_(688885) # to align the blocks by it's bottom edge
        _c_(688891, _a_(688887, _n_(688886, "b", lambda: b), "sety"), _a_(688889, _n_(688888, "self", lambda: self), "y") + _n_(688890, "yoffset", lambda: yoffset))
        _l_(688892)
        _c_(688895, _a_(688894, _n_(688893, "b", lambda: b), "unglow"))
        _l_(688896)

def show_text(text):
    _l_(688906)

    _c_(688900, _n_(688899, "goto", lambda: goto), 0,-250)
    _l_(688901)
    _c_(688904, _n_(688902, "write", lambda: write), _n_(688903, "text", lambda: text), align="center", font=("Courier", 16, "bold"))
    _l_(688905)

def start_sort():
    _l_(688920)

    _c_(688908, _n_(688907, "onkey", lambda: onkey), None,"space")
    _l_(688909)
    _c_(688911, _n_(688910, "clear", lambda: clear))
    _l_(688912)
    _c_(688914, _n_(688913, "show_text", lambda: show_text), "sort_me")
    _l_(688915)
    _c_(688918, _n_(688916, "sort_func", lambda: sort_func), _n_(688917, "s", lambda: s))
    _l_(688919)

def init_shelf(vals=(4, 8, 2, 9, 3, 1, 10, 7, 5, 6)):
    _l_(688935)

    s = _c_(688922, _n_(688921, "Shelf", lambda: Shelf), -200)
    _l_(688923)
    for i in _n_(688924, "vals", lambda: vals):
        _l_(688932)

        _c_(688930, _a_(688926, _n_(688925, "s", lambda: s), "push"), _c_(688929, _n_(688927, "Block", lambda: Block), _n_(688928, "i", lambda: i)))
        _l_(688931)
    aux = _n_(688933, "s", lambda: s)
    _l_(688934)
    return aux

def clear_window():
    _l_(688941)

    _c_(688939, _a_(688938, _c_(688937, _n_(688936, "getscreen", lambda: getscreen)), "clearscreen"))
    _l_(688940)

def main(func):
    _l_(688975)

    global sort_func
    _l_(688942)
    sort_func = _n_(688943, "func", lambda: func)
    _l_(688944)
    _c_(688948, _a_(688947, _c_(688946, _n_(688945, "getscreen", lambda: getscreen)), "clearscreen"))
    _l_(688949)
    _c_(688951, _n_(688950, "ht", lambda: ht)); _c_(688953, _n_(688952, "penup", lambda: penup))
    _l_(688954)
    _c_(688956, _n_(688955, "init_shelf", lambda: init_shelf))
    _l_(688957)
    _c_(688959, _n_(688958, "show_text", lambda: show_text), "press spacebar to start sorting")
    _l_(688960)
    _c_(688963, _n_(688961, "onkey", lambda: onkey), _n_(688962, "start_sort", lambda: start_sort), "space")
    _l_(688964)
    _c_(688967, _n_(688965, "onkey", lambda: onkey), _n_(688966, "bye", lambda: bye), "Escape")
    _l_(688968)
    _c_(688970, _n_(688969, "listen", lambda: listen))
    _l_(688971)
    _c_(688973, _n_(688972, "mainloop", lambda: mainloop))
    _l_(688974)