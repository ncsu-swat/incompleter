# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(692769)

except ImportError:
    pass
try:
    from gi.repository import Gtk, Poppler
    _l_(692771)

except ImportError:
    pass

testFile = 'file://' + _c_(692778, _a_(692774, _a_(692773, _n_(692772, "os", lambda: os), "path"), "join"), _c_(692777, _a_(692776, _n_(692775, "os", lambda: os), "getcwd")), 'printTestPdf.pdf')
_l_(692779)
pdfDocument = _c_(692784, _a_(692782, _a_(692781, _n_(692780, "Poppler", lambda: Poppler), "Document"), "new_from_file"), _n_(692783, "testFile", lambda: testFile), None)
_l_(692785)

class Example(_a_(692787, _n_(692786, "Gtk", lambda: Gtk), "Window")):
    _l_(692885)

    def __init__(self):
        _l_(692798)

        _c_(692792, _a_(692791, _n_(692788, "super", lambda: super)(_n_(692789, "Example", lambda: Example), _n_(692790, "self", lambda: self)), "__init__"))                
        _l_(692793)                
        _c_(692796, _a_(692795, _n_(692794, "self", lambda: self), "init_ui"))
        _l_(692797)

    def init_ui(self):
        _l_(692839)

        _c_(692801, _a_(692800, _n_(692799, "self", lambda: self), "set_title"), "Print Pdf Test")
        _l_(692802)
        _c_(692805, _a_(692804, _n_(692803, "self", lambda: self), "resize"), 230, 150)
        _l_(692806)
        _c_(692812, _a_(692808, _n_(692807, "self", lambda: self), "set_position"), _a_(692811, _a_(692810, _n_(692809, "Gtk", lambda: Gtk), "WindowPosition"), "CENTER"))
        _l_(692813)
        _c_(692818, _a_(692815, _n_(692814, "self", lambda: self), "connect"), "delete-event", _a_(692817, _n_(692816, "Gtk", lambda: Gtk), "main_quit"))                
        _l_(692819)                
        printButton = _c_(692822, _a_(692821, _n_(692820, "Gtk", lambda: Gtk), "Button"), 'Press Me')
        _l_(692823)
        _c_(692827, _a_(692825, _n_(692824, "self", lambda: self), "add"), _n_(692826, "printButton", lambda: printButton))
        _l_(692828)
        _c_(692833, _a_(692830, _n_(692829, "printButton", lambda: printButton), "connect"), 'clicked', _a_(692832, _n_(692831, "self", lambda: self), "on_printButton_clicked"))
        _l_(692834)
        _c_(692837, _a_(692836, _n_(692835, "self", lambda: self), "show_all"))
        _l_(692838)

    def on_printButton_clicked(self, widget):
        _l_(692869)

        """
        Handler for the button click.
        """                
        printOperation = _c_(692842, _a_(692841, _n_(692840, "Gtk", lambda: Gtk), "PrintOperation"))
        _l_(692843)
        _c_(692848, _a_(692845, _n_(692844, "printOperation", lambda: printOperation), "connect"), 'draw-page', _a_(692847, _n_(692846, "self", lambda: self), "on_printOperation_draw_page"))
        _l_(692849)
        _c_(692852, _a_(692851, _n_(692850, "printOperation", lambda: printOperation), "set_job_name"), 'Print Pdf Test')
        _l_(692853)
        _c_(692859, _a_(692855, _n_(692854, "printOperation", lambda: printOperation), "set_n_pages"), _c_(692858, _a_(692857, _n_(692856, "pdfDocument", lambda: pdfDocument), "get_n_pages")))
        _l_(692860)
        _c_(692867, _a_(692862, _n_(692861, "printOperation", lambda: printOperation), "run"), _a_(692865, _a_(692864, _n_(692863, "Gtk", lambda: Gtk), "PrintOperationAction"), "PRINT_DIALOG"),
                           parent=_n_(692866, "self", lambda: self))
        _l_(692868)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        _l_(692884)

        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = _c_(692872, _a_(692871, _n_(692870, "context", lambda: context), "get_cairo_context")) # <-- THIS IS THE LINE
        _l_(692873) # <-- THIS IS THE LINE
        page = _c_(692877, _a_(692875, _n_(692874, "pdfDocument", lambda: pdfDocument), "get_page"), _n_(692876, "pageNo", lambda: pageNo))
        _l_(692878)
        _c_(692882, _a_(692880, _n_(692879, "page", lambda: page), "render_for_printing"), _n_(692881, "cr", lambda: cr))
        _l_(692883)

def main():
    _l_(692893)

    app = _c_(692887, _n_(692886, "Example", lambda: Example))
    _l_(692888)
    _c_(692891, _a_(692890, _n_(692889, "Gtk", lambda: Gtk), "main"))
    _l_(692892)

if _n_(692894, "__name__", lambda: __name__) == "__main__":
    _l_(692898)

    _c_(692896, _n_(692895, "main", lambda: main))
    _l_(692897)