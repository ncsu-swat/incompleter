# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_dict_in_list(dicts, default=None, **kwargs):
    _l_(1540202)

    """Find first matching :obj:`dict` in :obj:`list`.

    :param list dicts: List of dictionaries.
    :param dict default: Optional. Default dictionary to return.
        Defaults to `None`.
    :param **kwargs: `key=value` pairs to match in :obj:`dict`.

    :returns: First matching :obj:`dict` from `dicts`.
    :rtype: dict

    """

    rval = _n_(1540177, "default", lambda: default)
    _l_(1540178)
    for d in _n_(1540179, "dicts", lambda: dicts):
        _l_(1540199)

        is_found = False
        _l_(1540180)

        # Search for keys in dict.
        for k, v in _c_(1540183, _a_(1540182, _n_(1540181, "kwargs", lambda: kwargs), "items")):
            _l_(1540193)

            if _c_(1540187, _a_(1540185, _n_(1540184, "d", lambda: d), "get"), _n_(1540186, "k", lambda: k), None) == _n_(1540188, "v", lambda: v):
                _l_(1540192)

                is_found = True
                _l_(1540189)

            else:
                is_found = False
                _l_(1540190)
                break
                _l_(1540191)

        if _n_(1540194, "is_found", lambda: is_found):
            _l_(1540198)

            rval = _n_(1540195, "d", lambda: d)
            _l_(1540196)
            break
            _l_(1540197)
    aux = _n_(1540200, "rval", lambda: rval)
    _l_(1540201)

    return aux


if _n_(1540203, "__name__", lambda: __name__) == '__main__':
    _l_(1540286)

    # Tests
    dicts = []
    _l_(1540204)
    keys = _c_(1540206, _a_(1540205, 'spam eggs shrubbery knight', "split"))
    _l_(1540207)

    start = 0
    _l_(1540208)
    for _ in _c_(1540210, _n_(1540209, "range", lambda: range), 4):
        _l_(1540227)

        dct = {_n_(1540211, "k", lambda: k): _n_(1540212, "v", lambda: v) for k, v in _c_(1540219, _n_(1540213, "zip", lambda: zip), _n_(1540214, "keys", lambda: keys), _c_(1540218, _n_(1540215, "range", lambda: range), _n_(1540216, "start", lambda: start), _n_(1540217, "start", lambda: start)+4))}
        _l_(1540220)
        _c_(1540224, _a_(1540222, _n_(1540221, "dicts", lambda: dicts), "append"), _n_(1540223, "dct", lambda: dct))
        _l_(1540225)
        start += 4
        _l_(1540226)

    # Find each dict based on 'spam' key only.  
    for x in _c_(1540232, _n_(1540228, "range", lambda: range), _c_(1540231, _n_(1540229, "len", lambda: len), _n_(1540230, "dicts", lambda: dicts))):
        _l_(1540242)

        spam = _n_(1540233, "x", lambda: x)*4
        _l_(1540234)
        assert _c_(1540238, _n_(1540235, "find_dict_in_list", lambda: find_dict_in_list), _n_(1540236, "dicts", lambda: dicts), spam=_n_(1540237, "spam", lambda: spam)) == _n_(1540239, "dicts", lambda: dicts)[_n_(1540240, "x", lambda: x)]
        _l_(1540241)

    # Find each dict based on 'spam' and 'shrubbery' keys.
    for x in _c_(1540247, _n_(1540243, "range", lambda: range), _c_(1540246, _n_(1540244, "len", lambda: len), _n_(1540245, "dicts", lambda: dicts))):
        _l_(1540258)

        spam = _n_(1540248, "x", lambda: x)*4
        _l_(1540249)
        assert _c_(1540254, _n_(1540250, "find_dict_in_list", lambda: find_dict_in_list), _n_(1540251, "dicts", lambda: dicts), spam=_n_(1540252, "spam", lambda: spam), shrubbery=_n_(1540253, "spam", lambda: spam)+2) == _n_(1540255, "dicts", lambda: dicts)[_n_(1540256, "x", lambda: x)]
        _l_(1540257)

    # Search for one correct key, one incorrect key:
    for x in _c_(1540263, _n_(1540259, "range", lambda: range), _c_(1540262, _n_(1540260, "len", lambda: len), _n_(1540261, "dicts", lambda: dicts))):
        _l_(1540272)

        spam = _n_(1540264, "x", lambda: x)*4
        _l_(1540265)
        assert _c_(1540270, _n_(1540266, "find_dict_in_list", lambda: find_dict_in_list), _n_(1540267, "dicts", lambda: dicts), spam=_n_(1540268, "spam", lambda: spam), shrubbery=_n_(1540269, "spam", lambda: spam)+1) is None
        _l_(1540271)

    # Search for non-existent dict.
    for x in _c_(1540277, _n_(1540273, "range", lambda: range), _c_(1540276, _n_(1540274, "len", lambda: len), _n_(1540275, "dicts", lambda: dicts))):
        _l_(1540285)

        spam = _n_(1540278, "x", lambda: x)+100
        _l_(1540279)
        assert _c_(1540283, _n_(1540280, "find_dict_in_list", lambda: find_dict_in_list), _n_(1540281, "dicts", lambda: dicts), spam=_n_(1540282, "spam", lambda: spam)) is None
        _l_(1540284)

