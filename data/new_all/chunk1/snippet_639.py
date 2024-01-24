# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/12946241/typeerrorenqueuqe-takes-1-positional-argument-but-2-were-passed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Queue_demo:
    _l_(380613)

    head=-1
    _l_(380578)
    tail=-1
    _l_(380579)
    a=[]
    _l_(380580)

    def enqueue(data=10):
        _l_(380600)

        if(_n_(380581, "head", lambda: head)==-1 and _n_(380582, "tail", lambda: tail)==-1):
            _l_(380599)

            head=_n_(380583, "head", lambda: head)+1
            _l_(380584)
            tail=_n_(380585, "tail", lambda: tail)+1
            _l_(380586)
            _c_(380590, _a_(380588, _n_(380587, "a", lambda: a), "append"), _n_(380589, "data", lambda: data))
            _l_(380591)
        else:
            tail=_n_(380592, "tail", lambda: tail)+1
            _l_(380593)
            _c_(380597, _a_(380595, _n_(380594, "a", lambda: a), "append"), _n_(380596, "data", lambda: data))
            _l_(380598)

    def dequeue():
        _l_(380612)

        y=_n_(380601, "a", lambda: a)[_n_(380602, "head", lambda: head)]
        _l_(380603)
        if(_n_(380604, "head", lambda: head)==_n_(380605, "tail", lambda: tail)):
            _l_(380609)

            head,tail=-1,-1
            _l_(380606)
        else:
            head=_n_(380607, "head", lambda: head)+1
            _l_(380608)
        aux = _n_(380610, "y", lambda: y)
        _l_(380611)
        return aux

q1=_c_(380615, _n_(380614, "Queue_demo", lambda: Queue_demo))
_l_(380616)
q2=_c_(380618, _n_(380617, "Queue_demo", lambda: Queue_demo))
_l_(380619)
_c_(380622, _a_(380621, _n_(380620, "q1", lambda: q1), "enqueue"), 12)
_l_(380623)

while(_a_(380625, _n_(380624, "q1", lambda: q1), "tail")==-1):
    _l_(380632)

    _c_(380630, _n_(380626, "print", lambda: print), _c_(380629, _a_(380628, _n_(380627, "q1", lambda: q1), "dequeue")))
    _l_(380631)