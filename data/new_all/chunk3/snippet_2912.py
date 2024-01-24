# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58583980/typeerror-must-be-real-number-not-stringvar-any-idea-on-fixing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(537582)

except ImportError:
    pass

#WINDOW PROPERTIES
GUI = _c_(537585, _a_(537584, _n_(537583, "tk", lambda: tk), "Tk"))
_l_(537586)
_c_(537589, _a_(537588, _n_(537587, "GUI", lambda: GUI), "title"), "Payroll Calculator")
_l_(537590)
_c_(537593, _a_(537592, _n_(537591, "GUI", lambda: GUI), "minsize"), '305','110')
_l_(537594)
_c_(537597, _a_(537596, _n_(537595, "GUI", lambda: GUI), "maxsize"), '305','110')
_l_(537598)

hoursWorked = _c_(537601, _a_(537600, _n_(537599, "tk", lambda: tk), "StringVar"))
_l_(537602)
payRate = _c_(537605, _a_(537604, _n_(537603, "tk", lambda: tk), "StringVar"))
_l_(537606)

#TAXES
states_dict = {'Alabama' : 0.035, 'Arizona' : 0.03565, 'Alaska' : 1, 'Arkansas' : 0.039, 'California' : 0.0715,
        'Colorado' : 1, 'Connecticut' : 0.04995, 'Delaware' : 0.044, 'Florida' : 1, 'Georgia' : 0.035, 'Hawaii' : 0.04825,
        'Idaho' : 4.5, 'Illinois' : 1, 'Indiana' : 1, 'Iowa' : 0.0467, 'Kansas' : 0.0405, 'Kentucky' : 0.04,
        'Louisiana' : 0.04, 'Maine' : 0.06475, 'Maryland' : 0.03875, 'Massachusetts' : 1, 'Michigan' : 1, 'Minnesota' : 0.076,
        'Mississippi' : 0.04, 'Missouri' : 0.0375, 'Montana' : 0.0395, 'Nebraska' : 0.0465, 'Nevada' : 1, 'New Hampshire' : 1,
        'New Jersey' : 0.05185, 'New Mexico' : 0.033, 'New York' : 0.0641, 'North Carolina' : 1, 'North Dakota' : 0.02, 'Ohio' : 0.0275, 'Oklahoma' : 0.0275,
        'Oregon' : 0.0745, 'Pennsylvania' : 1, 'Rhode Island' : 0.0487, 'South Carolina' : 0.035, 'South Dakota' : 1, 'Tennessee' : 1, 'Texas' : 1, 'Utah' : 1,
        'Vermont' : 0.0625, 'Washington' : 1, 'West Virginia' : 0.0475, 'Wisconsin' : 0.05825, 'Wyoming' : 1, 'District of Columbia' : 0.06475}
_l_(537607)

# NEW CALCULATE FUNCTION /////////////////////////////
def calculate():
    _l_(537659)

    state = _c_(537610, _a_(537609, _n_(537608, "opt", lambda: opt), "get"))
    _l_(537611)
    _c_(537616, _n_(537612, "print", lambda: print), _c_(537615, _a_(537613, 'state == {}', "format"), _n_(537614, "state", lambda: state)))
    _l_(537617)
    tax = _n_(537618, "states_dict", lambda: states_dict)[_n_(537619, "state", lambda: state)]
    _l_(537620)
    _c_(537626, _n_(537621, "print", lambda: print), _c_(537625, _a_(537622, 'tax in {} is {}', "format"), _n_(537623, "state", lambda: state), _n_(537624, "tax", lambda: tax)))
    _l_(537627)
    salary = (_c_(537632, _n_(537628, "float", lambda: float), _c_(537631, _a_(537630, _n_(537629, "hoursWorked", lambda: hoursWorked), "get"))) * _c_(537637, _n_(537633, "float", lambda: float), _c_(537636, _a_(537635, _n_(537634, "payRate", lambda: payRate), "get")))) - (_c_(537642, _n_(537638, "float", lambda: float), _c_(537641, _a_(537640, _n_(537639, "payRate", lambda: payRate), "get"))) * _n_(537643, "states_dict", lambda: states_dict)[_n_(537644, "state", lambda: state)])
    _l_(537645)
    _c_(537652, _n_(537646, "print", lambda: print), _c_(537651, _a_(537647, 'tax in {} is {} result in salary:{}', "format"), _n_(537648, "state", lambda: state), _n_(537649, "tax", lambda: tax), _n_(537650, "salary", lambda: salary)))
    _l_(537653)
    _c_(537657, _a_(537655, _n_(537654, "result", lambda: result), "set"), _n_(537656, "salary", lambda: salary))
    _l_(537658)
# ////////////////////////////////////////////////////

result = _c_(537662, _a_(537661, _n_(537660, "tk", lambda: tk), "StringVar"))
_l_(537663)

#ENTRY
_c_(537669, _a_(537668, _c_(537667, _a_(537665, _n_(537664, "tk", lambda: tk), "Label"), _n_(537666, "GUI", lambda: GUI), text='Pay Rate:', font="110"), "grid"), row=0)
_l_(537670)
_c_(537676, _a_(537675, _c_(537674, _a_(537672, _n_(537671, "tk", lambda: tk), "Label"), _n_(537673, "GUI", lambda: GUI), text='Hours Worked:', font="110"), "grid"), row=1)
_l_(537677)

e1 = _c_(537682, _a_(537679, _n_(537678, "tk", lambda: tk), "Entry"), _n_(537680, "GUI", lambda: GUI), textvariable = _n_(537681, "payRate", lambda: payRate))
_l_(537683)
e2 = _c_(537688, _a_(537685, _n_(537684, "tk", lambda: tk), "Entry"), _n_(537686, "GUI", lambda: GUI), textvariable = _n_(537687, "hoursWorked", lambda: hoursWorked))
_l_(537689)
_c_(537694, _a_(537691, _n_(537690, "e1", lambda: e1), "grid"), row = 0, column = 1, sticky = _a_(537693, _n_(537692, "tk", lambda: tk), "W"))
_l_(537695)
_c_(537700, _a_(537697, _n_(537696, "e2", lambda: e2), "grid"), row = 1, column = 1, sticky = _a_(537699, _n_(537698, "tk", lambda: tk), "W"))
_l_(537701)

#OPTION MENU
opt = _c_(537704, _a_(537703, _n_(537702, "tk", lambda: tk), "StringVar"))
_l_(537705)
_c_(537708, _a_(537707, _n_(537706, "opt", lambda: opt), "set"), "Choose a state")
_l_(537709)

option = _c_(537717, _a_(537716, _c_(537715, _a_(537711, _n_(537710, "tk", lambda: tk), "OptionMenu"), _n_(537712, "GUI", lambda: GUI), _n_(537713, "opt", lambda: opt), *_n_(537714, "states_dict", lambda: states_dict)), "grid"), row=2, column=0)
_l_(537718)

frame = _c_(537722, _a_(537720, _n_(537719, "tk", lambda: tk), "Frame"), _n_(537721, "GUI", lambda: GUI))
_l_(537723)
_c_(537726, _a_(537725, _n_(537724, "frame", lambda: frame), "grid"))
_l_(537727)

results = _c_(537734, _a_(537733, _c_(537732, _a_(537729, _n_(537728, "tk", lambda: tk), "Label"), _n_(537730, "GUI", lambda: GUI), textvariable = "Total Pay: $" + "%.2f" % _n_(537731, "result", lambda: result)), "grid"), row=3, column=1)
_l_(537735)

button = _c_(537740, _a_(537737, _n_(537736, "tk", lambda: tk), "Button"), _n_(537738, "frame", lambda: frame), text='Calculate', fg='red', command=_n_(537739, "calculate", lambda: calculate))
_l_(537741)
_c_(537744, _a_(537743, _n_(537742, "button", lambda: button), "grid"), row=1, column=0)
_l_(537745)

#SET DEFAULTS
_c_(537748, _a_(537747, _n_(537746, "hoursWorked", lambda: hoursWorked), "set"), 0)
_l_(537749)
_c_(537752, _a_(537751, _n_(537750, "payRate", lambda: payRate), "set"), 0)
_l_(537753)

#EVENT LOOP
_c_(537756, _a_(537755, _n_(537754, "GUI", lambda: GUI), "mainloop"))
_l_(537757)