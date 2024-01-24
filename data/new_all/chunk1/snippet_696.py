# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54840271/why-do-i-get-nameerror-name-is-not-defined-with-exec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(399425, _n_(399424, "exec", lambda: exec), "import random")
_l_(399426)
_c_(399428, _n_(399427, "exec", lambda: exec), "def f():\n\treturn random.randint(0, 10), random.randint(0, 10)")
_l_(399429)
_c_(399432, _c_(399431, _n_(399430, "locals", lambda: locals))['f'])
_l_(399433)