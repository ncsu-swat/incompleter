# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(683930)

except ImportError:
    pass
try:
    from gi.repository import Gtk
    _l_(683932)

except ImportError:
    pass
try:
    from weasyprint import HTML
    _l_(683934)

except ImportError:
    pass

testFile = _c_(683941, _a_(683937, _a_(683936, _n_(683935, "os", lambda: os), "path"), "join"), _c_(683940, _a_(683939, _n_(683938, "os", lambda: os), "getcwd")), 'printTestHtml.html')
_l_(683942)
pdfDocument = _c_(683947, _a_(683946, _c_(683945, _n_(683943, "HTML", lambda: HTML), filename=_n_(683944, "testFile", lambda: testFile)), "render"))
_l_(683948)

class Example(_a_(683950, _n_(683949, "Gtk", lambda: Gtk), "Window")):
    _l_(684054)

    def __init__(self):
        _l_(683961)

        _c_(683955, _a_(683954, _n_(683951, "super", lambda: super)(_n_(683952, "Example", lambda: Example), _n_(683953, "self", lambda: self)), "__init__"))           
        _l_(683956)           
        _c_(683959, _a_(683958, _n_(683957, "self", lambda: self), "init_ui"))
        _l_(683960)

    def init_ui(self):
        _l_(684002)

        _c_(683964, _a_(683963, _n_(683962, "self", lambda: self), "set_title"), "Print Html Test")
        _l_(683965)
        _c_(683968, _a_(683967, _n_(683966, "self", lambda: self), "resize"), 230, 150)
        _l_(683969)
        _c_(683975, _a_(683971, _n_(683970, "self", lambda: self), "set_position"), _a_(683974, _a_(683973, _n_(683972, "Gtk", lambda: Gtk), "WindowPosition"), "CENTER"))
        _l_(683976)
        _c_(683981, _a_(683978, _n_(683977, "self", lambda: self), "connect"), "delete-event", _a_(683980, _n_(683979, "Gtk", lambda: Gtk), "main_quit"))           
        _l_(683982)           
        printButton = _c_(683985, _a_(683984, _n_(683983, "Gtk", lambda: Gtk), "Button"), 'Press Me')
        _l_(683986)
        _c_(683990, _a_(683988, _n_(683987, "self", lambda: self), "add"), _n_(683989, "printButton", lambda: printButton))
        _l_(683991)
        _c_(683996, _a_(683993, _n_(683992, "printButton", lambda: printButton), "connect"), 'clicked', _a_(683995, _n_(683994, "self", lambda: self), "on_printButton_clicked"))
        _l_(683997)
        _c_(684000, _a_(683999, _n_(683998, "self", lambda: self), "show_all"))
        _l_(684001)

    def on_printButton_clicked(self, widget):
        _l_(684039)

        """
        Handler for the button click.
        """            
        printOperation = _c_(684005, _a_(684004, _n_(684003, "Gtk", lambda: Gtk), "PrintOperation"))
        _l_(684006)
        _c_(684011, _a_(684008, _n_(684007, "printOperation", lambda: printOperation), "connect"), 'begin-print', _a_(684010, _n_(684009, "self", lambda: self), "on_printOperation_begin_print"))
        _l_(684012)
        _c_(684017, _a_(684014, _n_(684013, "printOperation", lambda: printOperation), "connect"), 'draw-page', _a_(684016, _n_(684015, "self", lambda: self), "on_printOperation_draw_page"))
        _l_(684018)
        _c_(684021, _a_(684020, _n_(684019, "printOperation", lambda: printOperation), "set_job_name"), 'Print HTML Test')
        _l_(684022)
        _c_(684029, _a_(684024, _n_(684023, "printOperation", lambda: printOperation), "set_n_pages"), _c_(684028, _n_(684025, "len", lambda: len), _a_(684027, _n_(684026, "pdfDocument", lambda: pdfDocument), "pages")))
        _l_(684030)
        _c_(684037, _a_(684032, _n_(684031, "printOperation", lambda: printOperation), "run"), _a_(684035, _a_(684034, _n_(684033, "Gtk", lambda: Gtk), "PrintOperationAction"), "PRINT_DIALOG"),
                           parent=_n_(684036, "self", lambda: self))
        _l_(684038)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        _l_(684053)

        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = _c_(684042, _a_(684041, _n_(684040, "context", lambda: context), "get_cairo_context")) # <-- THIS IS THE LINE
        _l_(684043) # <-- THIS IS THE LINE
        page = _a_(684045, _n_(684044, "pdfDocument", lambda: pdfDocument), "pages")[_n_(684046, "pageNo", lambda: pageNo)]
        _l_(684047)
        _c_(684051, _a_(684049, _n_(684048, "page", lambda: page), "paint"), _n_(684050, "cr", lambda: cr)) # <-- there is a separate issue here
        _l_(684052) # <-- there is a separate issue here

def main():
    _l_(684062)

    app = _c_(684056, _n_(684055, "Example", lambda: Example))
    _l_(684057)
    _c_(684060, _a_(684059, _n_(684058, "Gtk", lambda: Gtk), "main"))
    _l_(684061)

if _n_(684063, "__name__", lambda: __name__) == "__main__":
    _l_(684067)

    _c_(684065, _n_(684064, "main", lambda: main))
    _l_(684066)