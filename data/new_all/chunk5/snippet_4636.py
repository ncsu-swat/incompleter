# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53824369/script-working-fine-while-it-should-raise-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5.QtCore import *
    _l_(679418)

except ImportError:
    pass
try:
    from PyQt5.QtGui import *
    _l_(679420)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import *
    _l_(679422)

except ImportError:
    pass
try:
    from pynput.keyboard import Key, Listener
    _l_(679424)

except ImportError:
    pass
try:
    from itertools import combinations
    _l_(679426)

except ImportError:
    pass
try:
    import sys
    _l_(679428)

except ImportError:
    pass
try:
    import re
    _l_(679430)

except ImportError:
    pass

class Window(_n_(679431, "QMainWindow", lambda: QMainWindow)):
    _l_(679961)

    def __init__(self):
        _l_(679691)

        _c_(679436, _a_(679435, _n_(679432, "super", lambda: super)(_n_(679433, "Window", lambda: Window), _n_(679434, "self", lambda: self)), "__init__"))
        _l_(679437)

        ##BELOW DETECTS WHEN THE USER PRESS ENTER
        _n_(679438, "self", lambda: self).listener = _c_(679442, _n_(679439, "Listener", lambda: Listener), on_press=_a_(679441, _n_(679440, "self", lambda: self), "on_press"))
        _l_(679443)
        _c_(679447, _a_(679446, _a_(679445, _n_(679444, "self", lambda: self), "listener"), "start"))                               
        _l_(679448)                               
        _n_(679449, "self", lambda: self).listener1 = _c_(679453, _n_(679450, "Listener", lambda: Listener), on_press=_a_(679452, _n_(679451, "self", lambda: self), "on_press_top"))
        _l_(679454)

        ##CENTERING THE SCREEN
        def center(self):
            _l_(679478)

            qr = _c_(679457, _a_(679456, _n_(679455, "QMainWindow", lambda: QMainWindow), "frameGeometry"))
            _l_(679458)
            cp = _c_(679464, _a_(679463, _c_(679462, _a_(679461, _c_(679460, _n_(679459, "QDesktopWidget", lambda: QDesktopWidget)), "availableGeometry")), "center"))
            _l_(679465)
            _c_(679469, _a_(679467, _n_(679466, "qr", lambda: qr), "moveCenter"), _n_(679468, "cp", lambda: cp))
            _l_(679470)
            _c_(679476, _a_(679472, _n_(679471, "self", lambda: self), "move"), _c_(679475, _a_(679474, _n_(679473, "qr", lambda: qr), "topLeft")))
            _l_(679477)

        ##JUST GUI
        _c_(679481, _a_(679480, _n_(679479, "self", lambda: self), "setWindowTitle"), "Foo")
        _l_(679482)
        _c_(679485, _a_(679484, _n_(679483, "self", lambda: self), "setFixedSize"), 950, 710)
        _l_(679486)
        _c_(679489, _a_(679488, _n_(679487, "self", lambda: self), "setStyleSheet"), "background-color: rgb(119,136,153)")
        _l_(679490)
        _c_(679495, _a_(679492, _n_(679491, "QApplication", lambda: QApplication), "setOverrideCursor"), _a_(679494, _n_(679493, "Qt", lambda: Qt), "PointingHandCursor"))
        _l_(679496)

        ##SET -LINE EDIT
        _n_(679497, "self", lambda: self).kume_edit = _c_(679500, _n_(679498, "QLineEdit", lambda: QLineEdit), _n_(679499, "self", lambda: self))
        _l_(679501)
        _c_(679505, _a_(679504, _a_(679503, _n_(679502, "self", lambda: self), "kume_edit"), "setText"), "{")
        _l_(679506)
        _c_(679510, _a_(679509, _a_(679508, _n_(679507, "self", lambda: self), "kume_edit"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(679511)

        fnt = _c_(679515, _a_(679514, _a_(679513, _n_(679512, "self", lambda: self), "kume_edit"), "font"))
        _l_(679516)
        _c_(679519, _a_(679518, _n_(679517, "fnt", lambda: fnt), "setPointSize"), 15)
        _l_(679520)
        _c_(679525, _a_(679523, _a_(679522, _n_(679521, "self", lambda: self), "kume_edit"), "setFont"), _n_(679524, "fnt", lambda: fnt))
        _l_(679526)
        _c_(679530, _a_(679529, _a_(679528, _n_(679527, "self", lambda: self), "kume_edit"), "setGeometry"), 140, 300, 300, 30)
        _l_(679531)
        ##

        ##SET -LABEL
        _n_(679532, "self", lambda: self).kume_label = _c_(679535, _n_(679533, "QLabel", lambda: QLabel), _n_(679534, "self", lambda: self))
        _l_(679536)
        _c_(679540, _a_(679539, _a_(679538, _n_(679537, "self", lambda: self), "kume_label"), "setText"), "SET:")
        _l_(679541)
        _c_(679545, _a_(679544, _a_(679543, _n_(679542, "self", lambda: self), "kume_label"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(679546)

        fnt1 = _c_(679550, _a_(679549, _a_(679548, _n_(679547, "self", lambda: self), "kume_label"), "font"))
        _l_(679551)
        _c_(679554, _a_(679553, _n_(679552, "fnt1", lambda: fnt1), "setPointSize"), 15)
        _l_(679555)
        _c_(679560, _a_(679558, _a_(679557, _n_(679556, "self", lambda: self), "kume_label"), "setFont"), _n_(679559, "fnt1", lambda: fnt1))
        _l_(679561)
        _c_(679565, _a_(679564, _a_(679563, _n_(679562, "self", lambda: self), "kume_label"), "setGeometry"), 50, 300, 60, 32)
        _l_(679566)
        ##

        ##TOPOLOGY -LINE EDIT
        _n_(679567, "self", lambda: self).top_edit = _c_(679570, _n_(679568, "QLineEdit", lambda: QLineEdit), _n_(679569, "self", lambda: self))
        _l_(679571)
        _c_(679575, _a_(679574, _a_(679573, _n_(679572, "self", lambda: self), "top_edit"), "setText"), "{{")
        _l_(679576)
        _c_(679580, _a_(679579, _a_(679578, _n_(679577, "self", lambda: self), "top_edit"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(679581)

        fnt2 = _c_(679585, _a_(679584, _a_(679583, _n_(679582, "self", lambda: self), "top_edit"), "font"))
        _l_(679586)
        _c_(679589, _a_(679588, _n_(679587, "fnt2", lambda: fnt2), "setPointSize"), 15)
        _l_(679590)
        _c_(679595, _a_(679593, _a_(679592, _n_(679591, "self", lambda: self), "top_edit"), "setFont"), _n_(679594, "fnt2", lambda: fnt2))
        _l_(679596)
        _c_(679600, _a_(679599, _a_(679598, _n_(679597, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, 300, 30)
        _l_(679601)
        ##

        ##TOPOLOGY -LABEL
        _n_(679602, "self", lambda: self).topo_label = _c_(679605, _n_(679603, "QLabel", lambda: QLabel), _n_(679604, "self", lambda: self))
        _l_(679606)
        _c_(679610, _a_(679609, _a_(679608, _n_(679607, "self", lambda: self), "topo_label"), "setText"), "TOP:")
        _l_(679611)
        _c_(679615, _a_(679614, _a_(679613, _n_(679612, "self", lambda: self), "topo_label"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(679616)

        fnt3 = _c_(679620, _a_(679619, _a_(679618, _n_(679617, "self", lambda: self), "topo_label"), "font"))
        _l_(679621)
        _c_(679624, _a_(679623, _n_(679622, "fnt3", lambda: fnt3), "setPointSize"), 15)
        _l_(679625)
        _c_(679630, _a_(679628, _a_(679627, _n_(679626, "self", lambda: self), "topo_label"), "setFont"), _n_(679629, "fnt3", lambda: fnt3))
        _l_(679631)
        _c_(679635, _a_(679634, _a_(679633, _n_(679632, "self", lambda: self), "topo_label"), "setGeometry"), 50, 400, 80, 32)
        _l_(679636)
        ##

        ##FUNCTION CHANGES THIS LABEL WHEN THE DESIRED CONDITION OCCURS
        _n_(679637, "self", lambda: self).top_label = _c_(679640, _n_(679638, "QLabel", lambda: QLabel), _n_(679639, "self", lambda: self))
        _l_(679641)
        fnt4 = _c_(679645, _a_(679644, _a_(679643, _n_(679642, "self", lambda: self), "top_label"), "font"))
        _l_(679646)
        _c_(679649, _a_(679648, _n_(679647, "fnt4", lambda: fnt4), "setPointSize"), 15)
        _l_(679650)
        _c_(679655, _a_(679653, _a_(679652, _n_(679651, "self", lambda: self), "top_label"), "setFont"), _n_(679654, "fnt4", lambda: fnt4))
        _l_(679656)
        _c_(679660, _a_(679659, _a_(679658, _n_(679657, "self", lambda: self), "top_label"), "setGeometry"), 140, 450, 900, 30)
        _l_(679661)
        ##

        ##BUTTON SHOWS THAT THE PROGRAM WORKING FINE
        ##CLICK THIS BUTTON BEFORE AND AFTER YOU RUN
        but = _c_(679664, _n_(679662, "QPushButton", lambda: QPushButton), _n_(679663, "self", lambda: self))
        _l_(679665)
        _c_(679668, _a_(679667, _n_(679666, "but", lambda: but), "setGeometry"), 500,400,50,50)
        _l_(679669)
        _c_(679672, _a_(679671, _n_(679670, "but", lambda: but), "setText"), "Click Me")
        _l_(679673)
        _c_(679679, _a_(679676, _a_(679675, _n_(679674, "but", lambda: but), "clicked"), "connect"), _a_(679678, _n_(679677, "self", lambda: self), "but_test"))
        _l_(679680)
        _n_(679681, "self", lambda: self).count_test = 0
        _l_(679682)
        ##

        _n_(679683, "self", lambda: self).top_ = 0
        _l_(679684)
        _n_(679685, "self", lambda: self).kord_ = 300
        _l_(679686)

        _c_(679689, _a_(679688, _n_(679687, "self", lambda: self), "show"))
        _l_(679690)

    def but_test(self):
        _l_(679703)

        _n_(679692, "self", lambda: self).count_test += 1        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        _l_(679693)        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        _c_(679701, _a_(679696, _a_(679695, _n_(679694, "self", lambda: self), "top_label"), "setText"), _c_(679700, _a_(679697, "The program working fine {}", "format"), _a_(679699, _n_(679698, "self", lambda: self), "count_test")))
        _l_(679702)

    def on_press(self,key):
        _l_(679746)


        if _n_(679704, "key", lambda: key) == _a_(679706, _n_(679705, "Key", lambda: Key), "enter"):
            _l_(679745)



            if _c_(679710, _a_(679709, _a_(679708, _n_(679707, "self", lambda: self), "kume_edit"), "text"))[-1] == ",":
                _l_(679744)

                _c_(679718, _a_(679713, _a_(679712, _n_(679711, "self", lambda: self), "kume_edit"), "setText"), _c_(679717, _a_(679716, _a_(679715, _n_(679714, "self", lambda: self), "kume_edit"), "text"))[:-1] + "}")
                _l_(679719)
                _c_(679723, _a_(679722, _a_(679721, _n_(679720, "self", lambda: self), "kume_edit"), "setReadOnly"), True)
                _l_(679724)
                _c_(679728, _a_(679727, _a_(679726, _n_(679725, "self", lambda: self), "listener1"), "start"))
                _l_(679729)
                _c_(679733, _a_(679732, _a_(679731, _n_(679730, "self", lambda: self), "listener"), "stop"))
                _l_(679734)

            else:
                _c_(679742, _a_(679737, _a_(679736, _n_(679735, "self", lambda: self), "kume_edit"), "setText"), _c_(679741, _a_(679740, _a_(679739, _n_(679738, "self", lambda: self), "kume_edit"), "text")) + ",")
                _l_(679743)


    def on_press_top(self,key):
        _l_(679850)


        if _n_(679747, "key", lambda: key) == _a_(679749, _n_(679748, "Key", lambda: Key), "enter"):
            _l_(679849)

            _n_(679750, "self", lambda: self).top_ += 15
            _l_(679751)

            if _a_(679753, _n_(679752, "self", lambda: self), "top_") > 220:
                _l_(679763)

                _n_(679754, "self", lambda: self).kord_ += 15
                _l_(679755)
                _c_(679761, _a_(679758, _a_(679757, _n_(679756, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, _a_(679760, _n_(679759, "self", lambda: self), "kord_"), 30)
                _l_(679762)

            if _c_(679767, _a_(679766, _a_(679765, _n_(679764, "self", lambda: self), "top_edit"), "text"))[-1] == "{":
                _l_(679848)

                _c_(679775, _a_(679770, _a_(679769, _n_(679768, "self", lambda: self), "top_edit"), "setText"), _c_(679774, _a_(679773, _a_(679772, _n_(679771, "self", lambda: self), "top_edit"), "text"))[:-2])
                _l_(679776)
                _c_(679784, _a_(679779, _a_(679778, _n_(679777, "self", lambda: self), "top_edit"), "setText"), _c_(679783, _a_(679782, _a_(679781, _n_(679780, "self", lambda: self), "top_edit"), "text")) + "}")
                _l_(679785)
                _c_(679789, _a_(679788, _a_(679787, _n_(679786, "self", lambda: self), "top_edit"), "setReadOnly"), True)
                _l_(679790)

                _c_(679796, _a_(679793, _a_(679792, _n_(679791, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, _a_(679795, _n_(679794, "self", lambda: self), "kord_"), 30)
                _l_(679797)

                _c_(679800, _a_(679799, _n_(679798, "self", lambda: self), "topoloji_mi"))  #####################HERE THE FUNCTION IS CALLED - ONLY HERE
                _l_(679801)  #####################HERE THE FUNCTION IS CALLED - ONLY HERE

                _c_(679805, _a_(679804, _a_(679803, _n_(679802, "self", lambda: self), "listener1"), "stop"))
                _l_(679806)

            elif _c_(679810, _a_(679809, _a_(679808, _n_(679807, "self", lambda: self), "top_edit"), "text"))[-1] == ",":
                _l_(679847)

                _c_(679818, _a_(679813, _a_(679812, _n_(679811, "self", lambda: self), "top_edit"), "setText"), _c_(679817, _a_(679816, _a_(679815, _n_(679814, "self", lambda: self), "top_edit"), "text"))[:-1] + "}")
                _l_(679819)
                _c_(679827, _a_(679822, _a_(679821, _n_(679820, "self", lambda: self), "top_edit"), "setText"), _c_(679826, _a_(679825, _a_(679824, _n_(679823, "self", lambda: self), "top_edit"), "text")) + ",")
                _l_(679828)
                _c_(679836, _a_(679831, _a_(679830, _n_(679829, "self", lambda: self), "top_edit"), "setText"), _c_(679835, _a_(679834, _a_(679833, _n_(679832, "self", lambda: self), "top_edit"), "text")) + "{")
                _l_(679837)

            else:
                _c_(679845, _a_(679840, _a_(679839, _n_(679838, "self", lambda: self), "top_edit"), "setText"), _c_(679844, _a_(679843, _a_(679842, _n_(679841, "self", lambda: self), "top_edit"), "text")) + ",")
                _l_(679846)


    def kumetop(self):
        _l_(679901)

        reg = r"\{(.*?)\}"
        _l_(679851)
        matches = _c_(679859, _a_(679853, _n_(679852, "re", lambda: re), "findall"), _n_(679854, "reg", lambda: reg), _c_(679858, _a_(679857, _a_(679856, _n_(679855, "self", lambda: self), "top_edit"), "text"))[1:-1])
        _l_(679860)

        top_set = []
        _l_(679861)
        _c_(679866, _a_(679863, _n_(679862, "top_set", lambda: top_set), "append"), _c_(679865, _n_(679864, "set", lambda: set)))
        _l_(679867)
        for x in _n_(679868, "matches", lambda: matches):
            _l_(679878)

            _c_(679876, _a_(679870, _n_(679869, "top_set", lambda: top_set), "append"), _c_(679875, _n_(679871, "set", lambda: set), _c_(679874, _a_(679873, _n_(679872, "x", lambda: x), "split"), ",")))
            _l_(679877)

        kume_set = []
        _l_(679879)
        for x in _c_(679883, _a_(679882, _a_(679881, _n_(679880, "self", lambda: self), "kume_edit"), "text")):
            _l_(679897)

            if _c_(679886, _a_(679885, _n_(679884, "x", lambda: x), "isalnum")):
                _l_(679896)

                _c_(679894, _a_(679888, _n_(679887, "kume_set", lambda: kume_set), "append"), _c_(679893, _n_(679889, "set", lambda: set), _c_(679892, _a_(679891, _n_(679890, "x", lambda: x), "split"), ",")))
                _l_(679895)
        aux = _n_(679898, "kume_set", lambda: kume_set),_n_(679899, "top_set", lambda: top_set)
        _l_(679900)
        return aux

    def topoloji_mi(self):
        _l_(679956)

        kume_set,top_set = _c_(679904, _a_(679903, _n_(679902, "self", lambda: self), "kumetop")) ###TAKING THE LISTS
        _l_(679905) ###TAKING THE LISTS


        for x in _c_(679908, _n_(679906, "combinations", lambda: combinations), _n_(679907, "top_set", lambda: top_set), 2):
            _l_(679955)


            ################WHATS THIS
            _c_(679910, _n_(679909, "print", lambda: print), "IM A PRINT FUNCTION WORKING FINE") ###THIS PRINT WORKS
            _l_(679911) ###THIS PRINT WORKS
            _c_(679916, _n_(679912, "print", lambda: print), _c_(679915, _n_(679913, "list", lambda: list), _n_(679914, "y", lambda: y)))
            _l_(679917)
            del list(y)[0]               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            _l_(679918)               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            _c_(679923, _n_(679919, "print", lambda: print), _c_(679922, _n_(679920, "type", lambda: type), _n_(679921, "y", lambda: y)))              ###CLICK THE TEST BUTTON
            _l_(679924)              ###CLICK THE TEST BUTTON

            if _c_(679927, _n_(679925, "len", lambda: len), _n_(679926, "z", lambda: z)) == _c_(679932, _n_(679928, "len", lambda: len), _c_(679931, _n_(679929, "list", lambda: list), _n_(679930, "y", lambda: y))) and _c_(679945, _n_(679933, "all", lambda: all), [_c_(679937, _a_(679935, _n_(679934, "z", lambda: z), "count"), _n_(679936, "i", lambda: i)) == _c_(679943, _a_(679941, _c_(679940, _n_(679938, "list", lambda: list), _n_(679939, "y", lambda: y)), "count"), _n_(679942, "i", lambda: i)) for i in _n_(679944, "kume_set", lambda: kume_set)]):
                _l_(679954)

                _c_(679949, _a_(679948, _a_(679947, _n_(679946, "self", lambda: self), "top_label"), "setText"), "BLABLABLA")
                _l_(679950)
                _c_(679952, _n_(679951, "print", lambda: print), "IM NOT WORKING")
                _l_(679953)



    def close_application(self):
        _l_(679960)

        _c_(679958, _n_(679957, "sys_exit", lambda: sys_exit))
        _l_(679959)

def run():
    _l_(679977)

    app = _c_(679965, _n_(679962, "QApplication", lambda: QApplication), _a_(679964, _n_(679963, "sys", lambda: sys), "argv"))
    _l_(679966)
    GUI = _c_(679968, _n_(679967, "Window", lambda: Window))
    _l_(679969)
    _c_(679975, _a_(679971, _n_(679970, "sys", lambda: sys), "exit"), _c_(679974, _a_(679973, _n_(679972, "app", lambda: app), "exec_")))
    _l_(679976)

_c_(679979, _n_(679978, "run", lambda: run))
_l_(679980)