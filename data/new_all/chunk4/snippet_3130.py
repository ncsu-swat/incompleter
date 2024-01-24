# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42150030/attributeerror-str-object-has-no-attribute-set-in-tkinter
#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.5
# In conjunction with Tcl version 8.6
#    Feb 10, 2017 09:38:24 AM
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(603589)

except ImportError:
    pass

try:
    _l_(603595)

    from Tkinter import *
    _l_(603590)
except _n_(603591, "ImportError", lambda: ImportError):
    _l_(603594)

    try:
        from tkinter import *
        _l_(603593)

    except ImportError:
        pass

try:
    _l_(603603)

    import ttk
    _l_(603596)
    py3 = 0
    _l_(603597)
except _n_(603598, "ImportError", lambda: ImportError):
    _l_(603602)

    try:
        import tkinter.ttk as ttk
        _l_(603600)

    except ImportError:
        pass
    py3 = 1
    _l_(603601)
try:
    import pulse_support
    _l_(603605)

except ImportError:
    pass

def vp_start_gui():
    _l_(603625)

    '''Starting point when module is the main routine.'''
    _l_(603606)
    global val, w, root, top
    _l_(603607)
    root = _c_(603609, _n_(603608, "Tk", lambda: Tk))
    _l_(603610)
    top = _c_(603613, _n_(603611, "Pulse", lambda: Pulse), _n_(603612, "root", lambda: root))
    _l_(603614)
    _c_(603619, _a_(603616, _n_(603615, "pulse_support", lambda: pulse_support), "init"), _n_(603617, "root", lambda: root), _n_(603618, "top", lambda: top))
    _l_(603620)
    _c_(603623, _a_(603622, _n_(603621, "root", lambda: root), "mainloop"))
    _l_(603624)

w = None
_l_(603626)
def create_Pulse(root, *args, **kwargs):
    _l_(603650)

    '''Starting point when module is imported by another program.'''
    _l_(603627)
    global w, w_win, rt
    _l_(603628)
    rt = _n_(603629, "root", lambda: root)
    _l_(603630)
    w = _c_(603633, _n_(603631, "Toplevel", lambda: Toplevel), _n_(603632, "root", lambda: root))
    _l_(603634)
    top = _c_(603637, _n_(603635, "Pulse", lambda: Pulse), _n_(603636, "w", lambda: w))
    _l_(603638)
    _c_(603645, _a_(603640, _n_(603639, "pulse_support", lambda: pulse_support), "init"), _n_(603641, "w", lambda: w), _n_(603642, "top", lambda: top), *_n_(603643, "args", lambda: args), **_n_(603644, "kwargs", lambda: kwargs))
    _l_(603646)
    aux = (_n_(603647, "w", lambda: w), _n_(603648, "top", lambda: top))
    _l_(603649)
    return aux

def destroy_Pulse():
    _l_(603657)

    global w
    _l_(603651)
    _c_(603654, _a_(603653, _n_(603652, "w", lambda: w), "destroy"))
    _l_(603655)
    w = None
    _l_(603656)

def startTimer():
    _l_(603664)

    global count
    _l_(603658)
    count = 0 # Reset it evert time the user starts the program
    _l_(603659) # Reset it evert time the user starts the program
    _c_(603662, _a_(603661, _n_(603660, "top", lambda: top), "setTimerString"), "12")
    _l_(603663)


def runProgram():
    _l_(603668)

    # Run the main program
    _c_(603666, _n_(603665, "startTimer", lambda: startTimer))
    _l_(603667)

def closeProgram():
    _l_(603672)

    aux = ""
    _l_(603671)
    exit(aux)


class Pulse:
    _l_(604032)

    def __init__(self, top=None):
        _l_(604024)

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _l_(603673)

        _n_(603674, "self", lambda: self)._bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _l_(603675)  # X11 color: 'gray85'
        _n_(603676, "self", lambda: self)._fgcolor = '#000000'  # X11 color: 'black'
        _l_(603677)  # X11 color: 'black'
        _n_(603678, "self", lambda: self)._compcolor = '#d9d9d9' # X11 color: 'gray85'
        _l_(603679) # X11 color: 'gray85'
        _n_(603680, "self", lambda: self)._ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _l_(603681) # X11 color: 'gray85' 
        _n_(603682, "self", lambda: self)._ana2color = '#d9d9d9' # X11 color: 'gray85' 
        _l_(603683) # X11 color: 'gray85' 

        _c_(603686, _a_(603685, _n_(603684, "top", lambda: top), "geometry"), "320x344+599+249")
        _l_(603687)
        _c_(603690, _a_(603689, _n_(603688, "top", lambda: top), "title"), "Pulse")
        _l_(603691)
        _c_(603694, _a_(603693, _n_(603692, "top", lambda: top), "configure"), background="#d9d9d9")
        _l_(603695)

        # Set the strings to use for the form
        _n_(603696, "self", lambda: self).countString = _c_(603698, _n_(603697, "StringVar", lambda: StringVar))
        _l_(603699)
        _n_(603700, "self", lambda: self).timerString = _c_(603702, _n_(603701, "StringVar", lambda: StringVar))
        _l_(603703)
        _n_(603704, "self", lambda: self).countString = "0"
        _l_(603705)
        _n_(603706, "self", lambda: self).timerString = "0"
        _l_(603707)

        _n_(603708, "self", lambda: self).btnExit = _c_(603711, _n_(603709, "Button", lambda: Button), _n_(603710, "top", lambda: top))
        _l_(603712)
        _c_(603716, _a_(603715, _a_(603714, _n_(603713, "self", lambda: self), "btnExit"), "place"), relx=0.84, rely=0.03, height=24, width=39)
        _l_(603717)
        _c_(603721, _a_(603720, _a_(603719, _n_(603718, "self", lambda: self), "btnExit"), "configure"), activebackground="#d9d9d9")
        _l_(603722)
        _c_(603726, _a_(603725, _a_(603724, _n_(603723, "self", lambda: self), "btnExit"), "configure"), activeforeground="#000000")
        _l_(603727)
        _c_(603731, _a_(603730, _a_(603729, _n_(603728, "self", lambda: self), "btnExit"), "configure"), background="#d9d9d9")
        _l_(603732)
        _c_(603737, _a_(603735, _a_(603734, _n_(603733, "self", lambda: self), "btnExit"), "configure"), command=_n_(603736, "closeProgram", lambda: closeProgram))
        _l_(603738)
        _c_(603742, _a_(603741, _a_(603740, _n_(603739, "self", lambda: self), "btnExit"), "configure"), disabledforeground="#a3a3a3")
        _l_(603743)
        _c_(603747, _a_(603746, _a_(603745, _n_(603744, "self", lambda: self), "btnExit"), "configure"), foreground="#000000")
        _l_(603748)
        _c_(603752, _a_(603751, _a_(603750, _n_(603749, "self", lambda: self), "btnExit"), "configure"), highlightbackground="#d9d9d9")
        _l_(603753)
        _c_(603757, _a_(603756, _a_(603755, _n_(603754, "self", lambda: self), "btnExit"), "configure"), highlightcolor="black")
        _l_(603758)
        _c_(603762, _a_(603761, _a_(603760, _n_(603759, "self", lambda: self), "btnExit"), "configure"), pady="0")
        _l_(603763)
        _c_(603767, _a_(603766, _a_(603765, _n_(603764, "self", lambda: self), "btnExit"), "configure"), text='''Exit''')
        _l_(603768)
        _c_(603772, _a_(603771, _a_(603770, _n_(603769, "self", lambda: self), "btnExit"), "configure"), width=39)
        _l_(603773)

        _n_(603774, "self", lambda: self).btnStart = _c_(603777, _n_(603775, "Button", lambda: Button), _n_(603776, "top", lambda: top))
        _l_(603778)
        _c_(603782, _a_(603781, _a_(603780, _n_(603779, "self", lambda: self), "btnStart"), "place"), relx=0.31, rely=0.17, height=104, width=125)
        _l_(603783)
        _c_(603787, _a_(603786, _a_(603785, _n_(603784, "self", lambda: self), "btnStart"), "configure"), activebackground="#d9d9d9")
        _l_(603788)
        _c_(603792, _a_(603791, _a_(603790, _n_(603789, "self", lambda: self), "btnStart"), "configure"), activeforeground="#000000")
        _l_(603793)
        _c_(603797, _a_(603796, _a_(603795, _n_(603794, "self", lambda: self), "btnStart"), "configure"), background="#d9d9d9")
        _l_(603798)
        _c_(603803, _a_(603801, _a_(603800, _n_(603799, "self", lambda: self), "btnStart"), "configure"), command=_n_(603802, "runProgram", lambda: runProgram))
        _l_(603804)
        _c_(603808, _a_(603807, _a_(603806, _n_(603805, "self", lambda: self), "btnStart"), "configure"), disabledforeground="#a3a3a3")
        _l_(603809)
        _c_(603813, _a_(603812, _a_(603811, _n_(603810, "self", lambda: self), "btnStart"), "configure"), foreground="#000000")
        _l_(603814)
        _c_(603818, _a_(603817, _a_(603816, _n_(603815, "self", lambda: self), "btnStart"), "configure"), highlightbackground="#d9d9d9")
        _l_(603819)
        _c_(603823, _a_(603822, _a_(603821, _n_(603820, "self", lambda: self), "btnStart"), "configure"), highlightcolor="black")
        _l_(603824)
        _c_(603828, _a_(603827, _a_(603826, _n_(603825, "self", lambda: self), "btnStart"), "configure"), pady="0")
        _l_(603829)
        _c_(603833, _a_(603832, _a_(603831, _n_(603830, "self", lambda: self), "btnStart"), "configure"), text='''Start''')
        _l_(603834)
        _c_(603838, _a_(603837, _a_(603836, _n_(603835, "self", lambda: self), "btnStart"), "configure"), width=125)
        _l_(603839)

        _n_(603840, "self", lambda: self).Label1 = _c_(603843, _n_(603841, "Label", lambda: Label), _n_(603842, "top", lambda: top))
        _l_(603844)
        _c_(603848, _a_(603847, _a_(603846, _n_(603845, "self", lambda: self), "Label1"), "place"), relx=0.31, rely=0.58, height=21, width=54)
        _l_(603849)
        _c_(603853, _a_(603852, _a_(603851, _n_(603850, "self", lambda: self), "Label1"), "configure"), background="#d9d9d9")
        _l_(603854)
        _c_(603858, _a_(603857, _a_(603856, _n_(603855, "self", lambda: self), "Label1"), "configure"), disabledforeground="#a3a3a3")
        _l_(603859)
        _c_(603863, _a_(603862, _a_(603861, _n_(603860, "self", lambda: self), "Label1"), "configure"), foreground="#000000")
        _l_(603864)
        _c_(603868, _a_(603867, _a_(603866, _n_(603865, "self", lambda: self), "Label1"), "configure"), text='''Timer:''')
        _l_(603869)
        _c_(603873, _a_(603872, _a_(603871, _n_(603870, "self", lambda: self), "Label1"), "configure"), width=54)
        _l_(603874)

        _n_(603875, "self", lambda: self).lblTimer = _c_(603878, _n_(603876, "Label", lambda: Label), _n_(603877, "top", lambda: top))
        _l_(603879)
        _c_(603883, _a_(603882, _a_(603881, _n_(603880, "self", lambda: self), "lblTimer"), "place"), relx=0.5, rely=0.58, height=21, width=32)
        _l_(603884)
        _c_(603888, _a_(603887, _a_(603886, _n_(603885, "self", lambda: self), "lblTimer"), "configure"), background="#a8aeff")
        _l_(603889)
        _c_(603893, _a_(603892, _a_(603891, _n_(603890, "self", lambda: self), "lblTimer"), "configure"), disabledforeground="#a3a3a3")
        _l_(603894)
        _c_(603898, _a_(603897, _a_(603896, _n_(603895, "self", lambda: self), "lblTimer"), "configure"), foreground="#000000")
        _l_(603899)
        _c_(603905, _a_(603902, _a_(603901, _n_(603900, "self", lambda: self), "lblTimer"), "configure"), textvariable=_a_(603904, _n_(603903, "self", lambda: self), "countString"))
        _l_(603906)
        _c_(603910, _a_(603909, _a_(603908, _n_(603907, "self", lambda: self), "lblTimer"), "configure"), width=32)
        _l_(603911)

        _n_(603912, "self", lambda: self).Label3 = _c_(603915, _n_(603913, "Label", lambda: Label), _n_(603914, "top", lambda: top))
        _l_(603916)
        _c_(603920, _a_(603919, _a_(603918, _n_(603917, "self", lambda: self), "Label3"), "place"), relx=0.33, rely=0.67, height=21, width=43)
        _l_(603921)
        _c_(603925, _a_(603924, _a_(603923, _n_(603922, "self", lambda: self), "Label3"), "configure"), background="#d9d9d9")
        _l_(603926)
        _c_(603930, _a_(603929, _a_(603928, _n_(603927, "self", lambda: self), "Label3"), "configure"), disabledforeground="#a3a3a3")
        _l_(603931)
        _c_(603935, _a_(603934, _a_(603933, _n_(603932, "self", lambda: self), "Label3"), "configure"), foreground="#000000")
        _l_(603936)
        _c_(603940, _a_(603939, _a_(603938, _n_(603937, "self", lambda: self), "Label3"), "configure"), text='''Count:''')
        _l_(603941)

        _n_(603942, "self", lambda: self).lblCount = _c_(603945, _n_(603943, "Label", lambda: Label), _n_(603944, "top", lambda: top))
        _l_(603946)
        _c_(603950, _a_(603949, _a_(603948, _n_(603947, "self", lambda: self), "lblCount"), "place"), relx=0.5, rely=0.67, height=21, width=32)
        _l_(603951)
        _c_(603955, _a_(603954, _a_(603953, _n_(603952, "self", lambda: self), "lblCount"), "configure"), activebackground="#f9f9f9")
        _l_(603956)
        _c_(603960, _a_(603959, _a_(603958, _n_(603957, "self", lambda: self), "lblCount"), "configure"), activeforeground="black")
        _l_(603961)
        _c_(603965, _a_(603964, _a_(603963, _n_(603962, "self", lambda: self), "lblCount"), "configure"), background="#ffa8a8")
        _l_(603966)
        _c_(603970, _a_(603969, _a_(603968, _n_(603967, "self", lambda: self), "lblCount"), "configure"), disabledforeground="#a3a3a3")
        _l_(603971)
        _c_(603975, _a_(603974, _a_(603973, _n_(603972, "self", lambda: self), "lblCount"), "configure"), foreground="#000000")
        _l_(603976)
        _c_(603980, _a_(603979, _a_(603978, _n_(603977, "self", lambda: self), "lblCount"), "configure"), highlightbackground="#d9d9d9")
        _l_(603981)
        _c_(603985, _a_(603984, _a_(603983, _n_(603982, "self", lambda: self), "lblCount"), "configure"), highlightcolor="black")
        _l_(603986)
        _c_(603992, _a_(603989, _a_(603988, _n_(603987, "self", lambda: self), "lblCount"), "configure"), textvariable=_a_(603991, _n_(603990, "self", lambda: self), "countString"))
        _l_(603993)

        _n_(603994, "self", lambda: self).Label4 = _c_(603997, _n_(603995, "Label", lambda: Label), _n_(603996, "top", lambda: top))
        _l_(603998)
        _c_(604002, _a_(604001, _a_(604000, _n_(603999, "self", lambda: self), "Label4"), "place"), relx=0.13, rely=0.84, height=36, width=237)
        _l_(604003)
        _c_(604007, _a_(604006, _a_(604005, _n_(604004, "self", lambda: self), "Label4"), "configure"), background="#d9d9d9")
        _l_(604008)
        _c_(604012, _a_(604011, _a_(604010, _n_(604009, "self", lambda: self), "Label4"), "configure"), disabledforeground="#a3a3a3")
        _l_(604013)
        _c_(604017, _a_(604016, _a_(604015, _n_(604014, "self", lambda: self), "Label4"), "configure"), foreground="#000000")
        _l_(604018)
        _c_(604022, _a_(604021, _a_(604020, _n_(604019, "self", lambda: self), "Label4"), "configure"), text='''Press the start button to start the program.
Every time your pulse beats, press the P key.''')
        _l_(604023)

    def setTimerString(self, newVal):
        _l_(604031)

        _c_(604029, _a_(604027, _a_(604026, _n_(604025, "self", lambda: self), "timerString"), "set"), _n_(604028, "newVal", lambda: newVal))
        _l_(604030)


if _n_(604033, "__name__", lambda: __name__) == '__main__':
    _l_(604037)

    _c_(604035, _n_(604034, "vp_start_gui", lambda: vp_start_gui))
    _l_(604036)