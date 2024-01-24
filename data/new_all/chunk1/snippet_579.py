# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40576845/typeerror-translate-takes-exactly-one-argument-2-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sms_encoding(data):
    _l_(416929)

    #start writing your code here
    _c_(416872, _n_(416870, "print", lambda: print), _n_(416871, "data", lambda: data))
    _l_(416873)
    _c_(416876, _a_(416875, _n_(416874, "data", lambda: data), "split"), " ")
    _l_(416877)
    data_list=_c_(416880, _a_(416879, _n_(416878, "data", lambda: data), "split"), " ")
    _l_(416881)
    sms_encd=[]
    _l_(416882)
    final_sms=""
    _l_(416883)
    for i in _c_(416888, _n_(416884, "range", lambda: range), _c_(416887, _n_(416885, "len", lambda: len), _n_(416886, "data_list", lambda: data_list))):
        _l_(416915)

        if _c_(416892, _a_(416891, _n_(416889, "data_list", lambda: data_list)[_n_(416890, "i", lambda: i)], "lower")) in  ['a','e','i','o','u']:
            _l_(416914)

            _c_(416897, _a_(416894, _n_(416893, "sms_encd", lambda: sms_encd), "append"), _n_(416895, "data_list", lambda: data_list)[_n_(416896, "i", lambda: i)])
            _l_(416898)
        elif _c_(416902, _n_(416899, "len", lambda: len), _n_(416900, "data_list", lambda: data_list)[_n_(416901, "i", lambda: i)])>1:
            _l_(416913)

            a = _c_(416906, _a_(416905, _n_(416903, "data_list", lambda: data_list)[_n_(416904, "i", lambda: i)], "translate"), None,'aeiouAEIOU')
            _l_(416907)
            _c_(416911, _a_(416909, _n_(416908, "sms_encd", lambda: sms_encd), "append"), _n_(416910, "a", lambda: a))
            _l_(416912)
    for j in _c_(416920, _n_(416916, "range", lambda: range), _c_(416919, _n_(416917, "len", lambda: len), _n_(416918, "sms_encd", lambda: sms_encd))):
        _l_(416926)

        final_sms += _c_(416924, _n_(416921, "str", lambda: str), _n_(416922, "sms_encd", lambda: sms_encd)[_n_(416923, "j", lambda: j)])+" "
        _l_(416925)
    aux = _n_(416927, "final_sms", lambda: final_sms)[:-1]
    _l_(416928)
    return aux
data="I will not repeat mistakes"
_l_(416930)
_c_(416935, _n_(416931, "print", lambda: print), _c_(416934, _n_(416932, "sms_encoding", lambda: sms_encoding), _n_(416933, "data", lambda: data))) 
_l_(416936) 