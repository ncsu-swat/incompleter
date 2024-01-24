# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76895825/pypdf-pdf-merge-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(603085, _a_(603084, _n_(603083, "website", lambda: website), "route"), '/test-pypdf', methods=('GET',))
def test_pypdf():
    _l_(603135)

    with _c_(603087, _n_(603086, "open", lambda: open), 'document.pdf', 'rb') as inFile, _c_(603089, _n_(603088, "open", lambda: open), 'overlay.pdf', 'rb') as overlay:
        _l_(603133)

        original = _c_(603092, _n_(603090, "PdfReader", lambda: PdfReader), _n_(603091, "inFile", lambda: inFile))
        _l_(603093)
        background = _a_(603095, _n_(603094, "original", lambda: original), "pages")[0]
        _l_(603096)
        _c_(603099, _n_(603097, "print", lambda: print), _n_(603098, "inFile", lambda: inFile))
        _l_(603100)
        _c_(603103, _n_(603101, "print", lambda: print), _n_(603102, "background", lambda: background))
        _l_(603104)
        _c_(603109, _n_(603105, "print", lambda: print), _c_(603108, _n_(603106, "type", lambda: type), _n_(603107, "background", lambda: background)))
        _l_(603110)
        foreground = _c_(603113, _n_(603111, "PdfReader", lambda: PdfReader), _n_(603112, "overlay", lambda: overlay))
        _l_(603114)
        o = _a_(603116, _n_(603115, "foreground", lambda: foreground), "pages")[0]
        _l_(603117)
        _c_(603120, _n_(603118, "print", lambda: print), _n_(603119, "o", lambda: o))
        _l_(603121)
        _c_(603126, _n_(603122, "print", lambda: print), _c_(603125, _n_(603123, "type", lambda: type), _n_(603124, "o", lambda: o)))
        _l_(603127)

        # merge the first two pages
        _c_(603131, _a_(603129, _n_(603128, "background", lambda: background), "merge_page"), _n_(603130, "o", lambda: o))
        _l_(603132)
    aux = 'success'
    _l_(603134)

    return aux