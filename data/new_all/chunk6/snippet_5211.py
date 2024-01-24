# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58782469/python-class-inheritance-attributeerror-error-while-calling-child-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import yaml
    _l_(362163)

except ImportError:
    pass
"""
Class created to read yaml files 
and extract requested literals seamlessly
"""

class GetConfig:
    _l_(362201)

    @_n_(362164, "staticmethod", lambda: staticmethod)
    def __check_values(*args):
        _l_(362185)

        yaml = _n_(362165, "args", lambda: args)[0]
        _l_(362166)
        keys = _n_(362167, "args", lambda: args)[1:]
        _l_(362168)
        integrity = True
        _l_(362169)
        arguments = [_n_(362170, "y", lambda: y) for y, in _c_(362173, _a_(362172, _n_(362171, "yaml", lambda: yaml), "items")) if _n_(362174, "y", lambda: y) not in _n_(362175, "keys", lambda: keys)]
        _l_(362176)
        if _c_(362179, _n_(362177, "len", lambda: len), _n_(362178, "arguments", lambda: arguments)) > 0:
            _l_(362181)

            integrity = False
            _l_(362180)
        aux = _n_(362182, "integrity", lambda: integrity), _n_(362183, "arguments", lambda: arguments)
        _l_(362184)
        return aux

    @_n_(362186, "classmethod", lambda: classmethod)
    def __load_yml(cls, yml_string):
        _l_(362200)

        with _c_(362191, _n_(362187, "open", lambda: open), _c_(362190, _a_(362188, "{}.yml", "format"), _n_(362189, "yml_string", lambda: yml_string)), 'r') as stream:
            _l_(362197)

            config = _c_(362195, _a_(362193, _n_(362192, "yaml", lambda: yaml), "safe_load"), _n_(362194, "stream", lambda: stream))
            _l_(362196)
        aux = _n_(362198, "config", lambda: config)
        _l_(362199)
        return aux


class GetConnection(_n_(362202, "GetConfig", lambda: GetConfig)):
    _l_(362258)

    def __init__(self, server_name, username, db):
        _l_(362227)

        """
        Generate database connection strings
            Arguments:
            :param server_name: as alphanumeric string
            :param username: as alphanumeric string
            :param db: as alphanumeric string
        """
        integrity, params = _c_(362211, _a_(362204, _n_(362203, "self", lambda: self), "__check_values"), _c_(362207, _a_(362206, _n_(362205, "self", lambda: self), "__load_yml"), 'connection_info'), _n_(362208, "server_name", lambda: server_name), _n_(362209, "username", lambda: username), _n_(362210, "db", lambda: db))
        _l_(362212)
        if _n_(362213, "integrity", lambda: integrity) is False:
            _l_(362217)

            _c_(362215, _n_(362214, "quit", lambda: quit))
            _l_(362216)
        _n_(362218, "self", lambda: self).server_name = _n_(362219, "server_name", lambda: server_name)
        _l_(362220)
        _n_(362221, "self", lambda: self).username = _n_(362222, "username", lambda: username)
        _l_(362223)
        _n_(362224, "self", lambda: self).db = _n_(362225, "db", lambda: db)
        _l_(362226)

    def __get_db_scope_access(self):
        _l_(362257)

        config = _c_(362230, _a_(362229, _n_(362228, "self", lambda: self), "__load_yml"), 'connection_info')
        _l_(362231)
        server = _n_(362232, "config", lambda: config)['server'][_a_(362234, _n_(362233, "self", lambda: self), "server_name")]['connection_string']
        _l_(362235)
        user = _n_(362236, "config", lambda: config)['server']['A']['databases'][_a_(362238, _n_(362237, "self", lambda: self), "db")]['db_credentials'][_a_(362240, _n_(362239, "self", lambda: self), "username")][0]
        _l_(362241)
        passw = _n_(362242, "config", lambda: config)['server']['A']['databases'][_a_(362244, _n_(362243, "self", lambda: self), "db")]['db_credentials'][_a_(362246, _n_(362245, "self", lambda: self), "username")][1]
        _l_(362247)
        db = _a_(362249, _n_(362248, "self", lambda: self), "db")
        _l_(362250)
        aux = _n_(362251, "server", lambda: server), _n_(362252, "db", lambda: db), _n_(362253, "user", lambda: user), _n_(362254, "passw", lambda: passw), _n_(362255, "config", lambda: config)
        _l_(362256)
        return aux


if _n_(362259, "__name__", lambda: __name__) == "__main__":
    _l_(362275)

    instance = _c_(362261, _n_(362260, "GetConnection", lambda: GetConnection), 'A', 'claudio', 'mmd1')
    _l_(362262)
    _c_(362265, _n_(362263, "print", lambda: print), _n_(362264, "instance", lambda: instance))
    _l_(362266)
    str = _c_(362269, _a_(362268, _n_(362267, "instance", lambda: instance), "connection_string"), 'mssql')
    _l_(362270)
    _c_(362273, _n_(362271, "print", lambda: print), _n_(362272, "str", lambda: str))
    _l_(362274)