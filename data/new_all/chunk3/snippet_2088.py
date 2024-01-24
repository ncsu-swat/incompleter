# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64963543/issues-with-python-decrypt-file-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from StringIO import StringIO
    _l_(548382)

except ImportError:
    pass
try:
    import os
    _l_(548384)

except ImportError:
    pass
try:
    import tkFileDialog
    _l_(548386)

except ImportError:
    pass

def crypt(t, k):
    _l_(548438)

    old = _c_(548389, _n_(548387, "StringIO", lambda: StringIO), _n_(548388, "t", lambda: t))
    _l_(548390)
    new = _c_(548393, _n_(548391, "StringIO", lambda: StringIO), _n_(548392, "t", lambda: t))
    _l_(548394)
    
    for position in _c_(548399, _n_(548395, "xrange", lambda: xrange), _c_(548398, _n_(548396, "len", lambda: len), _n_(548397, "t", lambda: t))):
        _l_(548429)

        bias = _c_(548406, _n_(548400, "ord", lambda: ord), _n_(548401, "k", lambda: k)[_n_(548402, "position", lambda: position) % _c_(548405, _n_(548403, "len", lambda: len), _n_(548404, "k", lambda: k))])
        _l_(548407)
        
        old_char = _c_(548412, _n_(548408, "ord", lambda: ord), _c_(548411, _a_(548410, _n_(548409, "old", lambda: old), "read"), 1))
        _l_(548413)
        new_char = _c_(548417, _n_(548414, "chr", lambda: chr), _n_(548415, "old_char", lambda: old_char) ^ _n_(548416, "bias", lambda: bias))
        _l_(548418)
        
        _c_(548422, _a_(548420, _n_(548419, "new", lambda: new), "seek"), _n_(548421, "position", lambda: position))
        _l_(548423)
        _c_(548427, _a_(548425, _n_(548424, "new", lambda: new), "write"), _n_(548426, "new_char", lambda: new_char))
        _l_(548428)
    
    _c_(548432, _a_(548431, _n_(548430, "new", lambda: new), "seek"), 0)
    _l_(548433)
    aux = _c_(548436, _a_(548435, _n_(548434, "new", lambda: new), "read"))
    _l_(548437)
    return aux


dirname = _c_(548441, _a_(548440, _n_(548439, "tkFileDialog", lambda: tkFileDialog), "askdirectory"), initialdir="/",  title='Please select a directory')
_l_(548442)
files = [_n_(548443, "f", lambda: f) for f in _c_(548447, _a_(548445, _n_(548444, "os", lambda: os), "listdir"), _n_(548446, "dirname", lambda: dirname)) if _c_(548453, _a_(548450, _a_(548449, _n_(548448, "os", lambda: os), "path"), "join"), _n_(548451, "dirname", lambda: dirname), _n_(548452, "f", lambda: f))]
_l_(548454)
for f in _n_(548455, "files", lambda: files):
    _l_(548497)

    t = _c_(548461, _a_(548458, _a_(548457, _n_(548456, "os", lambda: os), "path"), "join"), _n_(548459, "dirname", lambda: dirname), _n_(548460, "f", lambda: f))
    _l_(548462)
    tout = _c_(548468, _a_(548465, _a_(548464, _n_(548463, "os", lambda: os), "path"), "join"), _n_(548466, "dirname", lambda: dirname), 'decr_%s' % _n_(548467, "f", lambda: f))
    _l_(548469)
    
    f_in = _c_(548472, _n_(548470, "open", lambda: open), _n_(548471, "t", lambda: t), 'rb')
    _l_(548473)
    f_out = _c_(548476, _n_(548474, "open", lambda: open), _n_(548475, "tout", lambda: tout), 'wb')
    _l_(548477)
    key = "b8,xaA3rvXb-d&w8P6!9k7dQs.dbkLEw?t!3!`sM(,f!2^6h"
    _l_(548478)
    _c_(548487, _a_(548480, _n_(548479, "f_out", lambda: f_out), "write"), _c_(548486, _n_(548481, "crypt", lambda: crypt), _c_(548484, _a_(548483, _n_(548482, "f_in", lambda: f_in), "read")), _n_(548485, "key", lambda: key)))
    _l_(548488)
    _c_(548491, _a_(548490, _n_(548489, "f_in", lambda: f_in), "close"))
    _l_(548492)
    _c_(548495, _a_(548494, _n_(548493, "f_out", lambda: f_out), "close"))
    _l_(548496)