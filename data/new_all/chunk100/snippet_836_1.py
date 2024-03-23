# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(83278)

except ImportError:
    pass
_c_(83280, _n_(83279, "print", lambda: print), 'Write dictionaries to a CSV file:')
_l_(83281)
fw = _c_(83283, _n_(83282, "open", lambda: open), 'test.csv', 'w', newline='')
_l_(83284)
writer = _c_(83288, _a_(83286, _n_(83285, "csv", lambda: csv), "DictWriter"), _n_(83287, "fw", lambda: fw), fieldnames=['Name', 'Class'])
_l_(83289)
_c_(83292, _a_(83291, _n_(83290, "writer", lambda: writer), "writeheader"))
_l_(83293)
_c_(83296, _a_(83295, _n_(83294, "writer", lambda: writer), "writerow"), {'Name': 'Jasmine Barrett', 'Class': 'V'})
_l_(83297)
_c_(83300, _a_(83299, _n_(83298, "writer", lambda: writer), "writerow"), {'Name': 'Garry Watson', 'Class': 'V'})
_l_(83301)
_c_(83304, _a_(83303, _n_(83302, "writer", lambda: writer), "writerow"), {'Name': 'Courtney Caldwell', 'Class': 'VI'})
_l_(83305)
_c_(83308, _a_(83307, _n_(83306, "fw", lambda: fw), "close"))
_l_(83309)
fr = _c_(83311, _n_(83310, "open", lambda: open), 'test.csv', 'r')
_l_(83312)
for row in _n_(83313, "csv", lambda: csv):
    _l_(83318)

    _c_(83316, _n_(83314, "print", lambda: print), _n_(83315, "row", lambda: row))
    _l_(83317)
_c_(83321, _a_(83320, _n_(83319, "fr", lambda: fr), "close"))
_l_(83322)