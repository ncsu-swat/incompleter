# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081846/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(617517, _a_(617516, _n_(617515, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(617518, "login_required", lambda: login_required)
def test():
  _l_(617559)


  if _a_(617520, _n_(617519, "request", lambda: request), "is_xhr"):
    _l_(617557)


    try:
      _l_(617549)


      _dict = {
        "key1": "value1",
        "key2": "value2"
      }
      _l_(617521)

      if not "my_dict" in _n_(617522, "session", lambda: session):
        _l_(617530)

        _n_(617523, "session", lambda: session)["my_dict"] = [_n_(617524, "_dict", lambda: _dict)]
        _l_(617525)
      else:
        _n_(617526, "session", lambda: session)["my_dict"] = _n_(617527, "session", lambda: session)["my_dict"] + [_n_(617528, "_dict", lambda: _dict)]
        _l_(617529)

      _n_(617531, "session", lambda: session).modified = True
      _l_(617532)

      json_response = {
        "result": "success"
      }
      _l_(617533)

    except _n_(617534, "Exception", lambda: Exception) as e:
      _l_(617548)

      err = _c_(617544, _n_(617535, "_except", lambda: _except), line=_a_(617539, _c_(617538, _a_(617537, _n_(617536, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(617540, "e", lambda: e), function_name=_c_(617542, _n_(617541, "what_func", lambda: what_func)), script_name=_n_(617543, "__file__", lambda: __file__))
      _l_(617545)
      json_response = {"result": "failure", "msg": _n_(617546, "err", lambda: err)}
      _l_(617547)
    aux = _c_(617552, _n_(617550, "jsonify", lambda: jsonify), _n_(617551, "json_response", lambda: json_response))
    _l_(617553)

    return aux

  else:
    aux = _c_(617555, _n_(617554, "redirect", lambda: redirect), "/not-found")
    _l_(617556)
    return aux
  aux = ''
  _l_(617558)

  return aux