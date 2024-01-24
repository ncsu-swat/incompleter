# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38986341/python-nameerror-name-is-not-defined-related-to-having-default-input-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def circularFind(myByteArray, searchVal, start=0, end=_c_(432143, _n_(432141, "len", lambda: len), _n_(432142, "myByteArray", lambda: myByteArray))):
    _l_(432173)

    """
    Return the first-encountered index in bytearray where searchVal 
    is found, searching to the right, in incrementing-index order, and
    wrapping over the top and back to the beginning if index end < 
    index start
    """
    if (_n_(432144, "end", lambda: end) >= _n_(432145, "start", lambda: start)):
        _l_(432172)

        aux = _c_(432151, _a_(432147, _n_(432146, "myByteArray", lambda: myByteArray), "find"), _n_(432148, "searchVal", lambda: searchVal), _n_(432149, "start", lambda: start), _n_(432150, "end", lambda: end))
        _l_(432152)
        return aux
    else: #end < start, so search to highest index in bytearray, and then wrap around and search to "end" if nothing was found 
        index = _c_(432160, _a_(432154, _n_(432153, "myByteArray", lambda: myByteArray), "find"), _n_(432155, "searchVal", lambda: searchVal), _n_(432156, "start", lambda: start), _c_(432159, _n_(432157, "len", lambda: len), _n_(432158, "myByteArray", lambda: myByteArray)))
        _l_(432161)
        if (_n_(432162, "index", lambda: index) == -1):
            _l_(432169)

            #if searchVal not found yet, wrap around and keep searching 
            index = _c_(432167, _a_(432164, _n_(432163, "myByteArray", lambda: myByteArray), "find"), _n_(432165, "searchVal", lambda: searchVal), 0, _n_(432166, "end", lambda: end))
            _l_(432168)
        aux = _n_(432170, "index", lambda: index) 
        _l_(432171) 
        return aux 