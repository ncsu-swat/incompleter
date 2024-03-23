# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import difflib
    _l_(31423)

except ImportError:
    pass

def string_similarity(str1, str2):
    _l_(31438)

    result = _c_(31432, _a_(31425, _n_(31424, "difflib", lambda: difflib), "SequenceMatcher"), a=_c_(31428, _a_(31427, _n_(31426, "str1", lambda: str1), "lower")), b=_c_(31431, _a_(31430, _n_(31429, "str2", lambda: str2), "lower")))
    _l_(31433)
    aux = _c_(31436, _a_(31435, _n_(31434, "result", lambda: result), "ratio"))
    _l_(31437)
    return aux
str1 = 'Python Exercises'
_l_(31439)
_c_(31441, _n_(31440, "print", lambda: print), 'Original string:')
_l_(31442)
_c_(31445, _n_(31443, "print", lambda: print), _n_(31444, "str1", lambda: str1))
_l_(31446)
_c_(31449, _n_(31447, "print", lambda: print), _n_(31448, "str2", lambda: str2))
_l_(31450)
_c_(31452, _n_(31451, "print", lambda: print), 'Similarity between two said strings:')
_l_(31453)
_c_(31459, _n_(31454, "print", lambda: print), _c_(31458, _n_(31455, "string_similarity", lambda: string_similarity), _n_(31456, "str1", lambda: str1), _n_(31457, "str2", lambda: str2)))
_l_(31460)
str1 = 'Python Exercises'
_l_(31461)
str2 = 'Python Exercise'
_l_(31462)
_c_(31464, _n_(31463, "print", lambda: print), '\nOriginal string:')
_l_(31465)
_c_(31468, _n_(31466, "print", lambda: print), _n_(31467, "str1", lambda: str1))
_l_(31469)
_c_(31472, _n_(31470, "print", lambda: print), _n_(31471, "str2", lambda: str2))
_l_(31473)
_c_(31475, _n_(31474, "print", lambda: print), 'Similarity between two said strings:')
_l_(31476)
_c_(31482, _n_(31477, "print", lambda: print), _c_(31481, _n_(31478, "string_similarity", lambda: string_similarity), _n_(31479, "str1", lambda: str1), _n_(31480, "str2", lambda: str2)))
_l_(31483)
str1 = 'Python Exercises'
_l_(31484)
str2 = 'Python Ex.'
_l_(31485)
_c_(31487, _n_(31486, "print", lambda: print), '\nOriginal string:')
_l_(31488)
_c_(31491, _n_(31489, "print", lambda: print), _n_(31490, "str1", lambda: str1))
_l_(31492)
_c_(31495, _n_(31493, "print", lambda: print), _n_(31494, "str2", lambda: str2))
_l_(31496)
_c_(31498, _n_(31497, "print", lambda: print), 'Similarity between two said strings:')
_l_(31499)
_c_(31505, _n_(31500, "print", lambda: print), _c_(31504, _n_(31501, "string_similarity", lambda: string_similarity), _n_(31502, "str1", lambda: str1), _n_(31503, "str2", lambda: str2)))
_l_(31506)
str1 = 'Python Exercises'
_l_(31507)
str2 = 'Python'
_l_(31508)
_c_(31510, _n_(31509, "print", lambda: print), '\nOriginal string:')
_l_(31511)
_c_(31514, _n_(31512, "print", lambda: print), _n_(31513, "str1", lambda: str1))
_l_(31515)
_c_(31518, _n_(31516, "print", lambda: print), _n_(31517, "str2", lambda: str2))
_l_(31519)
_c_(31521, _n_(31520, "print", lambda: print), 'Similarity between two said strings:')
_l_(31522)
_c_(31528, _n_(31523, "print", lambda: print), _c_(31527, _n_(31524, "string_similarity", lambda: string_similarity), _n_(31525, "str1", lambda: str1), _n_(31526, "str2", lambda: str2)))
_l_(31529)
str1 = 'Python Exercises'
_l_(31530)
str1 = 'Java Exercises'
_l_(31531)
_c_(31533, _n_(31532, "print", lambda: print), '\nOriginal string:')
_l_(31534)
_c_(31537, _n_(31535, "print", lambda: print), _n_(31536, "str1", lambda: str1))
_l_(31538)
_c_(31541, _n_(31539, "print", lambda: print), _n_(31540, "str2", lambda: str2))
_l_(31542)
_c_(31544, _n_(31543, "print", lambda: print), 'Similarity between two said strings:')
_l_(31545)
_c_(31551, _n_(31546, "print", lambda: print), _c_(31550, _n_(31547, "string_similarity", lambda: string_similarity), _n_(31548, "str1", lambda: str1), _n_(31549, "str2", lambda: str2)))
_l_(31552)