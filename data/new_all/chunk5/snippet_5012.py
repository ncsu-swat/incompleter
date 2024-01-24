# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71583588/typeerror-menus-init-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(683357)

except ImportError:
    pass
try:
    from meanu_items import *
    _l_(683359)

except ImportError:
    pass


def main():
    _l_(683418)

    windows = _c_(683361, _n_(683360, "Tk", lambda: Tk))
    _l_(683362)
    _c_(683365, _a_(683364, _n_(683363, "windows", lambda: windows), "title"), "NotePad")
    _l_(683366)
    _c_(683369, _a_(683368, _n_(683367, "windows", lambda: windows), "minsize"), width=60, height=80)
    _l_(683370)
    _c_(683373, _a_(683372, _n_(683371, "windows", lambda: windows), "config"))
    _l_(683374)
    # Create place to write a text
    text = _c_(683377, _n_(683375, "Text", lambda: Text), _n_(683376, "windows", lambda: windows))
    _l_(683378)
    _c_(683381, _a_(683380, _n_(683379, "text", lambda: text), "focus"))
    _l_(683382)
    _c_(683385, _a_(683384, _n_(683383, "text", lambda: text), "grid"), pady=0.5, padx=10)
    _l_(683386)

    # Creating Scale
    scroll = _c_(683390, _n_(683387, "Scrollbar", lambda: Scrollbar), _n_(683388, "windows", lambda: windows), orient=_n_(683389, "VERTICAL", lambda: VERTICAL), )
    _l_(683391)
    _c_(683396, _a_(683393, _n_(683392, "scroll", lambda: scroll), "grid"), row=0, column=1, sticky=_n_(683394, "NS", lambda: NS) + _n_(683395, "SE", lambda: SE))
    _l_(683397)
    _c_(683402, _a_(683399, _n_(683398, "text", lambda: text), "config"), yscrollcommand=_a_(683401, _n_(683400, "scroll", lambda: scroll), "set"))
    _l_(683403)
    _c_(683408, _a_(683405, _n_(683404, "scroll", lambda: scroll), "config"), command=_a_(683407, _n_(683406, "text", lambda: text), "yview"))
    _l_(683409)

    menu = _c_(683412, _n_(683410, "Menus", lambda: Menus), _n_(683411, "windows", lambda: windows))
    _l_(683413)

    _c_(683416, _a_(683415, _n_(683414, "windows", lambda: windows), "mainloop"))
    _l_(683417)


if _n_(683419, "__name__", lambda: __name__) == '__main__':
    _l_(683423)

    _c_(683421, _n_(683420, "main", lambda: main))
    _l_(683422)