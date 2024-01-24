# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64985316/django-adding-data-into-model-from-nested-json-returning-typeerror-nonetype-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _n_(567643, "card_data", lambda: card_data):
  _l_(567668)

  _c_(567666, _a_(567646, _a_(567645, _n_(567644, "Card", lambda: Card), "objects"), "update_or_create"), id=_c_(567649, _a_(567648, _n_(567647, "i", lambda: i), "get"), 'id'),

    defaults={
      'name':       _c_(567652, _a_(567651, _n_(567650, "i", lambda: i), "get"), 'name'),
      'card_faces': _c_(567655, _a_(567654, _n_(567653, "i", lambda: i), "get"), 'card_faces'),
      'f_name':     _c_(567660, _a_(567659, _c_(567658, _a_(567657, _n_(567656, "i", lambda: i), "get"), 'card_faces')[0], "get"), 'name'),
      'b_name':     _c_(567665, _a_(567664, _c_(567663, _a_(567662, _n_(567661, "i", lambda: i), "get"), 'card_faces')[1], "get"), 'name'),
    }
  )
  _l_(567667)