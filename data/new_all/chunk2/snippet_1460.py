# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55794829/how-to-solve-the-error-attributeerror-type-object-image-has-no-attribute-op
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(465743)

except ImportError:
    pass
try:
    from PIL import ImageTk,Image
    _l_(465745)

except ImportError:
    pass

def plot_best_batsmen():
    _l_(465805)

    best_batsmen = _a_(465747, _n_(465746, "dataset", lambda: dataset), "loc")[_c_(465752, _a_(465751, _a_(465749, _n_(465748, "dataset", lambda: dataset), "loc")[_n_(465750, "dataset", lambda: dataset)['Innings']>=15,'Average'], "idxmax")),'Names']
    _l_(465753)
    message = ("The best Batsman of the Tournament could possibly be: ", _n_(465754, "best_batsmen", lambda: best_batsmen))
    _l_(465755)
    canvas_width = 500
    _l_(465756)
    canvas_height = 500
    _l_(465757)
    root = _c_(465759, _n_(465758, "Tk", lambda: Tk))
    _l_(465760)
    _c_(465763, _a_(465762, _n_(465761, "root", lambda: root), "geometry"), "600x600")
    _l_(465764)
    _c_(465767, _a_(465766, _n_(465765, "root", lambda: root), "title"), "New Window")
    _l_(465768)
    canvas = _c_(465773, _n_(465769, "Canvas", lambda: Canvas), _n_(465770, "root", lambda: root), width=_n_(465771, "canvas_width", lambda: canvas_width), height=_n_(465772, "canvas_height", lambda: canvas_height))
    _l_(465774)
    _c_(465779, _a_(465776, _n_(465775, "canvas", lambda: canvas), "create_text"), 1, 10, anchor=_n_(465777, "W", lambda: W), text=_n_(465778, "message", lambda: message))
    _l_(465780)
    img = _c_(465786, _a_(465782, _n_(465781, "ImageTk", lambda: ImageTk), "PhotoImage"), _c_(465785, _a_(465784, _n_(465783, "Image", lambda: Image), "open"), "prediction.jpg"))
    _l_(465787)
    _c_(465792, _a_(465789, _n_(465788, "canvas", lambda: canvas), "create_image"), 20, 20, anchor=_n_(465790, "NW", lambda: NW), image=_n_(465791, "img", lambda: img))
    _l_(465793)
    _n_(465794, "canvas", lambda: canvas).image = _n_(465795, "img", lambda: img)
    _l_(465796)
    _c_(465799, _a_(465798, _n_(465797, "canvas", lambda: canvas), "pack"))
    _l_(465800)
    _c_(465803, _a_(465802, _n_(465801, "root", lambda: root), "mainloop"))
    _l_(465804)