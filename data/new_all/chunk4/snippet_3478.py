# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73739789/parsing-xml-with-python-returning-nonetype-object-not-callable-typeerror-after
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(600944)

except ImportError:
    pass
try:
    import argparse
    _l_(600946)

except ImportError:
    pass


with _c_(600948, _n_(600947, "open", lambda: open), 'Sample1.xml.xml', 'r') as f:
    _l_(600953)

    data = _c_(600951, _a_(600950, _n_(600949, "f", lambda: f), "read"))
    _l_(600952)

Bs_data = _c_(600956, _n_(600954, "BeautifulSoup", lambda: BeautifulSoup), _n_(600955, "data", lambda: data), "xml")
_l_(600957)

findTag1 = _c_(600960, _a_(600959, _n_(600958, "Bs_data", lambda: Bs_data), "findaAll"), 'CATALOG')
_l_(600961)
findTag1Child = _c_(600964, _a_(600963, _n_(600962, "Bs_data", lambda: Bs_data), "find"), {'COMMON': ''})
_l_(600965)
findTag1Child2 = _c_(600968, _a_(600967, _n_(600966, "Bs_data", lambda: Bs_data), "find"), {'BOTANICAL'})
_l_(600969)




# Press the green button in the gutter to run the script.
if _n_(600970, "__name__", lambda: __name__) == '__main__':
    _l_(600983)

    _c_(600973, _n_(600971, "print", lambda: print), _n_(600972, "findTag1Child", lambda: findTag1Child))
    _l_(600974)
    _c_(600977, _n_(600975, "print", lambda: print), _n_(600976, "findTag1", lambda: findTag1))
    _l_(600978)
    _c_(600981, _n_(600979, "print", lambda: print), _n_(600980, "findTag1Child2", lambda: findTag1Child2))
    _l_(600982)