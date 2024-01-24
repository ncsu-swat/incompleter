# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65548276/applying-inception-but-get-the-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from IPython.display import Image, display
    _l_(634181)

except ImportError:
    pass
_c_(634183, _n_(634182, "Image", lambda: Image), 'images/07_inception_flowchart.png')
_l_(634184)
try:
    import inception
    _l_(634186)

except ImportError:
    pass
try:
    import matplotlib
    _l_(634188)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(634190)

except ImportError:
    pass
try:
    import numpy as np
    _l_(634192)

except ImportError:
    pass
try:
    import os
    _l_(634194)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(634196)

except ImportError:
    pass

_a_(634198, _n_(634197, "tf", lambda: tf), "__version__")
_l_(634199)

# Download the Inception model
_n_(634200, "inception", lambda: inception).data_dir = 'inception/'
_l_(634201)

def maybe_download():
    _l_(634211)

    """
    Download the Inception model from the internet if it does not already
    exist in the data_dir. The file is about 85 MB.
    """

    _c_(634203, _n_(634202, "print", lambda: print), "Downloading Inception v3 Model ...")
    _l_(634204)
    _c_(634209, _a_(634206, _n_(634205, "download", lambda: download), "maybe_download_and_extract"), url=_n_(634207, "data_url", lambda: data_url), download_dir=_n_(634208, "data_dir", lambda: data_dir))
    _l_(634210)

_c_(634214, _a_(634213, _n_(634212, "inception", lambda: inception), "maybe_download"))
_l_(634215)