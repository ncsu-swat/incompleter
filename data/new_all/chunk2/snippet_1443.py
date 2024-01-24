# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57940093/typeerror-init-missing-1-required-positional-argument-on-delete-djang
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FilerFileField(_a_(430907, _n_(430906, "models", lambda: models), "ForeignKey")):
    _l_(430978)

    default_form_class = AdminFileFormField
    _l_(430908)
    default_model_class = File 
    _l_(430909) 

    def __init__(self, **kwargs):
        _l_(430950)

        # We hard-code the `to` argument for ForeignKey.__init__
        dfl = _c_(430913, _n_(430910, "get_model_label", lambda: get_model_label), _a_(430912, _n_(430911, "self", lambda: self), "default_model_class"))
        _l_(430914)
        if "to" in _c_(430917, _a_(430916, _n_(430915, "kwargs", lambda: kwargs), "keys")):
            _l_(430939)

            old_to = _c_(430922, _n_(430918, "get_model_label", lambda: get_model_label), _c_(430921, _a_(430920, _n_(430919, "kwargs", lambda: kwargs), "pop"), "to"))
            _l_(430923)
            if _n_(430924, "old_to", lambda: old_to) != _n_(430925, "dfl", lambda: dfl):
                _l_(430938)

                msg = "%s can only be a ForeignKey to %s; %s passed" % (
                    _a_(430928, _a_(430927, _n_(430926, "self", lambda: self), "__class__"), "__name__"), _n_(430929, "dfl", lambda: dfl), _n_(430930, "old_to", lambda: old_to)
                )
                _l_(430931)
                _c_(430936, _a_(430933, _n_(430932, "warnings", lambda: warnings), "warn"), _n_(430934, "msg", lambda: msg), _n_(430935, "SyntaxWarning", lambda: SyntaxWarning))
                _l_(430937)
        _n_(430940, "kwargs", lambda: kwargs)['to'] = _n_(430941, "dfl", lambda: dfl)
        _l_(430942)
        _c_(430948, _a_(430946, _n_(430943, "super", lambda: super)(_n_(430944, "FilerFileField", lambda: FilerFileField), _n_(430945, "self", lambda: self)), "__init__"), **_n_(430947, "kwargs", lambda: kwargs))
        _l_(430949)

    def formfield(self, **kwargs):
        _l_(430977)

        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {
            'form_class': _a_(430952, _n_(430951, "self", lambda: self), "default_form_class"),
        }
        _l_(430953)
        try:
            _l_(430964)

            _n_(430954, "defaults", lambda: defaults)['rel'] = _a_(430956, _n_(430955, "self", lambda: self), "remote_field")
            _l_(430957)
        except _n_(430958, "AttributeError", lambda: AttributeError):
            _l_(430963)

            _n_(430959, "defaults", lambda: defaults)['rel'] = _a_(430961, _n_(430960, "self", lambda: self), "rel")
            _l_(430962)
        _c_(430968, _a_(430966, _n_(430965, "defaults", lambda: defaults), "update"), _n_(430967, "kwargs", lambda: kwargs))
        _l_(430969)
        aux = _c_(430975, _a_(430973, _n_(430970, "super", lambda: super)(_n_(430971, "FilerFileField", lambda: FilerFileField), _n_(430972, "self", lambda: self)), "formfield"), **_n_(430974, "defaults", lambda: defaults))
        _l_(430976)
        return aux