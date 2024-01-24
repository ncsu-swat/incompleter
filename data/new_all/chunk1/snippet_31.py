# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53680913/typeerror-cannot-unpack-non-iterable-nonetype-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(381429)

except ImportError:
    pass


def load_dataset():
    _l_(381524)

    def download(filename, source="http://yaan.lecun.com/exdb/mnist/"):
        _l_(381443)

        _c_(381432, _n_(381430, "print", lambda: print), "Downloading ",_n_(381431, "filename", lambda: filename))
        _l_(381433)
        try:
            import urllib
            _l_(381435)

        except ImportError:
            pass
        _c_(381441, _a_(381437, _n_(381436, "urllib", lambda: urllib), "urlretrieve"), _n_(381438, "source", lambda: source)+_n_(381439, "filename", lambda: filename),_n_(381440, "filename", lambda: filename))
        _l_(381442)
    try:
        import gzip
        _l_(381445)

    except ImportError:
        pass
    
    def load_mnist_images(filename):
        _l_(381523)

        if not _c_(381450, _a_(381448, _a_(381447, _n_(381446, "os", lambda: os), "path"), "exists"), _n_(381449, "filename", lambda: filename)):
            _l_(381455)

            _c_(381453, _n_(381451, "download", lambda: download), _n_(381452, "filename", lambda: filename))
            _l_(381454)
        with _c_(381459, _a_(381457, _n_(381456, "gzip", lambda: gzip), "open"), _n_(381458, "filename", lambda: filename),"rb") as f:
            _l_(381478)

            data=_c_(381467, _a_(381461, _n_(381460, "np", lambda: np), "frombuffer"), _c_(381464, _a_(381463, _n_(381462, "f", lambda: f), "read")), _a_(381466, _n_(381465, "np", lambda: np), "uint8"), offset=16)
            _l_(381468)
            
            data = _c_(381471, _a_(381470, _n_(381469, "data", lambda: data), "reshape"), -1,1,28,28)
            _l_(381472)
            aux = _n_(381473, "data", lambda: data)/_c_(381476, _a_(381475, _n_(381474, "np", lambda: np), "float32"), 256)
            _l_(381477)
            
            return aux

        def load_mnist_labels(filename):
            _l_(381505)

            if not _c_(381483, _a_(381481, _a_(381480, _n_(381479, "os", lambda: os), "path"), "exists"), _n_(381482, "filename", lambda: filename)):
                _l_(381488)

                _c_(381486, _n_(381484, "download", lambda: download), _n_(381485, "filename", lambda: filename))
                _l_(381487)
            with _c_(381492, _a_(381490, _n_(381489, "gzip", lambda: gzip), "open"), _n_(381491, "filename", lambda: filename),"rb") as f:
                _l_(381502)

                data = _c_(381500, _a_(381494, _n_(381493, "np", lambda: np), "frombuffer"), _c_(381497, _a_(381496, _n_(381495, "f", lambda: f), "read")), _a_(381499, _n_(381498, "np", lambda: np), "uint8"), offset=8)
                _l_(381501)
            aux = _n_(381503, "data", lambda: data)
            _l_(381504)
            return aux

        X_train = _c_(381507, _n_(381506, "load_mnist_images", lambda: load_mnist_images), "train-images-idx3-ubyte.gz")
        _l_(381508)
        y_train = _c_(381510, _n_(381509, "load_mnist_labels", lambda: load_mnist_labels), "train-labels-idx1-ubyte.gz")
        _l_(381511)
        X_test = _c_(381513, _n_(381512, "load_mnist_images", lambda: load_mnist_images), "t10k-images-idx3-ubyte.gz")
        _l_(381514)
        y_test = _c_(381516, _n_(381515, "load_mnist_labels", lambda: load_mnist_labels), "t10k-labels-idx1-ubyte.gz")
        _l_(381517)
        aux = _n_(381518, "X_train", lambda: X_train), _n_(381519, "y_train", lambda: y_train), _n_(381520, "X_test", lambda: X_test), _n_(381521, "y_test", lambda: y_test)
        _l_(381522)

        return aux


X_train, y_train, X_test, y_test = _c_(381526, _n_(381525, "load_dataset", lambda: load_dataset))
_l_(381527)
try:
    import matplotlib
    _l_(381529)

except ImportError:
    pass
_c_(381532, _a_(381531, _n_(381530, "matplotlib", lambda: matplotlib), "use"), "TkAgg")
_l_(381533)
try:
    import matplotlib.pyplot as plt
    _l_(381535)

except ImportError:
    pass
_c_(381542, _a_(381537, _n_(381536, "plt", lambda: plt), "show"), _c_(381541, _a_(381539, _n_(381538, "plt", lambda: plt), "imshow"), _n_(381540, "X_train", lambda: X_train)[3][0]))
_l_(381543)