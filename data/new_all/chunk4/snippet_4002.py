# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081846/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(632448, _a_(632447, _n_(632446, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(632449, "login_required", lambda: login_required)
def test():
  _l_(632490)


  if _a_(632451, _n_(632450, "request", lambda: request), "is_xhr"):
    _l_(632488)


    try:
      _l_(632480)


      _dict = {
        "key1": "value1",
        "key2": "value2"
      }
      _l_(632452)

      if not "my_dict" in _n_(632453, "session", lambda: session):
        _l_(632461)

        _n_(632454, "session", lambda: session)["my_dict"] = [_n_(632455, "_dict", lambda: _dict)]
        _l_(632456)
      else:
        _n_(632457, "session", lambda: session)["my_dict"] = _n_(632458, "session", lambda: session)["my_dict"] + [_n_(632459, "_dict", lambda: _dict)]
        _l_(632460)

      _n_(632462, "session", lambda: session).modified = True
      _l_(632463)

      json_response = {
        "result": "success"
      }
      _l_(632464)

    except _n_(632465, "Exception", lambda: Exception) as e:
      _l_(632479)

      err = _c_(632475, _n_(632466, "_except", lambda: _except), line=_a_(632470, _c_(632469, _a_(632468, _n_(632467, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(632471, "e", lambda: e), function_name=_c_(632473, _n_(632472, "what_func", lambda: what_func)), script_name=_n_(632474, "__file__", lambda: __file__))
      _l_(632476)
      json_response = {"result": "failure", "msg": _n_(632477, "err", lambda: err)}
      _l_(632478)
    aux = _c_(632483, _n_(632481, "jsonify", lambda: jsonify), _n_(632482, "json_response", lambda: json_response))
    _l_(632484)

    return aux

  else:
    aux = _c_(632486, _n_(632485, "redirect", lambda: redirect), "/not-found")
    _l_(632487)
    return aux
  aux = ''
  _l_(632489)

  return aux