# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67111305/attributeerror-str-object-has-no-attribute-add
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(593604)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(593606)

except ImportError:
    pass
try:
    import tkinter.ttk as ttk
    _l_(593608)

except ImportError:
    pass


class CollegeApp(_n_(593609, "Tk", lambda: Tk)):
    _l_(593662)

    def __init__(self):
        _l_(593652)

        _c_(593613, _a_(593611, _n_(593610, "Tk", lambda: Tk), "__init__"), _n_(593612, "self", lambda: self))
        _l_(593614)
        container = _c_(593618, _a_(593616, _n_(593615, "ttk", lambda: ttk), "Frame"), _n_(593617, "self", lambda: self))
        _l_(593619)
        _c_(593622, _a_(593621, _n_(593620, "container", lambda: container), "pack"), side="top", fill="both", expand=True)
        _l_(593623)
        _n_(593624, "self", lambda: self).frames = {}
        _l_(593625)
        for F in (_n_(593626, "IndividPage", lambda: IndividPage), _n_(593627, "NewPage", lambda: NewPage)):
            _l_(593642)

            frame = _c_(593631, _n_(593628, "F", lambda: F), _n_(593629, "container", lambda: container), _n_(593630, "self", lambda: self))
            _l_(593632)
            _a_(593634, _n_(593633, "self", lambda: self), "frames")[_n_(593635, "F", lambda: F)] = _n_(593636, "frame", lambda: frame)
            _l_(593637)
            _c_(593640, _a_(593639, _n_(593638, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(593641)
        _c_(593646, _a_(593644, _n_(593643, "self", lambda: self), "show_frame"), _n_(593645, "IndividPage", lambda: IndividPage))
        _l_(593647)
        _c_(593650, _a_(593649, _n_(593648, "self", lambda: self), "lift"))
        _l_(593651)

    def show_frame(self, cont):
        _l_(593661)

        frame = _a_(593654, _n_(593653, "self", lambda: self), "frames")[_n_(593655, "cont", lambda: cont)]
        _l_(593656)
        _c_(593659, _a_(593658, _n_(593657, "frame", lambda: frame), "tkraise"))
        _l_(593660)


class IndividPage(_a_(593664, _n_(593663, "ttk", lambda: ttk), "Frame")):
    _l_(593807)


    def __init__(self, parent, controller):
        _l_(593679)

        _n_(593665, "self", lambda: self).controller = _n_(593666, "controller", lambda: controller)
        _l_(593667)
        _c_(593673, _a_(593670, _a_(593669, _n_(593668, "ttk", lambda: ttk), "Frame"), "__init__"), _n_(593671, "self", lambda: self), _n_(593672, "parent", lambda: parent))
        _l_(593674)
        _c_(593677, _a_(593676, _n_(593675, "self", lambda: self), "userEntry"))
        _l_(593678)

    def userEntry(self):
        _l_(593724)

        headingTest = _c_(593682, _n_(593680, "Label", lambda: Label), _n_(593681, "self", lambda: self), text="Enter your UserName:", font="Arial 20")
        _l_(593683)
        _c_(593686, _a_(593685, _n_(593684, "headingTest", lambda: headingTest), "grid"), row=0, column=0, pady=5, padx=5)
        _l_(593687)

        _n_(593688, "self", lambda: self).usernameEnter = _c_(593691, _n_(593689, "Entry", lambda: Entry), _n_(593690, "self", lambda: self), width=40)
        _l_(593692)
        _c_(593696, _a_(593695, _a_(593694, _n_(593693, "self", lambda: self), "usernameEnter"), "grid"), row=0, column=1, padx=5, pady=5)
        _l_(593697)

        _n_(593698, "self", lambda: self).IndivName = _c_(593701, _n_(593699, "StringVar", lambda: StringVar), _n_(593700, "self", lambda: self))
        _l_(593702)
        _c_(593707, _a_(593705, _a_(593704, _n_(593703, "self", lambda: self), "IndivName"), "set"), _n_(593706, "Individuals", lambda: Individuals))
        _l_(593708)

        confirmBtn = _c_(593713, _n_(593709, "Button", lambda: Button), _n_(593710, "self", lambda: self), text="Confirm User", font="Arial 16",
                            command=_a_(593712, _n_(593711, "self", lambda: self), "confirm"))
        _l_(593714)

        _c_(593717, _a_(593716, _n_(593715, "confirmBtn", lambda: confirmBtn), "config"), height=4, width=12)
        _l_(593718)
        _c_(593722, _a_(593720, _n_(593719, "confirmBtn", lambda: confirmBtn), "grid"), row=2, column=2, sticky=_n_(593721, "E", lambda: E), padx=45, pady=360)
        _l_(593723)

    def confirm(self):
        _l_(593735)

        if _c_(593727, _a_(593726, _n_(593725, "self", lambda: self), "add_to_team")):
            _l_(593734)

            _c_(593732, _a_(593730, _a_(593729, _n_(593728, "self", lambda: self), "controller"), "show_frame"), _n_(593731, "NewPage", lambda: NewPage))
            _l_(593733)

    def add_to_team(self):
        _l_(593806)

        user = _c_(593739, _a_(593738, _a_(593737, _n_(593736, "self", lambda: self), "usernameEnter"), "get"))
        _l_(593740)
        if _c_(593743, _n_(593741, "len", lambda: len), _n_(593742, "user", lambda: user)) == 0:
            _l_(593749)

            _c_(593746, _a_(593745, _n_(593744, "messagebox", lambda: messagebox), "showwarning"), title='No user', message='Please enter a username!')
            _l_(593747)
            aux = ""
            _l_(593748)
            return aux
        if _c_(593753, _a_(593752, _a_(593751, _n_(593750, "self", lambda: self), "usernameEnter"), "get")):
            _l_(593760)

            _c_(593758, _a_(593756, _a_(593755, _n_(593754, "self", lambda: self), "controller"), "show_frame"), _n_(593757, "NewPage", lambda: NewPage))
            _l_(593759)

        Individuals = _c_(593764, _a_(593763, _a_(593762, _n_(593761, "self", lambda: self), "IndivName"), "get"))
        _l_(593765)

        if _n_(593766, "user", lambda: user) in _n_(593767, "Individuals", lambda: Individuals):
            _l_(593774)

            _c_(593772, _a_(593769, _n_(593768, "messagebox", lambda: messagebox), "showwarning"), title='In team', message=f'{_n_(593770, "user", lambda: user)} is already a member of {_n_(593771, "Individuals", lambda: Individuals)}!')
            _l_(593773)
        if _c_(593777, _n_(593775, 'len', lambda: len), _n_(593776, 'Individuals', lambda: Individuals)) > 20:
            _l_(593796)

            resp = _c_(593781, _a_(593779, _n_(593778, 'messagebox', lambda: messagebox), 'askyesno'), title='Individuals List is full',
                                       message=f'There are no more spaces in {_n_(593780, "Individuals", lambda: Individuals)}!\nDo you want to join the '
                                               f'team?')
            _l_(593782)
            _c_(593785, _n_(593783, 'print', lambda: print), _n_(593784, 'resp', lambda: resp))
            _l_(593786)
            if _n_(593787, 'resp', lambda: resp):
                _l_(593795)

                _c_(593792, _a_(593790, _a_(593789, _n_(593788, 'self', lambda: self), 'controller'), 'show_frame'), _n_(593791, 'NewPage', lambda: NewPage))
                _l_(593793)
            else:
                aux = ""
                _l_(593794)
                return aux

        _c_(593800, _a_(593798, _n_(593797, 'Individuals', lambda: Individuals), 'add'), _n_(593799, 'user', lambda: user))
        _l_(593801)
        _c_(593804, _n_(593802, 'print', lambda: print), _n_(593803, 'Individuals', lambda: Individuals))
        _l_(593805)


class NewPage(_a_(593809, _n_(593808, 'ttk', lambda: ttk), 'Frame')):
    _l_(593834)


    def __init__(self, parent, controller):
        _l_(593824)

        _n_(593810, 'self', lambda: self).controller = _n_(593811, 'controller', lambda: controller)
        _l_(593812)
        _c_(593818, _a_(593815, _a_(593814, _n_(593813, 'ttk', lambda: ttk), 'Frame'), '__init__'), _n_(593816, 'self', lambda: self), _n_(593817, 'parent', lambda: parent))
        _l_(593819)
        _c_(593822, _a_(593821, _n_(593820, 'self', lambda: self), 'userEntry'))
        _l_(593823)

    def userEntry(self):
        _l_(593833)

        textlbl = _c_(593827, _n_(593825, 'Label', lambda: Label), _n_(593826, 'self', lambda: self), text="New Page", font="Arial 20")
        _l_(593828)
        _c_(593831, _a_(593830, _n_(593829, 'textlbl', lambda: textlbl), 'grid'), row=0, column=0, pady=5, padx=5)
        _l_(593832)


if _n_(593835, '__name__', lambda: __name__) == '__main__':
    _l_(593854)

    Individuals = _c_(593837, _n_(593836, 'set', lambda: set))
    _l_(593838)
    app = _c_(593840, _n_(593839, 'CollegeApp', lambda: CollegeApp))
    _l_(593841)
    _c_(593844, _a_(593843, _n_(593842, 'app', lambda: app), 'geometry'), "800x500")
    _l_(593845)
    _c_(593848, _a_(593847, _n_(593846, 'app', lambda: app), 'title'), 'Points Counter')
    _l_(593849)
    _c_(593852, _a_(593851, _n_(593850, 'app', lambda: app), 'mainloop'))
    _l_(593853)