# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081846/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(593568, _a_(593567, _n_(593566, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(593569, "login_required", lambda: login_required)
def test():
  _l_(593598)


  if _a_(593571, _n_(593570, "request", lambda: request), "is_xhr"):
    _l_(593596)


    try:
      _l_(593588)


      json_response = {
        "result": "success"
      }
      _l_(593572)

    except _n_(593573, "Exception", lambda: Exception) as e:
      _l_(593587)

      err = _c_(593583, _n_(593574, "_except", lambda: _except), line=_a_(593578, _c_(593577, _a_(593576, _n_(593575, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(593579, "e", lambda: e), function_name=_c_(593581, _n_(593580, "what_func", lambda: what_func)), script_name=_n_(593582, "__file__", lambda: __file__))
      _l_(593584)
      json_response = {"result": "failure", "msg": _n_(593585, "err", lambda: err)}
      _l_(593586)
    aux = _c_(593591, _n_(593589, "jsonify", lambda: jsonify), _n_(593590, "json_response", lambda: json_response))
    _l_(593592)

    return aux

  else:
    aux = _c_(593594, _n_(593593, "redirect", lambda: redirect), "/not-found")
    _l_(593595)
    return aux
  aux = ''
  _l_(593597)

  return aux