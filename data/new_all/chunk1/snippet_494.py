# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35200142/typeerror-with-html-escaping-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from html import escape
    _l_(398659)

except ImportError:
    pass
project_name_unescaped = _c_(398664, _a_(398663, _c_(398662, _a_(398661, _n_(398660, "Project", lambda: Project), "get"), 'name'), "encode"), 'utf-8')
_l_(398665)
project_name = _c_(398668, _n_(398666, "escape", lambda: escape), _n_(398667, "project_name_unescaped", lambda: project_name_unescaped))
_l_(398669)