# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75333088/class-typeerror-metawear-accelerometer-and-gyroscope
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(620804)

except ImportError:
    pass
try:
    from mbientlab.metawear import MetaWear, libmetawear
    _l_(620806)

except ImportError:
    pass
try:
    from mbientlab.metawear.cbindings import *
    _l_(620808)

except ImportError:
    pass
try:
    from mbientlab.warble import *
    _l_(620810)

except ImportError:
    pass
try:
    from mbientlab.metawear import *
    _l_(620812)

except ImportError:
    pass
try:
    from threading import Event
    _l_(620814)

except ImportError:
    pass
try:
    from time import sleep
    _l_(620816)

except ImportError:
    pass
try:
    import ctypes
    _l_(620818)

except ImportError:
    pass

# Define the data handler method
def data_handler(data):
    _l_(620835)

    _c_(620825, _n_(620819, "print", lambda: print), _c_(620824, _a_(620820, "Accelerometer data: x = {0:.3f}, y = {1:.3f}, z = {2:.3f}", "format"), _n_(620821, "data", lambda: data)['accelerometer'][0], _n_(620822, "data", lambda: data)['accelerometer'][1], _n_(620823, "data", lambda: data)['accelerometer'][2]))
    _l_(620826)
    _c_(620833, _n_(620827, "print", lambda: print), _c_(620832, _a_(620828, "Gyro data: x = {0:.3f}, y = {1:.3f}, z = {2:.3f}", "format"), _n_(620829, "data", lambda: data)['gyro'][0], _n_(620830, "data", lambda: data)['gyro'][1], _n_(620831, "data", lambda: data)['gyro'][2]))
    _l_(620834)

# Create a state object to store information about the device and the number of data samples received
class State:
    _l_(620842)

    def __init__(self, device):
        _l_(620841)

        _n_(620836, "self", lambda: self).device = _n_(620837, "device", lambda: device)
        _l_(620838)
        _n_(620839, "self", lambda: self).samples = 0
        _l_(620840)

# Connect to the device using its MAC address
device = _c_(620844, _n_(620843, "MetaWear", lambda: MetaWear), "ADDRESS")
_l_(620845)
_c_(620848, _a_(620847, _n_(620846, "device", lambda: device), "connect"))
_l_(620849)

# Set the connection parameters
_c_(620854, _a_(620851, _n_(620850, "libmetawear", lambda: libmetawear), "mbl_mw_settings_set_connection_parameters"), _a_(620853, _n_(620852, "device", lambda: device), "board"), 7.5, 7.5, 0, 6000)
_l_(620855)

# Configure the accelerometer
_c_(620860, _a_(620857, _n_(620856, "libmetawear", lambda: libmetawear), "mbl_mw_acc_set_odr"), _a_(620859, _n_(620858, "device", lambda: device), "board"), 100)
_l_(620861)
_c_(620866, _a_(620863, _n_(620862, "libmetawear", lambda: libmetawear), "mbl_mw_acc_set_range"), _a_(620865, _n_(620864, "device", lambda: device), "board"), 8.0)
_l_(620867)
_c_(620872, _a_(620869, _n_(620868, "libmetawear", lambda: libmetawear), "mbl_mw_acc_write_acceleration_config"), _a_(620871, _n_(620870, "device", lambda: device), "board"))
_l_(620873)

# Configure the gyro
_c_(620878, _a_(620875, _n_(620874, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_set_odr"), _a_(620877, _n_(620876, "device", lambda: device), "board"), 100)
_l_(620879)
_c_(620884, _a_(620881, _n_(620880, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_set_range"), _a_(620883, _n_(620882, "device", lambda: device), "board"), 2000)
_l_(620885)
_c_(620890, _a_(620887, _n_(620886, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_write_config"), _a_(620889, _n_(620888, "device", lambda: device), "board"))
_l_(620891)

# Create a state object and subscribe to the accelerometer and gyro data streams
state = _c_(620894, _n_(620892, "State", lambda: State), _n_(620893, "device", lambda: device))
_l_(620895)
accelerometer = _c_(620900, _a_(620897, _n_(620896, "libmetawear", lambda: libmetawear), "mbl_mw_acc_get_acceleration_data_signal"), _a_(620899, _n_(620898, "device", lambda: device), "board"))
_l_(620901)
gyro = _c_(620906, _a_(620903, _n_(620902, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_get_rotation_data_signal"), _a_(620905, _n_(620904, "device", lambda: device), "board"))
_l_(620907)

cb_fun = _c_(620914, _c_(620912, _n_(620908, "CFUNCTYPE", lambda: CFUNCTYPE), None, _c_(620911, _n_(620909, "POINTER", lambda: POINTER), _n_(620910, "Data", lambda: Data))), _n_(620913, "data_handler", lambda: data_handler)) # NOT WORKING
_l_(620915) # NOT WORKING
_c_(620920, _a_(620917, _n_(620916, "libmetawear", lambda: libmetawear), "mbl_mw_datasignal_subscribe"), _n_(620918, "accelerometer", lambda: accelerometer), None, _n_(620919, "cb_fun", lambda: cb_fun)) # NOT WORKING
_l_(620921) # NOT WORKING
_c_(620926, _a_(620923, _n_(620922, "libmetawear", lambda: libmetawear), "mbl_mw_datasignal_subscribe"), _n_(620924, "gyro", lambda: gyro), None, _n_(620925, "cb_fun", lambda: cb_fun)) # NOT WORKING
_l_(620927) # NOT WORKING

# Start streaming dat
_c_(620932, _a_(620929, _n_(620928, "libmetawear", lambda: libmetawear), "mbl_mw_acc_enable_acceleration_sampling"), _a_(620931, _n_(620930, "device", lambda: device), "board"))
_l_(620933)
_c_(620938, _a_(620935, _n_(620934, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_enable_rotation_sampling"), _a_(620937, _n_(620936, "device", lambda: device), "board"))
_l_(620939)
_c_(620944, _a_(620941, _n_(620940, "libmetawear", lambda: libmetawear), "mbl_mw_acc_start"), _a_(620943, _n_(620942, "device", lambda: device), "board"))
_l_(620945)
_c_(620950, _a_(620947, _n_(620946, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_start"), _a_(620949, _n_(620948, "device", lambda: device), "board"))
_l_(620951)

#Wait for 5 seconds
_c_(620954, _a_(620953, _n_(620952, "time", lambda: time), "sleep"), 5.0)
_l_(620955)

#Stop the accelerometer and gyro
_c_(620960, _a_(620957, _n_(620956, "libmetawear", lambda: libmetawear), "mbl_mw_acc_stop"), _a_(620959, _n_(620958, "device", lambda: device), "board"))
_l_(620961)
_c_(620966, _a_(620963, _n_(620962, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_stop"), _a_(620965, _n_(620964, "device", lambda: device), "board"))
_l_(620967)

#Disable acceleration and rotation sampling
_c_(620972, _a_(620969, _n_(620968, "libmetawear", lambda: libmetawear), "mbl_mw_acc_disable_acceleration_sampling"), _a_(620971, _n_(620970, "device", lambda: device), "board"))
_l_(620973)
_c_(620978, _a_(620975, _n_(620974, "libmetawear", lambda: libmetawear), "mbl_mw_gyro_bmi160_disable_rotation_sampling"), _a_(620977, _n_(620976, "device", lambda: device), "board"))
_l_(620979)

#Disconnect from the device
_c_(620982, _a_(620981, _n_(620980, "device", lambda: device), "disconnect"))
_l_(620983)