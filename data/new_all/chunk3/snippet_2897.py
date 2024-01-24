# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59159518/list-of-lists-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lst = [['Descendant Without A Conscience', 'good', 'happy'], ['Wolf Of The Solstice', '30000', 'sad'], ['Women Of Hope', '-4000', 'neutral'], ['Pirates Of Perfection', '65467', 'neutral'], ['Warriors And Soldiers', '-5435', 'sad'], ['Butchers And Soldiers', '76542', 'sad'], ['World Of The Mountain', '6536543', 'sad'], ['Ruination Of Dusk', '-2000', 'happy'], ['Destroying The Stars', '5435', 'happy'], ['Blinded In My Enemies', '765745.5', 'happy'], ['Descendant Without A Conscience', 'good', 'happy']]
_l_(558005)

check_lst = _c_(558010, _n_(558006, "list", lambda: list), _c_(558009, _n_(558007, "set", lambda: set), _n_(558008, "lst", lambda: lst)))
_l_(558011)

for movie in _n_(558012, "lst", lambda: lst):
   _l_(558038)


   if _c_(558015, _n_(558013, "len", lambda: len), _n_(558014, "movie", lambda: movie)) > 3:
      _l_(558037)


      raise _c_(558017, _n_(558016, "ValueError", lambda: ValueError), 'Invalid input.')
      _l_(558018)


   elif _n_(558019, "movie", lambda: movie)[2] != _c_(558022, _a_(558021, _n_(558020, "movie", lambda: movie)[2], "lower")):
      _l_(558036)


      raise _c_(558024, _n_(558023, "ValueError", lambda: ValueError), 'Invalid input.')
      _l_(558025)

   elif _c_(558028, _n_(558026, "len", lambda: len), _n_(558027, "lst", lambda: lst)) != _c_(558031, _n_(558029, "len", lambda: len), _n_(558030, "check_lst", lambda: check_lst)):
      _l_(558035)

      raise _c_(558033, _n_(558032, "ValueError", lambda: ValueError), 'Invalid input.')
      _l_(558034)