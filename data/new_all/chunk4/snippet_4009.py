# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(620503, _a_(620502, _n_(620501, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(620504, "login_required", lambda: login_required)
def test():
  _l_(620545)


  if _a_(620506, _n_(620505, "request", lambda: request), "is_xhr"):
    _l_(620543)


    try:
      _l_(620535)


      _dict = {
        "key1": "value1",
        "key2": "value2"
      }
      _l_(620507)

      if not "my_dict" in _n_(620508, "session", lambda: session):
        _l_(620516)

        _n_(620509, "session", lambda: session)["my_dict"] = [_n_(620510, "_dict", lambda: _dict)]
        _l_(620511)
      else:
        _n_(620512, "session", lambda: session)["my_dict"] = _n_(620513, "session", lambda: session)["my_dict"] + [_n_(620514, "_dict", lambda: _dict)]
        _l_(620515)

      _n_(620517, "session", lambda: session).modified = True
      _l_(620518)

      json_response = {
        "result": "success"
      }
      _l_(620519)

    except _n_(620520, "Exception", lambda: Exception) as e:
      _l_(620534)

      err = _c_(620530, _n_(620521, "_except", lambda: _except), line=_a_(620525, _c_(620524, _a_(620523, _n_(620522, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(620526, "e", lambda: e), function_name=_c_(620528, _n_(620527, "what_func", lambda: what_func)), script_name=_n_(620529, "__file__", lambda: __file__))
      _l_(620531)
      json_response = {"result": "failure", "msg": _n_(620532, "err", lambda: err)}
      _l_(620533)
    aux = _c_(620538, _n_(620536, "jsonify", lambda: jsonify), _n_(620537, "json_response", lambda: json_response))
    _l_(620539)

    return aux

  else:
    aux = _c_(620541, _n_(620540, "redirect", lambda: redirect), "/not-found")
    _l_(620542)
    return aux
  aux = ''
  _l_(620544)

  return aux