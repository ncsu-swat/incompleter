# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53824369/script-working-fine-while-it-should-raise-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5.QtCore import *
    _l_(696091)

except ImportError:
    pass
try:
    from PyQt5.QtGui import *
    _l_(696093)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import *
    _l_(696095)

except ImportError:
    pass
try:
    from pynput.keyboard import Key, Listener
    _l_(696097)

except ImportError:
    pass
try:
    from itertools import combinations
    _l_(696099)

except ImportError:
    pass
try:
    import sys
    _l_(696101)

except ImportError:
    pass
try:
    import re
    _l_(696103)

except ImportError:
    pass

class Window(_n_(696104, "QMainWindow", lambda: QMainWindow)):
    _l_(696634)

    def __init__(self):
        _l_(696364)

        _c_(696109, _a_(696108, _n_(696105, "super", lambda: super)(_n_(696106, "Window", lambda: Window), _n_(696107, "self", lambda: self)), "__init__"))
        _l_(696110)

        ##BELOW DETECTS WHEN THE USER PRESS ENTER
        _n_(696111, "self", lambda: self).listener = _c_(696115, _n_(696112, "Listener", lambda: Listener), on_press=_a_(696114, _n_(696113, "self", lambda: self), "on_press"))
        _l_(696116)
        _c_(696120, _a_(696119, _a_(696118, _n_(696117, "self", lambda: self), "listener"), "start"))                               
        _l_(696121)                               
        _n_(696122, "self", lambda: self).listener1 = _c_(696126, _n_(696123, "Listener", lambda: Listener), on_press=_a_(696125, _n_(696124, "self", lambda: self), "on_press_top"))
        _l_(696127)

        ##CENTERING THE SCREEN
        def center(self):
            _l_(696151)

            qr = _c_(696130, _a_(696129, _n_(696128, "QMainWindow", lambda: QMainWindow), "frameGeometry"))
            _l_(696131)
            cp = _c_(696137, _a_(696136, _c_(696135, _a_(696134, _c_(696133, _n_(696132, "QDesktopWidget", lambda: QDesktopWidget)), "availableGeometry")), "center"))
            _l_(696138)
            _c_(696142, _a_(696140, _n_(696139, "qr", lambda: qr), "moveCenter"), _n_(696141, "cp", lambda: cp))
            _l_(696143)
            _c_(696149, _a_(696145, _n_(696144, "self", lambda: self), "move"), _c_(696148, _a_(696147, _n_(696146, "qr", lambda: qr), "topLeft")))
            _l_(696150)

        ##JUST GUI
        _c_(696154, _a_(696153, _n_(696152, "self", lambda: self), "setWindowTitle"), "Foo")
        _l_(696155)
        _c_(696158, _a_(696157, _n_(696156, "self", lambda: self), "setFixedSize"), 950, 710)
        _l_(696159)
        _c_(696162, _a_(696161, _n_(696160, "self", lambda: self), "setStyleSheet"), "background-color: rgb(119,136,153)")
        _l_(696163)
        _c_(696168, _a_(696165, _n_(696164, "QApplication", lambda: QApplication), "setOverrideCursor"), _a_(696167, _n_(696166, "Qt", lambda: Qt), "PointingHandCursor"))
        _l_(696169)

        ##SET -LINE EDIT
        _n_(696170, "self", lambda: self).kume_edit = _c_(696173, _n_(696171, "QLineEdit", lambda: QLineEdit), _n_(696172, "self", lambda: self))
        _l_(696174)
        _c_(696178, _a_(696177, _a_(696176, _n_(696175, "self", lambda: self), "kume_edit"), "setText"), "{")
        _l_(696179)
        _c_(696183, _a_(696182, _a_(696181, _n_(696180, "self", lambda: self), "kume_edit"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(696184)

        fnt = _c_(696188, _a_(696187, _a_(696186, _n_(696185, "self", lambda: self), "kume_edit"), "font"))
        _l_(696189)
        _c_(696192, _a_(696191, _n_(696190, "fnt", lambda: fnt), "setPointSize"), 15)
        _l_(696193)
        _c_(696198, _a_(696196, _a_(696195, _n_(696194, "self", lambda: self), "kume_edit"), "setFont"), _n_(696197, "fnt", lambda: fnt))
        _l_(696199)
        _c_(696203, _a_(696202, _a_(696201, _n_(696200, "self", lambda: self), "kume_edit"), "setGeometry"), 140, 300, 300, 30)
        _l_(696204)
        ##

        ##SET -LABEL
        _n_(696205, "self", lambda: self).kume_label = _c_(696208, _n_(696206, "QLabel", lambda: QLabel), _n_(696207, "self", lambda: self))
        _l_(696209)
        _c_(696213, _a_(696212, _a_(696211, _n_(696210, "self", lambda: self), "kume_label"), "setText"), "SET:")
        _l_(696214)
        _c_(696218, _a_(696217, _a_(696216, _n_(696215, "self", lambda: self), "kume_label"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(696219)

        fnt1 = _c_(696223, _a_(696222, _a_(696221, _n_(696220, "self", lambda: self), "kume_label"), "font"))
        _l_(696224)
        _c_(696227, _a_(696226, _n_(696225, "fnt1", lambda: fnt1), "setPointSize"), 15)
        _l_(696228)
        _c_(696233, _a_(696231, _a_(696230, _n_(696229, "self", lambda: self), "kume_label"), "setFont"), _n_(696232, "fnt1", lambda: fnt1))
        _l_(696234)
        _c_(696238, _a_(696237, _a_(696236, _n_(696235, "self", lambda: self), "kume_label"), "setGeometry"), 50, 300, 60, 32)
        _l_(696239)
        ##

        ##TOPOLOGY -LINE EDIT
        _n_(696240, "self", lambda: self).top_edit = _c_(696243, _n_(696241, "QLineEdit", lambda: QLineEdit), _n_(696242, "self", lambda: self))
        _l_(696244)
        _c_(696248, _a_(696247, _a_(696246, _n_(696245, "self", lambda: self), "top_edit"), "setText"), "{{")
        _l_(696249)
        _c_(696253, _a_(696252, _a_(696251, _n_(696250, "self", lambda: self), "top_edit"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(696254)

        fnt2 = _c_(696258, _a_(696257, _a_(696256, _n_(696255, "self", lambda: self), "top_edit"), "font"))
        _l_(696259)
        _c_(696262, _a_(696261, _n_(696260, "fnt2", lambda: fnt2), "setPointSize"), 15)
        _l_(696263)
        _c_(696268, _a_(696266, _a_(696265, _n_(696264, "self", lambda: self), "top_edit"), "setFont"), _n_(696267, "fnt2", lambda: fnt2))
        _l_(696269)
        _c_(696273, _a_(696272, _a_(696271, _n_(696270, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, 300, 30)
        _l_(696274)
        ##

        ##TOPOLOGY -LABEL
        _n_(696275, "self", lambda: self).topo_label = _c_(696278, _n_(696276, "QLabel", lambda: QLabel), _n_(696277, "self", lambda: self))
        _l_(696279)
        _c_(696283, _a_(696282, _a_(696281, _n_(696280, "self", lambda: self), "topo_label"), "setText"), "TOP:")
        _l_(696284)
        _c_(696288, _a_(696287, _a_(696286, _n_(696285, "self", lambda: self), "topo_label"), "setStyleSheet"), "QLineEdit{ background-color: orange; color: blue; font: 11 }")
        _l_(696289)

        fnt3 = _c_(696293, _a_(696292, _a_(696291, _n_(696290, "self", lambda: self), "topo_label"), "font"))
        _l_(696294)
        _c_(696297, _a_(696296, _n_(696295, "fnt3", lambda: fnt3), "setPointSize"), 15)
        _l_(696298)
        _c_(696303, _a_(696301, _a_(696300, _n_(696299, "self", lambda: self), "topo_label"), "setFont"), _n_(696302, "fnt3", lambda: fnt3))
        _l_(696304)
        _c_(696308, _a_(696307, _a_(696306, _n_(696305, "self", lambda: self), "topo_label"), "setGeometry"), 50, 400, 80, 32)
        _l_(696309)
        ##

        ##FUNCTION CHANGES THIS LABEL WHEN THE DESIRED CONDITION OCCURS
        _n_(696310, "self", lambda: self).top_label = _c_(696313, _n_(696311, "QLabel", lambda: QLabel), _n_(696312, "self", lambda: self))
        _l_(696314)
        fnt4 = _c_(696318, _a_(696317, _a_(696316, _n_(696315, "self", lambda: self), "top_label"), "font"))
        _l_(696319)
        _c_(696322, _a_(696321, _n_(696320, "fnt4", lambda: fnt4), "setPointSize"), 15)
        _l_(696323)
        _c_(696328, _a_(696326, _a_(696325, _n_(696324, "self", lambda: self), "top_label"), "setFont"), _n_(696327, "fnt4", lambda: fnt4))
        _l_(696329)
        _c_(696333, _a_(696332, _a_(696331, _n_(696330, "self", lambda: self), "top_label"), "setGeometry"), 140, 450, 900, 30)
        _l_(696334)
        ##

        ##BUTTON SHOWS THAT THE PROGRAM WORKING FINE
        ##CLICK THIS BUTTON BEFORE AND AFTER YOU RUN
        but = _c_(696337, _n_(696335, "QPushButton", lambda: QPushButton), _n_(696336, "self", lambda: self))
        _l_(696338)
        _c_(696341, _a_(696340, _n_(696339, "but", lambda: but), "setGeometry"), 500,400,50,50)
        _l_(696342)
        _c_(696345, _a_(696344, _n_(696343, "but", lambda: but), "setText"), "Click Me")
        _l_(696346)
        _c_(696352, _a_(696349, _a_(696348, _n_(696347, "but", lambda: but), "clicked"), "connect"), _a_(696351, _n_(696350, "self", lambda: self), "but_test"))
        _l_(696353)
        _n_(696354, "self", lambda: self).count_test = 0
        _l_(696355)
        ##

        _n_(696356, "self", lambda: self).top_ = 0
        _l_(696357)
        _n_(696358, "self", lambda: self).kord_ = 300
        _l_(696359)

        _c_(696362, _a_(696361, _n_(696360, "self", lambda: self), "show"))
        _l_(696363)

    def but_test(self):
        _l_(696376)

        _n_(696365, "self", lambda: self).count_test += 1        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        _l_(696366)        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        _c_(696374, _a_(696369, _a_(696368, _n_(696367, "self", lambda: self), "top_label"), "setText"), _c_(696373, _a_(696370, "The program working fine {}", "format"), _a_(696372, _n_(696371, "self", lambda: self), "count_test")))
        _l_(696375)

    def on_press(self,key):
        _l_(696419)


        if _n_(696377, "key", lambda: key) == _a_(696379, _n_(696378, "Key", lambda: Key), "enter"):
            _l_(696418)



            if _c_(696383, _a_(696382, _a_(696381, _n_(696380, "self", lambda: self), "kume_edit"), "text"))[-1] == ",":
                _l_(696417)

                _c_(696391, _a_(696386, _a_(696385, _n_(696384, "self", lambda: self), "kume_edit"), "setText"), _c_(696390, _a_(696389, _a_(696388, _n_(696387, "self", lambda: self), "kume_edit"), "text"))[:-1] + "}")
                _l_(696392)
                _c_(696396, _a_(696395, _a_(696394, _n_(696393, "self", lambda: self), "kume_edit"), "setReadOnly"), True)
                _l_(696397)
                _c_(696401, _a_(696400, _a_(696399, _n_(696398, "self", lambda: self), "listener1"), "start"))
                _l_(696402)
                _c_(696406, _a_(696405, _a_(696404, _n_(696403, "self", lambda: self), "listener"), "stop"))
                _l_(696407)

            else:
                _c_(696415, _a_(696410, _a_(696409, _n_(696408, "self", lambda: self), "kume_edit"), "setText"), _c_(696414, _a_(696413, _a_(696412, _n_(696411, "self", lambda: self), "kume_edit"), "text")) + ",")
                _l_(696416)


    def on_press_top(self,key):
        _l_(696523)


        if _n_(696420, "key", lambda: key) == _a_(696422, _n_(696421, "Key", lambda: Key), "enter"):
            _l_(696522)

            _n_(696423, "self", lambda: self).top_ += 15
            _l_(696424)

            if _a_(696426, _n_(696425, "self", lambda: self), "top_") > 220:
                _l_(696436)

                _n_(696427, "self", lambda: self).kord_ += 15
                _l_(696428)
                _c_(696434, _a_(696431, _a_(696430, _n_(696429, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, _a_(696433, _n_(696432, "self", lambda: self), "kord_"), 30)
                _l_(696435)

            if _c_(696440, _a_(696439, _a_(696438, _n_(696437, "self", lambda: self), "top_edit"), "text"))[-1] == "{":
                _l_(696521)

                _c_(696448, _a_(696443, _a_(696442, _n_(696441, "self", lambda: self), "top_edit"), "setText"), _c_(696447, _a_(696446, _a_(696445, _n_(696444, "self", lambda: self), "top_edit"), "text"))[:-2])
                _l_(696449)
                _c_(696457, _a_(696452, _a_(696451, _n_(696450, "self", lambda: self), "top_edit"), "setText"), _c_(696456, _a_(696455, _a_(696454, _n_(696453, "self", lambda: self), "top_edit"), "text")) + "}")
                _l_(696458)
                _c_(696462, _a_(696461, _a_(696460, _n_(696459, "self", lambda: self), "top_edit"), "setReadOnly"), True)
                _l_(696463)

                _c_(696469, _a_(696466, _a_(696465, _n_(696464, "self", lambda: self), "top_edit"), "setGeometry"), 140, 400, _a_(696468, _n_(696467, "self", lambda: self), "kord_"), 30)
                _l_(696470)

                _c_(696473, _a_(696472, _n_(696471, "self", lambda: self), "topoloji_mi"))  #####################HERE THE FUNCTION IS CALLED - ONLY HERE
                _l_(696474)  #####################HERE THE FUNCTION IS CALLED - ONLY HERE

                _c_(696478, _a_(696477, _a_(696476, _n_(696475, "self", lambda: self), "listener1"), "stop"))
                _l_(696479)

            elif _c_(696483, _a_(696482, _a_(696481, _n_(696480, "self", lambda: self), "top_edit"), "text"))[-1] == ",":
                _l_(696520)

                _c_(696491, _a_(696486, _a_(696485, _n_(696484, "self", lambda: self), "top_edit"), "setText"), _c_(696490, _a_(696489, _a_(696488, _n_(696487, "self", lambda: self), "top_edit"), "text"))[:-1] + "}")
                _l_(696492)
                _c_(696500, _a_(696495, _a_(696494, _n_(696493, "self", lambda: self), "top_edit"), "setText"), _c_(696499, _a_(696498, _a_(696497, _n_(696496, "self", lambda: self), "top_edit"), "text")) + ",")
                _l_(696501)
                _c_(696509, _a_(696504, _a_(696503, _n_(696502, "self", lambda: self), "top_edit"), "setText"), _c_(696508, _a_(696507, _a_(696506, _n_(696505, "self", lambda: self), "top_edit"), "text")) + "{")
                _l_(696510)

            else:
                _c_(696518, _a_(696513, _a_(696512, _n_(696511, "self", lambda: self), "top_edit"), "setText"), _c_(696517, _a_(696516, _a_(696515, _n_(696514, "self", lambda: self), "top_edit"), "text")) + ",")
                _l_(696519)


    def kumetop(self):
        _l_(696574)

        reg = r"\{(.*?)\}"
        _l_(696524)
        matches = _c_(696532, _a_(696526, _n_(696525, "re", lambda: re), "findall"), _n_(696527, "reg", lambda: reg), _c_(696531, _a_(696530, _a_(696529, _n_(696528, "self", lambda: self), "top_edit"), "text"))[1:-1])
        _l_(696533)

        top_set = []
        _l_(696534)
        _c_(696539, _a_(696536, _n_(696535, "top_set", lambda: top_set), "append"), _c_(696538, _n_(696537, "set", lambda: set)))
        _l_(696540)
        for x in _n_(696541, "matches", lambda: matches):
            _l_(696551)

            _c_(696549, _a_(696543, _n_(696542, "top_set", lambda: top_set), "append"), _c_(696548, _n_(696544, "set", lambda: set), _c_(696547, _a_(696546, _n_(696545, "x", lambda: x), "split"), ",")))
            _l_(696550)

        kume_set = []
        _l_(696552)
        for x in _c_(696556, _a_(696555, _a_(696554, _n_(696553, "self", lambda: self), "kume_edit"), "text")):
            _l_(696570)

            if _c_(696559, _a_(696558, _n_(696557, "x", lambda: x), "isalnum")):
                _l_(696569)

                _c_(696567, _a_(696561, _n_(696560, "kume_set", lambda: kume_set), "append"), _c_(696566, _n_(696562, "set", lambda: set), _c_(696565, _a_(696564, _n_(696563, "x", lambda: x), "split"), ",")))
                _l_(696568)
        aux = _n_(696571, "kume_set", lambda: kume_set),_n_(696572, "top_set", lambda: top_set)
        _l_(696573)
        return aux

    def topoloji_mi(self):
        _l_(696629)

        kume_set,top_set = _c_(696577, _a_(696576, _n_(696575, "self", lambda: self), "kumetop")) ###TAKING THE LISTS
        _l_(696578) ###TAKING THE LISTS


        for x in _c_(696581, _n_(696579, "combinations", lambda: combinations), _n_(696580, "top_set", lambda: top_set), 2):
            _l_(696628)


            ################WHATS THIS
            _c_(696583, _n_(696582, "print", lambda: print), "IM A PRINT FUNCTION WORKING FINE") ###THIS PRINT WORKS
            _l_(696584) ###THIS PRINT WORKS
            _c_(696589, _n_(696585, "print", lambda: print), _c_(696588, _n_(696586, "list", lambda: list), _n_(696587, "y", lambda: y)))
            _l_(696590)
            del list(y)[0]               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            _l_(696591)               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            _c_(696596, _n_(696592, "print", lambda: print), _c_(696595, _n_(696593, "type", lambda: type), _n_(696594, "y", lambda: y)))              ###CLICK THE TEST BUTTON
            _l_(696597)              ###CLICK THE TEST BUTTON

            if _c_(696600, _n_(696598, "len", lambda: len), _n_(696599, "z", lambda: z)) == _c_(696605, _n_(696601, "len", lambda: len), _c_(696604, _n_(696602, "list", lambda: list), _n_(696603, "y", lambda: y))) and _c_(696618, _n_(696606, "all", lambda: all), [_c_(696610, _a_(696608, _n_(696607, "z", lambda: z), "count"), _n_(696609, "i", lambda: i)) == _c_(696616, _a_(696614, _c_(696613, _n_(696611, "list", lambda: list), _n_(696612, "y", lambda: y)), "count"), _n_(696615, "i", lambda: i)) for i in _n_(696617, "kume_set", lambda: kume_set)]):
                _l_(696627)

                _c_(696622, _a_(696621, _a_(696620, _n_(696619, "self", lambda: self), "top_label"), "setText"), "BLABLABLA")
                _l_(696623)
                _c_(696625, _n_(696624, "print", lambda: print), "IM NOT WORKING")
                _l_(696626)



    def close_application(self):
        _l_(696633)

        _c_(696631, _n_(696630, "sys_exit", lambda: sys_exit))
        _l_(696632)

def run():
    _l_(696650)

    app = _c_(696638, _n_(696635, "QApplication", lambda: QApplication), _a_(696637, _n_(696636, "sys", lambda: sys), "argv"))
    _l_(696639)
    GUI = _c_(696641, _n_(696640, "Window", lambda: Window))
    _l_(696642)
    _c_(696648, _a_(696644, _n_(696643, "sys", lambda: sys), "exit"), _c_(696647, _a_(696646, _n_(696645, "app", lambda: app), "exec_")))
    _l_(696649)

_c_(696652, _n_(696651, "run", lambda: run))
_l_(696653)