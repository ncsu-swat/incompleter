# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53591660/python-docx-attributeerror-windowspath-object-has-no-attribute-seek
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(401326)

except ImportError:
    pass
try:
    import docx
    _l_(401328)

except ImportError:
    pass
try:
    from docx.shared import Cm
    _l_(401330)

except ImportError:
    pass

filepath = r"C:\Users\Admin\Desktop\img"
_l_(401331)
document = _c_(401334, _a_(401333, _n_(401332, "docx", lambda: docx), "Document"))
_l_(401335)

for file in _c_(401340, _a_(401339, _c_(401338, _n_(401336, "Path", lambda: Path), _n_(401337, "filepath", lambda: filepath)), "iterdir")):
    _l_(401352)

#    paragraph = document.add_paragraph(Path(file).resolve().stem)
    _c_(401350, _a_(401342, _n_(401341, "document", lambda: document), "add_picture"), _c_(401347, _a_(401346, _c_(401345, _n_(401343, "Path", lambda: Path), _n_(401344, "file", lambda: file)), "absolute")), width=_c_(401349, _n_(401348, "Cm", lambda: Cm), 15.0))
    _l_(401351)

_c_(401355, _a_(401354, _n_(401353, "document", lambda: document), "save"), 'test.docx')
_l_(401356)