# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/5512811/builtins-typeerror-must-be-str-not-bytes
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(48338)

except ImportError:
    pass
try:
    from datetime import date
    _l_(48340)

except ImportError:
    pass
try:
    from lxml import etree
    _l_(48342)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(48344)

except ImportError:
    pass

# Create the root element
page = _c_(48347, _a_(48346, _n_(48345, "etree", lambda: etree), "Element"), 'results')
_l_(48348)

# Make a new document tree
doc = _c_(48352, _a_(48350, _n_(48349, "etree", lambda: etree), "ElementTree"), _n_(48351, "page", lambda: page))
_l_(48353)

# Add the subelements
pageElement = _c_(48357, _a_(48355, _n_(48354, "etree", lambda: etree), "SubElement"), _n_(48356, "page", lambda: page), 'Country',Tim = 'Now', 
                                      name='Germany', AnotherParameter = 'Bye',
                                      Code='DE',
                                      Storage='Basic')
_l_(48358)
pageElement = _c_(48362, _a_(48360, _n_(48359, "etree", lambda: etree), "SubElement"), _n_(48361, "page", lambda: page), 'City', 
                                      name='Germany',
                                      Code='PZ',
                                      Storage='Basic',AnotherParameter = 'Hello')
_l_(48363)
# For multiple multiple attributes, use as shown above

# Save to XML file
outFile = _c_(48365, _n_(48364, "open", lambda: open), 'output.xml', 'w')
_l_(48366)
_c_(48370, _a_(48368, _n_(48367, "doc", lambda: doc), "write"), _n_(48369, "outFile", lambda: outFile)) 
_l_(48371) 