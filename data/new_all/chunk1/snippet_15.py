# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44144584/typeerror-cant-pickle-thread-lock-objects
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Process
    _l_(380634)

except ImportError:
    pass
try:
    from queue import Queue
    _l_(380636)

except ImportError:
    pass
try:
    import logging
    _l_(380638)

except ImportError:
    pass

def main():
    _l_(380653)

    x = _c_(380640, _n_(380639, "DataGenerator", lambda: DataGenerator))
    _l_(380641)
    try:
        _l_(380652)

        _c_(380644, _a_(380643, _n_(380642, "x", lambda: x), "run"))
        _l_(380645)
    except _n_(380646, "Exception", lambda: Exception) as e:
        _l_(380651)

        _c_(380649, _a_(380648, _n_(380647, "logging", lambda: logging), "exception"), "message")
        _l_(380650)


class DataGenerator:
    _l_(380752)


    def __init__(self):
        _l_(380660)

        _c_(380658, _a_(380655, _n_(380654, "logging", lambda: logging), "basicConfig"), filename='testing.log', level=_a_(380657, _n_(380656, "logging", lambda: logging), "INFO"))
        _l_(380659)

    def run(self):
        _l_(380692)

        _c_(380663, _a_(380662, _n_(380661, "logging", lambda: logging), "info"), "Running Generator")
        _l_(380664)
        queue = _c_(380666, _n_(380665, "Queue", lambda: Queue))
        _l_(380667)
        _c_(380674, _a_(380673, _c_(380672, _n_(380668, "Process", lambda: Process), target=_a_(380670, _n_(380669, "self", lambda: self), "package"), args=(_n_(380671, "queue", lambda: queue),)), "start"))
        _l_(380675)
        _c_(380678, _a_(380677, _n_(380676, "logging", lambda: logging), "info"), "Process started to generate data")
        _l_(380679)
        _c_(380686, _a_(380685, _c_(380684, _n_(380680, "Process", lambda: Process), target=_a_(380682, _n_(380681, "self", lambda: self), "send"), args=(_n_(380683, "queue", lambda: queue),)), "start"))
        _l_(380687)
        _c_(380690, _a_(380689, _n_(380688, "logging", lambda: logging), "info"), "Process started to send data.")
        _l_(380691)

    def package(self, queue):
        _l_(380710)

        while True:
            _l_(380709)

            for i in _c_(380694, _n_(380693, "range", lambda: range), 16):
                _l_(380708)

                datagram = _c_(380696, _n_(380695, "bytearray", lambda: bytearray))
                _l_(380697)
                _c_(380701, _a_(380699, _n_(380698, "datagram", lambda: datagram), "append"), _n_(380700, "i", lambda: i))
                _l_(380702)
                _c_(380706, _a_(380704, _n_(380703, "queue", lambda: queue), "put"), _n_(380705, "datagram", lambda: datagram))
                _l_(380707)

    def send(self, queue):
        _l_(380751)

        byte_array = _c_(380712, _n_(380711, "bytearray", lambda: bytearray))
        _l_(380713)
        while True:
            _l_(380750)

            size_of__queue = _c_(380716, _a_(380715, _n_(380714, "queue", lambda: queue), "qsize"))
            _l_(380717)
            _c_(380721, _a_(380719, _n_(380718, "logging", lambda: logging), "info"), " queue size %s", _n_(380720, "size_of_queue", lambda: size_of_queue))
            _l_(380722)
            if _n_(380723, "size_of_queue", lambda: size_of_queue) > 7:
                _l_(380749)

                for i in _c_(380725, _n_(380724, "range", lambda: range), 1, 8):
                    _l_(380735)

                    packet = _c_(380728, _a_(380727, _n_(380726, "queue", lambda: queue), "get"))
                    _l_(380729)
                    _c_(380733, _a_(380731, _n_(380730, "byte_array", lambda: byte_array), "append"), _n_(380732, "packet", lambda: packet))
                    _l_(380734)
                _c_(380738, _a_(380737, _n_(380736, "logging", lambda: logging), "info"), "Sending datagram ")
                _l_(380739)
                _c_(380744, _n_(380740, "print", lambda: print), _c_(380743, _n_(380741, "str", lambda: str), _n_(380742, "datagram", lambda: datagram)))
                _l_(380745)
                _c_(380747, _n_(380746, "byte_array", lambda: byte_array), 0)
                _l_(380748)

if _n_(380753, "__name__", lambda: __name__) == "__main__":
    _l_(380757)

    _c_(380755, _n_(380754, "main", lambda: main))
    _l_(380756)