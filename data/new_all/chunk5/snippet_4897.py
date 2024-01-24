# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42145686/issue-with-accessing-kivy-widgets-from-python-attributeerror-nonetype-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LoginScreen(_n_(694671, "Screen", lambda: Screen)):
    _l_(694737)

    spinner_bay = _c_(694672, ObjectProperty)#ListProperty()
    _l_(694673)#ListProperty()
    spinner_part_number = _c_(694674, ObjectProperty)#ListProperty()
    _l_(694675)#ListProperty()

    def __init__(self, **kwargs):
        _l_(694687)

        _c_(694681, _a_(694679, _n_(694676, "super", lambda: super)(_n_(694677, "LoginScreen", lambda: LoginScreen), _n_(694678, "self", lambda: self)), "__init__"), **_n_(694680, "kwargs", lambda: kwargs))
        _l_(694682)
        _c_(694685, _a_(694684, _n_(694683, "self", lambda: self), "load_login_view"))
        _l_(694686)

    def load_login_view(self):
        _l_(694736)

        _c_(694691, _n_(694688, "print", lambda: print), "Loading login screen ... " + _c_(694690, _n_(694689, "strftime", lambda: strftime), "%H:%M:%S"))
        _l_(694692)
        #Window.size = (300, 550) 

        PART_NUMBERS = []#ListProperty([])
        _l_(694693)#ListProperty([])
        BAY_NUMBERS = []#ListProperty([])
        _l_(694694)#ListProperty([])

        # Open configuration.txt file and find bay numbers & part numbers
        try:
            _l_(694735)

            config_file = _c_(694696, _n_(694695, "open", lambda: open), 'configuration.txt')
            _l_(694697)
            list_config_file = _c_(694700, _a_(694699, _n_(694698, "config_file", lambda: config_file), "readlines"))
            _l_(694701)
            #BAY_NUMBERS = bay_number_file.close
            _a_(694703, _n_(694702, "config_file", lambda: config_file), "close")
            _l_(694704)

            for line in _n_(694705, "list_config_file", lambda: list_config_file):
                _l_(694730)

                split_line = _c_(694708, _a_(694707, _n_(694706, "line", lambda: line), "split"), ' ')
                _l_(694709)
                _n_(694710, "split_line", lambda: split_line)[-1] = _c_(694713, _a_(694712, _n_(694711, "split_line", lambda: split_line)[-1], "strip"))
                _l_(694714)

                if 'PART_NUMBERS' in _n_(694715, "split_line", lambda: split_line):
                    _l_(694720)

                    _a_(694717, _n_(694716, "self", lambda: self), "spinner_part_number").values = _n_(694718, "split_line", lambda: split_line)[2:]
                    _l_(694719)

                if 'BAY_NUMBERS' in _n_(694721, "split_line", lambda: split_line):
                    _l_(694729)

                    #for i in range(int(split_line[2]), int(split_line[3]) + 1, 1):
                    _a_(694723, _n_(694722, "self", lambda: self), "spinner_bay").values = _n_(694724, "split_line", lambda: split_line)[2:]
                    _l_(694725)
                    _c_(694727, _n_(694726, "print", lambda: print), 'Loaded bay numbers.')
                    _l_(694728)
        except:
            _l_(694734)

            _c_(694732, _n_(694731, "print", lambda: print), "Error found.")
            _l_(694733)