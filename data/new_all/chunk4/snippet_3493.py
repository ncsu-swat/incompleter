# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73418212/attributeerror-module-networkx-has-no-attribute-nx-pydot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
serial_no = _c_(631353, _n_(631351, "str", lambda: str), _n_(631352, "i", lambda: i))
_l_(631354)
document = _c_(631359, _a_(631358, _c_(631357, _n_(631355, "open", lambda: open), 'DataSet/Source/'+_n_(631356, "serial_no", lambda: serial_no)+'.txt'), "read"))
_l_(631360)
doc = _c_(631366, _a_(631364, _c_(631363, _a_(631362, _n_(631361, "sentTokenizer", lambda: sentTokenizer), "sentTokenizing")), "sentTokenize"), _n_(631365, "document", lambda: document))
_l_(631367)
_c_(631370, _n_(631368, "print", lambda: print), 'doc',_n_(631369, "doc", lambda: doc))
_l_(631371)

filenamee, n = _c_(631375, _a_(631373, _n_(631372, "clustering", lambda: clustering), "startF"), _n_(631374, "doc", lambda: doc))
_l_(631376)
_c_(631379, _n_(631377, "print", lambda: print), "\n\nSource:",_n_(631378, "document", lambda: document))
_l_(631380)

summary = _c_(631383, _n_(631381, "getSummary", lambda: getSummary), _n_(631382, "filenamee", lambda: filenamee))
_l_(631384)
_c_(631387, _n_(631385, "print", lambda: print), '\n\nSummary:',_n_(631386, "summary", lambda: summary))
_l_(631388)

# save the summary
_c_(631390, _n_(631389, "createFolder", lambda: createFolder), 'DataSet/')
_l_(631391)
fi = _c_(631394, _n_(631392, "open", lambda: open), 'DataSet/'+_n_(631393, "serial_no", lambda: serial_no)+'.txt','+w')
_l_(631395)
_c_(631399, _a_(631397, _n_(631396, "fi", lambda: fi), "write"), _n_(631398, "summary", lambda: summary))
_l_(631400)