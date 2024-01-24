# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66972367/getting-typeerror-method-takes-0-positional-arguments-but-1-was-given-with-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import corpus as corp
    _l_(608434)

except ImportError:
    pass

def main():
    _l_(608447)

    corpus = _c_(608437, _a_(608436, _n_(608435, "corp", lambda: corp), "Corpus"), "review.txt")
    _l_(608438)
    corpus_list = _c_(608441, _a_(608440, _n_(608439, "corpus", lambda: corpus), "corpus_to_list"))
    _l_(608442)
    _c_(608445, _n_(608443, "print", lambda: print), _n_(608444, "corpus_list", lambda: corpus_list))
    _l_(608446)

if _n_(608448, "__name__", lambda: __name__) == "__main__":
    _l_(608452)

    _c_(608450, _n_(608449, "main", lambda: main))
    _l_(608451)