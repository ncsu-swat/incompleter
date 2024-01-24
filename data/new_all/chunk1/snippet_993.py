# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58418821/xml-parsing-error-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from lxml import etree
    _l_(388472)

except ImportError:
    pass
root = _c_(388478, _a_(388474, _n_(388473, "etree", lambda: etree), "XML"), _c_(388477, _a_(388476, _n_(388475, "my_xml", lambda: my_xml), "encode"), 'ascii'))
_l_(388479)
root2 = _c_(388485, _a_(388481, _n_(388480, "etree", lambda: etree), "XML"), _c_(388484, _a_(388483, _n_(388482, "my_xml2", lambda: my_xml2), "encode"), 'ascii'))
_l_(388486)

_c_(388489, _a_(388488, _n_(388487, "root", lambda: root), "xpath"), '//*[local-name()="name"]/text()')
_l_(388490)
_c_(388493, _a_(388492, _n_(388491, "root2", lambda: root2), "xpath"), '//*[local-name()="claim-text"]/text()')
_l_(388494)