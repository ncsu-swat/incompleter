# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36661245/what-does-this-attributeerror-means-int-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(624121)

except ImportError:
    pass
root=_c_(624123, _n_(624122, "Tk", lambda: Tk))
_l_(624124)
_c_(624127, _a_(624126, _n_(624125, "root", lambda: root), "geometry"), "512x512")
_l_(624128)

rows = 8
_l_(624129)
columns = 8
_l_(624130)
color1 = "#b35821" #Flery Orange
_l_(624131) #Flery Orange
color2 = "#efcb9d" #New Tan
_l_(624132) #New Tan
dim_square = 64
_l_(624133)

canvas=_c_(624136, _n_(624134, "Canvas", lambda: Canvas), _n_(624135, "root", lambda: root), width=512, height=512)
_l_(624137)
_c_(624140, _a_(624139, _n_(624138, "canvas", lambda: canvas), "pack"))
_l_(624141)

photo=_c_(624143, _n_(624142, "PhotoImage", lambda: PhotoImage), file="blackk.gif")
_l_(624144)

def draw_chessboard():
    _l_(624186)

    color = _n_(624145, "color2", lambda: color2)
    _l_(624146)
    for r in _c_(624149, _n_(624147, "range", lambda: range), _n_(624148, "rows", lambda: rows)):
        _l_(624185)

        color = _n_(624150, "color1", lambda: color1) if _n_(624151, "color", lambda: color) == _n_(624152, "color2", lambda: color2) else _n_(624153, "color2", lambda: color2)
        _l_(624154)
        for c in _c_(624157, _n_(624155, "range", lambda: range), _n_(624156, "columns", lambda: columns)):
            _l_(624184)

            x1 = (_n_(624158, "c", lambda: c) * _n_(624159, "dim_square", lambda: dim_square))
            _l_(624160)
            y1 = ((7-_n_(624161, "r", lambda: r)) * _n_(624162, "dim_square", lambda: dim_square))
            _l_(624163)
            x2 = _n_(624164, "x1", lambda: x1) + _n_(624165, "dim_square", lambda: dim_square)
            _l_(624166)
            y2 = _n_(624167, "y1", lambda: y1) + _n_(624168, "dim_square", lambda: dim_square)
            _l_(624169)
            _c_(624177, _a_(624171, _n_(624170, "canvas", lambda: canvas), "create_rectangle"), _n_(624172, "x1", lambda: x1), _n_(624173, "y1", lambda: y1), _n_(624174, "x2", lambda: x2), _n_(624175, "y2", lambda: y2), fill=_n_(624176, "color", lambda: color), tags="area")
            _l_(624178)
            color = _n_(624179, "color1", lambda: color1) if _n_(624180, "color", lambda: color) == _n_(624181, "color2", lambda: color2) else _n_(624182, "color2", lambda: color2)
            _l_(624183)

def draw_pieces():
    _l_(624194)

    _n_(624187, "canvas", lambda: canvas).create_image=_c_(624192, _n_(624188, "Canvas", lambda: Canvas), 30,30, image=_n_(624189, "photo", lambda: photo), anchor=_n_(624190, "CENTER", lambda: CENTER), state=_n_(624191, "NORMAL", lambda: NORMAL))
    _l_(624193)

_c_(624196, _n_(624195, "draw_chessboard", lambda: draw_chessboard))
_l_(624197)
_c_(624199, _n_(624198, "draw_pieces", lambda: draw_pieces))
_l_(624200)

_c_(624203, _a_(624202, _n_(624201, "root", lambda: root), "mainloop"))
_l_(624204)