# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57958178/attributeerror-transaction-object-has-no-attribute-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from py2neo import Graph
    _l_(448059)

except ImportError:
    pass
graph = _c_(448061, _n_(448060, "Graph", lambda: Graph), "bolt://localhost:7687", user="neo4j", password="mypass")
_l_(448062)
tx = _c_(448065, _a_(448064, _n_(448063, "graph", lambda: graph), "begin"))
_l_(448066)
for name in ["Mohammad", "Ahmad", "Dad", "Mom"]:
    _l_(448072)

    _c_(448070, _a_(448068, _n_(448067, "tx", lambda: tx), "append"), "CREATE (person:Person {name:{name}}) RETURN person", name=_n_(448069, "name", lambda: name))
    _l_(448071)
Mohammad, Ahmad, Dad, Mom = [_a_(448074, _n_(448073, "result", lambda: result), "one") for result in _c_(448077, _a_(448076, _n_(448075, "tx", lambda: tx), "commit"))]
_l_(448078)