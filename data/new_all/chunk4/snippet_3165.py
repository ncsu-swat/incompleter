# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33703951/getting-typeerror-object-of-type-builtin-function-or-method-has-no-len
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def CheckLength(num):
    _l_(599510)

    if _c_(599503, _n_(599501, "len", lambda: len), _n_(599502, "num", lambda: num))>=13 and _c_(599506, _n_(599504, "len", lambda: len), _n_(599505, "num", lambda: num))<=16:
        _l_(599509)

        aux = True
        _l_(599507)
        return aux
    else:
        aux = False
        _l_(599508)
        return aux
def CheckType(num):
    _l_(599524)

    if _n_(599511, "num", lambda: num)[0]=='4':
        _l_(599523)

        aux = 'Visa'
        _l_(599512)
        return aux
    elif _n_(599513, "num", lambda: num)[0]=='5':
        _l_(599522)

        aux = 'MasterCard'
        _l_(599514)
        return aux
    elif _n_(599515, "num", lambda: num)[0]=='6':
        _l_(599521)

        aux = 'Discover'
        _l_(599516)
        return aux
    elif _n_(599517, "num", lambda: num)[0:1]=='37':
        _l_(599520)

        aux = 'American Express'
        _l_(599518)
        return aux
    else:
        aux = 'Invalid Entry'
        _l_(599519)
        return aux
def Step1(num):
    _l_(599550)

    total=0
    _l_(599525)
    length=_c_(599528, _n_(599526, "len", lambda: len), _n_(599527, "num", lambda: num))
    _l_(599529)
    for i in _c_(599532, _n_(599530, "range", lambda: range), _n_(599531, "length", lambda: length)-1,-2,-2):
        _l_(599549)

        double=_c_(599536, _n_(599533, "int", lambda: int), _n_(599534, "num", lambda: num)[_n_(599535, "i", lambda: i)]*2)
        _l_(599537)
        if _n_(599538, "double", lambda: double)>9:
            _l_(599546)

            double=_n_(599539, "double", lambda: double)[0]+_n_(599540, "double", lambda: double)[1]
            _l_(599541)
            total+=_n_(599542, "double", lambda: double)
            _l_(599543)
        else:
            total+=_n_(599544, "double", lambda: double)
            _l_(599545)
        aux = _n_(599547, "total", lambda: total)        
        _l_(599548)        
        return aux        
def Step2(num):
    _l_(599564)

    total=0
    _l_(599551)
    length=_c_(599554, _n_(599552, "len", lambda: len), _n_(599553, "num", lambda: num))
    _l_(599555)
    for i in _c_(599558, _n_(599556, "range", lambda: range), _n_(599557, "length", lambda: length)-1,-1,-2):
        _l_(599561)

        total+=_n_(599559, "i", lambda: i)
        _l_(599560)
    aux = _n_(599562, "total", lambda: total)
    _l_(599563)
    return aux
def Step3(num):
    _l_(599576)

    total=_c_(599567, _n_(599565, "Step1", lambda: Step1), _n_(599566, "num", lambda: num))+_c_(599570, _n_(599568, "Step2", lambda: Step2), _n_(599569, "num", lambda: num))
    _l_(599571)
    if _n_(599572, "total", lambda: total)%10==0:
        _l_(599575)

        aux = True
        _l_(599573)
        return aux
    else:
        aux = False
        _l_(599574)
        return aux
def main():
    _l_(599616)

    inFile=_c_(599578, _n_(599577, "open", lambda: open), 'pa7.cards','r')
    _l_(599579)
    cardNum=_c_(599584, _a_(599583, _c_(599582, _a_(599581, _n_(599580, "inFile", lambda: inFile), "readline")), "strip"))
    _l_(599585)
    while _n_(599586, "cardNum", lambda: cardNum)!='99999':
        _l_(599611)

        validLength=_c_(599589, _n_(599587, "CheckLength", lambda: CheckLength), _n_(599588, "cardNum", lambda: cardNum))
        _l_(599590)
        validType=_c_(599593, _n_(599591, "CheckType", lambda: CheckType), _n_(599592, "cardNum", lambda: cardNum))
        _l_(599594)
        if _n_(599595, "validLength", lambda: validLength)==True and _n_(599596, "validType", lambda: validType)==True:
            _l_(599605)

            _c_(599599, _n_(599597, "print", lambda: print), _n_(599598, "cardNum", lambda: cardNum),"valid")
            _l_(599600)
        else:
            _c_(599603, _n_(599601, "print", lambda: print), _n_(599602, "cardNum", lambda: cardNum),"invalid")
            _l_(599604)
        cardNum=_a_(599609, _c_(599608, _a_(599607, _n_(599606, "inFile", lambda: inFile), "readline")), "strip")
        _l_(599610)
    _c_(599614, _a_(599613, _n_(599612, "inFile", lambda: inFile), "close"))
    _l_(599615)
_c_(599618, _n_(599617, "main", lambda: main))    
_l_(599619)    