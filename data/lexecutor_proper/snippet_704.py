# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_installation(rv):
    _l_(64406)

    current_version = _a_(64383, _n_(64382, "sys", lambda: sys), "version_info")
    _l_(64384)
    if _n_(64385, "current_version", lambda: current_version)[0] == _n_(64386, "rv", lambda: rv)[0] and _n_(64387, "current_version", lambda: current_version)[1] >= _n_(64388, "rv", lambda: rv)[1]:
        _l_(64404)

        pass
        _l_(64389)
    else:
        _c_(64398, _a_(64392, _a_(64391, _n_(64390, "sys", lambda: sys), "stderr"), "write"), "[%s] - Error: Your Python interpreter must be %d.%d or greater (within major version %d)\n" % (_a_(64394, _n_(64393, "sys", lambda: sys), "argv")[0], _n_(64395, "rv", lambda: rv)[0], _n_(64396, "rv", lambda: rv)[1], _n_(64397, "rv", lambda: rv)[0]) )
        _l_(64399)
        _c_(64402, _a_(64401, _n_(64400, "sys", lambda: sys), "exit"), -1)
        _l_(64403)
    aux = 0
    _l_(64405)
    return aux


# Calling the 'check_installation' function checks if Python is >= 2.7 and < 3
required_version = (2,7)
_l_(64407)
_c_(64410, _n_(64408, "check_installation", lambda: check_installation), _n_(64409, "required_version", lambda: required_version))
_l_(64411)

