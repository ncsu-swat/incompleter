# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60990112/typeerror-fit-takes-1-positional-argument-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myclass = _c_(348235, _n_(348232, "MyClass", lambda: MyClass), _n_(348233, "path1", lambda: path1), _n_(348234, "path2", lambda: path2))
_l_(348236)
skl_pipeline = _c_(348239, _n_(348237, "Pipeline", lambda: Pipeline), steps=[('myclass', _n_(348238, "myclass", lambda: myclass))])
_l_(348240)
_c_(348243, _a_(348242, _n_(348241, "skl_pipeline", lambda: skl_pipeline), "fit"), None)
_l_(348244)