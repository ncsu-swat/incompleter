# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66886458/attributeerror-importdenier-object-has-no-attribute-find-spec-when-loading
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from my_module.test_fun1 import test_fun1
    _l_(386760)

except ImportError:
    pass
try:
    from my_module._sub_module.test_fun import test_fun
    _l_(386762)

except ImportError:
    pass