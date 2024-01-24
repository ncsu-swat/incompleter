# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75979136/tkinter-updating-label-fails-with-attributeerror-frame-object-has-no-attribu
#!/usr/bin/python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(613302)

except ImportError:
    pass
try:
    import tkinter.ttk as ttk
    _l_(613304)

except ImportError:
    pass
try:
    import serial
    _l_(613306)

except ImportError:
    pass
Arduino = _c_(613309, _a_(613308, _n_(613307, "serial", lambda: serial), "Serial"), '/dev/ttyUSB3', '115200', timeout=1)
_l_(613310)
_c_(613312, _n_(613311, "print", lambda: print), 'Connection is working')
_l_(613313)

value1 = 0
_l_(613314)
value2 = 0
_l_(613315)
value3 = 0
_l_(613316)
value4 = 0
_l_(613317)

class App:
    _l_(613654)


    def readdata(self):
        _l_(613364)

        _c_(613322, _a_(613319, _n_(613318, "Arduino", lambda: Arduino), "write"), _c_(613321, _n_(613320, "bytes", lambda: bytes), 'n', 'utf-8'))
        _l_(613323)
        for x in _c_(613325, _n_(613324, "range", lambda: range), 0, 6):
            _l_(613337)

            _c_(613327, _n_(613326, "globals", lambda: globals))['raw%s' % _n_(613328, "x", lambda: x)] = _c_(613335, _a_(613334, _c_(613333, _a_(613332, _c_(613331, _a_(613330, _n_(613329, "Arduino", lambda: Arduino), "readline")), "decode")), "strip"))
            _l_(613336)
        _n_(613338, "self", lambda: self).value1 = _c_(613341, _n_(613339, "int", lambda: int), _n_(613340, "raw1", lambda: raw1))
        _l_(613342)
        _n_(613343, "self", lambda: self).value2 = _c_(613346, _n_(613344, "int", lambda: int), _n_(613345, "raw2", lambda: raw2))
        _l_(613347)
        _n_(613348, "self", lambda: self).value3 = _c_(613351, _n_(613349, "int", lambda: int), _n_(613350, "raw3", lambda: raw3))
        _l_(613352)
        _n_(613353, "self", lambda: self).value4 = _c_(613356, _n_(613354, "int", lambda: int), _n_(613355, "raw4", lambda: raw4))
        _l_(613357)
        _c_(613362, _a_(613359, _n_(613358, "App", lambda: App), "changelabels"), _a_(613361, _n_(613360, "self", lambda: self), "mainframe"))
        _l_(613363)

    def changelabels(self):
        _l_(613373)

        _c_(613371, _a_(613366, _n_(613365, "label1", lambda: label1), "config"), text=_c_(613370, _a_(613369, _a_(613368, _n_(613367, "self", lambda: self), "value1"), "get")))
        _l_(613372)

    def __init__(self, master=None):
        _l_(613647)

        # build ui
        _n_(613374, "self", lambda: self).appwindow = _c_(613377, _a_(613376, _n_(613375, "tk", lambda: tk), "Tk")) if _n_(613378, "master", lambda: master) is None else _c_(613382, _a_(613380, _n_(613379, "tk", lambda: tk), "Toplevel"), _n_(613381, "master", lambda: master))
        _l_(613383)
        _c_(613387, _a_(613386, _a_(613385, _n_(613384, "self", lambda: self), "appwindow"), "configure"), height=240, width=320)
        _l_(613388)
        _c_(613392, _a_(613391, _a_(613390, _n_(613389, "self", lambda: self), "appwindow"), "minsize"), 320, 240)
        _l_(613393)
        _n_(613394, "self", lambda: self).mainframe = _c_(613399, _a_(613396, _n_(613395, "ttk", lambda: ttk), "Frame"), _a_(613398, _n_(613397, "self", lambda: self), "appwindow"))
        _l_(613400)
        _c_(613404, _a_(613403, _a_(613402, _n_(613401, "self", lambda: self), "mainframe"), "configure"), height=240, width=320)
        _l_(613405)
        label1 = _c_(613410, _a_(613407, _n_(613406, "ttk", lambda: ttk), "Label"), _a_(613409, _n_(613408, "self", lambda: self), "mainframe"))
        _l_(613411)
        _n_(613412, "self", lambda: self).value1 = _c_(613415, _a_(613414, _n_(613413, "tk", lambda: tk), "IntVar"))
        _l_(613416)
        _c_(613421, _a_(613418, _n_(613417, "label1", lambda: label1), "configure"), textvariable=_a_(613420, _n_(613419, "self", lambda: self), "value1"))
        _l_(613422)
        _c_(613425, _a_(613424, _n_(613423, "label1", lambda: label1), "grid"), column=1, row=0)
        _l_(613426)
        label2 = _c_(613431, _a_(613428, _n_(613427, "ttk", lambda: ttk), "Label"), _a_(613430, _n_(613429, "self", lambda: self), "mainframe"))
        _l_(613432)
        _n_(613433, "self", lambda: self).value2 = _c_(613436, _a_(613435, _n_(613434, "tk", lambda: tk), "IntVar"))
        _l_(613437)
        _c_(613442, _a_(613439, _n_(613438, "label2", lambda: label2), "configure"), textvariable=_a_(613441, _n_(613440, "self", lambda: self), "value2"))
        _l_(613443)
        _c_(613446, _a_(613445, _n_(613444, "label2", lambda: label2), "grid"), column=1, row=1)
        _l_(613447)
        label3 = _c_(613452, _a_(613449, _n_(613448, "ttk", lambda: ttk), "Label"), _a_(613451, _n_(613450, "self", lambda: self), "mainframe"))
        _l_(613453)
        _n_(613454, "self", lambda: self).value3 = _c_(613457, _a_(613456, _n_(613455, "tk", lambda: tk), "IntVar"))
        _l_(613458)
        _c_(613463, _a_(613460, _n_(613459, "label3", lambda: label3), "configure"), textvariable=_a_(613462, _n_(613461, "self", lambda: self), "value3"))
        _l_(613464)
        _c_(613467, _a_(613466, _n_(613465, "label3", lambda: label3), "grid"), column=1, row=2)
        _l_(613468)
        label4 = _c_(613473, _a_(613470, _n_(613469, "ttk", lambda: ttk), "Label"), _a_(613472, _n_(613471, "self", lambda: self), "mainframe"))
        _l_(613474)
        _n_(613475, "self", lambda: self).value4 = _c_(613478, _a_(613477, _n_(613476, "tk", lambda: tk), "IntVar"))
        _l_(613479)
        _c_(613484, _a_(613481, _n_(613480, "label4", lambda: label4), "configure"), textvariable=_a_(613483, _n_(613482, "self", lambda: self), "value4"))
        _l_(613485)
        _c_(613488, _a_(613487, _n_(613486, "label4", lambda: label4), "grid"), column=1, row=3)
        _l_(613489)
        _n_(613490, "self", lambda: self).text1 = _c_(613495, _a_(613492, _n_(613491, "ttk", lambda: ttk), "Label"), _a_(613494, _n_(613493, "self", lambda: self), "mainframe"))
        _l_(613496)
        _c_(613500, _a_(613499, _a_(613498, _n_(613497, "self", lambda: self), "text1"), "configure"), text='Value1: ')
        _l_(613501)
        _c_(613505, _a_(613504, _a_(613503, _n_(613502, "self", lambda: self), "text1"), "grid"), column=0, row=0)
        _l_(613506)
        _n_(613507, "self", lambda: self).text2 = _c_(613512, _a_(613509, _n_(613508, "ttk", lambda: ttk), "Label"), _a_(613511, _n_(613510, "self", lambda: self), "mainframe"))
        _l_(613513)
        _c_(613517, _a_(613516, _a_(613515, _n_(613514, "self", lambda: self), "text2"), "configure"), text='Value2: ')
        _l_(613518)
        _c_(613522, _a_(613521, _a_(613520, _n_(613519, "self", lambda: self), "text2"), "grid"), column=0, row=1)
        _l_(613523)
        _n_(613524, "self", lambda: self).text3 = _c_(613529, _a_(613526, _n_(613525, "ttk", lambda: ttk), "Label"), _a_(613528, _n_(613527, "self", lambda: self), "mainframe"))
        _l_(613530)
        _c_(613534, _a_(613533, _a_(613532, _n_(613531, "self", lambda: self), "text3"), "configure"), text='Value3: ')
        _l_(613535)
        _c_(613539, _a_(613538, _a_(613537, _n_(613536, "self", lambda: self), "text3"), "grid"), column=0, row=2)
        _l_(613540)
        _n_(613541, "self", lambda: self).text4 = _c_(613546, _a_(613543, _n_(613542, "ttk", lambda: ttk), "Label"), _a_(613545, _n_(613544, "self", lambda: self), "mainframe"))
        _l_(613547)
        _c_(613551, _a_(613550, _a_(613549, _n_(613548, "self", lambda: self), "text4"), "configure"), text='Value4:  ')
        _l_(613552)
        _c_(613556, _a_(613555, _a_(613554, _n_(613553, "self", lambda: self), "text4"), "grid"), column=0, row=3)
        _l_(613557)
        progressbar1 = _c_(613562, _a_(613559, _n_(613558, "ttk", lambda: ttk), "Progressbar"), _a_(613561, _n_(613560, "self", lambda: self), "mainframe"))
        _l_(613563)
        _c_(613566, _a_(613565, _n_(613564, "progressbar1", lambda: progressbar1), "configure"), orient="horizontal")
        _l_(613567)
        _c_(613570, _a_(613569, _n_(613568, "progressbar1", lambda: progressbar1), "grid"), column=2, row=0)
        _l_(613571)
        progressbar2 = _c_(613576, _a_(613573, _n_(613572, "ttk", lambda: ttk), "Progressbar"), _a_(613575, _n_(613574, "self", lambda: self), "mainframe"))
        _l_(613577)
        _c_(613580, _a_(613579, _n_(613578, "progressbar2", lambda: progressbar2), "configure"), orient="horizontal")
        _l_(613581)
        _c_(613584, _a_(613583, _n_(613582, "progressbar2", lambda: progressbar2), "grid"), column=2, row=1)
        _l_(613585)
        progressbar3 = _c_(613590, _a_(613587, _n_(613586, "ttk", lambda: ttk), "Progressbar"), _a_(613589, _n_(613588, "self", lambda: self), "mainframe"))
        _l_(613591)
        _c_(613594, _a_(613593, _n_(613592, "progressbar3", lambda: progressbar3), "configure"), orient="horizontal")
        _l_(613595)
        _c_(613598, _a_(613597, _n_(613596, "progressbar3", lambda: progressbar3), "grid"), column=2, row=2)
        _l_(613599)
        progressbar4 = _c_(613604, _a_(613601, _n_(613600, "ttk", lambda: ttk), "Progressbar"), _a_(613603, _n_(613602, "self", lambda: self), "mainframe"))
        _l_(613605)
        _c_(613608, _a_(613607, _n_(613606, "progressbar4", lambda: progressbar4), "configure"), orient="horizontal")
        _l_(613609)
        _c_(613612, _a_(613611, _n_(613610, "progressbar4", lambda: progressbar4), "grid"), column=2, row=3)
        _l_(613613)
        _n_(613614, "self", lambda: self).refresh = _c_(613619, _a_(613616, _n_(613615, "ttk", lambda: ttk), "Button"), _a_(613618, _n_(613617, "self", lambda: self), "mainframe"))
        _l_(613620)
        _c_(613624, _a_(613623, _a_(613622, _n_(613621, "self", lambda: self), "refresh"), "configure"), text='Refresh')
        _l_(613625)
        _c_(613631, _a_(613628, _a_(613627, _n_(613626, "self", lambda: self), "refresh"), "configure"), command=_a_(613630, _n_(613629, "self", lambda: self), "readdata"))
        _l_(613632)
        _c_(613636, _a_(613635, _a_(613634, _n_(613633, "self", lambda: self), "refresh"), "grid"), column=1, row=4)
        _l_(613637)
        _c_(613641, _a_(613640, _a_(613639, _n_(613638, "self", lambda: self), "mainframe"), "pack"), side="top")
        _l_(613642)

        # Main widget
        _n_(613643, "self", lambda: self).mainwindow = _a_(613645, _n_(613644, "self", lambda: self), "appwindow")
        _l_(613646)

    def run(self):
        _l_(613653)

        _c_(613651, _a_(613650, _a_(613649, _n_(613648, "self", lambda: self), "mainwindow"), "mainloop"))
        _l_(613652)

if _n_(613655, "__name__", lambda: __name__) == "__main__":
    _l_(613663)

    app = _c_(613657, _n_(613656, "App", lambda: App))
    _l_(613658)
    _c_(613661, _a_(613660, _n_(613659, "app", lambda: app), "run"))
    _l_(613662)