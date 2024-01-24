# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57871615/boto3-get-tenancy-value-from-placement-gives-name-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(575327, _a_(575326, _a_(575325, _n_(575324, "client", lambda: client), "instances"), "all")):
    _l_(575335)

    for n in _a_(575329, _n_(575328, "i", lambda: i), "placement"):
        _l_(575334)

        if 'tenancy' in _n_(575330, "n", lambda: n)['Key']:
            _l_(575333)

            tenancy = _n_(575331, "n", lambda: n)['Value']
            _l_(575332)