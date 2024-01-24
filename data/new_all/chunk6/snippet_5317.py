# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67622575/typeerror-unsupported-operand-types-for-str-and-float-problem
# All constant value in the code:
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
G0 = 0.0000775  # Conductance quantum
_l_(351007)  # Conductance quantum
v = 0.1           # Bias voltage
_l_(351008)           # Bias voltage
Time_of_Loops = 1399951  # Time collected by LabVIEW， unit is ms
_l_(351009)  # Time collected by LabVIEW， unit is ms



# read data:
data = _c_(351012, _a_(351011, _n_(351010, "pd", lambda: pd), "read_csv"), 'C:\\Users\\fq20881\\OneDrive - University of Bristol\\OneDrive\\Data Analysis\\Data.txt', \
    sep=',', names=['Current', 'Position', 'Current2', 'Time2', 'PZT Voltage'])
_l_(351013)


_c_(351016, _a_(351015, _n_(351014, "data", lambda: data), "drop"), [0, 1], axis=0, inplace=True)
_l_(351017)
_c_(351020, _a_(351019, _n_(351018, "data", lambda: data), "reset_index"), drop=True, inplace=True)
_l_(351021)
nrows1 = _a_(351023, _n_(351022, "data", lambda: data), "shape")[0]
_l_(351024)
_c_(351026, _n_(351025, "print", lambda: print), 'row number of Current:')
_l_(351027)
_c_(351030, _n_(351028, "print", lambda: print), _n_(351029, "nrows1", lambda: nrows1))
_l_(351031)

data1 = _c_(351037, _a_(351033, _n_(351032, "pd", lambda: pd), "DataFrame"), columns=['Time', 'Conductance'], index=_c_(351036, _n_(351034, "range", lambda: range), 0, _n_(351035, "nrows1", lambda: nrows1)))
_l_(351038)
Speed_Time = _n_(351039, "Time_of_Loops", lambda: Time_of_Loops) / (_n_(351040, "nrows1", lambda: nrows1) * 1000)
_l_(351041)
_n_(351042, "data1", lambda: data1)['Time'] = _a_(351044, _n_(351043, "data1", lambda: data1), "index") * _n_(351045, "Speed_Time", lambda: Speed_Time)
_l_(351046)
_c_(351049, _n_(351047, "print", lambda: print), _n_(351048, "data1", lambda: data1))
_l_(351050)
_n_(351051, "data1", lambda: data1)['Conductance'] = _n_(351052, "data", lambda: data)['Current'] / (_n_(351053, "G0", lambda: G0) * _n_(351054, "v", lambda: v))
_l_(351055)
_c_(351058, _n_(351056, "print", lambda: print), _n_(351057, "data1", lambda: data1))
_l_(351059)