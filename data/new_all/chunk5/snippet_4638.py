# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53824369/script-working-fine-while-it-should-raise-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5.QtCore import *
    _l_(699590)

except ImportError:
    pass
try:
    from PyQt5.QtGui import *
    _l_(699592)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import *
    _l_(699594)

except ImportError:
    pass
try:
    from pynput.keyboard import Key, Listener
    _l_(699596)

except ImportError:
    pass
try:
    from itertools import combinations
    _l_(699598)

except ImportError:
    pass
try:
    import sys
    _l_(699600)

except ImportError:
    pass
try:
    import re
    _l_(699602)

except ImportError:
    pass

class Window(_n_(699603, "QMainWindow", lambda: QMainWindow)):
    _l_(700133)

    def __init__(self):
        _l_(699863)

        _c_(699608, _a_(699607, _n_(699604, "super", lambda: super)(_n_(699605, "Window", lambda: Window), _n_(699606, "self", lambda: self)), "__init__"))
        _l_(699609)

        ##BELOW DETECTS WHEN THE USER PRESS ENTER
        _n_(699610, "self", lambda: self).listener = _c_(699614, _n_(699611, "Listener", lambda: Listener), on_press=_a_(699613, _n_(699612, "self", lambda: self), "on_press"))
        _l_(699615)
        _c_(699619, _a_(699618, _a_(699617, _n_(699616, "self", lambda: self), "listener"), "start"))                               
        _l_(699620)                               
        _n_(699621, "self", lambda: self).listener1 = _c_(699625, _n_(699622, "Listener", lambda: Listener), on_press=_a_(699624, _n_(699623, "self", lambda: self), "on_press_top"))
        _l_(699626)

        ##CENTERING THE SCREEN
        def center(self):
            _l_(699650)

            qr = _c_(699629, _a_(699628, _n_(699627, "QMainWindow", lambda: QMainWindow), "frameGeometry"))
            _l_(699630)
            cp = _c_(699636, _a_(699635, _c_(699634, _a_(699633, _c_(699632, _n_(699631, "QDesktopWidget", lambda: QDesktopWidget)), "availableGeometry")), "center"))
            _l_(699637)
            _c_(699641, _a_(699639, _n_(699638, "qr", lambda: qr), "moveCenter"), _n_(699640, "cp", lambda: cp))
            _l_(699642)
            _c_(699648, _a_(699644, _n_(699643, "self", lambda: self), "move"), _c_(699647, _a_(699646, _n_(699645, "qr", lambda: qr), "topLeft")))
            _l_(699649)

        ##JUST GUI
        _c_(699653, _a_(699652, _n_(699651, "self", lambda: self), "setWindowTitle"), "Foo")
        _l_(699654)
        _c_(699657, _a_(699656, _n_(699655, "self", lambda: self), "setFixedSize"), 950, 710)
        _l_(699658)
        _c_(699661, _a_(699660, _n_(699659, "self", lambda: self), "setStyleSheet"), "background-color: rgb(119,136,153)")
        _l_(699662)
        _c_(699667, _a_(699664, _n_(699663, "QApplication", lambda: QApplication), "setOverrideCursor"), _a_(699666, _n_(699665, "Qt", lambda: Qt), "PointingHandCursor"))
        _l_(699668)

        ##SET -LINE EDIT
        _n_(699669, "self", lambda: self).kume_edit = _c_(699672, _n_(699670, "QLineEdit", lambda: QLineEdit), _n_(699671, "self", lambda: self))
        _l_(699673)
        _c_(699677, _a_(699676, _a_(699675, _n_(699674, "self", lambda: self), "kume_edit"), "setText"), "{")
        _l_(699678)
        _c_(699682, _a_(699681, _a_(699680, _n_(699679, "self", lambda: self), "kume_edit"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(699683)

        fnt = _c_(699687, _a_(699686, _a_(699685, _n_(699684, "self", lambda: self), "kume_edit"), "font"))
        _l_(699688)
        _c_(699691, _a_(699690, _n_(699689, "fnt", lambda: fnt), "setPointSize"), 15)
        _l_(699692)
        _c_(699697, _a_(699695, _a_(699694, _n_(699693, "self", lambda: self), "kume_edit"), "setFont"), _n_(699696, "fnt", lambda: fnt))
        _l_(699698)
        _c_(699702, _a_(699701, _a_(699700, _n_(699699, "self", lambda: self), "kume_edit"), "setGeometry"), 140, 300, 300, 30)
        _l_(699703)
        ##

        ##SET -LABEL
        _n_(699704, "self", lambda: self).kume_label = _c_(699707, _n_(699705, "QLabel", lambda: QLabel), _n_(699706, "self", lambda: self))
        _l_(699708)
        _c_(699712, _a_(699711, _a_(699710, _n_(699709, "self", lambda: self), "kume_label"), "setText"), "SET:")
        _l_(699713)
        _c_(699717, _a_(699716, _a_(699715, _n_(699714, "self", lambda: self), "kume_label"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(699718)

        fnt1 = _c_(699722, _a_(699721, _a_(699720, _n_(699719, "self", lambda: self), "kume_label"), "font"))
        _l_(699723)
        _c_(699726, _a_(699725, _n_(699724, "fnt1", lambda: fnt1), "setPointSize"), 15)
        _l_(699727)
        _c_(699732, _a_(699730, _a_(699729, _n_(699728, "self", lambda: self), "kume_label"), "setFont"), _n_(699731, "fnt1", lambda: fnt1))
        _l_(699733)
        _c_(699737, _a_(699736, _a_(699735, _n_(699734, "self", lambda: self), "kume_label"), "setGeometry"), 50, 300, 60, 32)
        _l_(699738)
        ##

        ##TOPOLOGY -LINE EDIT
        _n_(699739, "self", lambda: self).top_edit = _c_(699742, _n_(699740, "QLineEdit", lambda: QLineEdit), _n_(699741, "self", lambda: self))
        _l_(699743)
        _c_(699747, _a_(699746, _a_(699745, _n_(699744, "self", lambda: self), "top_edit"), "setText"), "{{")
        _l_(699748)
        _c_(699752, _a_(699751, _a_(699750, _n_(699749, "self", lambda: self), "top_edit"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(699753)

        fnt2 = _c_(699757, _a_(699756, _a_(699755, _n_(699754, "self", lambda: self), "top_edit"), "font"))
        _l_(699758)
        _c_(699761, _a_(699760, _n_(699759, "fnt2", lambda: fnt2), "setPointSize"), 15)
        _l_(699762)
        _c_(699767, _a_(699765, _a_(699764, _n_(699763, "self", lambda: self), "top_edit"), "setFont"), _n_(699766, "fnt2", lambda: fnt2))
        _l_(699768)
        _c_(699772, _a_(699771, _a_(699770, _n_(699769, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, 300, 30)
        _l_(699773)
        ##

        ##TOPOLOGY -LABEL
        _n_(699774, "self", lambda: self).topo_label = _c_(699777, _n_(699775, "QLabel", lambda: QLabel), _n_(699776, "self", lambda: self))
        _l_(699778)
        _c_(699782, _a_(699781, _a_(699780, _n_(699779, "self", lambda: self), "topo_label"), "setText"), "TOP:")
        _l_(699783)
        _c_(699787, _a_(699786, _a_(699785, _n_(699784, "self", lambda: self), "topo_label"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(699788)

        fnt3 = _c_(699792, _a_(699791, _a_(699790, _n_(699789, "self", lambda: self), "topo_label"), "font"))
        _l_(699793)
        _c_(699796, _a_(699795, _n_(699794, "fnt3", lambda: fnt3), "setPointSize"), 15)
        _l_(699797)
        _c_(699802, _a_(699800, _a_(699799, _n_(699798, "self", lambda: self), "topo_label"), "setFont"), _n_(699801, "fnt3", lambda: fnt3))
        _l_(699803)
        _c_(699807, _a_(699806, _a_(699805, _n_(699804, "self", lambda: self), "topo_label"), "setGeometry"), 50, 400, 80, 32)
        _l_(699808)
        ##

        ##FUNCTION CHANGES THIS LABEL WHEN THE DESIRED CONDITION OCCURS
        _n_(699809, "self", lambda: self).top_label = _c_(699812, _n_(699810, "QLabel", lambda: QLabel), _n_(699811, "self", lambda: self))
        _l_(699813)
        fnt4 = _c_(699817, _a_(699816, _a_(699815, _n_(699814, "self", lambda: self), "top_label"), "font"))
        _l_(699818)
        _c_(699821, _a_(699820, _n_(699819, "fnt4", lambda: fnt4), "setPointSize"), 15)
        _l_(699822)
        _c_(699827, _a_(699825, _a_(699824, _n_(699823, "self", lambda: self), "top_label"), "setFont"), _n_(699826, "fnt4", lambda: fnt4))
        _l_(699828)
        _c_(699832, _a_(699831, _a_(699830, _n_(699829, "self", lambda: self), "top_label"), "setGeometry"), 140, 450, 900, 30)
        _l_(699833)
        ##

        ##BUTTON SHOWS THAT THE PROGRAM WORKING FINE
        ##CLICK THIS BUTTON BEFORE AND AFTER YOU RUN
        but = _c_(699836, _n_(699834, "QPushButton", lambda: QPushButton), _n_(699835, "self", lambda: self))
        _l_(699837)
        _c_(699840, _a_(699839, _n_(699838, "but", lambda: but), "setGeometry"), 500,400,50,50)
        _l_(699841)
        _c_(699844, _a_(699843, _n_(699842, "but", lambda: but), "setText"), "Click Me")
        _l_(699845)
        _c_(699851, _a_(699848, _a_(699847, _n_(699846, "but", lambda: but), "clicked"), "connect"), _a_(699850, _n_(699849, "self", lambda: self), "but_test"))
        _l_(699852)
        _n_(699853, "self", lambda: self).count_test = 0
        _l_(699854)
        ##

        _n_(699855, "self", lambda: self).top_ = 0
        _l_(699856)
        _n_(699857, "self", lambda: self).kord_ = 300
        _l_(699858)

        _c_(699861, _a_(699860, _n_(699859, "self", lambda: self), "show"))
        _l_(699862)

    def but_test(self):
        _l_(699875)

        _n_(699864, "self", lambda: self).count_test += 1        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        _l_(699865)        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        _c_(699873, _a_(699868, _a_(699867, _n_(699866, "self", lambda: self), "top_label"), "setText"), _c_(699872, _a_(699869, "The program working fine {}", "format"), _a_(699871, _n_(699870, "self", lambda: self), "count_test")))
        _l_(699874)

    def on_press(self,key):
        _l_(699918)


        if _n_(699876, "key", lambda: key) == _a_(699878, _n_(699877, "Key", lambda: Key), "enter"):
            _l_(699917)



            if _c_(699882, _a_(699881, _a_(699880, _n_(699879, "self", lambda: self), "kume_edit"), "text"))[-1] == ",":
                _l_(699916)

                _c_(699890, _a_(699885, _a_(699884, _n_(699883, "self", lambda: self), "kume_edit"), "setText"), _c_(699889, _a_(699888, _a_(699887, _n_(699886, "self", lambda: self), "kume_edit"), "text"))[:-1] + "}")
                _l_(699891)
                _c_(699895, _a_(699894, _a_(699893, _n_(699892, "self", lambda: self), "kume_edit"), "setReadOnly"), True)
                _l_(699896)
                _c_(699900, _a_(699899, _a_(699898, _n_(699897, "self", lambda: self), "listener1"), "start"))
                _l_(699901)
                _c_(699905, _a_(699904, _a_(699903, _n_(699902, "self", lambda: self), "listener"), "stop"))
                _l_(699906)

            else:
                _c_(699914, _a_(699909, _a_(699908, _n_(699907, "self", lambda: self), "kume_edit"), "setText"), _c_(699913, _a_(699912, _a_(699911, _n_(699910, "self", lambda: self), "kume_edit"), "text")) + ",")
                _l_(699915)


    def on_press_top(self,key):
        _l_(700022)


        if _n_(699919, "key", lambda: key) == _a_(699921, _n_(699920, "Key", lambda: Key), "enter"):
            _l_(700021)

            _n_(699922, "self", lambda: self).top_ += 15
            _l_(699923)

            if _a_(699925, _n_(699924, "self", lambda: self), "top_") > 220:
                _l_(699935)

                _n_(699926, "self", lambda: self).kord_ += 15
                _l_(699927)
                _c_(699933, _a_(699930, _a_(699929, _n_(699928, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, _a_(699932, _n_(699931, "self", lambda: self), "kord_"), 30)
                _l_(699934)

            if _c_(699939, _a_(699938, _a_(699937, _n_(699936, "self", lambda: self), "top_edit"), "text"))[-1] == "{":
                _l_(700020)

                _c_(699947, _a_(699942, _a_(699941, _n_(699940, "self", lambda: self), "top_edit"), "setText"), _c_(699946, _a_(699945, _a_(699944, _n_(699943, "self", lambda: self), "top_edit"), "text"))[:-2])
                _l_(699948)
                _c_(699956, _a_(699951, _a_(699950, _n_(699949, "self", lambda: self), "top_edit"), "setText"), _c_(699955, _a_(699954, _a_(699953, _n_(699952, "self", lambda: self), "top_edit"), "text")) + "}")
                _l_(699957)
                _c_(699961, _a_(699960, _a_(699959, _n_(699958, "self", lambda: self), "top_edit"), "setReadOnly"), True)
                _l_(699962)

                _c_(699968, _a_(699965, _a_(699964, _n_(699963, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, _a_(699967, _n_(699966, "self", lambda: self), "kord_"), 30)
                _l_(699969)

                _c_(699972, _a_(699971, _n_(699970, "self", lambda: self), "topoloji_mi"))  #####################HERE THE FUNCTION IS CALLED - ONLY HERE
                _l_(699973)  #####################HERE THE FUNCTION IS CALLED - ONLY HERE

                _c_(699977, _a_(699976, _a_(699975, _n_(699974, "self", lambda: self), "listener1"), "stop"))
                _l_(699978)

            elif _c_(699982, _a_(699981, _a_(699980, _n_(699979, "self", lambda: self), "top_edit"), "text"))[-1] == ",":
                _l_(700019)

                _c_(699990, _a_(699985, _a_(699984, _n_(699983, "self", lambda: self), "top_edit"), "setText"), _c_(699989, _a_(699988, _a_(699987, _n_(699986, "self", lambda: self), "top_edit"), "text"))[:-1] + "}")
                _l_(699991)
                _c_(699999, _a_(699994, _a_(699993, _n_(699992, "self", lambda: self), "top_edit"), "setText"), _c_(699998, _a_(699997, _a_(699996, _n_(699995, "self", lambda: self), "top_edit"), "text")) + ",")
                _l_(700000)
                _c_(700008, _a_(700003, _a_(700002, _n_(700001, "self", lambda: self), "top_edit"), "setText"), _c_(700007, _a_(700006, _a_(700005, _n_(700004, "self", lambda: self), "top_edit"), "text")) + "{")
                _l_(700009)

            else:
                _c_(700017, _a_(700012, _a_(700011, _n_(700010, "self", lambda: self), "top_edit"), "setText"), _c_(700016, _a_(700015, _a_(700014, _n_(700013, "self", lambda: self), "top_edit"), "text")) + ",")
                _l_(700018)


    def kumetop(self):
        _l_(700073)

        reg = r"\{(.*?)\}"
        _l_(700023)
        matches = _c_(700031, _a_(700025, _n_(700024, "re", lambda: re), "findall"), _n_(700026, "reg", lambda: reg), _c_(700030, _a_(700029, _a_(700028, _n_(700027, "self", lambda: self), "top_edit"), "text"))[1:-1])
        _l_(700032)

        top_set = []
        _l_(700033)
        _c_(700038, _a_(700035, _n_(700034, "top_set", lambda: top_set), "append"), _c_(700037, _n_(700036, "set", lambda: set)))
        _l_(700039)
        for x in _n_(700040, "matches", lambda: matches):
            _l_(700050)

            _c_(700048, _a_(700042, _n_(700041, "top_set", lambda: top_set), "append"), _c_(700047, _n_(700043, "set", lambda: set), _c_(700046, _a_(700045, _n_(700044, "x", lambda: x), "split"), ",")))
            _l_(700049)

        kume_set = []
        _l_(700051)
        for x in _c_(700055, _a_(700054, _a_(700053, _n_(700052, "self", lambda: self), "kume_edit"), "text")):
            _l_(700069)

            if _c_(700058, _a_(700057, _n_(700056, "x", lambda: x), "isalnum")):
                _l_(700068)

                _c_(700066, _a_(700060, _n_(700059, "kume_set", lambda: kume_set), "append"), _c_(700065, _n_(700061, "set", lambda: set), _c_(700064, _a_(700063, _n_(700062, "x", lambda: x), "split"), ",")))
                _l_(700067)
        aux = _n_(700070, "kume_set", lambda: kume_set),_n_(700071, "top_set", lambda: top_set)
        _l_(700072)
        return aux

    def topoloji_mi(self):
        _l_(700128)

        kume_set,top_set = _c_(700076, _a_(700075, _n_(700074, "self", lambda: self), "kumetop")) ###TAKING THE LISTS
        _l_(700077) ###TAKING THE LISTS


        for x in _c_(700080, _n_(700078, "combinations", lambda: combinations), _n_(700079, "top_set", lambda: top_set), 2):
            _l_(700127)


            ################WHATS THIS
            _c_(700082, _n_(700081, "print", lambda: print), "IM A PRINT FUNCTION WORKING FINE") ###THIS PRINT WORKS
            _l_(700083) ###THIS PRINT WORKS
            _c_(700088, _n_(700084, "print", lambda: print), _c_(700087, _n_(700085, "list", lambda: list), _n_(700086, "y", lambda: y)))
            _l_(700089)
            del list(y)[0]               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            _l_(700090)               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            _c_(700095, _n_(700091, "print", lambda: print), _c_(700094, _n_(700092, "type", lambda: type), _n_(700093, "y", lambda: y)))              ###CLICK THE TEST BUTTON
            _l_(700096)              ###CLICK THE TEST BUTTON

            if _c_(700099, _n_(700097, "len", lambda: len), _n_(700098, "z", lambda: z)) == _c_(700104, _n_(700100, "len", lambda: len), _c_(700103, _n_(700101, "list", lambda: list), _n_(700102, "y", lambda: y))) and _c_(700117, _n_(700105, "all", lambda: all), [_c_(700109, _a_(700107, _n_(700106, "z", lambda: z), "count"), _n_(700108, "i", lambda: i)) == _c_(700115, _a_(700113, _c_(700112, _n_(700110, "list", lambda: list), _n_(700111, "y", lambda: y)), "count"), _n_(700114, "i", lambda: i)) for i in _n_(700116, "kume_set", lambda: kume_set)]):
                _l_(700126)

                _c_(700121, _a_(700120, _a_(700119, _n_(700118, "self", lambda: self), "top_label"), "setText"), "BLABLABLA")
                _l_(700122)
                _c_(700124, _n_(700123, "print", lambda: print), "IM NOT WORKING")
                _l_(700125)



    def close_application(self):
        _l_(700132)

        _c_(700130, _n_(700129, "sys_exit", lambda: sys_exit))
        _l_(700131)

def run():
    _l_(700149)

    app = _c_(700137, _n_(700134, "QApplication", lambda: QApplication), _a_(700136, _n_(700135, "sys", lambda: sys), "argv"))
    _l_(700138)
    GUI = _c_(700140, _n_(700139, "Window", lambda: Window))
    _l_(700141)
    _c_(700147, _a_(700143, _n_(700142, "sys", lambda: sys), "exit"), _c_(700146, _a_(700145, _n_(700144, "app", lambda: app), "exec_")))
    _l_(700148)

_c_(700151, _n_(700150, "run", lambda: run))
_l_(700152)