# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71897761/python-getopt-module-error-nameerror-name-opts-is-not-defined-after-importi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import getopt
    _l_(595708)

except ImportError:
    pass
try:
    import sys
    _l_(595710)

except ImportError:
    pass
    
   
question_id= None
_l_(595711)
arg_student = None
_l_(595712)
argv = _a_(595714, _n_(595713, "sys", lambda: sys), "argv")[1:]
_l_(595715)
_c_(595717, _n_(595716, "print", lambda: print), "test")
_l_(595718)

try:
    _l_(595728)

    opts, args = _c_(595722, _a_(595720, _n_(595719, "getopt", lambda: getopt), "getopt"), _n_(595721, "argv", lambda: argv), "i:s:", ["question_id=","arg_student="])
    _l_(595723)
except:
    _l_(595727)

    _c_(595725, _n_(595724, "print", lambda: print), "Error")
    _l_(595726)

for opt, arg in _n_(595729, "opts", lambda: opts):
    _l_(595738)

    if _n_(595730, "opt", lambda: opt) in ['-i', '--question_id']:
        _l_(595737)

        question_id = _n_(595731, "arg", lambda: arg)
        _l_(595732)
    elif _n_(595733, "opt", lambda: opt) in ['-s', '--arg_student']:
        _l_(595736)

        arg_student = _n_(595734, "arg", lambda: arg)
        _l_(595735)

_c_(595741, _n_(595739, "print", lambda: print), "Question Number: " + _n_(595740, "question_id", lambda: question_id))        
_l_(595742)        
_c_(595745, _n_(595743, "print", lambda: print), "Student response: " + _n_(595744, "arg_student", lambda: arg_student))
_l_(595746)