# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47824780/saving-data-into-solr-with-pysolr-get-rejected-attributeerror-str-object-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from solrq import Q
    _l_(473550)

except ImportError:
    pass
try:
    import pysolr
    _l_(473552)

except ImportError:
    pass
try:
    import jsonpickle
    _l_(473554)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(473556)

except ImportError:
    pass
try:
    from Model import Twitter
    _l_(473558)

except ImportError:
    pass



#conexion a solr
solr = _c_(473561, _a_(473560, _n_(473559, "pysolr", lambda: pysolr), "Solr"), 'http://localhost:8983/solr/twitter')
_l_(473562)

#query
query = _c_(473564, _n_(473563, "Q", lambda: Q), label="none")
_l_(473565)
results = _c_(473569, _a_(473567, _n_(473566, "solr", lambda: solr), "search"), _n_(473568, "query", lambda: query))
_l_(473570)


_c_(473577, _n_(473571, "print", lambda: print), _c_(473576, _a_(473572, "Saw {0} result(s).", "format"), _c_(473575, _n_(473573, "len", lambda: len), _n_(473574, "results", lambda: results))))
_l_(473578)

#testing the query
for result in _n_(473579, "results", lambda: results):
    _l_(473586)

    _c_(473584, _n_(473580, "print", lambda: print), _c_(473583, _a_(473581, "-->", "format"), _n_(473582, "result", lambda: result)['content']))
    _l_(473585)

#creating a new class with data    
twit = _c_(473588, _n_(473587, "Twitter", lambda: Twitter), "000002","content text","some label")  
_l_(473589)  
#list of twitter classes
coreData=[]
_l_(473590)

_c_(473594, _a_(473592, _n_(473591, "coreData", lambda: coreData), "append"), _n_(473593, "twit", lambda: twit))
_l_(473595)
#encoding to json
json=_c_(473601, _n_(473596, "str", lambda: str), _c_(473600, _a_(473598, _n_(473597, "jsonpickle", lambda: jsonpickle), "encode"), _n_(473599, "coreData", lambda: coreData), unpicklable=False))
_l_(473602)

_c_(473605, _n_(473603, "print", lambda: print), _n_(473604, "json", lambda: json))
_l_(473606)
#saving to solr
_c_(473610, _a_(473608, _n_(473607, "solr", lambda: solr), "add"), _n_(473609, "json", lambda: json))
_l_(473611)