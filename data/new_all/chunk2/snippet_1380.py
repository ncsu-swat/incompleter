# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67425476/how-to-get-rid-of-the-resize-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(442144)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(442146)

except ImportError:
    pass

image1 = _c_(442149, _a_(442148, _n_(442147, "Image", lambda: Image), "open"), "enseigne.JPEG")
_l_(442150)
image1= _c_(442154, _a_(442152, _n_(442151, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(442153, "image1", lambda: image1))
_l_(442155)
imageresize = _c_(442160, _a_(442157, _n_(442156, "image1", lambda: image1), "thumbnail"), (500,500), _a_(442159, _n_(442158, "Image", lambda: Image), "ANTIALIAS"))
_l_(442161)
imageresize = _c_(442165, _a_(442163, _n_(442162, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(442164, "imageresize", lambda: imageresize))
_l_(442166)
limage = _c_(442171, _a_(442168, _n_(442167, "tk", lambda: tk), "Label"), _n_(442169, "app", lambda: app), image=_n_(442170, "imageresize", lambda: imageresize))
_l_(442172)