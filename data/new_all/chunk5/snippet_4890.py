# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42739880/typeerror-not-supported-between-instances-of-block-and-block
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from turtle import *
    _l_(662152)

except ImportError:
    pass

class Block(_n_(662153, "Turtle", lambda: Turtle)):
    _l_(662196)

    def __init__(self, size):
        _l_(662179)

        _n_(662154, "self", lambda: self).size = _n_(662155, "size", lambda: size)
        _l_(662156)
        _c_(662160, _a_(662158, _n_(662157, "Turtle", lambda: Turtle), "__init__"), _n_(662159, "self", lambda: self), shape="square", visible=False)
        _l_(662161)
        _c_(662164, _a_(662163, _n_(662162, "self", lambda: self), "pu"))
        _l_(662165)
        _c_(662169, _a_(662167, _n_(662166, "self", lambda: self), "shapesize"), _n_(662168, "size", lambda: size) * 1.5, 1.5, 2) # square-->rectangle
        _l_(662170) # square-->rectangle
        _c_(662173, _a_(662172, _n_(662171, "self", lambda: self), "fillcolor"), "black")
        _l_(662174)
        _c_(662177, _a_(662176, _n_(662175, "self", lambda: self), "st"))
        _l_(662178)
    def glow(self):
        _l_(662184)

        _c_(662182, _a_(662181, _n_(662180, "self", lambda: self), "fillcolor"), "red")
        _l_(662183)
    def unglow(self):
        _l_(662189)

        _c_(662187, _a_(662186, _n_(662185, "self", lambda: self), "fillcolor"), "black")
        _l_(662188)
    def __repr__(self):
        _l_(662195)

        aux = _c_(662193, _a_(662190, "Block size: {0}", "format"), _a_(662192, _n_(662191, "self", lambda: self), "size"))
        _l_(662194)
        return aux

class Shelf(_n_(662197, "list", lambda: list)):
    _l_(662318)

    def __init__(self, y):
        _l_(662204)

        "create an shelf. y is y-position of first block"
        _l_(662198)
        _n_(662199, "self", lambda: self).y = _n_(662200, "y", lambda: y)
        _l_(662201)
        _n_(662202, "self", lambda: self).x = -150
        _l_(662203)
    def push(self, d):
        _l_(662232)

        width, _, _ = _c_(662207, _a_(662206, _n_(662205, "d", lambda: d), "shapesize"))
        _l_(662208)
        yoffset = _n_(662209, "width", lambda: width)/2 * 20 # to align the blocks by it's bottom edge
        _l_(662210) # to align the blocks by it's bottom edge
        _c_(662216, _a_(662212, _n_(662211, "d", lambda: d), "sety"), _a_(662214, _n_(662213, "self", lambda: self), "y") + _n_(662215, "yoffset", lambda: yoffset))
        _l_(662217)
        _c_(662225, _a_(662219, _n_(662218, "d", lambda: d), "setx"), _a_(662221, _n_(662220, "self", lambda: self), "x")+34*_c_(662224, _n_(662222, "len", lambda: len), _n_(662223, "self", lambda: self)))
        _l_(662226)
        _c_(662230, _a_(662228, _n_(662227, "self", lambda: self), "append"), _n_(662229, "d", lambda: d))
        _l_(662231)
    def _close_gap_from_i(self, i):
        _l_(662245)

        for b in _n_(662233, "self", lambda: self)[_n_(662234, "i", lambda: i):]:
            _l_(662244)

            xpos, _ = _c_(662237, _a_(662236, _n_(662235, "b", lambda: b), "pos"))
            _l_(662238)
            _c_(662242, _a_(662240, _n_(662239, "b", lambda: b), "setx"), _n_(662241, "xpos", lambda: xpos) - 34)
            _l_(662243)
    def _open_gap_from_i(self, i):
        _l_(662258)

        for b in _n_(662246, "self", lambda: self)[_n_(662247, "i", lambda: i):]:
            _l_(662257)

            xpos, _ = _c_(662250, _a_(662249, _n_(662248, "b", lambda: b), "pos"))
            _l_(662251)
            _c_(662255, _a_(662253, _n_(662252, "b", lambda: b), "setx"), _n_(662254, "xpos", lambda: xpos) + 34)
            _l_(662256)
    def pop(self, key):
        _l_(662280)

        b = _c_(662263, _a_(662260, _n_(662259, "list", lambda: list), "pop"), _n_(662261, "self", lambda: self), _n_(662262, "key", lambda: key))
        _l_(662264)
        _c_(662267, _a_(662266, _n_(662265, "b", lambda: b), "glow"))
        _l_(662268)
        _c_(662271, _a_(662270, _n_(662269, "b", lambda: b), "sety"), 200)
        _l_(662272)
        _c_(662276, _a_(662274, _n_(662273, "self", lambda: self), "_close_gap_from_i"), _n_(662275, "key", lambda: key))
        _l_(662277)
        aux = _n_(662278, "b", lambda: b)
        _l_(662279)
        return aux
    def insert(self, key, b):
        _l_(662317)

        _c_(662284, _a_(662282, _n_(662281, "self", lambda: self), "_open_gap_from_i"), _n_(662283, "key", lambda: key))
        _l_(662285)
        _c_(662291, _a_(662287, _n_(662286, "list", lambda: list), "insert"), _n_(662288, "self", lambda: self), _n_(662289, "key", lambda: key), _n_(662290, "b", lambda: b))
        _l_(662292)
        _c_(662298, _a_(662294, _n_(662293, "b", lambda: b), "setx"), _a_(662296, _n_(662295, "self", lambda: self), "x")+34*_n_(662297, "key", lambda: key))
        _l_(662299)
        width, _, _ = _c_(662302, _a_(662301, _n_(662300, "b", lambda: b), "shapesize"))
        _l_(662303)
        yoffset = _n_(662304, "width", lambda: width)/2 * 20 # to align the blocks by it's bottom edge
        _l_(662305) # to align the blocks by it's bottom edge
        _c_(662311, _a_(662307, _n_(662306, "b", lambda: b), "sety"), _a_(662309, _n_(662308, "self", lambda: self), "y") + _n_(662310, "yoffset", lambda: yoffset))
        _l_(662312)
        _c_(662315, _a_(662314, _n_(662313, "b", lambda: b), "unglow"))
        _l_(662316)

def show_text(text):
    _l_(662326)

    _c_(662320, _n_(662319, "goto", lambda: goto), 0,-250)
    _l_(662321)
    _c_(662324, _n_(662322, "write", lambda: write), _n_(662323, "text", lambda: text), align="center", font=("Courier", 16, "bold"))
    _l_(662325)

def start_sort():
    _l_(662340)

    _c_(662328, _n_(662327, "onkey", lambda: onkey), None,"space")
    _l_(662329)
    _c_(662331, _n_(662330, "clear", lambda: clear))
    _l_(662332)
    _c_(662334, _n_(662333, "show_text", lambda: show_text), "sort_me")
    _l_(662335)
    _c_(662338, _n_(662336, "sort_func", lambda: sort_func), _n_(662337, "s", lambda: s))
    _l_(662339)

def init_shelf(vals=(4, 8, 2, 9, 3, 1, 10, 7, 5, 6)):
    _l_(662355)

    s = _c_(662342, _n_(662341, "Shelf", lambda: Shelf), -200)
    _l_(662343)
    for i in _n_(662344, "vals", lambda: vals):
        _l_(662352)

        _c_(662350, _a_(662346, _n_(662345, "s", lambda: s), "push"), _c_(662349, _n_(662347, "Block", lambda: Block), _n_(662348, "i", lambda: i)))
        _l_(662351)
    aux = _n_(662353, "s", lambda: s)
    _l_(662354)
    return aux

def clear_window():
    _l_(662361)

    _c_(662359, _a_(662358, _c_(662357, _n_(662356, "getscreen", lambda: getscreen)), "clearscreen"))
    _l_(662360)

def main(func):
    _l_(662395)

    global sort_func
    _l_(662362)
    sort_func = _n_(662363, "func", lambda: func)
    _l_(662364)
    _c_(662368, _a_(662367, _c_(662366, _n_(662365, "getscreen", lambda: getscreen)), "clearscreen"))
    _l_(662369)
    _c_(662371, _n_(662370, "ht", lambda: ht)); _c_(662373, _n_(662372, "penup", lambda: penup))
    _l_(662374)
    _c_(662376, _n_(662375, "init_shelf", lambda: init_shelf))
    _l_(662377)
    _c_(662379, _n_(662378, "show_text", lambda: show_text), "press spacebar to start sorting")
    _l_(662380)
    _c_(662383, _n_(662381, "onkey", lambda: onkey), _n_(662382, "start_sort", lambda: start_sort), "space")
    _l_(662384)
    _c_(662387, _n_(662385, "onkey", lambda: onkey), _n_(662386, "bye", lambda: bye), "Escape")
    _l_(662388)
    _c_(662390, _n_(662389, "listen", lambda: listen))
    _l_(662391)
    _c_(662393, _n_(662392, "mainloop", lambda: mainloop))
    _l_(662394)