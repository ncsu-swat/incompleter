# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60315844/typeerror-pagination-object-is-not-iterable-in-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(447062, _a_(447061, _n_(447060, "api", lambda: api), "route"), '/', methods=["GET"])
@_c_(447065, _a_(447064, _n_(447063, "app", lambda: app), "route"), '/page/<int:page>')
class List(_n_(447066, "Resource", lambda: Resource)):
    _l_(447081)

    """USER data(s)"""

    def get(self, page=1):
        _l_(447080)

        """GET Lists"""
        all_data = _c_(447071, _a_(447069, _a_(447068, _n_(447067, "User", lambda: User), "query"), "paginate"), _n_(447070, "page", lambda: page), per_page=2)
        _l_(447072)
        result = _c_(447076, _a_(447074, _n_(447073, "user_serializer", lambda: user_serializer), "dump"), _n_(447075, "all_data", lambda: all_data))
        _l_(447077)
        aux = _n_(447078, "result", lambda: result)
        _l_(447079)
        return aux