# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68342294/what-is-the-cause-of-this-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import utils
    _l_(446888)

except ImportError:
    pass
try:
    import remote_exec
    _l_(446890)

except ImportError:
    pass
try:
    import post
    _l_(446892)

except ImportError:
    pass
try:
    import get
    _l_(446894)

except ImportError:
    pass
try:
    import error_handler
    _l_(446896)

except ImportError:
    pass
try:
    import os
    _l_(446898)

except ImportError:
    pass
try:
    import handle_space
    _l_(446900)

except ImportError:
    pass
try:
    import socket
    _l_(446902)

except ImportError:
    pass
try:
    import json
    _l_(446904)

except ImportError:
    pass
try:
    from requests import get
    _l_(446906)

except ImportError:
    pass
try:
    import sys
    _l_(446908)

except ImportError:
    pass
try:
    import temp
    _l_(446910)

except ImportError:
    pass

def only_dest_requires_jumpserver():
    _l_(446966)

    try:
        _l_(446965)

        dictionary = {
            "migration_type": _c_(446913, _a_(446912, _n_(446911, "utils", lambda: utils), "config_data"))["source_cloud"] + " to " + _c_(446916, _a_(446915, _n_(446914, "utils", lambda: utils), "config_data"))["dest_cloud"]
        }
        _l_(446917)

        _c_(446921, _a_(446919, _n_(446918, "utils", lambda: utils), "update_config_file"), _n_(446920, "dictionary", lambda: dictionary))
        _l_(446922)
        _c_(446930, _n_(446923, "print", lambda: print), "\nInitialising " + _c_(446926, _a_(446925, _n_(446924, "utils", lambda: utils), "config_data"))["source_cloud"] + " to " + _c_(446929, _a_(446928, _n_(446927, "utils", lambda: utils), "config_data"))["dest_cloud"] + " migration...")
        _l_(446931)
        hostname = _c_(446934, _a_(446933, _n_(446932, "socket", lambda: socket), "gethostname"))
        _l_(446935)

        if _n_(446936, "hostname", lambda: hostname) == _c_(446939, _a_(446938, _n_(446937, "utils", lambda: utils), "config_data"))["my_hostname"]:
            _l_(446950)

            # get.call_get()
            _c_(446942, _a_(446941, _n_(446940, "temp", lambda: temp), "func"))
            _l_(446943)
            _c_(446945, _n_(446944, "print", lambda: print), "\nData successfully exported from source to this machine.\nChecking for space availability at jumpserver...")
            _l_(446946)
            _c_(446948, _n_(446947, "print", lambda: print), "Done!")
            _l_(446949)
    except _n_(446951, "Exception", lambda: Exception) as error:
        _l_(446964)

        filename = _c_(446956, _a_(446954, _a_(446953, _n_(446952, "os", lambda: os), "path"), "basename"), _n_(446955, "__file__", lambda: __file__))
        _l_(446957)
        _c_(446962, _a_(446959, _n_(446958, "error_handler", lambda: error_handler), "print_exception_message"), _n_(446960, "error", lambda: error), _n_(446961, "filename", lambda: filename))
        _l_(446963)