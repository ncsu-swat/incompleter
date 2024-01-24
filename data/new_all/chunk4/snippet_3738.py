# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68922318/gwpy-package-gives-error-attributeerror-module-matplotlib-pyplot-has-no-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import pandas as pd
  _l_(619964)

except ImportError:
  pass
try:
  import seaborn as sns
  _l_(619966)

except ImportError:
  pass
try:
  from scipy import signal
  _l_(619968)

except ImportError:
  pass
try:
  from gwpy.timeseries import TimeSeries
  _l_(619970)

except ImportError:
  pass
try:
  from gwpy.plot import Plot
  _l_(619972)

except ImportError:
  pass
try:
  import matplotlib.pyplot as plt
  _l_(619974)

except ImportError:
  pass
_c_(619978, _a_(619977, _a_(619976, _n_(619975, "plt", lambda: plt), "style"), "use"), 'ggplot')
_l_(619979)


def get_tseries_from_file(file_name):
  _l_(620001)

  t_data = _c_(619983, _a_(619981, _n_(619980, "np", lambda: np), "load"), _n_(619982, "file_name", lambda: file_name))
  _l_(619984)
  tseries1 = _c_(619987, _n_(619985, "TimeSeries", lambda: TimeSeries), _n_(619986, "t_data", lambda: t_data)[0,:], sample_rate=2048)
  _l_(619988)
  tseries2 = _c_(619991, _n_(619989, "TimeSeries", lambda: TimeSeries), _n_(619990, "t_data", lambda: t_data)[1,:], sample_rate=2048)
  _l_(619992)
  tseries3 = _c_(619995, _n_(619993, "TimeSeries", lambda: TimeSeries), _n_(619994, "t_data", lambda: t_data)[2,:], sample_rate=2048)
  _l_(619996)
  aux = _n_(619997, "tseries1", lambda: tseries1), _n_(619998, "tseries2", lambda: tseries2), _n_(619999, "tseries3", lambda: tseries3)
  _l_(620000)
  return aux

def plot_tseries(t1, t2, t3):
  _l_(620024)

  plot = _c_(620006, _n_(620002, "Plot", lambda: Plot), _n_(620003, "t1", lambda: t1), _n_(620004, "t2", lambda: t2), _n_(620005, "t3", lambda: t3), separate=True, sharex=True, figsize=[20, 12])
  _l_(620007)
  ax = _c_(620010, _a_(620009, _n_(620008, "plot", lambda: plot), "gca"))
  _l_(620011)
  _c_(620014, _a_(620013, _n_(620012, "ax", lambda: ax), "set_xlim"), 0, 2)
  _l_(620015)
  _c_(620018, _a_(620017, _n_(620016, "ax", lambda: ax), "set_xlabel"), 'Time [s]')
  _l_(620019)
  _c_(620022, _a_(620021, _n_(620020, "plt", lambda: plt), "show"))
  _l_(620023)
file_1 = _n_(620025, "root_dir", lambda: root_dir) + 'train/0/0/0/000a5b6e5c.npy'
_l_(620026)
  
tseries1, tseries2, tseries3 = _c_(620029, _n_(620027, "get_tseries_from_file", lambda: get_tseries_from_file), _n_(620028, "file_1", lambda: file_1))
_l_(620030)

# Plotting the 3 TimeSeries
_c_(620035, _n_(620031, "plot_tseries", lambda: plot_tseries), _n_(620032, "tseries1", lambda: tseries1), _n_(620033, "tseries2", lambda: tseries2), _n_(620034, "tseries3", lambda: tseries3))
_l_(620036)