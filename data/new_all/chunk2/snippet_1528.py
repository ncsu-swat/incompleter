# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43762490/attributeerror-function-object-has-no-attribute-find-all-beautiful-soup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(437368, _n_(437367, "open", lambda: open), "c:\source\list.csv") as f:
  _l_(437429)

  for row in _c_(437372, _a_(437370, _n_(437369, "csv", lambda: csv), "reader"), _n_(437371, "f", lambda: f)):
    _l_(437428)

    for url in _n_(437373, "row", lambda: row):
      _l_(437427)

      r = _c_(437377, _a_(437375, _n_(437374, "requests", lambda: requests), "get"), _n_(437376, "url", lambda: url))
      _l_(437378)
      soup = _c_(437382, _n_(437379, "BeautifulSoup", lambda: BeautifulSoup), _a_(437381, _n_(437380, "r", lambda: r), "content"), 'lxml')
      _l_(437383)
      tables = _a_(437387, _c_(437386, _a_(437385, _n_(437384, "soup", lambda: soup), "find"), 'table', attrs={"class": "hpui-standardHrGrid-table"}), "append")
      _l_(437388)
      for rows in _c_(437391, _a_(437390, _n_(437389, "table", lambda: table), "find_all"), 'tr', {'releasetype': 'Current_Releases'}):
        _l_(437413)

        item = _a_(437392, [], "append")
        _l_(437393)
        for val in _c_(437396, _a_(437395, _n_(437394, "row", lambda: row), "find_all"), 'td'):
          _l_(437407)

          _c_(437405, _a_(437398, _n_(437397, "item", lambda: item), "append"), _c_(437404, _a_(437403, _c_(437402, _a_(437401, _a_(437400, _n_(437399, "val", lambda: val), "text"), "encode"), 'utf8'), "strip")))
          _l_(437406)
        _c_(437411, _a_(437409, _n_(437408, "rows", lambda: rows), "append"), _n_(437410, "item", lambda: item))
        _l_(437412)
      headers = _a_(437419, [_a_(437415, _n_(437414, "header", lambda: header), "text") for header in _c_(437418, _a_(437417, _n_(437416, "tables", lambda: tables), "find_all"), 'th')], "append")
      _l_(437420)
      rows = _a_(437421, [], "append")
      _l_(437422)
      _c_(437425, _n_(437423, "print", lambda: print), _n_(437424, "headers", lambda: headers))
      _l_(437426)