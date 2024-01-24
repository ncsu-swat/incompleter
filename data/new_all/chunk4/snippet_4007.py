# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081846/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(643367, _a_(643366, _n_(643365, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(643368, "login_required", lambda: login_required)
def test():
  _l_(643409)


  if _a_(643370, _n_(643369, "request", lambda: request), "is_xhr"):
    _l_(643407)


    try:
      _l_(643399)


      _dict = {
        "key1": "value1",
        "key2": "value2"
      }
      _l_(643371)

      if not "my_dict" in _n_(643372, "session", lambda: session):
        _l_(643380)

        _n_(643373, "session", lambda: session)["my_dict"] = [_n_(643374, "_dict", lambda: _dict)]
        _l_(643375)
      else:
        _n_(643376, "session", lambda: session)["my_dict"] = _n_(643377, "session", lambda: session)["my_dict"] + [_n_(643378, "_dict", lambda: _dict)]
        _l_(643379)

      _n_(643381, "session", lambda: session).modified = True
      _l_(643382)

      json_response = {
        "result": "success"
      }
      _l_(643383)

    except _n_(643384, "Exception", lambda: Exception) as e:
      _l_(643398)

      err = _c_(643394, _n_(643385, "_except", lambda: _except), line=_a_(643389, _c_(643388, _a_(643387, _n_(643386, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(643390, "e", lambda: e), function_name=_c_(643392, _n_(643391, "what_func", lambda: what_func)), script_name=_n_(643393, "__file__", lambda: __file__))
      _l_(643395)
      json_response = {"result": "failure", "msg": _n_(643396, "err", lambda: err)}
      _l_(643397)
    aux = _c_(643402, _n_(643400, "jsonify", lambda: jsonify), _n_(643401, "json_response", lambda: json_response))
    _l_(643403)

    return aux

  else:
    aux = _c_(643405, _n_(643404, "redirect", lambda: redirect), "/not-found")
    _l_(643406)
    return aux
  aux = ''
  _l_(643408)

  return aux