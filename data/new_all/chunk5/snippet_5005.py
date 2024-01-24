# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(672536)

except ImportError:
    pass
try:
    from gi.repository import Gtk, Poppler
    _l_(672538)

except ImportError:
    pass

testFile = 'file://' + _c_(672545, _a_(672541, _a_(672540, _n_(672539, "os", lambda: os), "path"), "join"), _c_(672544, _a_(672543, _n_(672542, "os", lambda: os), "getcwd")), 'printTestPdf.pdf')
_l_(672546)
pdfDocument = _c_(672551, _a_(672549, _a_(672548, _n_(672547, "Poppler", lambda: Poppler), "Document"), "new_from_file"), _n_(672550, "testFile", lambda: testFile), None)
_l_(672552)

class Example(_a_(672554, _n_(672553, "Gtk", lambda: Gtk), "Window")):
    _l_(672652)

    def __init__(self):
        _l_(672565)

        _c_(672559, _a_(672558, _n_(672555, "super", lambda: super)(_n_(672556, "Example", lambda: Example), _n_(672557, "self", lambda: self)), "__init__"))                
        _l_(672560)                
        _c_(672563, _a_(672562, _n_(672561, "self", lambda: self), "init_ui"))
        _l_(672564)

    def init_ui(self):
        _l_(672606)

        _c_(672568, _a_(672567, _n_(672566, "self", lambda: self), "set_title"), "Print Pdf Test")
        _l_(672569)
        _c_(672572, _a_(672571, _n_(672570, "self", lambda: self), "resize"), 230, 150)
        _l_(672573)
        _c_(672579, _a_(672575, _n_(672574, "self", lambda: self), "set_position"), _a_(672578, _a_(672577, _n_(672576, "Gtk", lambda: Gtk), "WindowPosition"), "CENTER"))
        _l_(672580)
        _c_(672585, _a_(672582, _n_(672581, "self", lambda: self), "connect"), "delete-event", _a_(672584, _n_(672583, "Gtk", lambda: Gtk), "main_quit"))                
        _l_(672586)                
        printButton = _c_(672589, _a_(672588, _n_(672587, "Gtk", lambda: Gtk), "Button"), 'Press Me')
        _l_(672590)
        _c_(672594, _a_(672592, _n_(672591, "self", lambda: self), "add"), _n_(672593, "printButton", lambda: printButton))
        _l_(672595)
        _c_(672600, _a_(672597, _n_(672596, "printButton", lambda: printButton), "connect"), 'clicked', _a_(672599, _n_(672598, "self", lambda: self), "on_printButton_clicked"))
        _l_(672601)
        _c_(672604, _a_(672603, _n_(672602, "self", lambda: self), "show_all"))
        _l_(672605)

    def on_printButton_clicked(self, widget):
        _l_(672636)

        """
        Handler for the button click.
        """                
        printOperation = _c_(672609, _a_(672608, _n_(672607, "Gtk", lambda: Gtk), "PrintOperation"))
        _l_(672610)
        _c_(672615, _a_(672612, _n_(672611, "printOperation", lambda: printOperation), "connect"), 'draw-page', _a_(672614, _n_(672613, "self", lambda: self), "on_printOperation_draw_page"))
        _l_(672616)
        _c_(672619, _a_(672618, _n_(672617, "printOperation", lambda: printOperation), "set_job_name"), 'Print Pdf Test')
        _l_(672620)
        _c_(672626, _a_(672622, _n_(672621, "printOperation", lambda: printOperation), "set_n_pages"), _c_(672625, _a_(672624, _n_(672623, "pdfDocument", lambda: pdfDocument), "get_n_pages")))
        _l_(672627)
        _c_(672634, _a_(672629, _n_(672628, "printOperation", lambda: printOperation), "run"), _a_(672632, _a_(672631, _n_(672630, "Gtk", lambda: Gtk), "PrintOperationAction"), "PRINT_DIALOG"),
                           parent=_n_(672633, "self", lambda: self))
        _l_(672635)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        _l_(672651)

        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = _c_(672639, _a_(672638, _n_(672637, "context", lambda: context), "get_cairo_context")) # <-- THIS IS THE LINE
        _l_(672640) # <-- THIS IS THE LINE
        page = _c_(672644, _a_(672642, _n_(672641, "pdfDocument", lambda: pdfDocument), "get_page"), _n_(672643, "pageNo", lambda: pageNo))
        _l_(672645)
        _c_(672649, _a_(672647, _n_(672646, "page", lambda: page), "render_for_printing"), _n_(672648, "cr", lambda: cr))
        _l_(672650)

def main():
    _l_(672660)

    app = _c_(672654, _n_(672653, "Example", lambda: Example))
    _l_(672655)
    _c_(672658, _a_(672657, _n_(672656, "Gtk", lambda: Gtk), "main"))
    _l_(672659)

if _n_(672661, "__name__", lambda: __name__) == "__main__":
    _l_(672665)

    _c_(672663, _n_(672662, "main", lambda: main))
    _l_(672664)