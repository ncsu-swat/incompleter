# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28261876/python3-askopenfilename-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   from tkinter import *
   _l_(404254)

except ImportError:
   pass
try:
   from tkinter import filedialog
   _l_(404256)

except ImportError:
   pass
try:
   from tkinter.filedialog import askopenfilename
   _l_(404258)

except ImportError:
   pass
try:
   from mtTkinter import *
   _l_(404260)

except ImportError:
   pass
try:
   import subprocess
   _l_(404262)

except ImportError:
   pass


def donothing():
   _l_(404275)

   filewin = _c_(404265, _n_(404263, "Toplevel", lambda: Toplevel), _n_(404264, "root", lambda: root))
   _l_(404266)
   button = _c_(404269, _n_(404267, "Button", lambda: Button), _n_(404268, "filewin", lambda: filewin), text="Do nothing button")
   _l_(404270)
   _c_(404273, _a_(404272, _n_(404271, "button", lambda: button), "pack"))
   _l_(404274)

def OpenFile():
   _l_(404286)

   file = _c_(404279, _n_(404276, "open", lambda: open), _c_(404278, _n_(404277, "askopenfilename", lambda: askopenfilename)),'r')
   _l_(404280)
   _c_(404284, _n_(404281, "print", lambda: print), _a_(404283, _n_(404282, "root", lambda: root), "file"))
   _l_(404285)

def Quit():
   _l_(404291)

   _c_(404289, _a_(404288, _n_(404287, "root", lambda: root), "destroy"))
   _l_(404290)

def Test():
   _l_(404298)

   _c_(404293, _n_(404292, "print", lambda: print), "Hello world")
   _l_(404294)
   _c_(404296, _n_(404295, "input", lambda: input), "Press return to exit")
   _l_(404297)

def Shell():
   _l_(404303)

#    print("Below is the output")
   _c_(404301, _a_(404300, _n_(404299, "subprocess", lambda: subprocess), "call"), './home/shanaka/bash_lerning/function1.sh',shell=True)
   _l_(404302)


root = _c_(404305, _n_(404304, "Tk", lambda: Tk))
_l_(404306)
_c_(404309, _a_(404308, _n_(404307, "root", lambda: root), "title"), "Volatility")
_l_(404310)
_c_(404313, _a_(404312, _n_(404311, "root", lambda: root), "geometry"), "600x400")
_l_(404314)

menubar = _c_(404317, _n_(404315, "Menu", lambda: Menu), _n_(404316, "root", lambda: root))
_l_(404318)
startmenu = _c_(404321, _n_(404319, "Menu", lambda: Menu), _n_(404320, "menubar", lambda: menubar), tearoff=0)
_l_(404322)
_c_(404326, _a_(404324, _n_(404323, "startmenu", lambda: startmenu), "add_command"), label="Import", command=_n_(404325, "OpenFile", lambda: OpenFile))
_l_(404327)
_c_(404330, _a_(404329, _n_(404328, "startmenu", lambda: startmenu), "add_separator"))
_l_(404331)
_c_(404335, _a_(404333, _n_(404332, "startmenu", lambda: startmenu), "add_command"), label="Exit", command=_n_(404334, "Quit", lambda: Quit))
_l_(404336)
_c_(404340, _a_(404338, _n_(404337, "menubar", lambda: menubar), "add_cascade"), label="Start", menu=_n_(404339, "startmenu", lambda: startmenu))
_l_(404341)

searchmenu = _c_(404344, _n_(404342, "Menu", lambda: Menu), _n_(404343, "menubar", lambda: menubar), tearoff=0)
_l_(404345)

submenu = _c_(404348, _n_(404346, "Menu", lambda: Menu), _n_(404347, "searchmenu", lambda: searchmenu))
_l_(404349)
_c_(404353, _a_(404351, _n_(404350, "submenu", lambda: submenu), "add_command"), label="New feed", command=_n_(404352, "Shell", lambda: Shell))
_l_(404354)
_c_(404357, _a_(404356, _n_(404355, "submenu", lambda: submenu), "add_command"), label="Bookmarks")
_l_(404358)
_c_(404361, _a_(404360, _n_(404359, "submenu", lambda: submenu), "add_command"), label="Mail")
_l_(404362)
_c_(404366, _a_(404364, _n_(404363, "searchmenu", lambda: searchmenu), "add_cascade"), label='Plugins', menu=_n_(404365, "submenu", lambda: submenu), underline=0)
_l_(404367)

_c_(404370, _a_(404369, _n_(404368, "searchmenu", lambda: searchmenu), "add_separator"))
_l_(404371)
#searchmenu.add_command(label="Plugins", command=Test)
_c_(404375, _a_(404373, _n_(404372, "searchmenu", lambda: searchmenu), "add_command"), label="Copy", command=_n_(404374, "donothing", lambda: donothing))
_l_(404376)
_c_(404380, _a_(404378, _n_(404377, "searchmenu", lambda: searchmenu), "add_command"), label="Paste", command=_n_(404379, "donothing", lambda: donothing))
_l_(404381)
_c_(404385, _a_(404383, _n_(404382, "searchmenu", lambda: searchmenu), "add_command"), label="Delete", command=_n_(404384, "donothing", lambda: donothing))
_l_(404386)
_c_(404390, _a_(404388, _n_(404387, "searchmenu", lambda: searchmenu), "add_command"), label="Select All", command=_n_(404389, "donothing", lambda: donothing))
_l_(404391)
_c_(404395, _a_(404393, _n_(404392, "menubar", lambda: menubar), "add_cascade"), label="Search", menu=_n_(404394, "searchmenu", lambda: searchmenu))
_l_(404396)

reportmenu = _c_(404399, _n_(404397, "Menu", lambda: Menu), _n_(404398, "menubar", lambda: menubar), tearoff=0)
_l_(404400)
_c_(404404, _a_(404402, _n_(404401, "reportmenu", lambda: reportmenu), "add_command"), label="Generate Reports", command=_n_(404403, "donothing", lambda: donothing))
_l_(404405)
_c_(404409, _a_(404407, _n_(404406, "menubar", lambda: menubar), "add_cascade"), label="Reports", menu=_n_(404408, "reportmenu", lambda: reportmenu))
_l_(404410)


helpmenu = _c_(404413, _n_(404411, "Menu", lambda: Menu), _n_(404412, "menubar", lambda: menubar), tearoff=0)
_l_(404414)
_c_(404418, _a_(404416, _n_(404415, "helpmenu", lambda: helpmenu), "add_command"), label="Help Index", command=_n_(404417, "donothing", lambda: donothing))
_l_(404419)
_c_(404423, _a_(404421, _n_(404420, "helpmenu", lambda: helpmenu), "add_command"), label="About...", command=_n_(404422, "donothing", lambda: donothing))
_l_(404424)
_c_(404428, _a_(404426, _n_(404425, "menubar", lambda: menubar), "add_cascade"), label="Help", menu=_n_(404427, "helpmenu", lambda: helpmenu))
_l_(404429)

_c_(404433, _a_(404431, _n_(404430, "root", lambda: root), "config"), menu=_n_(404432, "menubar", lambda: menubar))
_l_(404434)
_c_(404437, _a_(404436, _n_(404435, "root", lambda: root), "mainloop"))
_l_(404438)