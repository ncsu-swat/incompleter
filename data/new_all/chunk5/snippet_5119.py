# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58260024/attributeerror-str-object-has-no-attribute-firstchild
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(697954)

except ImportError:
    pass
try:
    from xml.dom.minidom import parse
    _l_(697956)

except ImportError:
    pass

j=0
_l_(697957)
path = "C:/Users/User/Downloads"
_l_(697958)
quantity = []
_l_(697959)
# for every file in directory (path above)
for filename in _c_(697963, _a_(697961, _n_(697960, "os", lambda: os), "listdir"), _n_(697962, "path", lambda: path)):
    _l_(698035)

    if not _c_(697966, _a_(697965, _n_(697964, "filename", lambda: filename), "endswith"), '.xml'):
        _l_(697967)

continue    fullname = _c_(697973, _a_(697970, _a_(697969, _n_(697968, "os", lambda: os), "path"), "join"), _n_(697971, "path", lambda: path), _n_(697972, "filename", lambda: filename)) # add path and file together
    _l_(697974) # add path and file together
    data = _c_(697977, _n_(697975, "parse", lambda: parse), _n_(697976, "fullname", lambda: fullname)) # parses XML
    _l_(697978) # parses XML
    ordernum = _c_(697981, _a_(697980, _n_(697979, "data", lambda: data), "getElementsByTagName"), 'OrderNumber') # gets OrderNumber from XML
    _l_(697982) # gets OrderNumber from XML
    _c_(697987, _n_(697983, "print", lambda: print), _a_(697986, _a_(697985, _n_(697984, "ordernum", lambda: ordernum)[0], "firstChild"), "nodeValue")) # prints OrderNumber from XML
    _l_(697988) # prints OrderNumber from XML
    quan = _c_(697991, _a_(697990, _n_(697989, "data", lambda: data), "getElementsByTagName"), 'OrderedQuantity') # same as above with OrderedQuantity
    _l_(697992) # same as above with OrderedQuantity
    k=0
    _l_(697993)
    l=0
    _l_(697994)
    for k, q in _c_(697997, _n_(697995, "enumerate", lambda: enumerate), _n_(697996, "quan", lambda: quan)):
        _l_(698010)

        if _a_(698000, _a_(697999, _n_(697998, "q", lambda: q), "firstChild"), "nodeValue") != None:
            _l_(698009)

            _c_(698007, _a_(698002, _n_(698001, "quantity", lambda: quantity), "append"), _a_(698006, _a_(698005, _n_(698003, "quan", lambda: quan)[_n_(698004, "k", lambda: k)], "firstChild"), "nodeValue"))
            _l_(698008)
    _c_(698013, _a_(698012, _n_(698011, "quantity", lambda: quantity), "append"), "||separator||")
    _l_(698014)
    for l, p in _c_(698017, _n_(698015, "enumerate", lambda: enumerate), _n_(698016, "ordernum", lambda: ordernum)):
        _l_(698030)

        if _a_(698020, _a_(698019, _n_(698018, "p", lambda: p), "firstChild"), "nodeValue") != None:
            _l_(698029)

            _c_(698027, _a_(698022, _n_(698021, "ordernum", lambda: ordernum), "append"), _a_(698026, _a_(698025, _n_(698023, "ordernum", lambda: ordernum)[_n_(698024, "l", lambda: l)], "firstChild"), "nodeValue"))
            _l_(698028)
    _c_(698033, _a_(698032, _n_(698031, "ordernum", lambda: ordernum), "append"), "||separator||")
    _l_(698034)