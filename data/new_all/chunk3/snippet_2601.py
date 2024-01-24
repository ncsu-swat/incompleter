# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69877663/how-to-fix-typeerror-vowels-missing-required-positional-argument-filehandl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def vowels(filehandle):
    _l_(536458)

    num_vowel = 0
    _l_(536447)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    _l_(536448)
    for c in _n_(536449, "filehandle", lambda: filehandle):
        _l_(536455)

        if _n_(536450, "c", lambda: c) in _n_(536451, "vowels", lambda: vowels):
            _l_(536454)

            num_vowel = _n_(536452, "num_vowel", lambda: num_vowel)+1
            _l_(536453)
    aux = _n_(536456, "num_vowel", lambda: num_vowel)
    _l_(536457)
    return aux

def consonants(filehandle):
    _l_(536480)

    num_con = 0
    _l_(536459)
    for c in _n_(536460, "filehandle", lambda: filehandle):
        _l_(536477)

        if _n_(536461, "c", lambda: c) >= 'a' and _n_(536462, "c", lambda: c) <= 'z':
            _l_(536476)

            if _n_(536463, "c", lambda: c) not in _n_(536464, "vowels", lambda: vowels):
                _l_(536467)

                num_con = _n_(536465, "num_con", lambda: num_con)+1
                _l_(536466)
        elif _n_(536468, "c", lambda: c)>='A' and _n_(536469, "c", lambda: c)<='Z':
            _l_(536475)

            if _n_(536470, "c", lambda: c) not in _n_(536471, "vowels", lambda: vowels):
                _l_(536474)

                num_con = _n_(536472, "num_con", lambda: num_con)+1
                _l_(536473)
    aux = _n_(536478, "num_con", lambda: num_con)
    _l_(536479)
    return aux

def case(filehandle):
    _l_(536498)

    uppercase = 0
    _l_(536481)
    lowercase = 0
    _l_(536482)
    for c in _n_(536483, "filehandle", lambda: filehandle):
        _l_(536494)

        if _n_(536484, "c", lambda: c)>='a' and _n_(536485, "c", lambda: c)<='z':
            _l_(536493)

            uppercase=_n_(536486, "uppercase", lambda: uppercase)+1
            _l_(536487)
        elif _n_(536488, "c", lambda: c)>='A' and _n_(536489, "c", lambda: c)<= 'Z':
            _l_(536492)

            lowercase=_n_(536490, "lowecase", lambda: lowecase)+1
            _l_(536491)
    aux = _n_(536495, "uppercase", lambda: uppercase), _n_(536496, "lowercase", lambda: lowercase)
    _l_(536497)
    return aux

def main():
    _l_(536540)

    vowel = _c_(536500, _n_(536499, "vowels", lambda: vowels))
    _l_(536501)
    consonants = _c_(536503, _n_(536502, "consonants", lambda: consonants))
    _l_(536504)
    uppercase, lowercase = _c_(536506, _n_(536505, "case", lambda: case))
    _l_(536507)
    try:
        _l_(536539)

        filename=_c_(536509, _n_(536508, "input", lambda: input), 'Enter name of text file: ')
        _l_(536510)
        filehandle=_c_(536512, _n_(536511, "open", lambda: open), 'words.txt', 'r')
        _l_(536513)

        _c_(536516, _n_(536514, "print", lambda: print), 'Vowels:', _n_(536515, "vowels", lambda: vowels))
        _l_(536517)
        _c_(536520, _n_(536518, "print", lambda: print), 'Consonants:', _n_(536519, "consonants", lambda: consonants))
        _l_(536521)
        _c_(536524, _n_(536522, "print", lambda: print), 'Uppercase:', _n_(536523, "uppercase", lambda: uppercase))
        _l_(536525)
        _c_(536528, _n_(536526, "print", lambda: print), 'Lowercase:', _n_(536527, "lowercase", lambda: lowercase))
        _l_(536529)

        _c_(536532, _a_(536531, _n_(536530, "filehandle", lambda: filehandle), "close"))
        _l_(536533)
    except _n_(536534, "IOError", lambda: IOError):
        _l_(536538)

        _c_(536536, _n_(536535, "print", lambda: print), 'FILE NOT FOUND')
        _l_(536537)


_c_(536542, _n_(536541, "main", lambda: main))
_l_(536543)