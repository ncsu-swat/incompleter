# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60888178/whats-wrong-with-my-python-about-typeerror-not-supported-between-instance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ipywidgets import interact_manual
    _l_(563171)

except ImportError:
    pass
def BMI(height, weight):
    _l_(563189)

    height = (_c_(563174, _n_(563172, "float", lambda: float), _n_(563173, "height", lambda: height)) / 100)**2
    _l_(563175)
    weight = _c_(563178, _n_(563176, "float", lambda: float), _n_(563177, "weight", lambda: weight))
    _l_(563179)
    BMI = _n_(563180, "weight", lambda: weight)/_n_(563181, "height", lambda: height)
    _l_(563182)
    _c_(563187, _n_(563183, "print", lambda: print), _c_(563186, _a_(563184, 'Your BMI is {:.2f}', "format"), _n_(563185, "BMI", lambda: BMI)))
    _l_(563188)

_c_(563192, _n_(563190, "interact_manual", lambda: interact_manual), _n_(563191, "BMI", lambda: BMI), height='Please enter your height', weight='Please enter your weight')
_l_(563193)

if _n_(563194, "BMI", lambda: BMI)<18.5:
    _l_(563206)

    _c_(563196, _n_(563195, "print", lambda: print), 'Eat more!')
    _l_(563197)
elif _n_(563198, "BMI", lambda: BMI) != 24:
    _l_(563205)

    _c_(563200, _n_(563199, "print", lambda: print), 'Take care of your health, eat less')
    _l_(563201)
else:
    _c_(563203, _n_(563202, "print", lambda: print), 'Nice:)')
    _l_(563204)