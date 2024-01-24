# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72036511/attribute-error-module-uctypes-has-no-attribute-int32
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ffilib
    _l_(592625)

except ImportError:
    pass
try:
    import uctypes
    _l_(592627)

except ImportError:
    pass
try:
    import array
    _l_(592629)

except ImportError:
    pass
try:
    import uos
    _l_(592631)

except ImportError:
    pass
try:
    import os
    _l_(592633)

except ImportError:
    pass
try:
    import utime
    _l_(592635)

except ImportError:
    pass
try:
    from signal import *
    _l_(592637)

except ImportError:
    pass

libc = _c_(592640, _a_(592639, _n_(592638, "ffilib", lambda: ffilib), "libc"))
_l_(592641)
librt = _c_(592644, _a_(592643, _n_(592642, "ffilib", lambda: ffilib), "open"), "librt")
_l_(592645)

CLOCK_REALTIME = 0
_l_(592646)
CLOCK_MONOTONIC = 1
_l_(592647)
SIGEV_SIGNAL = 0
_l_(592648)

sigval_t = {
    "sival_int": _a_(592650, _n_(592649, "uctypes", lambda: uctypes), "INT32") | 0,
    "sival_ptr": (_a_(592652, _n_(592651, "uctypes", lambda: uctypes), "PTR") | 0, _a_(592654, _n_(592653, "uctypes", lambda: uctypes), "UINT8")),
}
_l_(592655)

sigevent_t = {
    "sigev_value": (0, _n_(592656, "sigval_t", lambda: sigval_t)),
    "sigev_signo": _a_(592658, _n_(592657, "uctypes", lambda: uctypes), "INT32") | 8,
    "sigev_notify": _a_(592660, _n_(592659, "uctypes", lambda: uctypes), "INT32") | 12,
}
_l_(592661)

timespec_t = {
    "tv_sec": _a_(592663, _n_(592662, "uctypes", lambda: uctypes), "INT32") | 0,
    "tv_nsec": _a_(592665, _n_(592664, "uctypes", lambda: uctypes), "INT64") | 8,
}
_l_(592666)

itimerspec_t = {
    "it_interval": (0, _n_(592667, "timespec_t", lambda: timespec_t)),
    "it_value": (16, _n_(592668, "timespec_t", lambda: timespec_t)),
}
_l_(592669)


__libc_current_sigrtmin = _c_(592672, _a_(592671, _n_(592670, "libc", lambda: libc), "func"), "i", "__libc_current_sigrtmin", "")
_l_(592673)
SIGRTMIN = _c_(592675, _n_(592674, "__libc_current_sigrtmin", lambda: __libc_current_sigrtmin))
_l_(592676)

timer_create_ = _c_(592679, _a_(592678, _n_(592677, "librt", lambda: librt), "func"), "i", "timer_create", "ipp")
_l_(592680)
timer_settime_ = _c_(592683, _a_(592682, _n_(592681, "librt", lambda: librt), "func"), "i", "timer_settime", "PiPp")
_l_(592684)

def new(sdesc):
    _l_(592705)

    buf = _c_(592690, _n_(592685, "bytearray", lambda: bytearray), _c_(592689, _a_(592687, _n_(592686, "uctypes", lambda: uctypes), "sizeof"), _n_(592688, "sdesc", lambda: sdesc)))
    _l_(592691)
    s = _c_(592701, _a_(592693, _n_(592692, "uctypes", lambda: uctypes), "struct"), _c_(592697, _a_(592695, _n_(592694, "uctypes", lambda: uctypes), "addressof"), _n_(592696, "buf", lambda: buf)), _n_(592698, "sdesc", lambda: sdesc), _a_(592700, _n_(592699, "uctypes", lambda: uctypes), "NATIVE"))
    _l_(592702)
    aux = _n_(592703, "s", lambda: s)
    _l_(592704)
    return aux

def timer_create(sig_id):
    _l_(592734)

    sev = _c_(592708, _n_(592706, "new", lambda: new), _n_(592707, "sigevent_t", lambda: sigevent_t))
    _l_(592709)
    #print(sev)
    _n_(592710, "sev", lambda: sev).sigev_notify = _n_(592711, "SIGEV_SIGNAL", lambda: SIGEV_SIGNAL)
    _l_(592712)
    _n_(592713, "sev", lambda: sev).sigev_signo = _n_(592714, "SIGRTMIN", lambda: SIGRTMIN) + _n_(592715, "sig_id", lambda: sig_id)
    _l_(592716)
    timerid = _c_(592719, _a_(592718, _n_(592717, "array", lambda: array), "array"), 'P', [0])
    _l_(592720)
    r = _c_(592725, _n_(592721, "timer_create_", lambda: timer_create_), _n_(592722, "CLOCK_MONOTONIC", lambda: CLOCK_MONOTONIC), _n_(592723, "sev", lambda: sev), _n_(592724, "timerid", lambda: timerid))
    _l_(592726)
    _c_(592730, _a_(592728, _n_(592727, "os", lambda: os), "check_error"), _n_(592729, "r", lambda: r))
    _l_(592731)
    aux = _n_(592732, "timerid", lambda: timerid)[0]
    _l_(592733)
    #print("timerid", hex(timerid[0]))
    return aux

def timer_settime(tid, hz):
    _l_(592764)

    period = 1000000000 // _n_(592735, "hz", lambda: hz)
    _l_(592736)
    new_val = _c_(592739, _n_(592737, "new", lambda: new), _n_(592738, "itimerspec_t", lambda: itimerspec_t))
    _l_(592740)
    _a_(592742, _n_(592741, "new_val", lambda: new_val), "it_value").tv_nsec = _n_(592743, "period", lambda: period)
    _l_(592744)
    _a_(592746, _n_(592745, "new_val", lambda: new_val), "it_interval").tv_nsec = _n_(592747, "period", lambda: period)
    _l_(592748)
    #print("new_val:", bytes(new_val))
    old_val = _c_(592751, _n_(592749, "new", lambda: new), _n_(592750, "itimerspec_t", lambda: itimerspec_t))
    _l_(592752)
    #print(new_val, old_val)
    r = _c_(592757, _n_(592753, "timer_settime_", lambda: timer_settime_), _n_(592754, "tid", lambda: tid), 0, _n_(592755, "new_val", lambda: new_val), _n_(592756, "old_val", lambda: old_val))
    _l_(592758)
    _c_(592762, _a_(592760, _n_(592759, "os", lambda: os), "check_error"), _n_(592761, "r", lambda: r))
    _l_(592763)


class Timer:
    _l_(592802)


    def __init__(self, id, freq):
        _l_(592776)

        _n_(592765, "self", lambda: self).id = _n_(592766, "id", lambda: id)
        _l_(592767)
        _n_(592768, "self", lambda: self).tid = _c_(592771, _n_(592769, "timer_create", lambda: timer_create), _n_(592770, "id", lambda: id))
        _l_(592772)
        _n_(592773, "self", lambda: self).freq = _n_(592774, "freq", lambda: freq)
        _l_(592775)

    def callback(self, cb):
        _l_(592795)

        _n_(592777, "self", lambda: self).cb = _n_(592778, "cb", lambda: cb)
        _l_(592779)
        _c_(592785, _n_(592780, "timer_settime", lambda: timer_settime), _a_(592782, _n_(592781, "self", lambda: self), "tid"), _a_(592784, _n_(592783, "self", lambda: self), "freq"))
        _l_(592786)
        org_sig = _c_(592793, _n_(592787, "signal", lambda: signal), _n_(592788, "SIGRTMIN", lambda: SIGRTMIN) + _a_(592790, _n_(592789, "self", lambda: self), "id"), _a_(592792, _n_(592791, "self", lambda: self), "handler"))
        _l_(592794)

    def handler(self, signum):
        _l_(592801)

        #print('Signal handler called with signal', signum)
        _c_(592799, _a_(592797, _n_(592796, "self", lambda: self), "cb"), _n_(592798, "self", lambda: self))
        _l_(592800)