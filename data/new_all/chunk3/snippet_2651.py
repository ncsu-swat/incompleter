# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67946350/attributeerror-when-trying-to-created-nested-serializer-in-django-rest-framework
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SetsIndividualData(_n_(547679, "ListAPIView", lambda: ListAPIView)):
    _l_(547697)

    serializer_class = SetSerializers
    _l_(547680)

    def get_queryset(self):
        _l_(547696)

        setCode = _c_(547684, _a_(547683, _a_(547682, _n_(547681, "self", lambda: self), "kwargs"), "get"), 'setCode')
        _l_(547685)
        queryList = _c_(547692, _a_(547688, _a_(547687, _n_(547686, "Set", lambda: Set), "objects"), "filter"), code=_c_(547691, _a_(547690, _n_(547689, "setCode", lambda: setCode), "upper")))
        _l_(547693)
        aux = _n_(547694, "queryList", lambda: queryList)
        _l_(547695)
        return aux