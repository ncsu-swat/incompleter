# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61911606/typeerror-int-object-is-not-iterable-when-executin-sql-with-set-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cursor = _c_(552536, _a_(552535, _n_(552534, "connection", lambda: connection), "cursor"))
_l_(552537)
sql="SELECT id, name, state FROM domain WHERE state='2'"
_l_(552538)
_c_(552542, _a_(552540, _n_(552539, "cursor", lambda: cursor), "execute"), _n_(552541, "sql", lambda: sql))
_l_(552543)
records = _c_(552546, _a_(552545, _n_(552544, "cursor", lambda: cursor), "fetchall"))
_l_(552547)
_c_(552551, _n_(552548, "print", lambda: print), "Total number of records for deleting is: ", _a_(552550, _n_(552549, "cursor", lambda: cursor), "rowcount"))
_l_(552552)

deleted = _c_(552557, _n_(552553, "set", lambda: set), _c_(552556, _a_(552555, _n_(552554, "cursor", lambda: cursor), "execute"), "select distinct name from domain where state = 2"))
_l_(552558)
active = _c_(552563, _n_(552559, "set", lambda: set), _c_(552562, _a_(552561, _n_(552560, "cursor", lambda: cursor), "execute"), "select distinct name from domain where state != 2"))
_l_(552564)

to_delete = _n_(552565, "deleted", lambda: deleted) - _n_(552566, "active", lambda: active)
_l_(552567)

_c_(552569, _n_(552568, "print", lambda: print), 'Printing each domain record', "\n")
_l_(552570)
for row in _n_(552571, "records", lambda: records):
    _l_(552638)


    _c_(552574, _n_(552572, "print", lambda: print), "id = ", _n_(552573, "row", lambda: row)["id"], )
    _l_(552575)
    _c_(552578, _n_(552576, "print", lambda: print), "name = ", _n_(552577, "row", lambda: row)["name"])
    _l_(552579)
    _c_(552582, _n_(552580, "print", lambda: print), "state  = ", _n_(552581, "row", lambda: row)["state"], "\n")
    _l_(552583)

    id = _n_(552584, "row", lambda: row)["id"]
    _l_(552585)
    name = _n_(552586, "row", lambda: row)["name"]
    _l_(552587)
    state = _n_(552588, "row", lambda: row)["state"]
    _l_(552589)

    if _n_(552590, "to_delete", lambda: to_delete) == 2:
        _l_(552637)

        try:
            _l_(552625)

            if _c_(552595, _a_(552593, _a_(552592, _n_(552591, "os", lambda: os), "path"), "exists"), '/data/sa/' + _n_(552594, "name", lambda: name)):
                _l_(552619)

                _c_(552598, _n_(552596, "print", lambda: print), 'found records for deleting: ' + _n_(552597, "name", lambda: name), "\n")
                _l_(552599)
                _c_(552603, _n_(552600, "print", lambda: print), "Total number of records for deleting is: ", _a_(552602, _n_(552601, "cursor", lambda: cursor), "rowcount"))
                _l_(552604)
                _c_(552606, _n_(552605, "input", lambda: input), "Press Enter to continue...")
                _l_(552607)
                _c_(552611, _a_(552609, _n_(552608, "shutil", lambda: shutil), "rmtree"), '/data/sa/' + _n_(552610, "name", lambda: name))
                _l_(552612)
                _c_(552614, _n_(552613, "print", lambda: print), 'records deleted')            
                _l_(552615)            
            else:
                _c_(552617, _n_(552616, "print", lambda: print), 'no Directory found')
                _l_(552618)
        #    pass
        except _n_(552620, "Exception", lambda: Exception) as error:
            _l_(552624)

            _c_(552622, _n_(552621, "print", lambda: print), "Directory already deleted or never existed")
            _l_(552623)
    else:
        _c_(552627, _n_(552626, "print", lambda: print), 'no records for deleting found')
        _l_(552628)
        _c_(552631, _n_(552629, "print", lambda: print), 'domain', _n_(552630, "name", lambda: name))
        _l_(552632)
        _c_(552635, _n_(552633, "print", lambda: print), 'hast state', _n_(552634, "state", lambda: state), "\n")
        _l_(552636)

_c_(552640, _n_(552639, "quit", lambda: quit))
_l_(552641)
_c_(552644, _a_(552643, _n_(552642, "connection", lambda: connection), "close"))
_l_(552645)