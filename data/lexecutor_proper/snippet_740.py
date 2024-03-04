# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
# Python list with append()
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(64585, _a_(64581, _n_(64580, "np", lambda: np), "mean"), _c_(64584, _a_(64583, _n_(64582, "timeit", lambda: timeit), "repeat"), setup="a = []", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
_l_(64586)
# 0.054 +/- 0.025 msec

# Python array with append()
_c_(64592, _a_(64588, _n_(64587, "np", lambda: np), "mean"), _c_(64591, _a_(64590, _n_(64589, "timeit", lambda: timeit), "repeat"), setup="import array; a = array.array('f')", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
_l_(64593)
# 0.104 +/- 0.025 msec

# Numpy array with append()
_c_(64599, _a_(64595, _n_(64594, "np", lambda: np), "mean"), _c_(64598, _a_(64597, _n_(64596, "timeit", lambda: timeit), "repeat"), setup="import numpy as np; a = np.array([])", stmt="np.append(a, [1.0])", number=1000, repeat=5000)) * 1000
_l_(64600)
# 5.183 +/- 0.950 msec

# Python list using +=
_c_(64606, _a_(64602, _n_(64601, "np", lambda: np), "mean"), _c_(64605, _a_(64604, _n_(64603, "timeit", lambda: timeit), "repeat"), setup="a = []", stmt="a += [1.0]", number=1000, repeat=5000)) * 1000
_l_(64607)
# 0.062 +/- 0.021 msec

# Python array using += 
_c_(64613, _a_(64609, _n_(64608, "np", lambda: np), "mean"), _c_(64612, _a_(64611, _n_(64610, "timeit", lambda: timeit), "repeat"), setup="import array; a = array.array('f')", stmt="a += array.array('f', [1.0]) ", number=1000, repeat=5000)) * 1000
_l_(64614)
# 0.289 +/- 0.043 msec

# Python list using extend()
_c_(64620, _a_(64616, _n_(64615, "np", lambda: np), "mean"), _c_(64619, _a_(64618, _n_(64617, "timeit", lambda: timeit), "repeat"), setup="a = []", stmt="a.extend([1.0])", number=1000, repeat=5000)) * 1000
_l_(64621)
# 0.083 +/- 0.020 msec

# Python array using extend()
_c_(64627, _a_(64623, _n_(64622, "np", lambda: np), "mean"), _c_(64626, _a_(64625, _n_(64624, "timeit", lambda: timeit), "repeat"), setup="import array; a = array.array('f')", stmt="a.extend([1.0]) ", number=1000, repeat=5000)) * 1000
_l_(64628)
# 0.169 +/- 0.034

