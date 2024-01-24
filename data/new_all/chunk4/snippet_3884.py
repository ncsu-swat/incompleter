# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66005371/problem-with-my-python-api-typeerror-object-of-type-set-is-not-json-serializa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(590502)

    infos = _c_(590478, _a_(590477, _n_(590476, "client", lambda: client), "api"), method='Infos.getInfos')
    _l_(590479)
    clientj = _c_(590484, _a_(590481, _n_(590480, "client", lambda: client), "api"), 'Client.getList',params={
        'order':{},
        'pagination':{},
        'search':{'periodecreated_start':{_c_(590483, _n_(590482, "int", lambda: int), 1577836800)}
        }
    })
    _l_(590485)
except _a_(590487, _n_(590486, "sellsy_api", lambda: sellsy_api), "SellsyAuthenticateError") as e:
    _l_(590494)

    _c_(590492, _n_(590488, "print", lambda: print), _c_(590491, _a_(590489, 'Authentication failed ! Details : {}', "format"), _n_(590490, "e", lambda: e)))
    _l_(590493)
except _a_(590496, _n_(590495, "sellsy_api", lambda: sellsy_api), "SellsyError") as e:
    _l_(590501)

    _c_(590499, _n_(590497, "print", lambda: print), _n_(590498, "e", lambda: e)) 
    _l_(590500) 