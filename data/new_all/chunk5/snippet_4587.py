# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54962167/typeerror-float-argument-must-be-a-string-or-a-number-not-polygon-linestr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
root = _c_(686398, _a_(686397, _n_(686396, "tk", lambda: tk), "Tk"))
_l_(686399)
filename=_c_(686402, _a_(686401, _n_(686400, "filedialog", lambda: filedialog), "askopenfilename"))
_l_(686403)
shape=_c_(686407, _a_(686405, _n_(686404, "gpd", lambda: gpd), "read_file"), _n_(686406, "filename", lambda: filename))
_l_(686408)
_c_(686411, _a_(686410, _n_(686409, "root", lambda: root), "wm_title"), "GIS")
_l_(686412)
f = _c_(686414, _n_(686413, "Figure", lambda: Figure), figsize = (5,5), dpi = 100)
_l_(686415)
a = _c_(686418, _a_(686417, _n_(686416, "f", lambda: f), "add_subplot"), 111)
_l_(686419)
_c_(686423, _a_(686421, _n_(686420, "a", lambda: a), "plot"), _n_(686422, "shape", lambda: shape))
_l_(686424)
canvas = _c_(686428, _n_(686425, "FigureCanvasTkAgg", lambda: FigureCanvasTkAgg), _n_(686426, "f", lambda: f),master = _n_(686427, "root", lambda: root))
_l_(686429)
_c_(686432, _a_(686431, _n_(686430, "canvas", lambda: canvas), "draw"))
_l_(686433)
_c_(686442, _a_(686437, _c_(686436, _a_(686435, _n_(686434, "canvas", lambda: canvas), "get_tk_widget")), "pack"), side = _a_(686439, _n_(686438, "tk", lambda: tk), "TOP"), fill = _a_(686441, _n_(686440, "tk", lambda: tk), "BOTH"), expand = True)
_l_(686443)
_c_(686446, _a_(686445, _n_(686444, "root", lambda: root), "mainloop"))
_l_(686447)