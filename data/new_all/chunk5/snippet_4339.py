# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59486590/getting-a-type-error-in-google-colab-that-was-running-just-fine
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
temp_arr = -_c_(658194, _a_(658192, _n_(658191, "np", lambda: np), "sort"), -_n_(658193, "erray", lambda: erray),axis=1)
_l_(658195)
ent_sum = _c_(658200, _a_(658197, _n_(658196, "np", lambda: np), "zeros"), _a_(658199, _n_(658198, "erray", lambda: erray), "shape")[0])
_l_(658201)
loc = _c_(658206, _a_(658203, _n_(658202, "np", lambda: np), "zeros"), _a_(658205, _n_(658204, "erray", lambda: erray), "shape")[0])
_l_(658207)
#print(erray[-2])
#print(temp_arr)
i = 0
_l_(658208)
for row in _n_(658209, "temp_arr", lambda: temp_arr):
  _l_(658225)

  _n_(658210, "ent_sum", lambda: ent_sum)[_n_(658211, "i", lambda: i)] = _c_(658214, _n_(658212, "sum", lambda: sum), _n_(658213, "row", lambda: row))
  _l_(658215)
  i += 1
  _l_(658216)
  for col in _n_(658217, "row", lambda: row):
    _l_(658224)

    if _n_(658218, "i", lambda: i) == 1:
      _l_(658223)

      _c_(658221, _n_(658219, "print", lambda: print), _n_(658220, "col", lambda: col))
      _l_(658222)