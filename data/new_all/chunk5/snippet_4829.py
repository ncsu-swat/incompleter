# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42145686/issue-with-accessing-kivy-widgets-from-python-attributeerror-nonetype-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LoginScreen(_n_(655938, "Screen", lambda: Screen)):
    _l_(656004)

    spinner_bay = _c_(655939, ObjectProperty)#ListProperty()
    _l_(655940)#ListProperty()
    spinner_part_number = _c_(655941, ObjectProperty)#ListProperty()
    _l_(655942)#ListProperty()

    def __init__(self, **kwargs):
        _l_(655954)

        _c_(655948, _a_(655946, _n_(655943, "super", lambda: super)(_n_(655944, "LoginScreen", lambda: LoginScreen), _n_(655945, "self", lambda: self)), "__init__"), **_n_(655947, "kwargs", lambda: kwargs))
        _l_(655949)
        _c_(655952, _a_(655951, _n_(655950, "self", lambda: self), "load_login_view"))
        _l_(655953)

    def load_login_view(self):
        _l_(656003)

        _c_(655958, _n_(655955, "print", lambda: print), "Loading login screen ... " + _c_(655957, _n_(655956, "strftime", lambda: strftime), "%H:%M:%S"))
        _l_(655959)
        #Window.size = (300, 550) 

        PART_NUMBERS = []#ListProperty([])
        _l_(655960)#ListProperty([])
        BAY_NUMBERS = []#ListProperty([])
        _l_(655961)#ListProperty([])

        # Open configuration.txt file and find bay numbers & part numbers
        try:
            _l_(656002)

            config_file = _c_(655963, _n_(655962, "open", lambda: open), 'configuration.txt')
            _l_(655964)
            list_config_file = _c_(655967, _a_(655966, _n_(655965, "config_file", lambda: config_file), "readlines"))
            _l_(655968)
            #BAY_NUMBERS = bay_number_file.close
            _a_(655970, _n_(655969, "config_file", lambda: config_file), "close")
            _l_(655971)

            for line in _n_(655972, "list_config_file", lambda: list_config_file):
                _l_(655997)

                split_line = _c_(655975, _a_(655974, _n_(655973, "line", lambda: line), "split"), ' ')
                _l_(655976)
                _n_(655977, "split_line", lambda: split_line)[-1] = _c_(655980, _a_(655979, _n_(655978, "split_line", lambda: split_line)[-1], "strip"))
                _l_(655981)

                if 'PART_NUMBERS' in _n_(655982, "split_line", lambda: split_line):
                    _l_(655987)

                    _a_(655984, _n_(655983, "self", lambda: self), "spinner_part_number").values = _n_(655985, "split_line", lambda: split_line)[2:]
                    _l_(655986)

                if 'BAY_NUMBERS' in _n_(655988, "split_line", lambda: split_line):
                    _l_(655996)

                    #for i in range(int(split_line[2]), int(split_line[3]) + 1, 1):
                    _a_(655990, _n_(655989, "self", lambda: self), "spinner_bay").values = _n_(655991, "split_line", lambda: split_line)[2:]
                    _l_(655992)
                    _c_(655994, _n_(655993, "print", lambda: print), 'Loaded bay numbers.')
                    _l_(655995)
        except:
            _l_(656001)

            _c_(655999, _n_(655998, "print", lambda: print), "Error found.")
            _l_(656000)