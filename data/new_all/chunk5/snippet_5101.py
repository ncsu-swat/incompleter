# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65269660/getting-attributeerror-trying-to-access-math-sqrtx-in-tkinter-app
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(667377)

except ImportError:
    pass
try:
    import math
    _l_(667379)

except ImportError:
    pass

root = _c_(667381, _n_(667380, "Tk", lambda: Tk))
_l_(667382)
_c_(667385, _a_(667384, _n_(667383, "root", lambda: root), "title"), "More Complex Calculator")
_l_(667386)

entry_1 = _c_(667389, _n_(667387, "Entry", lambda: Entry), _n_(667388, "root", lambda: root), width = 50, borderwidth = 5)
_l_(667390)
_c_(667393, _a_(667392, _n_(667391, "entry_1", lambda: entry_1), "grid"), row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
_l_(667394)

def button_click(number):
    _l_(667414)

    current = _c_(667397, _a_(667396, _n_(667395, "entry_1", lambda: entry_1), "get"))
    _l_(667398)
    _c_(667402, _a_(667400, _n_(667399, "entry_1", lambda: entry_1), "delete"), 0, _n_(667401, "END", lambda: END))
    _l_(667403)
    _c_(667412, _a_(667405, _n_(667404, "entry_1", lambda: entry_1), "insert"), 0,_c_(667408, _n_(667406, "str", lambda: str), _n_(667407, "current", lambda: current)) + _c_(667411, _n_(667409, "str", lambda: str), _n_(667410, "number", lambda: number)))
    _l_(667413)

def button_add():
    _l_(667431)

    first_number = _c_(667417, _a_(667416, _n_(667415, "entry_1", lambda: entry_1), "get"))
    _l_(667418)
    global f_num
    _l_(667419)
    global math
    _l_(667420)
    math = "addition"
    _l_(667421)
    f_num = _c_(667424, _n_(667422, "int", lambda: int), _n_(667423, "first_number", lambda: first_number))
    _l_(667425)
    _c_(667429, _a_(667427, _n_(667426, "entry_1", lambda: entry_1), "delete"), 0, _n_(667428, "END", lambda: END))
    _l_(667430)

def button_sub():
    _l_(667448)

    first_number = _c_(667434, _a_(667433, _n_(667432, "entry_1", lambda: entry_1), "get"))
    _l_(667435)
    global f_num
    _l_(667436)
    global math
    _l_(667437)
    math = "subtraction"
    _l_(667438)
    f_num = _c_(667441, _n_(667439, "int", lambda: int), _n_(667440, "first_number", lambda: first_number))
    _l_(667442)
    _c_(667446, _a_(667444, _n_(667443, "entry_1", lambda: entry_1), "delete"), 0, _n_(667445, "END", lambda: END))
    _l_(667447)

def button_mult():
    _l_(667465)

    first_number = _c_(667451, _a_(667450, _n_(667449, "entry_1", lambda: entry_1), "get"))
    _l_(667452)
    global f_num
    _l_(667453)
    global math
    _l_(667454)
    math = "multiplication"
    _l_(667455)
    f_num = _c_(667458, _n_(667456, "int", lambda: int), _n_(667457, "first_number", lambda: first_number))
    _l_(667459)
    _c_(667463, _a_(667461, _n_(667460, "entry_1", lambda: entry_1), "delete"), 0, _n_(667462, "END", lambda: END))
    _l_(667464)

def button_div():
    _l_(667482)

    first_number = _c_(667468, _a_(667467, _n_(667466, "entry_1", lambda: entry_1), "get"))
    _l_(667469)
    global f_num
    _l_(667470)
    global math
    _l_(667471)
    math = "division"
    _l_(667472)
    f_num = _c_(667475, _n_(667473, "int", lambda: int), _n_(667474, "first_number", lambda: first_number))
    _l_(667476)
    _c_(667480, _a_(667478, _n_(667477, "entry_1", lambda: entry_1), "delete"), 0, _n_(667479, "END", lambda: END))
    _l_(667481)

def button_square():
    _l_(667494)

    first_number = _c_(667485, _a_(667484, _n_(667483, "entry_1", lambda: entry_1), "get"))
    _l_(667486)
    global f_num
    _l_(667487)
    global math
    _l_(667488)
    math = "square"
    _l_(667489)
    f_num = _c_(667492, _n_(667490, "int", lambda: int), _n_(667491, "first_number", lambda: first_number))
    _l_(667493)

def button_root():
    _l_(667506)

    first_number = _c_(667497, _a_(667496, _n_(667495, "entry_1", lambda: entry_1), "get"))
    _l_(667498)
    global f_num
    _l_(667499)
    global math
    _l_(667500)
    math = "root"
    _l_(667501)
    f_num = _c_(667504, _n_(667502, "int", lambda: int), _n_(667503, "first_number", lambda: first_number))
    _l_(667505)

def button_enter():
    _l_(667573)

    second_number = _c_(667509, _a_(667508, _n_(667507, "entry_1", lambda: entry_1), "get"))
    _l_(667510)
    _c_(667514, _a_(667512, _n_(667511, "entry_1", lambda: entry_1), "delete"), 0, _n_(667513, "END", lambda: END))
    _l_(667515)
    if _n_(667516, "math", lambda: math) == "addition":
        _l_(667572)

        _c_(667523, _a_(667518, _n_(667517, "entry_1", lambda: entry_1), "insert"), 0, _n_(667519, "f_num", lambda: f_num) + _c_(667522, _n_(667520, "int", lambda: int), _n_(667521, "second_number", lambda: second_number)))
        _l_(667524)
    elif _n_(667525, "math", lambda: math) == "subtraction":
        _l_(667571)

        _c_(667532, _a_(667527, _n_(667526, "entry_1", lambda: entry_1), "insert"), 0, _n_(667528, "f_num", lambda: f_num) - _c_(667531, _n_(667529, "int", lambda: int), _n_(667530, "second_number", lambda: second_number)))
        _l_(667533)
    elif _n_(667534, "math", lambda: math) == "multiplication":
        _l_(667570)

        _c_(667541, _a_(667536, _n_(667535, "entry_1", lambda: entry_1), "insert"), 0, _n_(667537, "f_num", lambda: f_num) * _c_(667540, _n_(667538, "int", lambda: int), _n_(667539, "second_number", lambda: second_number)))
        _l_(667542)
    elif _n_(667543, "math", lambda: math) == "division":
        _l_(667569)

        _c_(667550, _a_(667545, _n_(667544, "entry_1", lambda: entry_1), "insert"), 0, _n_(667546, "f_num", lambda: f_num) / _c_(667549, _n_(667547, "int", lambda: int), _n_(667548, "second_number", lambda: second_number)))
        _l_(667551)
    elif _n_(667552, "math", lambda: math) == "square":
        _l_(667568)

        _c_(667556, _a_(667554, _n_(667553, "entry_1", lambda: entry_1), "insert"), 0, _n_(667555, "f_num", lambda: f_num)**2)
        _l_(667557)
    elif _n_(667558, "math", lambda: math) ==  "root":
        _l_(667567)

        _c_(667565, _a_(667560, _n_(667559, "entry_1", lambda: entry_1), "insert"), 0, _c_(667564, _a_(667562, _n_(667561, "math", lambda: math), "sqrt"), _n_(667563, "f_num", lambda: f_num)))
        _l_(667566)

def button_clear():
    _l_(667579)

    _c_(667577, _a_(667575, _n_(667574, "entry_1", lambda: entry_1), "delete"), 0, _n_(667576, "END", lambda: END))
    _l_(667578)

button_0 = _c_(667584, _n_(667580, "Button", lambda: Button), _n_(667581, "root", lambda: root), text = "0", padx = 40, pady = 20, command = lambda: _c_(667583, _n_(667582, "button_click", lambda: button_click), 0))
_l_(667585)
button_1 = _c_(667590, _n_(667586, "Button", lambda: Button), _n_(667587, "root", lambda: root), text = "1", padx = 40, pady = 20, command = lambda: _c_(667589, _n_(667588, "button_click", lambda: button_click), 1))
_l_(667591)
button_2 = _c_(667596, _n_(667592, "Button", lambda: Button), _n_(667593, "root", lambda: root), text = "2", padx = 40, pady = 20, command = lambda: _c_(667595, _n_(667594, "button_click", lambda: button_click), 2))
_l_(667597)
button_3 = _c_(667602, _n_(667598, "Button", lambda: Button), _n_(667599, "root", lambda: root), text = "3", padx = 40, pady = 20, command = lambda: _c_(667601, _n_(667600, "button_click", lambda: button_click), 3))
_l_(667603)
button_4 = _c_(667608, _n_(667604, "Button", lambda: Button), _n_(667605, "root", lambda: root), text = "4", padx = 40, pady = 20, command = lambda: _c_(667607, _n_(667606, "button_click", lambda: button_click), 4))
_l_(667609)
button_5 = _c_(667614, _n_(667610, "Button", lambda: Button), _n_(667611, "root", lambda: root), text = "5", padx = 40, pady = 20, command = lambda: _c_(667613, _n_(667612, "button_click", lambda: button_click), 5))
_l_(667615)
button_6 = _c_(667620, _n_(667616, "Button", lambda: Button), _n_(667617, "root", lambda: root), text = "6", padx = 40, pady = 20, command = lambda: _c_(667619, _n_(667618, "button_click", lambda: button_click), 6))
_l_(667621)
button_7 = _c_(667626, _n_(667622, "Button", lambda: Button), _n_(667623, "root", lambda: root), text = "7", padx = 40, pady = 20, command = lambda: _c_(667625, _n_(667624, "button_click", lambda: button_click), 7))
_l_(667627)
button_8 = _c_(667632, _n_(667628, "Button", lambda: Button), _n_(667629, "root", lambda: root), text = "8", padx = 40, pady = 20, command = lambda: _c_(667631, _n_(667630, "button_click", lambda: button_click), 8))
_l_(667633)
button_9 = _c_(667638, _n_(667634, "Button", lambda: Button), _n_(667635, "root", lambda: root), text = "9", padx = 40, pady = 20, command = lambda: _c_(667637, _n_(667636, "button_click", lambda: button_click), 9))
_l_(667639)
button_pi = _c_(667646, _n_(667640, "Button", lambda: Button), _n_(667641, "root", lambda: root), text = "π", padx = 39, pady = 20, command = lambda: _c_(667645, _n_(667642, "button_click", lambda: button_click), _a_(667644, _n_(667643, "math", lambda: math), "pi")))
_l_(667647)
button_e = _c_(667654, _n_(667648, "Button", lambda: Button), _n_(667649, "root", lambda: root), text = "e", padx = 40, pady = 20, command = lambda: _c_(667653, _n_(667650, "button_click", lambda: button_click), _a_(667652, _n_(667651, "math", lambda: math), "e")))
_l_(667655)

button_add = _c_(667659, _n_(667656, "Button", lambda: Button), _n_(667657, "root", lambda: root), text = "+", padx = 39, pady = 20, command = _n_(667658, "button_add", lambda: button_add))
_l_(667660)
button_enter = _c_(667664, _n_(667661, "Button", lambda: Button), _n_(667662, "root", lambda: root), text = "=", padx = 39, pady = 20, command = _n_(667663, "button_enter", lambda: button_enter))
_l_(667665)
button_clear = _c_(667669, _n_(667666, "Button", lambda: Button), _n_(667667, "root", lambda: root), text = "C", padx = 39, pady = 20, command = _n_(667668, "button_clear", lambda: button_clear))
_l_(667670)

button_sub = _c_(667674, _n_(667671, "Button", lambda: Button), _n_(667672, "root", lambda: root), text = "-", padx = 41, pady = 20, command = _n_(667673, "button_sub", lambda: button_sub))
_l_(667675)
button_mult = _c_(667679, _n_(667676, "Button", lambda: Button), _n_(667677, "root", lambda: root), text = "x", padx = 40, pady = 20, command = _n_(667678, "button_mult", lambda: button_mult))
_l_(667680)
button_div = _c_(667684, _n_(667681, "Button", lambda: Button), _n_(667682, "root", lambda: root), text = "÷", padx = 40, pady = 20, command = _n_(667683, "button_div", lambda: button_div))
_l_(667685)

button_square = _c_(667689, _n_(667686, "Button", lambda: Button), _n_(667687, "root", lambda: root), text = "x²", padx = 38, pady = 20, command = _n_(667688, "button_square", lambda: button_square))
_l_(667690)
button_sqroot = _c_(667694, _n_(667691, "Button", lambda: Button), _n_(667692, "root", lambda: root), text = "√x", padx = 36, pady = 20, command = _n_(667693, "button_root", lambda: button_root))
_l_(667695)

_c_(667698, _a_(667697, _n_(667696, "button_1", lambda: button_1), "grid"), row = 4, column = 0)
_l_(667699)
_c_(667702, _a_(667701, _n_(667700, "button_2", lambda: button_2), "grid"), row = 4, column = 1)
_l_(667703)
_c_(667706, _a_(667705, _n_(667704, "button_3", lambda: button_3), "grid"), row = 4, column = 2)
_l_(667707)

_c_(667710, _a_(667709, _n_(667708, "button_4", lambda: button_4), "grid"), row = 3, column = 0)
_l_(667711)
_c_(667714, _a_(667713, _n_(667712, "button_5", lambda: button_5), "grid"), row = 3, column = 1)
_l_(667715)
_c_(667718, _a_(667717, _n_(667716, "button_6", lambda: button_6), "grid"), row = 3, column = 2)
_l_(667719)

_c_(667722, _a_(667721, _n_(667720, "button_7", lambda: button_7), "grid"), row = 2, column = 0)
_l_(667723)
_c_(667726, _a_(667725, _n_(667724, "button_8", lambda: button_8), "grid"), row = 2, column = 1)
_l_(667727)
_c_(667730, _a_(667729, _n_(667728, "button_9", lambda: button_9), "grid"), row = 2, column = 2)
_l_(667731)

_c_(667734, _a_(667733, _n_(667732, "button_0", lambda: button_0), "grid"), row = 5, column = 1)
_l_(667735)
_c_(667738, _a_(667737, _n_(667736, "button_square", lambda: button_square), "grid"), row = 1, column = 2)
_l_(667739)
_c_(667742, _a_(667741, _n_(667740, "button_sqroot", lambda: button_sqroot), "grid"), row = 1, column = 3)
_l_(667743)

_c_(667746, _a_(667745, _n_(667744, "button_add", lambda: button_add), "grid"), row = 2, column = 3)
_l_(667747)
_c_(667750, _a_(667749, _n_(667748, "button_enter", lambda: button_enter), "grid"), row = 5, column = 2)
_l_(667751)
_c_(667754, _a_(667753, _n_(667752, "button_clear", lambda: button_clear), "grid"), row = 5, column = 0)
_l_(667755)

_c_(667758, _a_(667757, _n_(667756, "button_pi", lambda: button_pi), "grid"), row = 1, column = 0)
_l_(667759)
_c_(667762, _a_(667761, _n_(667760, "button_e", lambda: button_e), "grid"), row = 1, column = 1)
_l_(667763)

_c_(667766, _a_(667765, _n_(667764, "button_sub", lambda: button_sub), "grid"), row = 3, column = 3)
_l_(667767)
_c_(667770, _a_(667769, _n_(667768, "button_mult", lambda: button_mult), "grid"), row = 4, column = 3)
_l_(667771)
_c_(667774, _a_(667773, _n_(667772, "button_div", lambda: button_div), "grid"), row = 5, column = 3)
_l_(667775)

_c_(667778, _a_(667777, _n_(667776, "root", lambda: root), "mainloop"))
_l_(667779)