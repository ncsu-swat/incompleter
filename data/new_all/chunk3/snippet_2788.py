# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63019333/getting-nameerror-while-importing-a-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bot import T_bot
    _l_(526275)

except ImportError:
    pass

update_id= None
_l_(526276)

def make_reply(msg):
    _l_(526280)

    reply= 'okay'
    _l_(526277)
    aux = _n_(526278, "reply", lambda: reply)
    _l_(526279)
    return aux

update_id= None
_l_(526281)

while True:
    _l_(526313)

    
    updates= _c_(526286, _a_(526283, _n_(526282, "T_bot", lambda: T_bot), "gett"), _n_(526284, "self", lambda: self), offset= _n_(526285, "update_id", lambda: update_id))
    _l_(526287)
    updates= _n_(526288, "updates", lambda: updates)["result"]
    _l_(526289)
    if _n_(526290, "updates", lambda: updates):
        _l_(526312)

        for item in _n_(526291, "updates", lambda: updates):
            _l_(526311)

            update_id= _n_(526292, "item", lambda: item)['update_id']
            _l_(526293)
            try:
                _l_(526310)

                message= _n_(526294, "item", lambda: item)['message']['text']
                _l_(526295)
            except:
                _l_(526309)

                message= None
                _l_(526296)
                fromm= _n_(526297, "item", lambda: item)['message']['from']['id']
                _l_(526298)
                reply= _c_(526301, _n_(526299, "make_reply", lambda: make_reply), _n_(526300, "message", lambda: message))
                _l_(526302)
                _c_(526307, _a_(526304, _n_(526303, "T_bot", lambda: T_bot), "send"), _n_(526305, "reply", lambda: reply), _n_(526306, "fromm", lambda: fromm))
                _l_(526308)