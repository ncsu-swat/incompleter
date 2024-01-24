# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75333088/class-typeerror-metawear-accelerometer-and-gyroscope
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cb_fun = _c_(608851, _c_(608849, _n_(608845, "CFUNCTYPE", lambda: CFUNCTYPE), None, _c_(608848, _n_(608846, "POINTER", lambda: POINTER), _n_(608847, "Data", lambda: Data))), _n_(608850, "data_handler", lambda: data_handler))
_l_(608852)
_c_(608857, _a_(608854, _n_(608853, "libmetawear", lambda: libmetawear), "mbl_mw_datasignal_subscribe"), _n_(608855, "accelerometer", lambda: accelerometer), None, _n_(608856, "cb_fun", lambda: cb_fun))
_l_(608858)
_c_(608863, _a_(608860, _n_(608859, "libmetawear", lambda: libmetawear), "mbl_mw_datasignal_subscribe"), _n_(608861, "gyro", lambda: gyro), None, _n_(608862, "cb_fun", lambda: cb_fun))
_l_(608864)