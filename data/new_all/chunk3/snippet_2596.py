# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70096375/fasttext-typeerror-loadmodel-incompatible-function-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fasttext
    _l_(550035)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(550037)

except ImportError:
    pass

base_path = _c_(550039, _n_(550038, "Path", lambda: Path), "..")
_l_(550040)
fasttext_model = _n_(550041, "base_path", lambda: base_path) / "models" / "cc.de.300.bin"
_l_(550042)

class EmbeddingVectorizer:
    _l_(550063)

    def __init__(self):
        _l_(550049)


        _n_(550043, "self", lambda: self).embedding_model = _c_(550047, _a_(550045, _n_(550044, "fasttext", lambda: fasttext), "load_model"), _n_(550046, "fasttext_model", lambda: fasttext_model))
        _l_(550048)

    def __call__(self, doc):
        _l_(550062)

        """
        Convert address to embedding vectors
        :param address: The address to convert
        :return: The embeddings vectors
        """
        embeddings = []
        _l_(550050)
        for word in _n_(550051, "doc", lambda: doc):
            _l_(550059)

            _c_(550057, _a_(550053, _n_(550052, "embeddings", lambda: embeddings), "append"), _a_(550055, _n_(550054, "self", lambda: self), "embedding_model")[_n_(550056, "word", lambda: word)])
            _l_(550058)
        aux = _n_(550060, "embeddings", lambda: embeddings)
        _l_(550061)
        return aux

embedding_model = _c_(550065, _n_(550064, "EmbeddingVectorizer", lambda: EmbeddingVectorizer))
_l_(550066)