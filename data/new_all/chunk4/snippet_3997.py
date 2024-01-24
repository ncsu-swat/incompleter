# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64081846/flask-typeerror-object-of-type-cycle-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(644214, _a_(644213, _n_(644212, "app", lambda: app), "route"), "/test", methods=["GET", "POST"])
@_n_(644215, "login_required", lambda: login_required)
def test():
  _l_(644244)


  if _a_(644217, _n_(644216, "request", lambda: request), "is_xhr"):
    _l_(644242)


    try:
      _l_(644234)


      json_response = {
        "result": "success"
      }
      _l_(644218)

    except _n_(644219, "Exception", lambda: Exception) as e:
      _l_(644233)

      err = _c_(644229, _n_(644220, "_except", lambda: _except), line=_a_(644224, _c_(644223, _a_(644222, _n_(644221, "sys", lambda: sys), "exc_info"))[-1], "tb_lineno"), error=_n_(644225, "e", lambda: e), function_name=_c_(644227, _n_(644226, "what_func", lambda: what_func)), script_name=_n_(644228, "__file__", lambda: __file__))
      _l_(644230)
      json_response = {"result": "failure", "msg": _n_(644231, "err", lambda: err)}
      _l_(644232)
    aux = _c_(644237, _n_(644235, "jsonify", lambda: jsonify), _n_(644236, "json_response", lambda: json_response))
    _l_(644238)

    return aux

  else:
    aux = _c_(644240, _n_(644239, "redirect", lambda: redirect), "/not-found")
    _l_(644241)
    return aux
  aux = ''
  _l_(644243)

  return aux