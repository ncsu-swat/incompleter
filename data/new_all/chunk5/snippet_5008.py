# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(698037)

except ImportError:
    pass
try:
    from gi.repository import Gtk, Poppler
    _l_(698039)

except ImportError:
    pass

testFile = 'file://' + _c_(698046, _a_(698042, _a_(698041, _n_(698040, "os", lambda: os), "path"), "join"), _c_(698045, _a_(698044, _n_(698043, "os", lambda: os), "getcwd")), 'printTestPdf.pdf')
_l_(698047)
pdfDocument = _c_(698052, _a_(698050, _a_(698049, _n_(698048, "Poppler", lambda: Poppler), "Document"), "new_from_file"), _n_(698051, "testFile", lambda: testFile), None)
_l_(698053)

class Example(_a_(698055, _n_(698054, "Gtk", lambda: Gtk), "Window")):
    _l_(698153)

    def __init__(self):
        _l_(698066)

        _c_(698060, _a_(698059, _n_(698056, "super", lambda: super)(_n_(698057, "Example", lambda: Example), _n_(698058, "self", lambda: self)), "__init__"))                
        _l_(698061)                
        _c_(698064, _a_(698063, _n_(698062, "self", lambda: self), "init_ui"))
        _l_(698065)

    def init_ui(self):
        _l_(698107)

        _c_(698069, _a_(698068, _n_(698067, "self", lambda: self), "set_title"), "Print Pdf Test")
        _l_(698070)
        _c_(698073, _a_(698072, _n_(698071, "self", lambda: self), "resize"), 230, 150)
        _l_(698074)
        _c_(698080, _a_(698076, _n_(698075, "self", lambda: self), "set_position"), _a_(698079, _a_(698078, _n_(698077, "Gtk", lambda: Gtk), "WindowPosition"), "CENTER"))
        _l_(698081)
        _c_(698086, _a_(698083, _n_(698082, "self", lambda: self), "connect"), "delete-event", _a_(698085, _n_(698084, "Gtk", lambda: Gtk), "main_quit"))                
        _l_(698087)                
        printButton = _c_(698090, _a_(698089, _n_(698088, "Gtk", lambda: Gtk), "Button"), 'Press Me')
        _l_(698091)
        _c_(698095, _a_(698093, _n_(698092, "self", lambda: self), "add"), _n_(698094, "printButton", lambda: printButton))
        _l_(698096)
        _c_(698101, _a_(698098, _n_(698097, "printButton", lambda: printButton), "connect"), 'clicked', _a_(698100, _n_(698099, "self", lambda: self), "on_printButton_clicked"))
        _l_(698102)
        _c_(698105, _a_(698104, _n_(698103, "self", lambda: self), "show_all"))
        _l_(698106)

    def on_printButton_clicked(self, widget):
        _l_(698137)

        """
        Handler for the button click.
        """                
        printOperation = _c_(698110, _a_(698109, _n_(698108, "Gtk", lambda: Gtk), "PrintOperation"))
        _l_(698111)
        _c_(698116, _a_(698113, _n_(698112, "printOperation", lambda: printOperation), "connect"), 'draw-page', _a_(698115, _n_(698114, "self", lambda: self), "on_printOperation_draw_page"))
        _l_(698117)
        _c_(698120, _a_(698119, _n_(698118, "printOperation", lambda: printOperation), "set_job_name"), 'Print Pdf Test')
        _l_(698121)
        _c_(698127, _a_(698123, _n_(698122, "printOperation", lambda: printOperation), "set_n_pages"), _c_(698126, _a_(698125, _n_(698124, "pdfDocument", lambda: pdfDocument), "get_n_pages")))
        _l_(698128)
        _c_(698135, _a_(698130, _n_(698129, "printOperation", lambda: printOperation), "run"), _a_(698133, _a_(698132, _n_(698131, "Gtk", lambda: Gtk), "PrintOperationAction"), "PRINT_DIALOG"),
                           parent=_n_(698134, "self", lambda: self))
        _l_(698136)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        _l_(698152)

        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = _c_(698140, _a_(698139, _n_(698138, "context", lambda: context), "get_cairo_context")) # <-- THIS IS THE LINE
        _l_(698141) # <-- THIS IS THE LINE
        page = _c_(698145, _a_(698143, _n_(698142, "pdfDocument", lambda: pdfDocument), "get_page"), _n_(698144, "pageNo", lambda: pageNo))
        _l_(698146)
        _c_(698150, _a_(698148, _n_(698147, "page", lambda: page), "render_for_printing"), _n_(698149, "cr", lambda: cr))
        _l_(698151)

def main():
    _l_(698161)

    app = _c_(698155, _n_(698154, "Example", lambda: Example))
    _l_(698156)
    _c_(698159, _a_(698158, _n_(698157, "Gtk", lambda: Gtk), "main"))
    _l_(698160)

if _n_(698162, "__name__", lambda: __name__) == "__main__":
    _l_(698166)

    _c_(698164, _n_(698163, "main", lambda: main))
    _l_(698165)