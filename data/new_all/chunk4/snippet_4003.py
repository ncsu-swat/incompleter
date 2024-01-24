# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(638362, _a_(638361, _n_(638360, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(638363, "login_required", lambda: login_required)
def test():
  _l_(638392)


  if _a_(638365, _n_(638364, "request", lambda: request), "is_xhr"):
    _l_(638390)


    try:
      _l_(638382)


      json_response = {
        "result": "success"
      }
      _l_(638366)

    except _n_(638367, "Exception", lambda: Exception) as e:
      _l_(638381)

      err = _c_(638377, _n_(638368, "_except", lambda: _except), line=_a_(638372, _c_(638371, _a_(638370, _n_(638369, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(638373, "e", lambda: e), function_name=_c_(638375, _n_(638374, "what_func", lambda: what_func)), script_name=_n_(638376, "__file__", lambda: __file__))
      _l_(638378)
      json_response = {"result": "failure", "msg": _n_(638379, "err", lambda: err)}
      _l_(638380)
    aux = _c_(638385, _n_(638383, "jsonify", lambda: jsonify), _n_(638384, "json_response", lambda: json_response))
    _l_(638386)

    return aux

  else:
    aux = _c_(638388, _n_(638387, "redirect", lambda: redirect), "/not-found")
    _l_(638389)
    return aux
  aux = ''
  _l_(638391)

  return aux