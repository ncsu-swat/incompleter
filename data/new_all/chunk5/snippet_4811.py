# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47418938/typeerror-unsupported-operand-types-for-int-and-tuple
#!/usr/bin/python
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(692900)

except ImportError:
    pass
try:
    import random as r
    _l_(692902)

except ImportError:
    pass
try:
    from math import *
    _l_(692904)

except ImportError:
    pass



def ouvrir(nomimage):
    _l_(692912)

    img=_c_(692908, _a_(692906, _n_(692905, "Image", lambda: Image), "open"), _n_(692907, "nomimage", lambda: nomimage))  
    _l_(692909)  
    aux = _n_(692910, "img", lambda: img)
    _l_(692911)
    return aux

def affiche(img):
    _l_(692917)

    _c_(692915, _a_(692914, _n_(692913, "img", lambda: img), "show"))
    _l_(692916)


def imc2img(imc,n):
    _l_(692956)

    img=_c_(692922, _a_(692919, _n_(692918, "Image", lambda: Image), "new"), "F",_a_(692921, _n_(692920, "imc", lambda: imc), "size")) 
    _l_(692923) 
    pixc=_c_(692926, _a_(692925, _n_(692924, "imc", lambda: imc), "load")) 
    _l_(692927) 
    pixg=_c_(692930, _a_(692929, _n_(692928, "img", lambda: img), "load"))
    _l_(692931)
    width = _a_(692933, _n_(692932, "imc", lambda: imc), "size")[0] 
    _l_(692934) 
    height=_a_(692936, _n_(692935, "imc", lambda: imc), "size")[1]
    _l_(692937)
    for j in _c_(692940, _n_(692938, "range", lambda: range), _n_(692939, "height", lambda: height)):
        _l_(692953)

        for i in _c_(692943, _n_(692941, "range", lambda: range), _n_(692942, "width", lambda: width)):
            _l_(692952)

            _n_(692944, "pixg", lambda: pixg)[_n_(692945, "i", lambda: i),_n_(692946, "j", lambda: j)]=_n_(692947, "pixc", lambda: pixc)[_n_(692948, "i", lambda: i),_n_(692949, "j", lambda: j)][_n_(692950, "n", lambda: n)]
            _l_(692951)
    aux = _n_(692954, "img", lambda: img)
    _l_(692955)
    return aux

def imc2r(ims):
    _l_(692963)

    imr=_c_(692959, _n_(692957, "imc2img", lambda: imc2img), _n_(692958, "ims", lambda: ims),1)
    _l_(692960)
    aux = _n_(692961, "imr", lambda: imr)
    _l_(692962)
    return aux

def inverse_image(ims):
    _l_(693001)

    img=_c_(692968, _a_(692965, _n_(692964, "Image", lambda: Image), "new"), "L",_a_(692967, _n_(692966, "ims", lambda: ims), "size"))
    _l_(692969)
    pixc=_c_(692972, _a_(692971, _n_(692970, "ims", lambda: ims), "load"))
    _l_(692973)
    pixg=_c_(692976, _a_(692975, _n_(692974, "img", lambda: img), "load"))
    _l_(692977)
    width=_a_(692979, _n_(692978, "ims", lambda: ims), "size")[0]
    _l_(692980)
    height=_a_(692982, _n_(692981, "ims", lambda: ims), "size")[1]
    _l_(692983)
    for j in _c_(692986, _n_(692984, "range", lambda: range), _n_(692985, "height", lambda: height)):
        _l_(692998)

        for i in _c_(692989, _n_(692987, "range", lambda: range), _n_(692988, "width", lambda: width)):
            _l_(692997)

            imi=_n_(692990, "pixg", lambda: pixg)[_n_(692991, "i", lambda: i),_n_(692992, "j", lambda: j)]=_n_(692993, "pixc", lambda: pixc)[(255-_n_(692994, "i", lambda: i)),(255-_n_(692995, "j", lambda: j))]
            _l_(692996)
    aux = _n_(692999, "imi", lambda: imi)
    _l_(693000)
    return aux