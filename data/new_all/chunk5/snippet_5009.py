# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(706022)

except ImportError:
    pass
try:
    from gi.repository import Gtk
    _l_(706024)

except ImportError:
    pass
try:
    from weasyprint import HTML
    _l_(706026)

except ImportError:
    pass

testFile = _c_(706033, _a_(706029, _a_(706028, _n_(706027, "os", lambda: os), "path"), "join"), _c_(706032, _a_(706031, _n_(706030, "os", lambda: os), "getcwd")), 'printTestHtml.html')
_l_(706034)
pdfDocument = _c_(706039, _a_(706038, _c_(706037, _n_(706035, "HTML", lambda: HTML), filename=_n_(706036, "testFile", lambda: testFile)), "render"))
_l_(706040)

class Example(_a_(706042, _n_(706041, "Gtk", lambda: Gtk), "Window")):
    _l_(706146)

    def __init__(self):
        _l_(706053)

        _c_(706047, _a_(706046, _n_(706043, "super", lambda: super)(_n_(706044, "Example", lambda: Example), _n_(706045, "self", lambda: self)), "__init__"))           
        _l_(706048)           
        _c_(706051, _a_(706050, _n_(706049, "self", lambda: self), "init_ui"))
        _l_(706052)

    def init_ui(self):
        _l_(706094)

        _c_(706056, _a_(706055, _n_(706054, "self", lambda: self), "set_title"), "Print Html Test")
        _l_(706057)
        _c_(706060, _a_(706059, _n_(706058, "self", lambda: self), "resize"), 230, 150)
        _l_(706061)
        _c_(706067, _a_(706063, _n_(706062, "self", lambda: self), "set_position"), _a_(706066, _a_(706065, _n_(706064, "Gtk", lambda: Gtk), "WindowPosition"), "CENTER"))
        _l_(706068)
        _c_(706073, _a_(706070, _n_(706069, "self", lambda: self), "connect"), "delete-event", _a_(706072, _n_(706071, "Gtk", lambda: Gtk), "main_quit"))           
        _l_(706074)           
        printButton = _c_(706077, _a_(706076, _n_(706075, "Gtk", lambda: Gtk), "Button"), 'Press Me')
        _l_(706078)
        _c_(706082, _a_(706080, _n_(706079, "self", lambda: self), "add"), _n_(706081, "printButton", lambda: printButton))
        _l_(706083)
        _c_(706088, _a_(706085, _n_(706084, "printButton", lambda: printButton), "connect"), 'clicked', _a_(706087, _n_(706086, "self", lambda: self), "on_printButton_clicked"))
        _l_(706089)
        _c_(706092, _a_(706091, _n_(706090, "self", lambda: self), "show_all"))
        _l_(706093)

    def on_printButton_clicked(self, widget):
        _l_(706131)

        """
        Handler for the button click.
        """            
        printOperation = _c_(706097, _a_(706096, _n_(706095, "Gtk", lambda: Gtk), "PrintOperation"))
        _l_(706098)
        _c_(706103, _a_(706100, _n_(706099, "printOperation", lambda: printOperation), "connect"), 'begin-print', _a_(706102, _n_(706101, "self", lambda: self), "on_printOperation_begin_print"))
        _l_(706104)
        _c_(706109, _a_(706106, _n_(706105, "printOperation", lambda: printOperation), "connect"), 'draw-page', _a_(706108, _n_(706107, "self", lambda: self), "on_printOperation_draw_page"))
        _l_(706110)
        _c_(706113, _a_(706112, _n_(706111, "printOperation", lambda: printOperation), "set_job_name"), 'Print HTML Test')
        _l_(706114)
        _c_(706121, _a_(706116, _n_(706115, "printOperation", lambda: printOperation), "set_n_pages"), _c_(706120, _n_(706117, "len", lambda: len), _a_(706119, _n_(706118, "pdfDocument", lambda: pdfDocument), "pages")))
        _l_(706122)
        _c_(706129, _a_(706124, _n_(706123, "printOperation", lambda: printOperation), "run"), _a_(706127, _a_(706126, _n_(706125, "Gtk", lambda: Gtk), "PrintOperationAction"), "PRINT_DIALOG"),
                           parent=_n_(706128, "self", lambda: self))
        _l_(706130)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        _l_(706145)

        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = _c_(706134, _a_(706133, _n_(706132, "context", lambda: context), "get_cairo_context")) # <-- THIS IS THE LINE
        _l_(706135) # <-- THIS IS THE LINE
        page = _a_(706137, _n_(706136, "pdfDocument", lambda: pdfDocument), "pages")[_n_(706138, "pageNo", lambda: pageNo)]
        _l_(706139)
        _c_(706143, _a_(706141, _n_(706140, "page", lambda: page), "paint"), _n_(706142, "cr", lambda: cr)) # <-- there is a separate issue here
        _l_(706144) # <-- there is a separate issue here

def main():
    _l_(706154)

    app = _c_(706148, _n_(706147, "Example", lambda: Example))
    _l_(706149)
    _c_(706152, _a_(706151, _n_(706150, "Gtk", lambda: Gtk), "main"))
    _l_(706153)

if _n_(706155, "__name__", lambda: __name__) == "__main__":
    _l_(706159)

    _c_(706157, _n_(706156, "main", lambda: main))
    _l_(706158)