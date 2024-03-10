# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48087533/with-self-driver-session-as-session-attributeerror-enter-when-link-to-neo4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from neo4j.v1 import GraphDatabase
    _l_(604039)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(604041)

except ImportError:
    pass


class LeaderNeo4j(_n_(604042, "object", lambda: object)):
    _l_(604074)

    def __init__(self, driver):
        _l_(604046)

        _n_(604043, "self", lambda: self).driver = _n_(604044, "driver", lambda: driver)
        _l_(604045)

    def close(self):
        _l_(604052)

        _c_(604050, _a_(604049, _a_(604048, _n_(604047, "self", lambda: self), "driver"), "close"))
        _l_(604051)

    def add_relation(self, name, friend_name):
        _l_(604065)

        with _a_(604055, _a_(604054, _n_(604053, "self", lambda: self), "driver"), "session") as session:
            _l_(604064)

            _c_(604062, _a_(604057, _n_(604056, "session", lambda: session), "write_transaction"), _a_(604059, _n_(604058, "self", lambda: self), "create_relation"), _n_(604060, "name", lambda: name), _n_(604061, "friend_name", lambda: friend_name))
            _l_(604063)

    @_n_(604066, "staticmethod", lambda: staticmethod)
    def create_relation(tx, name, friend_name):
        _l_(604073)

        _c_(604071, _a_(604068, _n_(604067, "tx", lambda: tx), "run"), "MATCH (d1:Department {department_name: $name}),(d2:Department {department_name: $friend_name})"
               "MERGE (d1)-[:下级]->(d2)",
               name=_n_(604069, "name", lambda: name), friend_name=_n_(604070, "friend_name", lambda: friend_name))
        _l_(604072)


if _n_(604075, "__name__", lambda: __name__) == '__main__':
    _l_(604119)

    uri = "bolt://localhost:7687"
    _l_(604076)
    driver = _c_(604080, _a_(604078, _n_(604077, "GraphDatabase", lambda: GraphDatabase), "driver"), _n_(604079, "uri", lambda: uri), auth=("neo4j", "HBUE112"))
    _l_(604081)
    MyNH = _c_(604084, _n_(604082, "LeaderNeo4j", lambda: LeaderNeo4j), _n_(604083, "driver", lambda: driver))
    _l_(604085)
    _c_(604088, _n_(604086, "print", lambda: print), _n_(604087, "MyNH", lambda: MyNH))
    _l_(604089)
    directory = r"D:\Program Files\neo4j-community-3.3.1\import"
    _l_(604090)
    f_name = r"bumen.csv"
    _l_(604091)
    file_data = _c_(604096, _a_(604093, _n_(604092, "pd", lambda: pd), "read_csv"), _n_(604094, "directory", lambda: directory) + '\\' + _n_(604095, "f_name", lambda: f_name), encoding='utf-8')
    _l_(604097)
    for i in _c_(604101, _n_(604098, "range", lambda: range), _a_(604100, _n_(604099, "file_data", lambda: file_data), "shape")[0]):
        _l_(604118)

        line = _c_(604105, _a_(604103, _n_(604102, "file_data", lambda: file_data), "irow"), _n_(604104, "i", lambda: i))
        _l_(604106)
        _c_(604110, _n_(604107, "print", lambda: print), _n_(604108, "line", lambda: line)[0], _n_(604109, "line", lambda: line)[1])
        _l_(604111)
        _c_(604116, _a_(604113, _n_(604112, "MyNH", lambda: MyNH), "add_relation"), _n_(604114, "line", lambda: line)[0], _n_(604115, "line", lambda: line)[1])
        _l_(604117)