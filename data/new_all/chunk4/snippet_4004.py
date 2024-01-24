# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(585992, _a_(585991, _n_(585990, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(585993, "login_required", lambda: login_required)
def test():
  _l_(586034)


  if _a_(585995, _n_(585994, "request", lambda: request), "is_xhr"):
    _l_(586032)


    try:
      _l_(586024)


      _dict = {
        "key1": "value1",
        "key2": "value2"
      }
      _l_(585996)

      if not "my_dict" in _n_(585997, "session", lambda: session):
        _l_(586005)

        _n_(585998, "session", lambda: session)["my_dict"] = [_n_(585999, "_dict", lambda: _dict)]
        _l_(586000)
      else:
        _n_(586001, "session", lambda: session)["my_dict"] = _n_(586002, "session", lambda: session)["my_dict"] + [_n_(586003, "_dict", lambda: _dict)]
        _l_(586004)

      _n_(586006, "session", lambda: session).modified = True
      _l_(586007)

      json_response = {
        "result": "success"
      }
      _l_(586008)

    except _n_(586009, "Exception", lambda: Exception) as e:
      _l_(586023)

      err = _c_(586019, _n_(586010, "_except", lambda: _except), line=_a_(586014, _c_(586013, _a_(586012, _n_(586011, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(586015, "e", lambda: e), function_name=_c_(586017, _n_(586016, "what_func", lambda: what_func)), script_name=_n_(586018, "__file__", lambda: __file__))
      _l_(586020)
      json_response = {"result": "failure", "msg": _n_(586021, "err", lambda: err)}
      _l_(586022)
    aux = _c_(586027, _n_(586025, "jsonify", lambda: jsonify), _n_(586026, "json_response", lambda: json_response))
    _l_(586028)

    return aux

  else:
    aux = _c_(586030, _n_(586029, "redirect", lambda: redirect), "/not-found")
    _l_(586031)
    return aux
  aux = ''
  _l_(586033)

  return aux