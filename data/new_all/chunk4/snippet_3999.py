# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(620223, _a_(620222, _n_(620221, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(620224, "login_required", lambda: login_required)
def test():
  _l_(620253)


  if _a_(620226, _n_(620225, "request", lambda: request), "is_xhr"):
    _l_(620251)


    try:
      _l_(620243)


      json_response = {
        "result": "success"
      }
      _l_(620227)

    except _n_(620228, "Exception", lambda: Exception) as e:
      _l_(620242)

      err = _c_(620238, _n_(620229, "_except", lambda: _except), line=_a_(620233, _c_(620232, _a_(620231, _n_(620230, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(620234, "e", lambda: e), function_name=_c_(620236, _n_(620235, "what_func", lambda: what_func)), script_name=_n_(620237, "__file__", lambda: __file__))
      _l_(620239)
      json_response = {"result": "failure", "msg": _n_(620240, "err", lambda: err)}
      _l_(620241)
    aux = _c_(620246, _n_(620244, "jsonify", lambda: jsonify), _n_(620245, "json_response", lambda: json_response))
    _l_(620247)

    return aux

  else:
    aux = _c_(620249, _n_(620248, "redirect", lambda: redirect), "/not-found")
    _l_(620250)
    return aux
  aux = ''
  _l_(620252)

  return aux