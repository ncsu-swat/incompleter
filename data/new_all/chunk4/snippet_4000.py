# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(580483, _a_(580482, _n_(580481, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(580484, "login_required", lambda: login_required)
def test():
  _l_(580525)


  if _a_(580486, _n_(580485, "request", lambda: request), "is_xhr"):
    _l_(580523)


    try:
      _l_(580515)


      _dict = {
        "key1": "value1",
        "key2": "value2"
      }
      _l_(580487)

      if not "my_dict" in _n_(580488, "session", lambda: session):
        _l_(580496)

        _n_(580489, "session", lambda: session)["my_dict"] = [_n_(580490, "_dict", lambda: _dict)]
        _l_(580491)
      else:
        _n_(580492, "session", lambda: session)["my_dict"] = _n_(580493, "session", lambda: session)["my_dict"] + [_n_(580494, "_dict", lambda: _dict)]
        _l_(580495)

      _n_(580497, "session", lambda: session).modified = True
      _l_(580498)

      json_response = {
        "result": "success"
      }
      _l_(580499)

    except _n_(580500, "Exception", lambda: Exception) as e:
      _l_(580514)

      err = _c_(580510, _n_(580501, "_except", lambda: _except), line=_a_(580505, _c_(580504, _a_(580503, _n_(580502, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(580506, "e", lambda: e), function_name=_c_(580508, _n_(580507, "what_func", lambda: what_func)), script_name=_n_(580509, "__file__", lambda: __file__))
      _l_(580511)
      json_response = {"result": "failure", "msg": _n_(580512, "err", lambda: err)}
      _l_(580513)
    aux = _c_(580518, _n_(580516, "jsonify", lambda: jsonify), _n_(580517, "json_response", lambda: json_response))
    _l_(580519)

    return aux

  else:
    aux = _c_(580521, _n_(580520, "redirect", lambda: redirect), "/not-found")
    _l_(580522)
    return aux
  aux = ''
  _l_(580524)

  return aux