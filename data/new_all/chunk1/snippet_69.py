# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53135439/issue-with-add-method-in-tensorflow-attributeerror-module-tensorflow-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import keras as K
  _l_(398912)

except ImportError:
  pass
try:
  from keras.models import Sequential
  _l_(398914)

except ImportError:
  pass
try:
  from keras.layers import Dense
  _l_(398916)

except ImportError:
  pass
try:
  from tensorflow import set_random_seed
  _l_(398918)

except ImportError:
  pass

for hidden_neuron in _n_(398919, "hidden_neurons", lambda: hidden_neurons):
  _l_(398923)

  model = _c_(398921, _n_(398920, "Sequential", lambda: Sequential))
  _l_(398922)