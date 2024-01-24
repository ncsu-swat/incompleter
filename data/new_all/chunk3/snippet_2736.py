# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64816017/typeerror-function-object-is-not-subscriptable-while-the-error-line-is-worki
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def DESCRYSubAESHex(SubHex1, FullKey):
    _l_(558539)


    #print(SubHex1)
    #print(FullKey)
    for a in _c_(558471, _n_(558470, "range", lambda: range), 16):
        _l_(558484)

        #print(SubHex1[a])
        #print(FullKey[0][a])
        _n_(558472, "SubHex1", lambda: SubHex1)[_n_(558473, "a", lambda: a)] = _c_(558482, _n_(558474, "xor_strings", lambda: xor_strings), _n_(558475, "SubHex1", lambda: SubHex1)[_n_(558476, "a", lambda: a)],_n_(558477, "FullKey", lambda: FullKey)[_c_(558480, _n_(558478, "len", lambda: len), _n_(558479, "FullKey", lambda: FullKey)) - 1][_n_(558481, "a", lambda: a)])         
        _l_(558483)         

    for a in _c_(558489, _n_(558485, "range", lambda: range), _c_(558488, _n_(558486, "len", lambda: len), _n_(558487, "FullKey", lambda: FullKey)) - 2):
        _l_(558516)

        #print(SubHex1)
        SubHex1 = _c_(558492, _n_(558490, "ReVerseShiftRowMK2", lambda: ReVerseShiftRowMK2), _n_(558491, "SubHex1", lambda: SubHex1))
        _l_(558493)
       

        SubHex1 = _c_(558496, _n_(558494, "reVeredSBox", lambda: reVeredSBox), _n_(558495, "SubHex1", lambda: SubHex1))
        _l_(558497)

      

        for b in _c_(558499, _n_(558498, "range", lambda: range), 16):
            _l_(558513)

            _n_(558500, "SubHex1", lambda: SubHex1)[_n_(558501, "b", lambda: b)] = _c_(558511, _n_(558502, "xor_strings", lambda: xor_strings), _n_(558503, "SubHex1", lambda: SubHex1)[_n_(558504, "b", lambda: b)],_n_(558505, "FullKey", lambda: FullKey)[(_c_(558508, _n_(558506, "len", lambda: len), _n_(558507, "FullKey", lambda: FullKey)) - 2) - _n_(558509, "a", lambda: a)][_n_(558510, "b", lambda: b)])       
            _l_(558512)       
        
        SubHex1 = _n_(558514, "reVersedMixCol", lambda: reVersedMixCol)
        _l_(558515)

    SubHex1 = _c_(558519, _n_(558517, "ReVerseShiftRowMK2", lambda: ReVerseShiftRowMK2), _n_(558518, "SubHex1", lambda: SubHex1))
    _l_(558520)

    SubHex1 = _c_(558523, _n_(558521, "reVeredSBox", lambda: reVeredSBox), _n_(558522, "SubHex1", lambda: SubHex1))
    _l_(558524)

    for b in _c_(558526, _n_(558525, "range", lambda: range), 16):
        _l_(558536)

        _n_(558527, "SubHex1", lambda: SubHex1)[_n_(558528, "b", lambda: b)] = _c_(558534, _n_(558529, "xor_strings", lambda: xor_strings), _n_(558530, "SubHex1", lambda: SubHex1)[_n_(558531, "b", lambda: b)],_n_(558532, "FullKey", lambda: FullKey)[0][_n_(558533, "b", lambda: b)]) 
        _l_(558535) 
    aux = _n_(558537, "SubHex1", lambda: SubHex1)
    _l_(558538)

    

    return aux

_c_(558545, _n_(558540, "print", lambda: print), _c_(558544, _n_(558541, "DESCRYSubAESHex", lambda: DESCRYSubAESHex), _n_(558542, "S", lambda: S), _n_(558543, "A", lambda: A)))
_l_(558546)