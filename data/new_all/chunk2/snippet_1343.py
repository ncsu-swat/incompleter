# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31912643/typeerror-cant-convert-bytes-object-to-str-implicitly-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tree = _c_(437696, _a_(437694, _n_(437693, "ET", lambda: ET), "ElementTree"), _n_(437695, "element_table", lambda: element_table))
_l_(437697)
xml = _c_(437701, _a_(437699, _n_(437698, "ET", lambda: ET), "tostring"), _n_(437700, "element_table", lambda: element_table))
_l_(437702)
xml = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><?xml-  stylesheet type=\"text/xsl\" href=\".\/xsl\/brsdk.xsl\"?>" + _n_(437703, "xml", lambda: xml)
_l_(437704)
obis_file = _c_(437709, _n_(437705, "open", lambda: open), "OBIS_Support_Chart_" + _c_(437708, _a_(437707, _n_(437706, "sdk_version", lambda: sdk_version), "replace"), ".","_" ) +   ".xml", "w" )
_l_(437710)
_c_(437716, _a_(437712, _n_(437711, "obis_file", lambda: obis_file), "write"), _c_(437715, _a_(437714, _n_(437713, "xml", lambda: xml), "decode"), 'utf8') )
_l_(437717)