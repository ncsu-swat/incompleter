# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66972367/getting-typeerror-method-takes-0-positional-arguments-but-1-was-given-with-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import corpus as corp
    _l_(586068)

except ImportError:
    pass

def main():
    _l_(586081)

    corpus = _c_(586071, _a_(586070, _n_(586069, "corp", lambda: corp), "Corpus"), "review.txt")
    _l_(586072)
    corpus_list = _c_(586075, _a_(586074, _n_(586073, "corpus", lambda: corpus), "corpus_to_list"))
    _l_(586076)
    _c_(586079, _n_(586077, "print", lambda: print), _n_(586078, "corpus_list", lambda: corpus_list))
    _l_(586080)

if _n_(586082, "__name__", lambda: __name__) == "__main__":
    _l_(586086)

    _c_(586084, _n_(586083, "main", lambda: main))
    _l_(586085)