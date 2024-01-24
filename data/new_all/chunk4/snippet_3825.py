# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67015173/django-rest-api-attributeerror-the-serializer-field-might-be-named-incorrectly
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework.views import APIView
    _l_(628499)

except ImportError:
    pass
try:
    from rest_framework.response import Response
    _l_(628501)

except ImportError:
    pass
try:
    from analysis.business import get_constituents
    _l_(628503)

except ImportError:
    pass
try:
    from .serializers import ConstituentNameLists
    _l_(628505)

except ImportError:
    pass

class ConstituentList(_n_(628506, "APIView", lambda: APIView)):
    _l_(628531)

    '''
    Returns the List of Constituents
    '''
    _l_(628507)
    def get(self, request, indexname='ALLSTOCKS'):
        _l_(628530)

        '''
        Returns the Constituent List
        '''
        _l_(628508)
        # Capturing Inputs in Appropriate Cases
        indexname = _c_(628511, _a_(628510, _n_(628509, "indexname", lambda: indexname), "upper"))
        _l_(628512)
        constituents = _c_(628515, _n_(628513, "get_constituents", lambda: get_constituents), indexname=_n_(628514, "indexname", lambda: indexname))
        _l_(628516)
        _c_(628519, _n_(628517, "print", lambda: print), _n_(628518, "constituents", lambda: constituents))
        _l_(628520)
        serializer = _c_(628523, _n_(628521, "ConstituentNameLists", lambda: ConstituentNameLists), _n_(628522, "constituents", lambda: constituents))
        _l_(628524)
        aux = _c_(628528, _n_(628525, "Response", lambda: Response), _a_(628527, _n_(628526, "serializer", lambda: serializer), "data"))
        _l_(628529)
        return aux