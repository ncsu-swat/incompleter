# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56246570/typeerror-init-missing-1-required-positional-argument-branches-but-argu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Gerrit:
    _l_(449861)

    connections = {
        'consumer': _c_(449818, MyGerritClient, host='gerrit.consumer.com', username=_c_(449817, _a_(449816, getpass, "getuser"))),
        'b2b': _c_(449821, MyGerritClient, host='gerrit.b2b.com', username=_c_(449820, _a_(449819, getpass, "getuser")))
    }
    _l_(449822)

    def __init__(self, segment, rev_id, branches):
        _l_(449860)

        _c_(449824, _n_(449823, "print", lambda: print), "TRACE: Gerrit::__init__()")
        _l_(449825)
        _n_(449826, "self", lambda: self).branches = _n_(449827, "branches", lambda: branches)
        _l_(449828)
        _n_(449829, "self", lambda: self).review = None  # Type: GerritChange
        _l_(449830)  # Type: GerritChange
        _n_(449831, "self", lambda: self).gerrit_client = _a_(449833, _n_(449832, "self", lambda: self), "connections")[_n_(449834, "segment", lambda: segment)]
        _l_(449835)
        for review_candidate in _c_(449840, _a_(449838, _a_(449837, _n_(449836, "self", lambda: self), "gerrit_client"), "query"), _n_(449839, "rev_id", lambda: rev_id)):
            _l_(449852)

            if _c_(449845, _a_(449842, _n_(449841, "self", lambda: self), "branch_is_valid"), _a_(449844, _n_(449843, "review_candidate", lambda: review_candidate), "branch")) and _a_(449847, _n_(449846, "review_candidate", lambda: review_candidate), "status") != 'ABANDONED':
                _l_(449851)

                _n_(449848, "self", lambda: self).review = _n_(449849, "review_candidate", lambda: review_candidate)
                _l_(449850)
        _n_(449853, "self", lambda: self).approved = False
        _l_(449854)
        _n_(449855, "self", lambda: self).rev_id = _n_(449856, "rev_id", lambda: rev_id)
        _l_(449857)
        _n_(449858, "self", lambda: self).merged = False
        _l_(449859)