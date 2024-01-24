# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48040985/hexdigest-throws-typeerror-required-argument-length-pos-1-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(532250)

except ImportError:
    pass


arguments = [[_c_(532255, _a_(532252, _n_(532251, "hashlib", lambda: hashlib), "md5"), _c_(532254, _a_(532253, 'hello', "encode")))]]
_l_(532256)
f = _c_(532258, _n_(532257, "open", lambda: open), 'Dictionary.txt', 'r')
_l_(532259)
words = _c_(532262, _a_(532261, _n_(532260, "f", lambda: f), "readlines"))
_l_(532263)
_c_(532266, _a_(532265, _n_(532264, "f", lambda: f), "close"))
_l_(532267)
# Remember to strip the \n's
cracked = {}
_l_(532268)
for ciphertext in _n_(532269, "arguments", lambda: arguments)[0]:
    _l_(532300)

    for word in _n_(532270, "words", lambda: words):
        _l_(532299)

        for alg in _a_(532272, _n_(532271, "hashlib", lambda: hashlib), "algorithms_guaranteed"):
            _l_(532298)

            _c_(532277, _n_(532273, "exec", lambda: exec), _c_(532276, _a_(532274, "hashed = hashlib.{}(word.encode())", "format"), _n_(532275, "alg", lambda: alg)))
            _l_(532278)
            if _c_(532281, _a_(532280, _n_(532279, "hashed", lambda: hashed), "hexdigest")) == _n_(532282, "ciphertext", lambda: ciphertext):
                _l_(532297)

                _n_(532283, "cracked", lambda: cracked)[_n_(532284, "ciphertext", lambda: ciphertext)] = [_n_(532285, "word", lambda: word), _n_(532286, "alg", lambda: alg)]
                _l_(532287)
                _c_(532294, _n_(532288, "print", lambda: print), _c_(532293, _a_(532289, "[+] Found {} as {} with {} algorithm!", "format"), _n_(532290, "ciphertext", lambda: ciphertext), _n_(532291, "word", lambda: word), _n_(532292, "alg", lambda: alg)))
                _l_(532295)
                break
                _l_(532296)
_c_(532303, _n_(532301, "print", lambda: print), _n_(532302, "cracked", lambda: cracked))
_l_(532304)