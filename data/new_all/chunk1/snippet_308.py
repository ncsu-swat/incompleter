# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37369901/attributeerror-httpresponse-object-has-no-attribute-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request
    _l_(401787)

except ImportError:
    pass
try:
    import urllib
    _l_(401789)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(401791)

except ImportError:
    pass

symbolsfile = _c_(401793, _n_(401792, "open", lambda: open), "Stocklist.txt")
_l_(401794)

symbolslist = _c_(401797, _a_(401796, _n_(401795, "symbolsfile", lambda: symbolsfile), "read"))
_l_(401798)

thesymbolslist = _c_(401801, _a_(401800, _n_(401799, "symbolslist", lambda: symbolslist), "split"), "\n")
_l_(401802)

i=0
_l_(401803)


while _n_(401804, "i", lambda: i)<_c_(401807, _n_(401805, "len", lambda: len), _n_(401806, "thesymbolslist", lambda: thesymbolslist)):
    _l_(401831)

    theurl = "http://www.google.com/finance/getprices?q=" + _n_(401808, "thesymbolslist", lambda: thesymbolslist)[_n_(401809, "i", lambda: i)] + "&i=10&p=25m&f=c"
    _l_(401810)
    thepage = _c_(401814, _a_(401812, _a_(401811, urllib, "request"), "urlopen"), _n_(401813, "theurl", lambda: theurl))
    _l_(401815)
    _c_(401827, _n_(401816, "print", lambda: print), _n_(401817, "thesymbolslist", lambda: thesymbolslist)[_n_(401818, "i", lambda: i)] + " price is " + _c_(401821, _a_(401820, _n_(401819, "thepage", lambda: thepage), "split"))[_c_(401826, _n_(401822, "len", lambda: len), _c_(401825, _a_(401824, _n_(401823, "thepage", lambda: thepage), "split")))-1])
    _l_(401828)
    i= _n_(401829, "i", lambda: i)+1
    _l_(401830)