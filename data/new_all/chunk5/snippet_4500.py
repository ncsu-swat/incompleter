# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56553165/how-to-fix-typeerror-catg-id-is-an-invalid-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Choice(_a_(689030, _n_(689029, "models", lambda: models), "Model")):
    _l_(689042)

    chname = _c_(689033, _a_(689031, models, "ForeignKey"), Product, on_delete=_a_(689032, models, "CASCADE"))
    _l_(689034)
    chn = _c_(689036, _a_(689035, models, "CharField"), max_length=1000, default=" ")
    _l_(689037)


    def __str__(self):
        _l_(689041)

        aux = _a_(689039, _n_(689038, "self", lambda: self), "chn")
        _l_(689040)
        return aux