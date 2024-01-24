# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45871308/typeerror-frame-object-is-not-callable-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas
    _l_(538520)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(538522)

except ImportError:
    pass
#assigns a dataframe variable
summer17=_c_(538525, _a_(538524, _n_(538523, "pandas", lambda: pandas), "read_excel"), "summer17.xlsx","list")
_l_(538526)

window=_c_(538528, _n_(538527, "Tk", lambda: Tk))#Start of the main window
_l_(538529)#Start of the main window
row_widget = _c_(538532, _n_(538530, "Frame", lambda: Frame), _n_(538531, "window", lambda: window))#Creates a frame or "megawidget"
_l_(538533)#Creates a frame or "megawidget"
_c_(538536, _a_(538535, _n_(538534, "row_widget", lambda: row_widget), "grid"))
_l_(538537)
#Variaous variables for widget parameters
tw_height = 1.5
_l_(538538)
tw_width1 = 30
_l_(538539)
tw_width2 = 5
_l_(538540)
brew_row = 14
_l_(538541)
#Text blocks for megawidget
t1=_c_(538546, _n_(538542, "Text", lambda: Text), _n_(538543, "row_widget", lambda: row_widget),height=_n_(538544, "tw_height", lambda: tw_height),width=_n_(538545, "tw_width1", lambda: tw_width1))
_l_(538547)
_c_(538550, _a_(538549, _n_(538548, "t1", lambda: t1), "grid"), row=0,column=0)
_l_(538551)
_c_(538558, _a_(538553, _n_(538552, "t1", lambda: t1), "insert"), _n_(538554, "END", lambda: END),_a_(538556, _n_(538555, "summer17", lambda: summer17), "iloc")[_n_(538557, "brew_row", lambda: brew_row),0])
_l_(538559)

t2=_c_(538564, _n_(538560, "Text", lambda: Text), _n_(538561, "row_widget", lambda: row_widget),height=_n_(538562, "tw_height", lambda: tw_height),width=_n_(538563, "tw_width1", lambda: tw_width1))
_l_(538565)
_c_(538568, _a_(538567, _n_(538566, "t2", lambda: t2), "grid"), row=0,column=1)
_l_(538569)
_c_(538576, _a_(538571, _n_(538570, "t2", lambda: t2), "insert"), _n_(538572, "END", lambda: END),_a_(538574, _n_(538573, "summer17", lambda: summer17), "iloc")[_n_(538575, "brew_row", lambda: brew_row),1])
_l_(538577)

t3=_c_(538582, _n_(538578, "Text", lambda: Text), _n_(538579, "row_widget", lambda: row_widget),height=_n_(538580, "tw_height", lambda: tw_height),width=_n_(538581, "tw_width2", lambda: tw_width2))
_l_(538583)
_c_(538586, _a_(538585, _n_(538584, "t3", lambda: t3), "grid"), row=0,column=2)
_l_(538587)
_c_(538594, _a_(538589, _n_(538588, "t3", lambda: t3), "insert"), _n_(538590, "END", lambda: END),_a_(538592, _n_(538591, "summer17", lambda: summer17), "iloc")[_n_(538593, "brew_row", lambda: brew_row),2])
_l_(538595)

t4=_c_(538600, _n_(538596, "Text", lambda: Text), _n_(538597, "row_widget", lambda: row_widget),height=_n_(538598, "tw_height", lambda: tw_height),width=_n_(538599, "tw_width2", lambda: tw_width2))
_l_(538601)
_c_(538604, _a_(538603, _n_(538602, "t4", lambda: t4), "grid"), row=0,column=3)
_l_(538605)
_c_(538612, _a_(538607, _n_(538606, "t4", lambda: t4), "insert"), _n_(538608, "END", lambda: END),_a_(538610, _n_(538609, "summer17", lambda: summer17), "iloc")[_n_(538611, "brew_row", lambda: brew_row),3])
_l_(538613)

t5=_c_(538618, _n_(538614, "Text", lambda: Text), _n_(538615, "row_widget", lambda: row_widget),height=_n_(538616, "tw_height", lambda: tw_height),width=_n_(538617, "tw_width2", lambda: tw_width2))
_l_(538619)
_c_(538622, _a_(538621, _n_(538620, "t5", lambda: t5), "grid"), row=0,column=4)
_l_(538623)
_c_(538630, _a_(538625, _n_(538624, "t5", lambda: t5), "insert"), _n_(538626, "END", lambda: END),_a_(538628, _n_(538627, "summer17", lambda: summer17), "iloc")[_n_(538629, "brew_row", lambda: brew_row),4])
_l_(538631)

t6=_c_(538636, _n_(538632, "Text", lambda: Text), _n_(538633, "row_widget", lambda: row_widget),height=_n_(538634, "tw_height", lambda: tw_height),width=_n_(538635, "tw_width2", lambda: tw_width2))
_l_(538637)
_c_(538640, _a_(538639, _n_(538638, "t6", lambda: t6), "grid"), row=0,column=5)
_l_(538641)
_c_(538648, _a_(538643, _n_(538642, "t6", lambda: t6), "insert"), _n_(538644, "END", lambda: END),_a_(538646, _n_(538645, "summer17", lambda: summer17), "iloc")[_n_(538647, "brew_row", lambda: brew_row),5])
_l_(538649)
#for loop to create new instances of the megawidget
for i in _c_(538655, _n_(538650, "range", lambda: range), _c_(538654, _n_(538651, "len", lambda: len), _a_(538653, _n_(538652, "summer17", lambda: summer17), "index"))):
    _l_(538665)

    row = _c_(538658, _n_(538656, "row_widget", lambda: row_widget), _n_(538657, "Frame", lambda: Frame))
    _l_(538659)
    _c_(538663, _a_(538661, _n_(538660, "row", lambda: row), "grid"), row=_n_(538662, "i", lambda: i),column=0)
    _l_(538664)

_c_(538668, _a_(538667, _n_(538666, "window", lambda: window), "mainloop"))
_l_(538669)