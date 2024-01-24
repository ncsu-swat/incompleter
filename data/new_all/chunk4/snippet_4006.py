# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081846/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(628392, _a_(628391, _n_(628390, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(628393, "login_required", lambda: login_required)
def test():
  _l_(628422)


  if _a_(628395, _n_(628394, "request", lambda: request), "is_xhr"):
    _l_(628420)


    try:
      _l_(628412)


      json_response = {
        "result": "success"
      }
      _l_(628396)

    except _n_(628397, "Exception", lambda: Exception) as e:
      _l_(628411)

      err = _c_(628407, _n_(628398, "_except", lambda: _except), line=_a_(628402, _c_(628401, _a_(628400, _n_(628399, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(628403, "e", lambda: e), function_name=_c_(628405, _n_(628404, "what_func", lambda: what_func)), script_name=_n_(628406, "__file__", lambda: __file__))
      _l_(628408)
      json_response = {"result": "failure", "msg": _n_(628409, "err", lambda: err)}
      _l_(628410)
    aux = _c_(628415, _n_(628413, "jsonify", lambda: jsonify), _n_(628414, "json_response", lambda: json_response))
    _l_(628416)

    return aux

  else:
    aux = _c_(628418, _n_(628417, "redirect", lambda: redirect), "/not-found")
    _l_(628419)
    return aux
  aux = ''
  _l_(628421)

  return aux