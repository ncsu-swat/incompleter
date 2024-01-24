# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35280588/typeerror-execute-got-an-unexpected-keyword-argument-multi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
query = "DELETE FROM Service_Machine WHERE Id=(SELECT Id FROM Machines WHERE Id="+_n_(378833, "id", lambda: id)+");" \
        "DELETE FROM Machine_Usage WHERE Id=(SELECT Id FROM Machines WHERE Id="+_n_(378834, "id", lambda: id)+");" \
                    "DELETE FROM Machines WHERE Id="+_n_(378835, "id", lambda: id)+");"
_l_(378836)
_c_(378839, _n_(378837, "print", lambda: print), _n_(378838, "query", lambda: query))
_l_(378840)
_c_(378845, _a_(378843, _a_(378842, _n_(378841, "self", lambda: self), "cursor"), "execute"), _n_(378844, "query", lambda: query), multi=True)
_l_(378846)