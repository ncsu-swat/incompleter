# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59422448/with-file-openr-encoding-utf-8-as-f-attributeerror-str-object-has-no-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pathlib
    _l_(545740)

except ImportError:
    pass
try:
    import lxml.etree as etree
    _l_(545742)

except ImportError:
    pass
try:
    from lxml.builder import ElementMaker
    _l_(545744)

except ImportError:
    pass
try:
    import functools
    _l_(545746)

except ImportError:
    pass
try:
    import operator
    _l_(545748)

except ImportError:
    pass

# Extract the name
cwd = _c_(545752, _a_(545751, _a_(545750, _n_(545749, "pathlib", lambda: pathlib), "Path"), "cwd"))
_l_(545753)
dirs = _c_(545763, _n_(545754, "list", lambda: list), _c_(545762, _n_(545755, "filter", lambda: filter), lambda d: _c_(545758, _a_(545757, _n_(545756, "d", lambda: d), "is_dir")), _c_(545761, _a_(545760, _n_(545759, "cwd", lambda: cwd), "iterdir"))))
_l_(545764)
langs = [_a_(545766, _n_(545765, "dir_", lambda: dir_), "name") for dir_ in _n_(545767, "dirs", lambda: dirs)]
_l_(545768)
files = _c_(545774, _n_(545769, "map", lambda: map), _c_(545772, _a_(545771, _n_(545770, "operator", lambda: operator), "methodcaller"), 'glob', '*.xml'), _n_(545773, "dirs", lambda: dirs))
_l_(545775)
files = _c_(545789, _n_(545776, "map", lambda: map), lambda d: _c_(545787, _n_(545777, "list", lambda: list), _c_(545786, _n_(545778, "map", lambda: map), lambda f: _a_(545784, _c_(545783, _a_(545782, _c_(545781, _a_(545780, _n_(545779, "f", lambda: f), "with_suffix"), ''), "with_suffix"), ''), "name"), _n_(545785, "d", lambda: d))), _n_(545788, "files", lambda: files))
_l_(545790)
filenames = _c_(545798, _n_(545791, "set", lambda: set), _c_(545797, _a_(545793, _n_(545792, "functools", lambda: functools), "reduce"), _a_(545795, _n_(545794, "operator", lambda: operator), "add"), _n_(545796, "files", lambda: files)))
_l_(545799)

#print(langs)
#print(filenames)

# I will add the names of the files to the identifiers
identifiers = _c_(545801, _n_(545800, "dict", lambda: dict))
_l_(545802)

for file in _n_(545803, "filenames", lambda: filenames):
    _l_(545828)

    with _c_(545806, _a_(545805, _n_(545804, "file", lambda: file), "open"), 'r',encoding="utf-8") as f:
        _l_(545812)

        tree = _c_(545810, _a_(545808, _n_(545807, "etree", lambda: etree), "parse"), _n_(545809, "file", lambda: file))
        _l_(545811)
    root = _c_(545815, _a_(545814, _n_(545813, "tree", lambda: tree), "getroot"))
    _l_(545816)
    _n_(545817, "identifiers", lambda: identifiers)[_n_(545818, "filename", lambda: filename)] = _n_(545819, "root", lambda: root)
    _l_(545820)
    _c_(545826, _n_(545821, "print", lambda: print), _c_(545825, _n_(545822, "list", lambda: list), _a_(545824, _n_(545823, "root", lambda: root), "tag")))
    _l_(545827)