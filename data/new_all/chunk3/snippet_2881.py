# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60043979/how-to-resolve-typeerror-when-migrating-code-to-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
found_qr = None
_l_(539834)
while not _n_(539835, "found_qr", lambda: found_qr):
    _l_(539864)

    _c_(539837, _n_(539836, "keep_alive", lambda: keep_alive), 1,5)
    _l_(539838)
    _c_(539841, _a_(539840, _n_(539839, "time", lambda: time), "sleep"), 4)
    _l_(539842)
    process = None
    _l_(539843)
    stdout_list = None
    _l_(539844)
    process = _c_(539850, _a_(539846, _n_(539845, "subprocess", lambda: subprocess), "Popen"), 'grep -E -o ".Source QR CODE :.{0,65}" ' + _n_(539847, "latest_file", lambda: latest_file) + ' | tail -1', shell=True, stdout=_a_(539849, _n_(539848, "subprocess", lambda: subprocess), "PIPE"),)
    _l_(539851)
    stdout_list = _c_(539854, _a_(539853, _n_(539852, "process", lambda: process), "communicate"))
    _l_(539855)
    stdout_list = _n_(539856, "stdout_list", lambda: stdout_list)[0]
    _l_(539857)
    if _c_(539860, _a_(539859, _n_(539858, "stdout_list", lambda: stdout_list), "find"), "Source QR CODE") == -1:
        _l_(539863)

        found_qr = None
        _l_(539861)
    else:
        found_qr = 'found!'
        _l_(539862)