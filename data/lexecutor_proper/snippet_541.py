# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def lowercase_keys(obj):
  _l_(63608)

  if _c_(63571, _n_(63568, "isinstance", lambda: isinstance), _n_(63569, "obj", lambda: obj), _n_(63570, "dict", lambda: dict)):
    _l_(63605)

    obj = {_c_(63574, _a_(63573, _n_(63572, "key", lambda: key), "lower")): _n_(63575, "value", lambda: value) for key, value in _c_(63578, _a_(63577, _n_(63576, "obj", lambda: obj), "items"))}
    _l_(63579)
    for key, value in _c_(63582, _a_(63581, _n_(63580, "obj", lambda: obj), "items")):
      _l_(63604)

      if _c_(63586, _n_(63583, "isinstance", lambda: isinstance), _n_(63584, "value", lambda: value), _n_(63585, "list", lambda: list)):
        _l_(63597)

        for idx, item in _c_(63589, _n_(63587, "enumerate", lambda: enumerate), _n_(63588, "value", lambda: value)):
          _l_(63596)

          _n_(63590, "value", lambda: value)[_n_(63591, "idx", lambda: idx)] = _c_(63594, _n_(63592, "lowercase_keys", lambda: lowercase_keys), _n_(63593, "item", lambda: item))
          _l_(63595)
      _n_(63598, "obj", lambda: obj)[_n_(63599, "key", lambda: key)] = _c_(63602, _n_(63600, "lowercase_keys", lambda: lowercase_keys), _n_(63601, "value", lambda: value))
      _l_(63603)
  aux = _n_(63606, "obj", lambda: obj) 
  _l_(63607) 
  return aux 

json_str = {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}], "EMB_DICT": {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}]}}
_l_(63609)

_c_(63612, _n_(63610, "lowercase_keys", lambda: lowercase_keys), _n_(63611, "json_str", lambda: json_str))
_l_(63613)


_n_(63614, "Out", lambda: Out)[0]: {'foo': 'BAR',
 'bar': 123,
 'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}],
 'emb_dict': {'foo': 'BAR',
  'bar': 123,
  'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}]}}
_l_(63615)

