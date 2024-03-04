# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12332975/installing-python-module-within-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(64098)

except ImportError:
    pass
try:
    import subprocess
    _l_(64100)

except ImportError:
    pass
try:
    import pkg_resources
    _l_(64102)

except ImportError:
    pass
try:
    from pkg_resources import DistributionNotFound, VersionConflict
    _l_(64104)

except ImportError:
    pass

def should_install_requirement(requirement):
    _l_(64118)

    should_install = False
    _l_(64105)
    try:
        _l_(64115)

        _c_(64109, _a_(64107, _n_(64106, "pkg_resources", lambda: pkg_resources), "require"), _n_(64108, "requirement", lambda: requirement))
        _l_(64110)
    except (_n_(64111, "DistributionNotFound", lambda: DistributionNotFound), _n_(64112, "VersionConflict", lambda: VersionConflict)):
        _l_(64114)

        should_install = True
        _l_(64113)
    aux = _n_(64116, "should_install", lambda: should_install)
    _l_(64117)
    return aux


def install_packages(requirement_list):
    _l_(64146)

    try:
        _l_(64145)

        requirements = [
            _n_(64119, "requirement", lambda: requirement)
            for requirement in _n_(64120, "requirement_list", lambda: requirement_list)
            if _c_(64123, _n_(64121, "should_install_requirement", lambda: should_install_requirement), _n_(64122, "requirement", lambda: requirement))
        ]
        _l_(64124)
        if _c_(64127, _n_(64125, "len", lambda: len), _n_(64126, "requirements", lambda: requirements)) > 0:
            _l_(64138)

            _c_(64133, _a_(64129, _n_(64128, "subprocess", lambda: subprocess), "check_call"), [_a_(64131, _n_(64130, "sys", lambda: sys), "executable"), "-m", "pip", "install", *_n_(64132, "requirements", lambda: requirements)])
            _l_(64134)
        else:
            _c_(64136, _n_(64135, "print", lambda: print), "Requirements already satisfied.")
            _l_(64137)

    except _n_(64139, "Exception", lambda: Exception) as e:
        _l_(64144)

        _c_(64142, _n_(64140, "print", lambda: print), _n_(64141, "e", lambda: e))
        _l_(64143)

requirement_list = ['requests', 'httpx==0.18.2']
_l_(64147)
_c_(64150, _n_(64148, "install_packages", lambda: install_packages), _n_(64149, "requirement_list", lambda: requirement_list))
_l_(64151)

