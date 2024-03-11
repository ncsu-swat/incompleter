# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73271900/bind-all-in-tkinter-module-command-does-not-work-for-me-return-self-funcargs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(595336)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(595338)

except ImportError:
    pass
try:
    from tkinter import font
    _l_(595340)

except ImportError:
    pass
try:
    import tkinter
    _l_(595342)

except ImportError:
    pass
try:
    from sys import *
    _l_(595344)

except ImportError:
    pass
try:
    import sys
    _l_(595346)

except ImportError:
    pass
try:
    from sys import argv
    _l_(595348)

except ImportError:
    pass


if _c_(595351, _n_(595349, "len", lambda: len), _n_(595350, "argv", lambda: argv)) > 1:
    _l_(595356)

    global filename
    _l_(595352)
    filename = _n_(595353, "argv", lambda: argv)[1]
    _l_(595354)
else:
    a = 0
    _l_(595355)



try:
    _l_(595495)

    #def find():
    def new_file():
        _l_(595395)

        _c_(595360, _a_(595358, _n_(595357, "text", lambda: text), "delete"), 0.0,_n_(595359, "END", lambda: END))
        _l_(595361)
        global file2
        _l_(595362)
        file2=_c_(595365, _a_(595364, _n_(595363, "filedialog", lambda: filedialog), "asksaveasfile"), mode='w', defaultextension=".txt")
        _l_(595366)
        file2=_a_(595368, _n_(595367, "file2", lambda: file2), "name")
        _l_(595369)
        global counterofnum
        _l_(595370)
        counterofnum = 1
        _l_(595371)
        global new
        _l_(595372)
        new = 1
        _l_(595373)
        global filename
        _l_(595374)
        filename=_n_(595375, "file2", lambda: file2)
        _l_(595376)
        data=_c_(595380, _a_(595378, _n_(595377, "text", lambda: text), "get"), 0.0, _n_(595379, "END", lambda: END))
        _l_(595381)
        file1=_c_(595384, _n_(595382, "open", lambda: open), _n_(595383, "filename", lambda: filename),"w")
        _l_(595385)
        _c_(595389, _a_(595387, _n_(595386, "file1", lambda: file1), "write"), _n_(595388, "data", lambda: data))
        _l_(595390)
        _c_(595393, _a_(595392, _n_(595391, "file1", lambda: file1), "flush"))
        _l_(595394)
    def open_file():
        _l_(595414)

        file1=_c_(595398, _a_(595397, _n_(595396, "filedialog", lambda: filedialog), "askopenfile"), mode='r')
        _l_(595399)
        data=_c_(595402, _a_(595401, _n_(595400, "file1", lambda: file1), "read"))
        _l_(595403)
        _c_(595407, _a_(595405, _n_(595404, "text", lambda: text), "delete"), 0.0,_n_(595406, "END", lambda: END))
        _l_(595408)
        _c_(595412, _a_(595410, _n_(595409, "text", lambda: text), "insert"), 0.0,_n_(595411, "data", lambda: data)) #Inserts data
        _l_(595413) #Inserts data
    counterofnum = 0
    _l_(595415)
    def save_file():
        _l_(595472)

        global filename
        _l_(595416)
        global counterofnum
        _l_(595417)
        if _n_(595418, "counterofnum", lambda: counterofnum) == 0:
            _l_(595451)

            global file2
            _l_(595419)
            file2=_c_(595422, _a_(595421, _n_(595420, "filedialog", lambda: filedialog), "asksaveasfile"), mode='w', defaultextension=".txt")
            _l_(595423)
            file2=_a_(595425, _n_(595424, "file2", lambda: file2), "name")
            _l_(595426)
            counterofnum = 1
            _l_(595427)
        elif _n_(595428, "new", lambda: new) == 1:
            _l_(595450)

            global filename
            _l_(595429)
            filename=_n_(595430, "file2", lambda: file2)
            _l_(595431)
            data=_c_(595435, _a_(595433, _n_(595432, "text", lambda: text), "get"), 0.0, _n_(595434, "END", lambda: END))
            _l_(595436)
            file1=_c_(595439, _n_(595437, "open", lambda: open), _n_(595438, "filename", lambda: filename),"w")
            _l_(595440)
            _c_(595444, _a_(595442, _n_(595441, "file1", lambda: file1), "write"), _n_(595443, "data", lambda: data))
            _l_(595445)
            _c_(595448, _a_(595447, _n_(595446, "file1", lambda: file1), "flush"))
            _l_(595449)
        filename=_n_(595452, "file2", lambda: file2)
        _l_(595453)
        data=_c_(595457, _a_(595455, _n_(595454, "text", lambda: text), "get"), 0.0, _n_(595456, "END", lambda: END))
        _l_(595458)
        file1=_c_(595461, _n_(595459, "open", lambda: open), _n_(595460, "filename", lambda: filename),"w")
        _l_(595462)
        _c_(595466, _a_(595464, _n_(595463, "file1", lambda: file1), "write"), _n_(595465, "data", lambda: data))
        _l_(595467)
        _c_(595470, _a_(595469, _n_(595468, "file1", lambda: file1), "flush"))
        _l_(595471)
    def save_as():
        _l_(595491)

        file1=_c_(595475, _a_(595474, _n_(595473, "filedialog", lambda: filedialog), "asksaveasfile"), mode='w')
        _l_(595476)
        data=_c_(595480, _a_(595478, _n_(595477, "text", lambda: text), "get"), 0.0,_n_(595479, "END", lambda: END))
        _l_(595481)
        _c_(595485, _a_(595483, _n_(595482, "file1", lambda: file1), "write"), _n_(595484, "data", lambda: data))
        _l_(595486)
        _c_(595489, _a_(595488, _n_(595487, "file1", lambda: file1), "flush"))
        _l_(595490)

except _n_(595492, "AttributeError", lambda: AttributeError):
    _l_(595494)

    a = 0
    _l_(595493)

try:
    _l_(595502)

    if _n_(595496, "filename", lambda: filename) is None:
        _l_(595498)

        filename = "Untitled.txt"
        _l_(595497)
except _n_(595499, "NameError", lambda: NameError):
    _l_(595501)

    filename = "Untitled.txt"
    _l_(595500)


gui=_c_(595504, _n_(595503, "Tk", lambda: Tk)) #tkinter object.
_l_(595505) #tkinter object.
titled = 'Text Editor - ' + _n_(595506, "filename", lambda: filename)
_l_(595507)
_c_(595511, _a_(595509, _n_(595508, "gui", lambda: gui), "title"), _n_(595510, "titled", lambda: titled))
_l_(595512)
_c_(595515, _a_(595514, _n_(595513, "gui", lambda: gui), "geometry"), "1200x600")
_l_(595516)
frame = _c_(595519, _n_(595517, "Frame", lambda: Frame), _n_(595518, "gui", lambda: gui))
_l_(595520)
_c_(595523, _a_(595522, _n_(595521, "frame", lambda: frame), "pack"), pady=5)
_l_(595524)
text_scroll = _c_(595527, _n_(595525, "Scrollbar", lambda: Scrollbar), _n_(595526, "frame", lambda: frame))
_l_(595528)
_c_(595533, _a_(595530, _n_(595529, "text_scroll", lambda: text_scroll), "pack"), side=_n_(595531, "RIGHT", lambda: RIGHT), fill=_n_(595532, "Y", lambda: Y))
_l_(595534)
text = _c_(595539, _n_(595535, "Text", lambda: Text), _n_(595536, "frame", lambda: frame), width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=_a_(595538, _n_(595537, "text_scroll", lambda: text_scroll), "set"))
_l_(595540)
_c_(595543, _a_(595542, _n_(595541, "text", lambda: text), "pack")) #Display the text
_l_(595544) #Display the text
_c_(595549, _a_(595546, _n_(595545, "text_scroll", lambda: text_scroll), "config"), command = _a_(595548, _n_(595547, "text", lambda: text), "yview"))
_l_(595550)
mymenu=_c_(595552, _n_(595551, "Menu", lambda: Menu), tearoff=False)
_l_(595553)
list1=_c_(595555, _n_(595554, "Menu", lambda: Menu), tearoff=False)
_l_(595556)
list2=_c_(595558, _n_(595557, "Menu", lambda: Menu), tearoff=False)
_l_(595559)
_c_(595563, _a_(595561, _n_(595560, "list1", lambda: list1), "add_command"), label='New File',command=_n_(595562, "new_file", lambda: new_file), accelerator='Ctrl+N') #Create menus.
_l_(595564) #Create menus.
_c_(595568, _a_(595566, _n_(595565, "list1", lambda: list1), "bind_all"), "<Control-n>", _n_(595567, "new_file", lambda: new_file))
_l_(595569)
_c_(595573, _a_(595571, _n_(595570, "list1", lambda: list1), "add_command"), label='Save File',command=_n_(595572, "save_file", lambda: save_file), accelerator='Ctrl+S')
_l_(595574)
_c_(595578, _a_(595576, _n_(595575, "list1", lambda: list1), "bind_all"), "<Control-s>", _n_(595577, "save_file", lambda: save_file))
_l_(595579)
_c_(595583, _a_(595581, _n_(595580, "list1", lambda: list1), "add_command"), label='Save File As',command=_n_(595582, "save_as", lambda: save_as), accelerator='Ctrl+Shift+S')
_l_(595584)
_c_(595588, _a_(595586, _n_(595585, "list1", lambda: list1), "bind_all"), "<Control-Shift-s>", _n_(595587, "save_as", lambda: save_as))
_l_(595589)
_c_(595593, _a_(595591, _n_(595590, "list1", lambda: list1), "add_command"), label='Open File',command=_n_(595592, "open_file", lambda: open_file), accelerator='Ctrl+O')
_l_(595594)
_c_(595598, _a_(595596, _n_(595595, "list1", lambda: list1), "bind_all"), "<Control-o>", _n_(595597, "open_file", lambda: open_file))
_l_(595599)
_c_(595604, _a_(595601, _n_(595600, "list1", lambda: list1), "add_command"), label='Exit',command=_a_(595603, _n_(595602, "gui", lambda: gui), "quit"), accelerator='Alt+F4')
_l_(595605)
_c_(595609, _a_(595607, _n_(595606, "mymenu", lambda: mymenu), "add_cascade"), label='File', menu=_n_(595608, "list1", lambda: list1)) #Create a file option.
_l_(595610) #Create a file option.
_c_(595614, _a_(595612, _n_(595611, "mymenu", lambda: mymenu), "add_cascade"), label="Edit", menu=_n_(595613, "list2", lambda: list2))
_l_(595615)
_c_(595623, _a_(595617, _n_(595616, "list2", lambda: list2), "add_command"), label="Cut", \
                    accelerator="Ctrl+X", \
                    command=lambda: \
                            _c_(595622, _a_(595621, _c_(595620, _a_(595619, _n_(595618, "gui", lambda: gui), "focus_get")), "event_generate"), '<<Cut>>'))
_l_(595624)
_c_(595632, _a_(595626, _n_(595625, "list2", lambda: list2), "add_command"), label="Copy", \
                    accelerator="Ctrl+C", \
                    command=lambda: \
                            _c_(595631, _a_(595630, _c_(595629, _a_(595628, _n_(595627, "gui", lambda: gui), "focus_get")), "event_generate"), '<<Copy>>'))
_l_(595633)
_c_(595641, _a_(595635, _n_(595634, "list2", lambda: list2), "add_command"), label="Paste", \
                    accelerator="Ctrl+V", \
                    command=lambda: \
                            _c_(595640, _a_(595639, _c_(595638, _a_(595637, _n_(595636, "gui", lambda: gui), "focus_get")), "event_generate"), '<<Paste>>'))
_l_(595642)
_c_(595650, _a_(595644, _n_(595643, "list2", lambda: list2), "add_command"), label="Undo", \
                    accelerator="Ctrl+Z", \
                    command=lambda: \
                            _c_(595649, _a_(595648, _c_(595647, _a_(595646, _n_(595645, "gui", lambda: gui), "focus_get")), "event_generate"), '<<Undo>>'))
_l_(595651)
_c_(595659, _a_(595653, _n_(595652, "list2", lambda: list2), "add_command"), label="Redo", \
                    accelerator="Ctrl+Shift+X", \
                    command=lambda: \
                            _c_(595658, _a_(595657, _c_(595656, _a_(595655, _n_(595654, "gui", lambda: gui), "focus_get")), "event_generate"), '<<Redo>>'))
_l_(595660)
#list2.add_command(label="Find",command=find)
_c_(595664, _a_(595662, _n_(595661, "gui", lambda: gui), "config"), menu=_n_(595663, "mymenu", lambda: mymenu))
_l_(595665)
_c_(595668, _a_(595667, _n_(595666, "gui", lambda: gui), "mainloop"))
_l_(595669)