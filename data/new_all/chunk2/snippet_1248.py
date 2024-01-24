# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64511584/parsing-xml-in-python-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.etree.ElementTree as ET
    _l_(425442)

except ImportError:
    pass

data = '''<person>
<date>Wednesday, Oct 14 2020 1:03AM</date>
<email hide="yes" />
<username>John Doe</username>
</person>'''
_l_(425443)


tree = _c_(425447, _a_(425445, _n_(425444, "ET", lambda: ET), "fromstring"), _n_(425446, "data", lambda: data))
_l_(425448)
_c_(425455, _n_(425449, "print", lambda: print), "Date:", _c_(425454, _a_(425453, _c_(425452, _a_(425451, _n_(425450, "tree", lambda: tree), "find"), 'date'), "text")))
_l_(425456)
_c_(425463, _n_(425457, "print", lambda: print), "Email attr:", _c_(425462, _a_(425461, _c_(425460, _a_(425459, _n_(425458, "tree", lambda: tree), "find"), 'email'), "get"), 'hide'))
_l_(425464)