# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72598949/appending-new-value-to-dictionary-key-gives-attributeerror-int-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
movies = ['star wars', 'avenger', 'iron man', 'spider man', 'star wars', 'spider man', 'iron man', 'star wars', 'star wars']
_l_(639372)
schedule = {}
_l_(639373)

for day, movie in _c_(639376, _n_(639374, "enumerate", lambda: enumerate), _n_(639375, "movies", lambda: movies)):
  _l_(639390)

  if _n_(639377, "movie", lambda: movie) not in _n_(639378, "schedule", lambda: schedule):
    _l_(639389)

    _n_(639379, "schedule", lambda: schedule)[_n_(639380, "movie", lambda: movie)] = _n_(639381, "day", lambda: day)
    _l_(639382)
  else:
    _c_(639387, _a_(639385, _n_(639383, "schedule", lambda: schedule)[_n_(639384, "movie", lambda: movie)], "append"), _n_(639386, "day", lambda: day))
    _l_(639388)
_c_(639393, _n_(639391, "print", lambda: print), _n_(639392, "schedule", lambda: schedule))
_l_(639394)