# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43328437/typeerror-object-of-type-categorymodel-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Category(_a_(438244, _n_(438243, "models", lambda: models), "Model")):
    _l_(438252)

    name = _c_(438246, _a_(438245, models, "CharField"), max_length=200)
    _l_(438247)

    def __str__(self):
        _l_(438251)

        aux = _a_(438249, _n_(438248, "self", lambda: self), "name")
        _l_(438250)
        return aux