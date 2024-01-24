# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55705409/how-to-fix-nameerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        from tkinter import *
        _l_(543959)

except ImportError:
        pass
try:
        from PIL import Image, ImageTk
        _l_(543961)

except ImportError:
        pass
try:
        from tkinter import filedialog
        _l_(543963)

except ImportError:
        pass
try:
        import cv2
        _l_(543965)

except ImportError:
        pass

def select_image():
        _l_(544060)

        global panelA, panelB
        _l_(543966)
        path = _c_(543969, _a_(543968, _n_(543967, "filedialog", lambda: filedialog), "askopenfilename"))
        _l_(543970)
        if _c_(543973, _n_(543971, "len", lambda: len), _n_(543972, "path", lambda: path)) > 0:
                _l_(544018)

                image = _c_(543977, _a_(543975, _n_(543974, "cv2", lambda: cv2), "imread"), _n_(543976, "path", lambda: path))
                _l_(543978)
                gray = _c_(543984, _a_(543980, _n_(543979, "cv2", lambda: cv2), "cvtColor"), _n_(543981, "image", lambda: image), _a_(543983, _n_(543982, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
                _l_(543985)
                edged = _c_(543989, _a_(543987, _n_(543986, "cv2", lambda: cv2), "Canny"), _n_(543988, "gray", lambda: gray), 50, 100)
                _l_(543990)
                image = _c_(543996, _a_(543992, _n_(543991, "cv2", lambda: cv2), "cvtColor"), _n_(543993, "image", lambda: image), _a_(543995, _n_(543994, "cv2", lambda: cv2), "COLOR_BGR2RGB"))
                _l_(543997)
                image = _c_(544001, _a_(543999, _n_(543998, "Image", lambda: Image), "fromarray"), _n_(544000, "image", lambda: image))
                _l_(544002)
                edged = _c_(544006, _a_(544004, _n_(544003, "Image", lambda: Image), "fromarray"), _n_(544005, "edged", lambda: edged))
                _l_(544007)
                image = _c_(544011, _a_(544009, _n_(544008, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(544010, "image", lambda: image))
                _l_(544012)
                edged = _c_(544016, _a_(544014, _n_(544013, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(544015, "edged", lambda: edged))    
                _l_(544017)    
        if _n_(544019, "panelA", lambda: panelA) is None or _n_(544020, "panelB", lambda: panelB) is None:
                _l_(544059)

                panelA = _c_(544023, _n_(544021, "Label", lambda: Label), image=_n_(544022, "image", lambda: image))
                _l_(544024)
                _n_(544025, "panelA", lambda: panelA).image = _n_(544026, "image", lambda: image)
                _l_(544027)
                _c_(544030, _a_(544029, _n_(544028, "panelA", lambda: panelA), "pack"), side="left", padx=10, pady=10)
                _l_(544031)
                panelB = _c_(544034, _n_(544032, "Label", lambda: Label), image=_n_(544033, "edged", lambda: edged))
                _l_(544035)
                _n_(544036, "panelB", lambda: panelB).image = _n_(544037, "edged", lambda: edged)
                _l_(544038)
                _c_(544041, _a_(544040, _n_(544039, "panelB", lambda: panelB), "pack"), side="right", padx=10, pady=10)
                _l_(544042)
        else:
                _c_(544046, _a_(544044, _n_(544043, "panelA", lambda: panelA), "configure"), image=_n_(544045, "image", lambda: image))
                _l_(544047)
                _c_(544051, _a_(544049, _n_(544048, "panelB", lambda: panelB), "configure"), image=_n_(544050, "edged", lambda: edged))
                _l_(544052)
                _n_(544053, "panelA", lambda: panelA).image = _n_(544054, "image", lambda: image)
                _l_(544055)
                _n_(544056, "panelB", lambda: panelB).image = _n_(544057, "edged", lambda: edged)
                _l_(544058)
root = _c_(544062, _n_(544061, "Tk", lambda: Tk))
_l_(544063)
panelA = None
_l_(544064)
panelB = None
_l_(544065)

btn = _c_(544069, _n_(544066, "Button", lambda: Button), _n_(544067, "root", lambda: root), text="Select an image", command=_n_(544068, "select_image", lambda: select_image))
_l_(544070)
_c_(544073, _a_(544072, _n_(544071, "btn", lambda: btn), "pack"), side="bottom", fill="both", expand="yes", padx="10", pady="10")
_l_(544074)

_c_(544077, _a_(544076, _n_(544075, "root", lambda: root), "mainloop"))
_l_(544078)