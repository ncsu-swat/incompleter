# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66005371/problem-with-my-python-api-typeerror-object-of-type-set-is-not-json-serializa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(638891)

    infos = _c_(638867, _a_(638866, _n_(638865, "client", lambda: client), "api"), method='Infos.getInfos')
    _l_(638868)
    clientj = _c_(638873, _a_(638870, _n_(638869, "client", lambda: client), "api"), 'Client.getList',params={
        'order':{},
        'pagination':{},
        'search':{'periodecreated_start':{_c_(638872, _n_(638871, "int", lambda: int), 1577836800)}
        }
    })
    _l_(638874)
except _a_(638876, _n_(638875, "sellsy_api", lambda: sellsy_api), "SellsyAuthenticateError") as e:
    _l_(638883)

    _c_(638881, _n_(638877, "print", lambda: print), _c_(638880, _a_(638878, 'Authentication failed ! Details : {}', "format"), _n_(638879, "e", lambda: e)))
    _l_(638882)
except _a_(638885, _n_(638884, "sellsy_api", lambda: sellsy_api), "SellsyError") as e:
    _l_(638890)

    _c_(638888, _n_(638886, "print", lambda: print), _n_(638887, "e", lambda: e)) 
    _l_(638889) 