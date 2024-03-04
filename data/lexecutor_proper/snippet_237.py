# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FlagAction(_a_(62045, _n_(62044, "argparse", lambda: argparse), "Action")):
    _l_(62119)

    # From http://bugs.python.org/issue8538

    def __init__(self, option_strings, dest, default=None,
                 required=False, help=None, metavar=None,
                 positive_prefixes=['--'], negative_prefixes=['--no-']):
        _l_(62101)

        _n_(62046, "self", lambda: self).positive_strings = _c_(62048, _n_(62047, "set", lambda: set))
        _l_(62049)
        _n_(62050, "self", lambda: self).negative_strings = _c_(62052, _n_(62051, "set", lambda: set))
        _l_(62053)
        for string in _n_(62054, "option_strings", lambda: option_strings):
            _l_(62080)

            assert _c_(62058, _a_(62056, _n_(62055, "re", lambda: re), "match"), r'--[A-z]+', _n_(62057, "string", lambda: string))
            _l_(62059)
            suffix = _n_(62060, "string", lambda: string)[2:]
            _l_(62061)
            for positive_prefix in _n_(62062, "positive_prefixes", lambda: positive_prefixes):
                _l_(62070)

                _c_(62068, _a_(62065, _a_(62064, _n_(62063, "self", lambda: self), "positive_strings"), "add"), _n_(62066, "positive_prefix", lambda: positive_prefix) + _n_(62067, "suffix", lambda: suffix))
                _l_(62069)
            for negative_prefix in _n_(62071, "negative_prefixes", lambda: negative_prefixes):
                _l_(62079)

                _c_(62077, _a_(62074, _a_(62073, _n_(62072, "self", lambda: self), "negative_strings"), "add"), _n_(62075, "negative_prefix", lambda: negative_prefix) + _n_(62076, "suffix", lambda: suffix))
                _l_(62078)
        strings = _c_(62086, _n_(62081, "list", lambda: list), _a_(62083, _n_(62082, "self", lambda: self), "positive_strings") | _a_(62085, _n_(62084, "self", lambda: self), "negative_strings"))
        _l_(62087)
        _c_(62099, _a_(62091, _n_(62088, "super", lambda: super)(_n_(62089, "FlagAction", lambda: FlagAction), _n_(62090, "self", lambda: self)), "__init__"), option_strings=_n_(62092, "strings", lambda: strings), dest=_n_(62093, "dest", lambda: dest),
                                         nargs=0, const=None, default=_n_(62094, "default", lambda: default), type=_n_(62095, "bool", lambda: bool), choices=None,
                                         required=_n_(62096, "required", lambda: required), help=_n_(62097, "help", lambda: help), metavar=_n_(62098, "metavar", lambda: metavar))
        _l_(62100)

    def __call__(self, parser, namespace, values, option_string=None):
        _l_(62118)

        if _n_(62102, "option_string", lambda: option_string) in _a_(62104, _n_(62103, "self", lambda: self), "positive_strings"):
            _l_(62117)

            _c_(62109, _n_(62105, "setattr", lambda: setattr), _n_(62106, "namespace", lambda: namespace), _a_(62108, _n_(62107, "self", lambda: self), "dest"), True)
            _l_(62110)
        else:
            _c_(62115, _n_(62111, "setattr", lambda: setattr), _n_(62112, "namespace", lambda: namespace), _a_(62114, _n_(62113, "self", lambda: self), "dest"), False)
            _l_(62116)

