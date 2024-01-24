# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59238837/typeerror-tensors-in-list-passed-to-values-of-pack-op-have-types-string-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
packed_dataset = _c_(656544, _a_(656542, _n_(656541, "temp_dataset", lambda: temp_dataset), "map"), _n_(656543, "pack", lambda: pack))
_l_(656545)

for features, labels in _c_(656548, _a_(656547, _n_(656546, "packed_dataset", lambda: packed_dataset), "take"), 1):
  _l_(656564)

  _c_(656553, _n_(656549, "print", lambda: print), _c_(656552, _a_(656551, _n_(656550, "features", lambda: features), "numpy")))
  _l_(656554)
  _c_(656556, _n_(656555, "print", lambda: print))
  _l_(656557)
  _c_(656562, _n_(656558, "print", lambda: print), _c_(656561, _a_(656560, _n_(656559, "labels", lambda: labels), "numpy")))
  _l_(656563)