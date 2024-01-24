# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25374355/attributeerror-object-has-no-attribute-listbox
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(433496)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(433498)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(433500)

except ImportError:
    pass

class App:
    _l_(433713)

    def __init__(self):
        _l_(433648)

        _n_(433501, "self", lambda: self).master = _c_(433503, _n_(433502, "Tk", lambda: Tk))
        _l_(433504)
        _n_(433505, "self", lambda: self).di = {'Asia': ['Japan', 'China', 'Malaysia', 'India', 'Korea',
                            'Vietnam', 'Laos', 'Thailand', 'Singapore',
                            'Indonesia', 'Taiwan'],
                     'Europe': ['Germany', 'France', 'Switzerland'],
                     'Africa': ['Nigeria', 'Kenya', 'Ethiopia', 'Ghana',
                                'Congo', 'Senegal', 'Guinea', 'Mali', 'Cameroun',
                                'Benin', 'Tanzania', 'South Africa', 'Zimbabwe']}
        _l_(433506)
        _n_(433507, "self", lambda: self).variable_a = _c_(433509, _n_(433508, "StringVar", lambda: StringVar))
        _l_(433510)
        _n_(433511, "self", lambda: self).frame_optionmenu = _c_(433516, _a_(433513, _n_(433512, "ttk", lambda: ttk), "Frame"), _a_(433515, _n_(433514, "self", lambda: self), "master"))
        _l_(433517)
        _c_(433521, _a_(433520, _a_(433519, _n_(433518, "self", lambda: self), "frame_optionmenu"), "pack"))
        _l_(433522)
        _c_(433528, _a_(433525, _a_(433524, _n_(433523, "self", lambda: self), "variable_a"), "trace"), 'w', _a_(433527, _n_(433526, "self", lambda: self), "updateoptions"))
        _l_(433529)
        options = _c_(433535, _n_(433530, "sorted", lambda: sorted), _c_(433534, _a_(433533, _a_(433532, _n_(433531, "self", lambda: self), "di"), "keys")))
        _l_(433536)
        _n_(433537, "self", lambda: self).optionmenu = _c_(433546, _a_(433539, _n_(433538, "ttk", lambda: ttk), "OptionMenu"), _a_(433541, _n_(433540, "self", lambda: self), "frame_optionmenu"), _a_(433543, _n_(433542, "self", lambda: self), "variable_a"), _n_(433544, "options", lambda: options)[0], *_n_(433545, "options", lambda: options))
        _l_(433547)

        _c_(433551, _a_(433550, _a_(433549, _n_(433548, "self", lambda: self), "variable_a"), "set"), 'Asia')
        _l_(433552)
        _c_(433556, _a_(433555, _a_(433554, _n_(433553, "self", lambda: self), "optionmenu"), "pack"))
        _l_(433557)
        _n_(433558, "self", lambda: self).btn = _c_(433565, _a_(433560, _n_(433559, "ttk", lambda: ttk), "Button"), _a_(433562, _n_(433561, "self", lambda: self), "master"), text="Submit", width=8, command=_a_(433564, _n_(433563, "self", lambda: self), "submit"))
        _l_(433566)
        _c_(433570, _a_(433569, _a_(433568, _n_(433567, "self", lambda: self), "btn"), "pack"))
        _l_(433571)

        _n_(433572, "self", lambda: self).frame_listbox = _c_(433577, _a_(433574, _n_(433573, "ttk", lambda: ttk), "Frame"), _a_(433576, _n_(433575, "self", lambda: self), "master"))
        _l_(433578)

        _c_(433584, _a_(433581, _a_(433580, _n_(433579, "self", lambda: self), "frame_listbox"), "pack"), side=_n_(433582, "RIGHT", lambda: RIGHT), fill=_n_(433583, "Y", lambda: Y))
        _l_(433585)
        _n_(433586, "self", lambda: self).scrollbar = _c_(433590, _n_(433587, "Scrollbar", lambda: Scrollbar), _a_(433589, _n_(433588, "self", lambda: self), "frame_listbox") )
        _l_(433591)
        _c_(433597, _a_(433594, _a_(433593, _n_(433592, "self", lambda: self), "scrollbar"), "pack"), side=_n_(433595, "RIGHT", lambda: RIGHT), fill=_n_(433596, "Y", lambda: Y))
        _l_(433598)
        _n_(433599, "self", lambda: self).listbox = _c_(433607, _n_(433600, "Listbox", lambda: Listbox), _a_(433602, _n_(433601, "self", lambda: self), "frame_listbox"), selectmode=_n_(433603, "SINGLE", lambda: SINGLE), yscrollcommand=_a_(433606, _a_(433605, _n_(433604, "self", lambda: self), "scrollbar"), "set"))
        _l_(433608)
        _c_(433615, _a_(433611, _a_(433610, _n_(433609, "self", lambda: self), "scrollbar"), "config"), command=_a_(433614, _a_(433613, _n_(433612, "self", lambda: self), "listbox"), "yview"))
        _l_(433616)
        _c_(433620, _a_(433619, _a_(433618, _n_(433617, "self", lambda: self), "listbox"), "pack"))
        _l_(433621)

        #Populate listbox
        for each in _a_(433623, _n_(433622, "self", lambda: self), "di")[_c_(433627, _a_(433626, _a_(433625, _n_(433624, "self", lambda: self), "variable_a"), "get"))]:
            _l_(433635)

            _c_(433633, _a_(433630, _a_(433629, _n_(433628, "self", lambda: self), "listbox"), "insert"), _n_(433631, "END", lambda: END), _n_(433632, "each", lambda: each))
            _l_(433634)
        _c_(433641, _a_(433638, _a_(433637, _n_(433636, "self", lambda: self), "listbox"), "bind"), "<Double-Button-1>", _a_(433640, _n_(433639, "self", lambda: self), "OnDouble"))
        _l_(433642)

        _c_(433646, _a_(433645, _a_(433644, _n_(433643, "self", lambda: self), "master"), "mainloop"))
        _l_(433647)

    def updateoptions(self, *args):
        _l_(433680)

        countries = _a_(433650, _n_(433649, "self", lambda: self), "di")[_c_(433654, _a_(433653, _a_(433652, _n_(433651, "self", lambda: self), "variable_a"), "get"))]
        _l_(433655)
        _c_(433659, _a_(433658, _a_(433657, _n_(433656, "self", lambda: self), "listbox"), "delete"), 0, 'end')
        _l_(433660)
        for each in _a_(433662, _n_(433661, "self", lambda: self), "di")[_c_(433666, _a_(433665, _a_(433664, _n_(433663, "self", lambda: self), "variable_a"), "get"))]:
            _l_(433674)

            _c_(433672, _a_(433669, _a_(433668, _n_(433667, "self", lambda: self), "listbox"), "insert"), _n_(433670, "END", lambda: END), _n_(433671, "each", lambda: each))
            _l_(433673)
        _c_(433678, _a_(433677, _a_(433676, _n_(433675, "self", lambda: self), "listbox"), "pack"))
        _l_(433679)

    def submit(self, *args):
        _l_(433695)

        var = _c_(433684, _a_(433683, _a_(433682, _n_(433681, "self", lambda: self), "variable_a"), "get"))
        _l_(433685)
        if _c_(433689, _a_(433687, _n_(433686, "messagebox", lambda: messagebox), "askokcancel"), "Selection", "Confirm selection: " + _n_(433688, "var", lambda: var)):
            _l_(433694)

            _c_(433692, _n_(433690, "print", lambda: print), _n_(433691, "var", lambda: var))
            _l_(433693)

    def OnDouble(self, event):
        _l_(433712)

        widget = _a_(433697, _n_(433696, "event", lambda: event), "widget")
        _l_(433698)
        selection = _c_(433701, _a_(433700, _n_(433699, "widget", lambda: widget), "curselection"))
        _l_(433702)
        value = _c_(433706, _a_(433704, _n_(433703, "widget", lambda: widget), "get"), _n_(433705, "selection", lambda: selection)[0])
        _l_(433707)
        _c_(433710, _n_(433708, "print", lambda: print), _n_(433709, "value", lambda: value))
        _l_(433711)

_c_(433715, _n_(433714, "App", lambda: App))
_l_(433716)