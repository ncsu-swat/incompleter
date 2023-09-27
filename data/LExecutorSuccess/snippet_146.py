# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
words=_c_(1548236, _n_(1548235, "input", lambda: input), "Enter the word to test")
_l_(1548237)
# If I have a user enter discontinous threads it becomes a problem
# input = "   he llo, ho w are y ou  "
n=_c_(1548240, _a_(1548239, _n_(1548238, "words", lambda: words), "strip"))
_l_(1548241)
_c_(1548244, _n_(1548242, "print", lambda: print), _n_(1548243, "n", lambda: n))
_l_(1548245)
# output "he llo, ho w are y ou" - only leading & trailing spaces are removed 

def whitespace(words):
    _l_(1548256)

    r=_c_(1548248, _a_(1548247, _n_(1548246, "words", lambda: words), "replace"), ' ','') # removes all whitespace
    _l_(1548249) # removes all whitespace
    n=_c_(1548252, _a_(1548251, _n_(1548250, "r", lambda: r), "replace"), ',','|') # other uses of replace
    _l_(1548253) # other uses of replace
    aux = _n_(1548254, "n", lambda: n)
    _l_(1548255)
    return aux
def run():
    _l_(1548271)

    words=_c_(1548258, _n_(1548257, "input", lambda: input), "Enter the word to test") # take user input
    _l_(1548259) # take user input
    m=_c_(1548262, _n_(1548260, "whitespace", lambda: whitespace), _n_(1548261, "words", lambda: words)) #encase the def in run() to imporve usability on various functions
    _l_(1548263) #encase the def in run() to imporve usability on various functions
    o=_c_(1548266, _a_(1548265, _n_(1548264, "m", lambda: m), "count"), 'f') # for testing
    _l_(1548267) # for testing
    aux = _n_(1548268, "m", lambda: m),_n_(1548269, "o", lambda: o)
    _l_(1548270)
    return aux
_c_(1548275, _n_(1548272, "print", lambda: print), _c_(1548274, _n_(1548273, "run", lambda: run)))
_l_(1548276)
_n_(1548277, "output", lambda: output)- ('hello|howareyou', 0)
_l_(1548278)

