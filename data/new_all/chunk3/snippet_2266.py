# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54274442/module-imported-in-one-function-nameerror-in-another-function-called-afterward
#!/usr/bin/python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import importlib.util
    _l_(524236)

except ImportError:
    pass
try:
    from subprocess import Popen, PIPE, STDOUT
    _l_(524238)

except ImportError:
    pass
try:
    import sys
    _l_(524240)

except ImportError:
    pass
try:
    import subprocess
    _l_(524242)

except ImportError:
    pass
try:
    import time
    _l_(524244)

except ImportError:
    pass


accessToken                 = 'ABC'
_l_(524245)
dropletName                 = 'newDropletAndTag'
_l_(524246)
tagName                     = _n_(524247, "dropletName", lambda: dropletName)
_l_(524248)

def Install():
    _l_(524250)

    pass
    _l_(524249)


def CreateDroplet():
    _l_(524258)

    newDroplet = _c_(524256, _a_(524252, _n_(524251, "digitalocean", lambda: digitalocean), "Droplet"), token       = _n_(524253, "accessToken", lambda: accessToken), 
                                        name        = _n_(524254, "dropletName", lambda: dropletName),
                                        region      = 'NYC1',
                                        image       = 'ubuntu-16-04-x64',
                                        size_slug   = 's-1vcpu-1gb',
                                        ssh_keys    = _n_(524255, "sshKeysList", lambda: sshKeysList), 
                                        backups     = False
                                        )    
    _l_(524257)    

def Run():
    _l_(524277)

    try:
        import digitalocean
        _l_(524260)

    except ImportError:
        pass
    myManager = _c_(524264, _a_(524262, _n_(524261, "digitalocean", lambda: digitalocean), "Manager"), token=_n_(524263, "accessToken", lambda: accessToken))
    _l_(524265)
    myDroplets = _c_(524269, _a_(524267, _n_(524266, "myManager", lambda: myManager), "get_all_droplets"), tag_name=_n_(524268, "tagName", lambda: tagName))
    _l_(524270)

    _c_(524272, _n_(524271, "Install", lambda: Install)) 
    _l_(524273) 
    _c_(524275, _n_(524274, "CreateDroplet", lambda: CreateDroplet))
    _l_(524276)


def Main():
    _l_(524293)

    #START OF SCRIPT
    _c_(524279, _n_(524278, "print", lambda: print), '\n\n\n')
    _l_(524280)
    _c_(524282, _n_(524281, "print", lambda: print), '---- Start Of Script ----')
    _l_(524283)
    _c_(524285, _n_(524284, "Run", lambda: Run))
    _l_(524286)
    _c_(524288, _n_(524287, "print", lambda: print), '---- End Of Script ----')
    _l_(524289)
    _c_(524291, _n_(524290, "print", lambda: print), '\n\n\n')
    _l_(524292)
if _n_(524294, "__name__", lambda: __name__) == '__main__':
    _l_(524298)

    _c_(524296, _n_(524295, "Main", lambda: Main))
    _l_(524297)