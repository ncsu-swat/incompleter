# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58782469/python-class-inheritance-attributeerror-error-while-calling-child-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import yaml
    _l_(351290)

except ImportError:
    pass
"""
Class created to read yaml files 
and extract requested literals seamlessly
"""

class GetConfig:
    _l_(351328)

    @_n_(351291, "staticmethod", lambda: staticmethod)
    def __check_values(*args):
        _l_(351312)

        yaml = _n_(351292, "args", lambda: args)[0]
        _l_(351293)
        keys = _n_(351294, "args", lambda: args)[1:]
        _l_(351295)
        integrity = True
        _l_(351296)
        arguments = [_n_(351297, "y", lambda: y) for y, in _c_(351300, _a_(351299, _n_(351298, "yaml", lambda: yaml), "items")) if _n_(351301, "y", lambda: y) not in _n_(351302, "keys", lambda: keys)]
        _l_(351303)
        if _c_(351306, _n_(351304, "len", lambda: len), _n_(351305, "arguments", lambda: arguments)) > 0:
            _l_(351308)

            integrity = False
            _l_(351307)
        aux = _n_(351309, "integrity", lambda: integrity), _n_(351310, "arguments", lambda: arguments)
        _l_(351311)
        return aux

    @_n_(351313, "classmethod", lambda: classmethod)
    def __load_yml(cls, yml_string):
        _l_(351327)

        with _c_(351318, _n_(351314, "open", lambda: open), _c_(351317, _a_(351315, "{}.yml", "format"), _n_(351316, "yml_string", lambda: yml_string)), 'r') as stream:
            _l_(351324)

            config = _c_(351322, _a_(351320, _n_(351319, "yaml", lambda: yaml), "safe_load"), _n_(351321, "stream", lambda: stream))
            _l_(351323)
        aux = _n_(351325, "config", lambda: config)
        _l_(351326)
        return aux


class GetConnection(_n_(351329, "GetConfig", lambda: GetConfig)):
    _l_(351385)

    def __init__(self, server_name, username, db):
        _l_(351354)

        """
        Generate database connection strings
            Arguments:
            :param server_name: as alphanumeric string
            :param username: as alphanumeric string
            :param db: as alphanumeric string
        """
        integrity, params = _c_(351338, _a_(351331, _n_(351330, "self", lambda: self), "__check_values"), _c_(351334, _a_(351333, _n_(351332, "self", lambda: self), "__load_yml"), 'connection_info'), _n_(351335, "server_name", lambda: server_name), _n_(351336, "username", lambda: username), _n_(351337, "db", lambda: db))
        _l_(351339)
        if _n_(351340, "integrity", lambda: integrity) is False:
            _l_(351344)

            _c_(351342, _n_(351341, "quit", lambda: quit))
            _l_(351343)
        _n_(351345, "self", lambda: self).server_name = _n_(351346, "server_name", lambda: server_name)
        _l_(351347)
        _n_(351348, "self", lambda: self).username = _n_(351349, "username", lambda: username)
        _l_(351350)
        _n_(351351, "self", lambda: self).db = _n_(351352, "db", lambda: db)
        _l_(351353)

    def __get_db_scope_access(self):
        _l_(351384)

        config = _c_(351357, _a_(351356, _n_(351355, "self", lambda: self), "__load_yml"), 'connection_info')
        _l_(351358)
        server = _n_(351359, "config", lambda: config)['server'][_a_(351361, _n_(351360, "self", lambda: self), "server_name")]['connection_string']
        _l_(351362)
        user = _n_(351363, "config", lambda: config)['server']['A']['databases'][_a_(351365, _n_(351364, "self", lambda: self), "db")]['db_credentials'][_a_(351367, _n_(351366, "self", lambda: self), "username")][0]
        _l_(351368)
        passw = _n_(351369, "config", lambda: config)['server']['A']['databases'][_a_(351371, _n_(351370, "self", lambda: self), "db")]['db_credentials'][_a_(351373, _n_(351372, "self", lambda: self), "username")][1]
        _l_(351374)
        db = _a_(351376, _n_(351375, "self", lambda: self), "db")
        _l_(351377)
        aux = _n_(351378, "server", lambda: server), _n_(351379, "db", lambda: db), _n_(351380, "user", lambda: user), _n_(351381, "passw", lambda: passw), _n_(351382, "config", lambda: config)
        _l_(351383)
        return aux


if _n_(351386, "__name__", lambda: __name__) == "__main__":
    _l_(351402)

    instance = _c_(351388, _n_(351387, "GetConnection", lambda: GetConnection), 'A', 'claudio', 'mmd1')
    _l_(351389)
    _c_(351392, _n_(351390, "print", lambda: print), _n_(351391, "instance", lambda: instance))
    _l_(351393)
    str = _c_(351396, _a_(351395, _n_(351394, "instance", lambda: instance), "connection_string"), 'mssql')
    _l_(351397)
    _c_(351400, _n_(351398, "print", lambda: print), _n_(351399, "str", lambda: str))
    _l_(351401)