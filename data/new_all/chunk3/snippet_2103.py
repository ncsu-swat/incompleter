# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63840413/typeerror-method-object-is-not-subscriptable-flask-sql
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(578693, _a_(578692, _n_(578691, "app", lambda: app), "route"), '/<string:autor>')
def iniciarSesion(autor):
    _l_(578702)

    autor_id = _a_(578698, _c_(578697, _a_(578695, _n_(578694, "db", lambda: db), "execute"), "SELECT id FROM autores WHERE autor = :autor", {"autor":_n_(578696, "autor", lambda: autor)}), "fetchone")[0]
    _l_(578699)
    aux = _n_(578700, "autor_id", lambda: autor_id)
    _l_(578701)
    return aux