# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60807377/why-is-python-giving-attributeerror-even-when-the-attribute-does-exist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""
Shortest distance between two cells in a matrix or grid

"""

class Tile:
  _l_(465880)

  def __init__(self, row, col, dist):
    _l_(465879)

    _n_(465870, "self", lambda: self).row = _n_(465871, "row", lambda: row)
    _l_(465872)
    _n_(465873, "self", lambda: self).col = _n_(465874, "col", lambda: col)
    _l_(465875)
    _n_(465876, "self", lambda: self).dist = _n_(465877, "dist", lambda: dist)
    _l_(465878)

def min_path(rows, cols, lot):
  _l_(466046)

  start_node = _c_(465882, _n_(465881, "Tile", lambda: Tile), 0, 0, 0)
  _l_(465883)
  q = []
  _l_(465884)
  _c_(465888, _a_(465886, _n_(465885, "q", lambda: q), "append"), _n_(465887, "start_node", lambda: start_node))
  _l_(465889)
  visited = [[False]*_n_(465890, "cols", lambda: cols) for i in _c_(465893, _n_(465891, "range", lambda: range), _n_(465892, "rows", lambda: rows))]
  _l_(465894)

  for i in _c_(465897, _n_(465895, "range", lambda: range), _n_(465896, "rows", lambda: rows)):
    _l_(465910)

    for j in _c_(465900, _n_(465898, "range", lambda: range), _n_(465899, "cols", lambda: cols)):
      _l_(465909)

      if _n_(465901, "lot", lambda: lot)[_n_(465902, "i", lambda: i)][_n_(465903, "j", lambda: j)] == 0:
        _l_(465908)

        _n_(465904, "visited", lambda: visited)[_n_(465905, "i", lambda: i)][_n_(465906, "j", lambda: j)] = True
        _l_(465907)

  while _n_(465911, "q", lambda: q):
    _l_(466044)

    new_tile = _c_(465914, _a_(465913, _n_(465912, "q", lambda: q), "pop"), 0)
    _l_(465915)

    _c_(465919, _n_(465916, "print", lambda: print), _a_(465918, _n_(465917, "new_tile", lambda: new_tile), "row"))
    _l_(465920)

    if _n_(465921, "lot", lambda: lot)[_a_(465923, _n_(465922, "new_tile", lambda: new_tile), "row")][_a_(465925, _n_(465924, "new_tile", lambda: new_tile), "col")] == 9:
      _l_(465929)

      aux = _a_(465927, _n_(465926, "new_tile", lambda: new_tile), "dist")
      _l_(465928)
      return aux

    if _a_(465931, _n_(465930, "new_tile", lambda: new_tile), "row") - 1 >= 0 and _n_(465932, "visited", lambda: visited)[_a_(465934, _n_(465933, "new_tile", lambda: new_tile), "row") - 1][_a_(465936, _n_(465935, "new_tile", lambda: new_tile), "col")] == False:
      _l_(465957)

      _c_(465944, _n_(465937, "Tile", lambda: Tile), _a_(465939, _n_(465938, "new_tile", lambda: new_tile), "row") - 1, _a_(465941, _n_(465940, "new_tile", lambda: new_tile), "col"), _a_(465943, _n_(465942, "new_tile", lambda: new_tile), "dist") + 1)
      _l_(465945)
      _c_(465949, _a_(465947, _n_(465946, "q", lambda: q), "append"), _n_(465948, "Tile", lambda: Tile))
      _l_(465950)
      _n_(465951, "visited", lambda: visited)[_a_(465953, _n_(465952, "new_tile", lambda: new_tile), "row") - 1][_a_(465955, _n_(465954, "new_tile", lambda: new_tile), "col")] = True
      _l_(465956)

    if _a_(465959, _n_(465958, "new_tile", lambda: new_tile), "row") + 1 < _n_(465960, "rows", lambda: rows) and _n_(465961, "visited", lambda: visited)[_a_(465963, _n_(465962, "new_tile", lambda: new_tile), "row") + 1][_a_(465965, _n_(465964, "new_tile", lambda: new_tile), "col")] == False:
      _l_(465986)

      _c_(465973, _n_(465966, "Tile", lambda: Tile), _a_(465968, _n_(465967, "new_tile", lambda: new_tile), "row") + 1, _a_(465970, _n_(465969, "new_tile", lambda: new_tile), "col"), _a_(465972, _n_(465971, "new_tile", lambda: new_tile), "dist") + 1)
      _l_(465974)
      _c_(465978, _a_(465976, _n_(465975, "q", lambda: q), "append"), _n_(465977, "Tile", lambda: Tile))
      _l_(465979)
      _n_(465980, "visited", lambda: visited)[_a_(465982, _n_(465981, "new_tile", lambda: new_tile), "row") + 1][_a_(465984, _n_(465983, "new_tile", lambda: new_tile), "col")] = True
      _l_(465985)

    if _a_(465988, _n_(465987, "new_tile", lambda: new_tile), "col") - 1 >= 0 and _n_(465989, "visited", lambda: visited)[_a_(465991, _n_(465990, "new_tile", lambda: new_tile), "row")][_a_(465993, _n_(465992, "new_tile", lambda: new_tile), "col") - 1] == False:
      _l_(466014)

      _c_(466001, _n_(465994, "Tile", lambda: Tile), _a_(465996, _n_(465995, "new_tile", lambda: new_tile), "row"), _a_(465998, _n_(465997, "new_tile", lambda: new_tile), "col") - 1, _a_(466000, _n_(465999, "new_tile", lambda: new_tile), "dist") + 1)
      _l_(466002)
      _c_(466006, _a_(466004, _n_(466003, "q", lambda: q), "append"), _n_(466005, "Tile", lambda: Tile))
      _l_(466007)
      _n_(466008, "visited", lambda: visited)[_a_(466010, _n_(466009, "new_tile", lambda: new_tile), "row")][_a_(466012, _n_(466011, "new_tile", lambda: new_tile), "col") - 1] = True
      _l_(466013)

    if _a_(466016, _n_(466015, "new_tile", lambda: new_tile), "col") + 1 < _n_(466017, "cols", lambda: cols) and _n_(466018, "visited", lambda: visited)[_a_(466020, _n_(466019, "new_tile", lambda: new_tile), "row")][_a_(466022, _n_(466021, "new_tile", lambda: new_tile), "col") + 1] == False:
      _l_(466043)

      _c_(466030, _n_(466023, "Tile", lambda: Tile), _a_(466025, _n_(466024, "new_tile", lambda: new_tile), "row"), _a_(466027, _n_(466026, "new_tile", lambda: new_tile), "col") + 1, _a_(466029, _n_(466028, "new_tile", lambda: new_tile), "dist") + 1)
      _l_(466031)
      _c_(466035, _a_(466033, _n_(466032, "q", lambda: q), "append"), _n_(466034, "Tile", lambda: Tile))
      _l_(466036)
      _n_(466037, "visited", lambda: visited)[_a_(466039, _n_(466038, "new_tile", lambda: new_tile), "row")][_a_(466041, _n_(466040, "new_tile", lambda: new_tile), "col") + 1] = True
      _l_(466042)
  aux = -1
  _l_(466045)

  return aux


if _n_(466047, "__name__", lambda: __name__) == "__main__":
  _l_(466057)

  lot = [
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 9, 0],
  ]
  _l_(466048)
  result = _c_(466051, _n_(466049, "min_path", lambda: min_path), 4, 4, _n_(466050, "lot", lambda: lot))
  _l_(466052)
  _c_(466055, _n_(466053, "print", lambda: print), _n_(466054, "result", lambda: result))
  _l_(466056)