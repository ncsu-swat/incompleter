# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71753625/python-subprocess-call-file-not-found-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import minecraft_launcher_lib
    _l_(475049)

except ImportError:
    pass
try:
    import subprocess
    _l_(475051)

except ImportError:
    pass

minecraft_directory = "C:\\Users\\Mert KAPLANDAR\\AppData\\Roaming\\.minecraft"
_l_(475052)

options = _c_(475056, _a_(475055, _a_(475054, _n_(475053, "minecraft_launcher_lib", lambda: minecraft_launcher_lib), "utils"), "generate_test_options"))
_l_(475057)

minecraft_command = _c_(475063, _a_(475060, _a_(475059, _n_(475058, "minecraft_launcher_lib", lambda: minecraft_launcher_lib), "command"), "get_minecraft_command"), "1.8.9", _n_(475061, "minecraft_directory", lambda: minecraft_directory), _n_(475062, "options", lambda: options))
_l_(475064)

_c_(475068, _a_(475066, _n_(475065, "subprocess", lambda: subprocess), "call"), _n_(475067, "minecraft_command", lambda: minecraft_command))
_l_(475069)