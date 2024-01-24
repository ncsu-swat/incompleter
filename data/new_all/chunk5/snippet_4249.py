# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60826193/type-error-while-writing-header-to-a-file-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(663359)

except ImportError:
    pass
try:
    import requests
    _l_(663361)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(663363)

except ImportError:
    pass

url='http://www.mapsofindia.com/districts-india/'
_l_(663364)
response=_c_(663368, _a_(663366, _n_(663365, "requests", lambda: requests), "get"), _n_(663367, "url", lambda: url))
_l_(663369)
html=_a_(663371, _n_(663370, "response", lambda: response), "content")
_l_(663372)

soup=_c_(663375, _n_(663373, "BeautifulSoup", lambda: BeautifulSoup), _n_(663374, "html", lambda: html),'html.parser')
_l_(663376)
table=_c_(663379, _a_(663378, _n_(663377, "soup", lambda: soup), "find"), 'table', attrs={'class':'tableizer-table'})
_l_(663380)
list_of_rows=[]
_l_(663381)
for row in _c_(663384, _a_(663383, _n_(663382, "table", lambda: table), "findAll"), 'tr')[1:]:
    _l_(663401)

    list_of_cells=[]
    _l_(663385)
    for cell in _c_(663388, _a_(663387, _n_(663386, "row", lambda: row), "findAll"), 'td'):
        _l_(663395)

        _c_(663393, _a_(663390, _n_(663389, "list_of_cells", lambda: list_of_cells), "append"), _a_(663392, _n_(663391, "cell", lambda: cell), "text"))
        _l_(663394)
    _c_(663399, _a_(663397, _n_(663396, "list_of_rows", lambda: list_of_rows), "append"), _n_(663398, "list_of_cells", lambda: list_of_cells))
    _l_(663400)
outfile=_c_(663403, _n_(663402, "open", lambda: open), './immates.csv','wb')
_l_(663404)
writer=_c_(663408, _a_(663406, _n_(663405, "csv", lambda: csv), "writer"), _n_(663407, "outfile", lambda: outfile))
_l_(663409)
_c_(663412, _a_(663411, _n_(663410, "writer", lambda: writer), "writerow"), ["SNo", "States", "Dist", "Population"])
_l_(663413)
_c_(663417, _a_(663415, _n_(663414, "writer", lambda: writer), "writerows"), _n_(663416, "list_of_rows", lambda: list_of_rows))
_l_(663418)