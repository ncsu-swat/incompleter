# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39841881/typeerror-python-unit-testing-using-mock
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
session = _c_(673444, _n_(673439, "scoped_session", lambda: scoped_session), _c_(673443, _n_(673440, "sessionmaker", lambda: sessionmaker), bind=_a_(673442, _n_(673441, "db_state", lambda: db_state), "engine")))
_l_(673445)
@_c_(673450, _n_(673446, "use_kwargs", lambda: use_kwargs), {
    'user_id': _c_(673449, _a_(673448, _n_(673447, "fields", lambda: fields), "Integer"), location='json', required=True)
})
def create_user(user_id):
    _l_(673473)

    with _n_(673451, "session", lambda: session) as s:
        _l_(673472)

        try:
            _l_(673471)

            result = _c_(673456, _a_(673453, _n_(673452, "user_dao", lambda: user_dao), "create_user"), _n_(673454, "s", lambda: s), _n_(673455, "user_id", lambda: user_id))
            _l_(673457)
            aux = _c_(673461, _a_(673459, _n_(673458, "json", lambda: json), "dumps"), _n_(673460, "result", lambda: result)), 200, {'Content-Type': 'application/json; charset=utf-8'}
            _l_(673462)
            return aux
        except _n_(673463, "SQLAlchemyError", lambda: SQLAlchemyError):
            _l_(673470)

            result = {"Fatal": "Id not found"}
            _l_(673464)
            aux = _c_(673468, _a_(673466, _n_(673465, "json", lambda: json), "dumps"), _n_(673467, "result", lambda: result)), 404, {'Content-Type': 'application/json; charset=utf-8'}
            _l_(673469)
            return aux