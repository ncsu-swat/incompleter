# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(617859, _a_(617858, _n_(617857, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(617860, "login_required", lambda: login_required)
def test():
  _l_(617889)


  if _a_(617862, _n_(617861, "request", lambda: request), "is_xhr"):
    _l_(617887)


    try:
      _l_(617879)


      json_response = {
        "result": "success"
      }
      _l_(617863)

    except _n_(617864, "Exception", lambda: Exception) as e:
      _l_(617878)

      err = _c_(617874, _n_(617865, "_except", lambda: _except), line=_a_(617869, _c_(617868, _a_(617867, _n_(617866, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(617870, "e", lambda: e), function_name=_c_(617872, _n_(617871, "what_func", lambda: what_func)), script_name=_n_(617873, "__file__", lambda: __file__))
      _l_(617875)
      json_response = {"result": "failure", "msg": _n_(617876, "err", lambda: err)}
      _l_(617877)
    aux = _c_(617882, _n_(617880, "jsonify", lambda: jsonify), _n_(617881, "json_response", lambda: json_response))
    _l_(617883)

    return aux

  else:
    aux = _c_(617885, _n_(617884, "redirect", lambda: redirect), "/not-found")
    _l_(617886)
    return aux
  aux = ''
  _l_(617888)

  return aux