# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/5512811/builtins-typeerror-must-be-str-not-bytes
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(395188)

except ImportError:
    pass
try:
    from datetime import date
    _l_(395190)

except ImportError:
    pass
try:
    from lxml import etree
    _l_(395192)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(395194)

except ImportError:
    pass

# Create the root element
page = _c_(395197, _a_(395196, _n_(395195, "etree", lambda: etree), "Element"), 'results')
_l_(395198)

# Make a new document tree
doc = _c_(395202, _a_(395200, _n_(395199, "etree", lambda: etree), "ElementTree"), _n_(395201, "page", lambda: page))
_l_(395203)

# Add the subelements
pageElement = _c_(395207, _a_(395205, _n_(395204, "etree", lambda: etree), "SubElement"), _n_(395206, "page", lambda: page), 'Country',Tim = 'Now', 
                                      name='Germany', AnotherParameter = 'Bye',
                                      Code='DE',
                                      Storage='Basic')
_l_(395208)
pageElement = _c_(395212, _a_(395210, _n_(395209, "etree", lambda: etree), "SubElement"), _n_(395211, "page", lambda: page), 'City', 
                                      name='Germany',
                                      Code='PZ',
                                      Storage='Basic',AnotherParameter = 'Hello')
_l_(395213)
# For multiple multiple attributes, use as shown above

# Save to XML file
outFile = _c_(395215, _n_(395214, "open", lambda: open), 'output.xml', 'w')
_l_(395216)
_c_(395220, _a_(395218, _n_(395217, "doc", lambda: doc), "write"), _n_(395219, "outFile", lambda: outFile)) 
_l_(395221) 