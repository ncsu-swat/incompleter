# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/18146921/cairo-introspection-errors-in-eclipse-with-pydev-typeerror-couldnt-find-conve
#!/usr/bin/env python3 

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(658252)

except ImportError:
    pass
try:
    from gi.repository import Gtk
    _l_(658254)

except ImportError:
    pass
try:
    from weasyprint import HTML
    _l_(658256)

except ImportError:
    pass

testFile = _c_(658263, _a_(658259, _a_(658258, _n_(658257, "os", lambda: os), "path"), "join"), _c_(658262, _a_(658261, _n_(658260, "os", lambda: os), "getcwd")), 'printTestHtml.html')
_l_(658264)
pdfDocument = _c_(658269, _a_(658268, _c_(658267, _n_(658265, "HTML", lambda: HTML), filename=_n_(658266, "testFile", lambda: testFile)), "render"))
_l_(658270)

class Example(_a_(658272, _n_(658271, "Gtk", lambda: Gtk), "Window")):
    _l_(658376)

    def __init__(self):
        _l_(658283)

        _c_(658277, _a_(658276, _n_(658273, "super", lambda: super)(_n_(658274, "Example", lambda: Example), _n_(658275, "self", lambda: self)), "__init__"))           
        _l_(658278)           
        _c_(658281, _a_(658280, _n_(658279, "self", lambda: self), "init_ui"))
        _l_(658282)

    def init_ui(self):
        _l_(658324)

        _c_(658286, _a_(658285, _n_(658284, "self", lambda: self), "set_title"), "Print Html Test")
        _l_(658287)
        _c_(658290, _a_(658289, _n_(658288, "self", lambda: self), "resize"), 230, 150)
        _l_(658291)
        _c_(658297, _a_(658293, _n_(658292, "self", lambda: self), "set_position"), _a_(658296, _a_(658295, _n_(658294, "Gtk", lambda: Gtk), "WindowPosition"), "CENTER"))
        _l_(658298)
        _c_(658303, _a_(658300, _n_(658299, "self", lambda: self), "connect"), "delete-event", _a_(658302, _n_(658301, "Gtk", lambda: Gtk), "main_quit"))           
        _l_(658304)           
        printButton = _c_(658307, _a_(658306, _n_(658305, "Gtk", lambda: Gtk), "Button"), 'Press Me')
        _l_(658308)
        _c_(658312, _a_(658310, _n_(658309, "self", lambda: self), "add"), _n_(658311, "printButton", lambda: printButton))
        _l_(658313)
        _c_(658318, _a_(658315, _n_(658314, "printButton", lambda: printButton), "connect"), 'clicked', _a_(658317, _n_(658316, "self", lambda: self), "on_printButton_clicked"))
        _l_(658319)
        _c_(658322, _a_(658321, _n_(658320, "self", lambda: self), "show_all"))
        _l_(658323)

    def on_printButton_clicked(self, widget):
        _l_(658361)

        """
        Handler for the button click.
        """            
        printOperation = _c_(658327, _a_(658326, _n_(658325, "Gtk", lambda: Gtk), "PrintOperation"))
        _l_(658328)
        _c_(658333, _a_(658330, _n_(658329, "printOperation", lambda: printOperation), "connect"), 'begin-print', _a_(658332, _n_(658331, "self", lambda: self), "on_printOperation_begin_print"))
        _l_(658334)
        _c_(658339, _a_(658336, _n_(658335, "printOperation", lambda: printOperation), "connect"), 'draw-page', _a_(658338, _n_(658337, "self", lambda: self), "on_printOperation_draw_page"))
        _l_(658340)
        _c_(658343, _a_(658342, _n_(658341, "printOperation", lambda: printOperation), "set_job_name"), 'Print HTML Test')
        _l_(658344)
        _c_(658351, _a_(658346, _n_(658345, "printOperation", lambda: printOperation), "set_n_pages"), _c_(658350, _n_(658347, "len", lambda: len), _a_(658349, _n_(658348, "pdfDocument", lambda: pdfDocument), "pages")))
        _l_(658352)
        _c_(658359, _a_(658354, _n_(658353, "printOperation", lambda: printOperation), "run"), _a_(658357, _a_(658356, _n_(658355, "Gtk", lambda: Gtk), "PrintOperationAction"), "PRINT_DIALOG"),
                           parent=_n_(658358, "self", lambda: self))
        _l_(658360)

    def on_printOperation_draw_page(self, printOperation, context, pageNo):
        _l_(658375)

        """
        Handler for the draw-page signal from the printOperation.
        """
        cr = _c_(658364, _a_(658363, _n_(658362, "context", lambda: context), "get_cairo_context")) # <-- THIS IS THE LINE
        _l_(658365) # <-- THIS IS THE LINE
        page = _a_(658367, _n_(658366, "pdfDocument", lambda: pdfDocument), "pages")[_n_(658368, "pageNo", lambda: pageNo)]
        _l_(658369)
        _c_(658373, _a_(658371, _n_(658370, "page", lambda: page), "paint"), _n_(658372, "cr", lambda: cr)) # <-- there is a separate issue here
        _l_(658374) # <-- there is a separate issue here

def main():
    _l_(658384)

    app = _c_(658378, _n_(658377, "Example", lambda: Example))
    _l_(658379)
    _c_(658382, _a_(658381, _n_(658380, "Gtk", lambda: Gtk), "main"))
    _l_(658383)

if _n_(658385, "__name__", lambda: __name__) == "__main__":
    _l_(658389)

    _c_(658387, _n_(658386, "main", lambda: main))
    _l_(658388)