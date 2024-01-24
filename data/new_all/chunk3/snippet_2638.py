# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68169670/batching-python-gmail-api-attributeerror-dict-object-has-no-attribute-resu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for searchResultPart in _n_(577942, "searchResultParts", lambda: searchResultParts):
    _l_(577999)

    batch = _c_(577944, _n_(577943, "BatchHttpRequest", lambda: BatchHttpRequest)) 
    _l_(577945) 
    batch2 = _c_(577947, _n_(577946, "BatchHttpRequest", lambda: BatchHttpRequest))
    _l_(577948)
    for msgID in _n_(577949, "searchResultPart", lambda: searchResultPart):
        _l_(577990)

        request1 = _c_(577960, _a_(577959, _c_(577958, _a_(577955, _c_(577954, _a_(577953, _c_(577952, _a_(577951, _n_(577950, "service", lambda: service), "users")), "messages")), "get"), userId=_n_(577956, "userID", lambda: userID), id=_n_(577957, "msgID", lambda: msgID)), "execute"))
        _l_(577961)
        _c_(577964, _a_(577963, _n_(577962, "request1", lambda: request1), "update"), {"resumable" : None}) #TRIED THIS DOES NOT WORK
        _l_(577965) #TRIED THIS DOES NOT WORK
        request2 = _c_(577976, _a_(577975, _c_(577974, _a_(577971, _c_(577970, _a_(577969, _c_(577968, _a_(577967, _n_(577966, "service", lambda: service), "users")), "messages")), "modify"), userId=_n_(577972, "userID", lambda: userID), id=_n_(577973, "msgID", lambda: msgID), body={'removeLabelIds': ['UNREAD']}), "execute"))
        _l_(577977)
        _c_(577982, _a_(577979, _n_(577978, "batch", lambda: batch), "add"), request=_n_(577980, "request1", lambda: request1),request_id=_n_(577981, "msgID", lambda: msgID)) #Fetch the message
        _l_(577983) #Fetch the message
        _c_(577988, _a_(577985, _n_(577984, "batch2", lambda: batch2), "add"), request=_n_(577986, "request2", lambda: request2),request_id=_n_(577987, "msgID", lambda: msgID)) #Mark the fetched messages as read
        _l_(577989) #Mark the fetched messages as read
    _c_(577993, _a_(577992, _n_(577991, "batch", lambda: batch), "execute")) 
    _l_(577994) 
    _c_(577997, _a_(577996, _n_(577995, "batch2", lambda: batch2), "execute"))
    _l_(577998)