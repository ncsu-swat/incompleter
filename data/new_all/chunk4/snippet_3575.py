# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72036511/attribute-error-module-uctypes-has-no-attribute-int32
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ffilib
    _l_(634499)

except ImportError:
    pass
try:
    import uctypes
    _l_(634501)

except ImportError:
    pass
try:
    import array
    _l_(634503)

except ImportError:
    pass
try:
    import uos
    _l_(634505)

except ImportError:
    pass
try:
    import os
    _l_(634507)

except ImportError:
    pass
try:
    import utime
    _l_(634509)

except ImportError:
    pass
try:
    from signal import *
    _l_(634511)

except ImportError:
    pass

libc = _c_(634514, _a_(634513, _n_(634512, "ffilib", lambda: ffilib), "libc"))
_l_(634515)
librt = _c_(634518, _a_(634517, _n_(634516, "ffilib", lambda: ffilib), "open"), "librt")
_l_(634519)

CLOCK_REALTIME = 0
_l_(634520)
CLOCK_MONOTONIC = 1
_l_(634521)
SIGEV_SIGNAL = 0
_l_(634522)

sigval_t = {
    "sival_int": _a_(634524, _n_(634523, "uctypes", lambda: uctypes), "INT32") | 0,
    "sival_ptr": (_a_(634526, _n_(634525, "uctypes", lambda: uctypes), "PTR") | 0, _a_(634528, _n_(634527, "uctypes", lambda: uctypes), "UINT8")),
}
_l_(634529)

sigevent_t = {
    "sigev_value": (0, _n_(634530, "sigval_t", lambda: sigval_t)),
    "sigev_signo": _a_(634532, _n_(634531, "uctypes", lambda: uctypes), "INT32") | 8,
    "sigev_notify": _a_(634534, _n_(634533, "uctypes", lambda: uctypes), "INT32") | 12,
}
_l_(634535)

timespec_t = {
    "tv_sec": _a_(634537, _n_(634536, "uctypes", lambda: uctypes), "INT32") | 0,
    "tv_nsec": _a_(634539, _n_(634538, "uctypes", lambda: uctypes), "INT64") | 8,
}
_l_(634540)

itimerspec_t = {
    "it_interval": (0, _n_(634541, "timespec_t", lambda: timespec_t)),
    "it_value": (16, _n_(634542, "timespec_t", lambda: timespec_t)),
}
_l_(634543)


__libc_current_sigrtmin = _c_(634546, _a_(634545, _n_(634544, "libc", lambda: libc), "func"), "i", "__libc_current_sigrtmin", "")
_l_(634547)
SIGRTMIN = _c_(634549, _n_(634548, "__libc_current_sigrtmin", lambda: __libc_current_sigrtmin))
_l_(634550)

timer_create_ = _c_(634553, _a_(634552, _n_(634551, "librt", lambda: librt), "func"), "i", "timer_create", "ipp")
_l_(634554)
timer_settime_ = _c_(634557, _a_(634556, _n_(634555, "librt", lambda: librt), "func"), "i", "timer_settime", "PiPp")
_l_(634558)

def new(sdesc):
    _l_(634579)

    buf = _c_(634564, _n_(634559, "bytearray", lambda: bytearray), _c_(634563, _a_(634561, _n_(634560, "uctypes", lambda: uctypes), "sizeof"), _n_(634562, "sdesc", lambda: sdesc)))
    _l_(634565)
    s = _c_(634575, _a_(634567, _n_(634566, "uctypes", lambda: uctypes), "struct"), _c_(634571, _a_(634569, _n_(634568, "uctypes", lambda: uctypes), "addressof"), _n_(634570, "buf", lambda: buf)), _n_(634572, "sdesc", lambda: sdesc), _a_(634574, _n_(634573, "uctypes", lambda: uctypes), "NATIVE"))
    _l_(634576)
    aux = _n_(634577, "s", lambda: s)
    _l_(634578)
    return aux

def timer_create(sig_id):
    _l_(634608)

    sev = _c_(634582, _n_(634580, "new", lambda: new), _n_(634581, "sigevent_t", lambda: sigevent_t))
    _l_(634583)
    #print(sev)
    _n_(634584, "sev", lambda: sev).sigev_notify = _n_(634585, "SIGEV_SIGNAL", lambda: SIGEV_SIGNAL)
    _l_(634586)
    _n_(634587, "sev", lambda: sev).sigev_signo = _n_(634588, "SIGRTMIN", lambda: SIGRTMIN) + _n_(634589, "sig_id", lambda: sig_id)
    _l_(634590)
    timerid = _c_(634593, _a_(634592, _n_(634591, "array", lambda: array), "array"), 'P', [0])
    _l_(634594)
    r = _c_(634599, _n_(634595, "timer_create_", lambda: timer_create_), _n_(634596, "CLOCK_MONOTONIC", lambda: CLOCK_MONOTONIC), _n_(634597, "sev", lambda: sev), _n_(634598, "timerid", lambda: timerid))
    _l_(634600)
    _c_(634604, _a_(634602, _n_(634601, "os", lambda: os), "check_error"), _n_(634603, "r", lambda: r))
    _l_(634605)
    aux = _n_(634606, "timerid", lambda: timerid)[0]
    _l_(634607)
    #print("timerid", hex(timerid[0]))
    return aux

def timer_settime(tid, hz):
    _l_(634638)

    period = 1000000000 // _n_(634609, "hz", lambda: hz)
    _l_(634610)
    new_val = _c_(634613, _n_(634611, "new", lambda: new), _n_(634612, "itimerspec_t", lambda: itimerspec_t))
    _l_(634614)
    _a_(634616, _n_(634615, "new_val", lambda: new_val), "it_value").tv_nsec = _n_(634617, "period", lambda: period)
    _l_(634618)
    _a_(634620, _n_(634619, "new_val", lambda: new_val), "it_interval").tv_nsec = _n_(634621, "period", lambda: period)
    _l_(634622)
    #print("new_val:", bytes(new_val))
    old_val = _c_(634625, _n_(634623, "new", lambda: new), _n_(634624, "itimerspec_t", lambda: itimerspec_t))
    _l_(634626)
    #print(new_val, old_val)
    r = _c_(634631, _n_(634627, "timer_settime_", lambda: timer_settime_), _n_(634628, "tid", lambda: tid), 0, _n_(634629, "new_val", lambda: new_val), _n_(634630, "old_val", lambda: old_val))
    _l_(634632)
    _c_(634636, _a_(634634, _n_(634633, "os", lambda: os), "check_error"), _n_(634635, "r", lambda: r))
    _l_(634637)


class Timer:
    _l_(634676)


    def __init__(self, id, freq):
        _l_(634650)

        _n_(634639, "self", lambda: self).id = _n_(634640, "id", lambda: id)
        _l_(634641)
        _n_(634642, "self", lambda: self).tid = _c_(634645, _n_(634643, "timer_create", lambda: timer_create), _n_(634644, "id", lambda: id))
        _l_(634646)
        _n_(634647, "self", lambda: self).freq = _n_(634648, "freq", lambda: freq)
        _l_(634649)

    def callback(self, cb):
        _l_(634669)

        _n_(634651, "self", lambda: self).cb = _n_(634652, "cb", lambda: cb)
        _l_(634653)
        _c_(634659, _n_(634654, "timer_settime", lambda: timer_settime), _a_(634656, _n_(634655, "self", lambda: self), "tid"), _a_(634658, _n_(634657, "self", lambda: self), "freq"))
        _l_(634660)
        org_sig = _c_(634667, _n_(634661, "signal", lambda: signal), _n_(634662, "SIGRTMIN", lambda: SIGRTMIN) + _a_(634664, _n_(634663, "self", lambda: self), "id"), _a_(634666, _n_(634665, "self", lambda: self), "handler"))
        _l_(634668)

    def handler(self, signum):
        _l_(634675)

        #print('Signal handler called with signal', signum)
        _c_(634673, _a_(634671, _n_(634670, "self", lambda: self), "cb"), _n_(634672, "self", lambda: self))
        _l_(634674)