# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.dom.minidom
    _l_(61582)

except ImportError:
    pass

file = _c_(61584, _n_(61583, "open", lambda: open), "./content.xml", 'r')
_l_(61585)
xml_string = _c_(61588, _a_(61587, _n_(61586, "file", lambda: file), "read"))
_l_(61589)
_c_(61592, _a_(61591, _n_(61590, "file", lambda: file), "close"))
_l_(61593)

parsed_xml = _c_(61598, _a_(61596, _a_(61595, _a_(61594, xml, "dom"), "minidom"), "parseString"), _n_(61597, "xml_string", lambda: xml_string))
_l_(61599)
pretty_xml_as_string = _c_(61602, _a_(61601, _n_(61600, "parsed_xml", lambda: parsed_xml), "toprettyxml"))
_l_(61603)

file = _c_(61605, _n_(61604, "open", lambda: open), "./content_new.xml", 'w')
_l_(61606)
_c_(61610, _a_(61608, _n_(61607, "file", lambda: file), "write"), _n_(61609, "pretty_xml_as_string", lambda: pretty_xml_as_string))
_l_(61611)
_c_(61614, _a_(61613, _n_(61612, "file", lambda: file), "close"))
_l_(61615)

