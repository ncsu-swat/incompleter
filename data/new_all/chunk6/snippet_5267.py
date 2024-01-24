# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74753310/how-to-solve-this-error-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(348449)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(348451)

except ImportError:
    pass
try:
    from tkinter import filedialog as fd
    _l_(348453)

except ImportError:
    pass

app = _c_(348455, _n_(348454, "Tk", lambda: Tk))
_l_(348456)
file_path = ''
_l_(348457)
def set_file_path(path):
    _l_(348461)

    global file_path
    _l_(348458)
    file_path = _n_(348459, "path", lambda: path)
    _l_(348460)



def open_text_file():
    _l_(348472)

    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    _l_(348462)
    file = _c_(348466, _a_(348464, _n_(348463, "fd", lambda: fd), "askopenfile"), filetypes=_n_(348465, "filetypes", lambda: filetypes))
    _l_(348467)
    _c_(348470, _n_(348468, "set_file_path", lambda: set_file_path), _n_(348469, "file", lambda: file))
    _l_(348471)

def main(row, column, file):
    _l_(348488)

    file = _c_(348476, _a_(348474, _n_(348473, "pd", lambda: pd), "read_excel"), _n_(348475, "file", lambda: file))
    _l_(348477)
    row_new = _n_(348478, "row", lambda: row) - 1
    _l_(348479)
    column_new = _n_(348480, "column", lambda: column) - 1
    _l_(348481)
    text = _n_(348482, "file", lambda: file)[_n_(348483, "column_new", lambda: column_new)][_n_(348484, "row_new", lambda: row_new)]
    _l_(348485)
    aux = _n_(348486, "text", lambda: text)
    _l_(348487)
    return aux


_c_(348491, _a_(348490, _n_(348489, "app", lambda: app), "title"), 'XLSX Reader')
_l_(348492)
_c_(348495, _a_(348494, _n_(348493, "app", lambda: app), "geometry"), "400x400")
_l_(348496)
open_button = _c_(348500, _n_(348497, "Button", lambda: Button), _n_(348498, "app", lambda: app), text='Choose File', command=_n_(348499, "open_text_file", lambda: open_text_file))
_l_(348501)
_c_(348504, _a_(348503, _n_(348502, "open_button", lambda: open_button), "pack"))
_l_(348505)
row = _c_(348508, _n_(348506, "Entry", lambda: Entry), _n_(348507, "app", lambda: app))
_l_(348509)
_c_(348512, _a_(348511, _n_(348510, "row", lambda: row), "pack"))
_l_(348513)
column = _c_(348516, _n_(348514, "Entry", lambda: Entry), _n_(348515, "app", lambda: app))
_l_(348517)
_c_(348520, _a_(348519, _n_(348518, "column", lambda: column), "pack"))
_l_(348521)
Submit = _c_(348529, _n_(348522, "Button", lambda: Button), _n_(348523, "app", lambda: app), text='Get Text', command=_c_(348528, _n_(348524, "main", lambda: main), row=_n_(348525, "row", lambda: row),column=_n_(348526, "column", lambda: column),file=_n_(348527, "file_path", lambda: file_path)))
_l_(348530)
_c_(348533, _a_(348532, _n_(348531, "Submit", lambda: Submit), "pack"))
_l_(348534)
output = _c_(348536, _n_(348535, "main", lambda: main))
_l_(348537)
label = _c_(348540, _n_(348538, "Label", lambda: Label), text=_n_(348539, "output", lambda: output))
_l_(348541)
_c_(348544, _a_(348543, _n_(348542, "label", lambda: label), "pack"))
_l_(348545)

_c_(348548, _a_(348547, _n_(348546, "app", lambda: app), "mainloop"))
_l_(348549)