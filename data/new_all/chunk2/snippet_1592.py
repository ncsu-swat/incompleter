# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73704946/typeerror-type-object-is-not-iterable-drf
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from django.db import models
  _l_(466648)

except ImportError:
  pass
try:
  from django.contrib.auth import get_user_model
  _l_(466650)

except ImportError:
  pass
try:
  import datetime
  _l_(466652)

except ImportError:
  pass

User = _c_(466654, _n_(466653, "get_user_model", lambda: get_user_model))
_l_(466655)

class Actor(_a_(466657, _n_(466656, "models", lambda: models), "Model")):
  _l_(466666)

  name = _c_(466660, _a_(466659, _n_(466658, "models", lambda: models), "CharField"), max_length=255)
  _l_(466661)
  first_name = _c_(466664, _a_(466663, _n_(466662, "models", lambda: models), "CharField"), max_length=255)
  _l_(466665)

class Movie(_a_(466668, _n_(466667, "models", lambda: models), "Model")):
  _l_(466716)

  title = _c_(466671, _a_(466670, _n_(466669, "models", lambda: models), "CharField"), max_length=255)
  _l_(466672)
  description = _c_(466675, _a_(466674, _n_(466673, "models", lambda: models), "CharField"), max_length=255, default='Description')
  _l_(466676)
  date = _c_(466682, _a_(466678, _n_(466677, "models", lambda: models), "DateTimeField"), default=_a_(466681, _a_(466680, _n_(466679, "datetime", lambda: datetime), "date"), "today"))
  _l_(466683)
  created_on = _c_(466686, _a_(466685, _n_(466684, "models", lambda: models), "DateTimeField"), auto_now_add = True)
  _l_(466687)
  actors = _c_(466691, _a_(466689, _n_(466688, "models", lambda: models), "ManyToManyField"), _n_(466690, "Actor", lambda: Actor))
  _l_(466692)
  user = _c_(466698, _a_(466694, _n_(466693, "models", lambda: models), "ForeignKey"), _n_(466695, "User", lambda: User), on_delete=_a_(466697, _n_(466696, "models", lambda: models), "CASCADE"))
  _l_(466699)
  def average_reviews(self):
    _l_(466715)

    if _c_(466702, _n_(466700, "hasattr", lambda: hasattr), _n_(466701, "self", lambda: self), '_average_reviews'):
      _l_(466706)

      aux = _a_(466704, _n_(466703, "self", lambda: self), "_average_reviews")
      _l_(466705)
      return aux
    aux = _c_(466713, _a_(466709, _a_(466708, _n_(466707, "self", lambda: self), "reviews"), "aggregate"), _c_(466712, _a_(466711, _n_(466710, "models", lambda: models), "Avg"), 'mark'))
    _l_(466714)
    return aux
class Reviews(_a_(466718, _n_(466717, "models", lambda: models), "Model")):
  _l_(466730)

  mark = _c_(466721, _a_(466720, _n_(466719, "models", lambda: models), "IntegerField"), default=5)
  _l_(466722)
  movie = _c_(466728, _a_(466724, _n_(466723, "models", lambda: models), "ForeignKey"), _n_(466725, "Movie", lambda: Movie), on_delete=_a_(466727, _n_(466726, "models", lambda: models), "CASCADE"))
  _l_(466729)