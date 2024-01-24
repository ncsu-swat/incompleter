# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46834364/python-3typeerror-must-be-str-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from classStack import Stack
    _l_(399056)

except ImportError:
    pass
try:
    from classTree import BinaryTree
    _l_(399058)

except ImportError:
    pass

def buildParseTree(fpexp):
    _l_(399139)

    fplist = _c_(399061, _a_(399060, _n_(399059, "fpexp", lambda: fpexp), "split"))
    _l_(399062)
    pStack = _c_(399064, _n_(399063, "Stack", lambda: Stack))
    _l_(399065)
    eTree = _c_(399067, _n_(399066, "BinaryTree", lambda: BinaryTree), '')
    _l_(399068)
    _c_(399072, _a_(399070, _n_(399069, "pStack", lambda: pStack), "push"), _n_(399071, "eTree", lambda: eTree))
    _l_(399073)
    currentTree = _n_(399074, "eTree", lambda: eTree)
    _l_(399075)
    for i in _n_(399076, "fplist", lambda: fplist):
        _l_(399136)

        if _n_(399077, "i", lambda: i) == '(':
            _l_(399135)

            _c_(399080, _a_(399079, _n_(399078, "currentTree", lambda: currentTree), "insertLeft"), '')
            _l_(399081)
            _c_(399085, _a_(399083, _n_(399082, "pStack", lambda: pStack), "push"), _n_(399084, "currentTree", lambda: currentTree))
            _l_(399086)
            currentTree = _c_(399089, _a_(399088, _n_(399087, "currentTree", lambda: currentTree), "getLeftChild"))
            _l_(399090)

        elif _n_(399091, "i", lambda: i) not in ['+', '-', '*', '/', ')']:
            _l_(399134)

            _c_(399097, _a_(399093, _n_(399092, "currentTree", lambda: currentTree), "setRootVal"), _c_(399096, _n_(399094, "int", lambda: int), _n_(399095, "i", lambda: i)))
            _l_(399098)
            parent = _c_(399101, _a_(399100, _n_(399099, "pStack", lambda: pStack), "pop"))
            _l_(399102)
            currentTree = _n_(399103, "parent", lambda: parent)
            _l_(399104)

        elif _n_(399105, "i", lambda: i) in ['+', '-', '*', '/']:
            _l_(399133)

            _c_(399109, _a_(399107, _n_(399106, "currentTree", lambda: currentTree), "setRootVal"), _n_(399108, "i", lambda: i))
            _l_(399110)
            _c_(399113, _a_(399112, _n_(399111, "currentTree", lambda: currentTree), "insertRight"), '')
            _l_(399114)
            _c_(399118, _a_(399116, _n_(399115, "pStack", lambda: pStack), "push"), _n_(399117, "currentTree", lambda: currentTree))
            _l_(399119)
            currentTree = _c_(399122, _a_(399121, _n_(399120, "currentTree", lambda: currentTree), "getRightChild"))
            _l_(399123)

        elif _n_(399124, "i", lambda: i) == ')':
            _l_(399132)

            currentTree = _c_(399127, _a_(399126, _n_(399125, "pStack", lambda: pStack), "pop"))
            _l_(399128)

        else:
            raise _c_(399130, _n_(399129, "ValueError", lambda: ValueError), "No se contempla el carácter evaluado")
            _l_(399131)
    aux = _n_(399137, "eTree", lambda: eTree)
    _l_(399138)

    return aux

ParseTree = _c_(399141, _n_(399140, "buildParseTree", lambda: buildParseTree), "( 8 * 5 )")
_l_(399142)
_c_(399145, _a_(399144, _n_(399143, "ParseTree", lambda: ParseTree), "printPostordenTree"), 0)
_l_(399146)