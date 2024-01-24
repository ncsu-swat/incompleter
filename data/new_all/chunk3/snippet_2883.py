# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59946870/with-path-openr-encoding-utf-8-as-file-attributeerror-generator-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pathlib
    _l_(550655)

except ImportError:
    pass
try:
    import functools
    _l_(550657)

except ImportError:
    pass
try:
    import operator
    _l_(550659)

except ImportError:
    pass
try:
    import lxml.etree as etree
    _l_(550661)

except ImportError:
    pass
try:
    from lxml.builder import ElementMaker
    _l_(550663)

except ImportError:
    pass

ATTRIB = {"xsi": "test.xsd", "xmlns": "http://www.w3.org/2001/XMLSchema-instance"}
_l_(550664)



def is_element(node):
    _l_(550671)

    aux = _c_(550667, _n_(550665, "hasattr", lambda: hasattr), _n_(550666, "node", lambda: node), 'attrib') and 'name' in _a_(550669, _n_(550668, "node", lambda: node), "attrib")
    _l_(550670)
    return aux


def create_plural(item):
    _l_(550673)

    pass
    _l_(550672)



def main():
    _l_(550772)

    cwd = _c_(550677, _a_(550676, _a_(550675, _n_(550674, "pathlib", lambda: pathlib), "Path"), "cwd"))
    _l_(550678)
    directories = _c_(550688, _n_(550679, "list", lambda: list), _c_(550687, _n_(550680, "filter", lambda: filter), lambda path: _c_(550683, _a_(550682, _n_(550681, "path", lambda: path), "is_dir")), _c_(550686, _a_(550685, _n_(550684, "cwd", lambda: cwd), "iterdir"))))
    _l_(550689)
    langs = [_a_(550691, _n_(550690, "path", lambda: path), "name") for path in _n_(550692, "directories", lambda: directories)]
    _l_(550693)
    files = _c_(550699, _n_(550694, "map", lambda: map), _c_(550697, _a_(550696, _n_(550695, "operator", lambda: operator), "methodcaller"), 'glob', '*.xml'), _n_(550698, "directories", lambda: directories))
    _l_(550700)
    #trees = dict.fromkeys(unique_names, dict())


    for path in _n_(550701, "files", lambda: files):
        _l_(550771)

        with _c_(550704, _a_(550703, _n_(550702, "path", lambda: path), "open"), 'r', encoding="utf-8") as file:
            _l_(550710)

            tree = _c_(550708, _a_(550706, _n_(550705, "etree", lambda: etree), "parse"), _n_(550707, "file", lambda: file))
            _l_(550709)
        root = _c_(550713, _a_(550712, _n_(550711, "tree", lambda: tree), "getroot"))
        _l_(550714)
        name = _a_(550720, _c_(550719, _a_(550718, _c_(550717, _a_(550716, _n_(550715, "xml_path", lambda: xml_path), "with_suffix"), ''), "with_suffix"), ''), "name")
        _l_(550721)
        out_tree = _n_(550722, "trees", lambda: trees)[_n_(550723, "name", lambda: name)]
        _l_(550724)



        for child in _c_(550728, _n_(550725, "filter", lambda: filter), _n_(550726, "is_element", lambda: is_element), _n_(550727, "root", lambda: root)):
            _l_(550770)

            id = _a_(550730, _n_(550729, "child", lambda: child), "attrib")['name']
            _l_(550731)
            text = _a_(550733, _n_(550732, "child", lambda: child), "text")
            _l_(550734)
            if _n_(550735, "id", lambda: id) not in _n_(550736, "out_tree", lambda: out_tree):
                _l_(550742)

                _n_(550737, "out_tree", lambda: out_tree)[_n_(550738, "id", lambda: id)] = _c_(550740, _n_(550739, "list", lambda: list))
                _l_(550741)
            item = _c_(550748, _a_(550744, _n_(550743, "etree", lambda: etree), "Element"), 'language', attrib={"lang": _a_(550747, _a_(550746, _n_(550745, "path", lambda: path), "parent"), "name"), "status": "Reviewed"})
            _l_(550749)
            if _a_(550751, _n_(550750, "child", lambda: child), "tag") == "plurals":
                _l_(550763)

                _n_(550752, "item", lambda: item).text = _c_(550755, _n_(550753, "create_plural", lambda: create_plural), _n_(550754, "child", lambda: child))
                _l_(550756)
            else:
                _n_(550757, "item", lambda: item).text = _c_(550761, _a_(550759, _n_(550758, "etree", lambda: etree), "CDATA"), _n_(550760, "text", lambda: text))
                _l_(550762)
            _c_(550768, _a_(550766, _n_(550764, "out_tree", lambda: out_tree)[_n_(550765, "id", lambda: id)], "append"), _n_(550767, "item", lambda: item))
            _l_(550769)



if _n_(550773, "__name__", lambda: __name__) == '__main__':
    _l_(550777)

    _c_(550775, _n_(550774, "main", lambda: main))
    _l_(550776)