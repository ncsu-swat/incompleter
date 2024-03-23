# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67037067/attributeerror-module-tensorflow-keras-mixed-precision-has-no-attribute-set
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(378870)

except ImportError:
    pass
try:
    import datetime
    _l_(378872)

except ImportError:
    pass
try:
    import os
    _l_(378874)

except ImportError:
    pass
try:
    import numpy as np
    _l_(378876)

except ImportError:
    pass
try:
    from ravens import agents
    _l_(378878)

except ImportError:
    pass
try:
    from ravens import Dataset
    _l_(378880)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(378882)

except ImportError:
    pass

# tf.keras.mixed_precision.set_global_policy('mixed_float16')

# OR

# policy = tf.keras.mixed_precision.Policy('mixed_float16')
# mixed_precision.set_global_policy(policy)